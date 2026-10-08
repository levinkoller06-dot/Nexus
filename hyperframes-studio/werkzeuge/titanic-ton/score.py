import numpy as np, wave, json
SR=44100; T=json.load(open('timing.json')); DUR=T['total']; N=int(DUR*SR)
segs=T['segs']; SC=[0]+[s['start']-0.4 for s in segs[1:]]+[DUR]
rng=np.random.default_rng(5)
def tt(d): return np.arange(int(SR*d))/SR
def place(buf,sig,t,pan=0,g=1):
    i=int(round(t*SR))
    if i>=N: return
    if i<0: sig=sig[-i:]; i=0
    s=sig[:N-i]; buf[i:i+len(s),0]+=s*g*np.sqrt(.5*(1-pan)); buf[i:i+len(s),1]+=s*g*np.sqrt(.5*(1+pan))
def filt(x,lo=None,hi=None,o=2):
    X=np.fft.rfft(x,axis=0); f=np.fft.rfftfreq(x.shape[0],1/SR); H=np.ones_like(f)
    if hi: H/=np.sqrt(1+(f/hi)**(2*o))
    if lo: H/=np.sqrt(1+(lo/np.maximum(f,1))**(2*o))
    return np.fft.irfft(X*(H[:,None] if x.ndim>1 else H),x.shape[0],axis=0)
def reverb(x,decay=2.5,mix=.35):
    L=int(SR*decay); t=np.arange(L)/SR
    ir=np.stack([rng.standard_normal(L),rng.standard_normal(L)],1)*np.exp(-t*6.9/decay)[:,None]
    ir=filt(ir,150,6000); ir/=np.sqrt((ir**2).sum(0))
    n=x.shape[0]+L; F=1<<(n-1).bit_length()
    y=np.fft.irfft(np.fft.rfft(x,F,axis=0)*np.fft.rfft(ir,F,axis=0),F,axis=0)[:x.shape[0]]
    return x*(1-mix)+y*mix*2.5
mid=lambda m:440*2**((m-69)/12)
def piano(m,d,v=1):
    f=mid(m); t=tt(d+1.5)
    s=sum(np.sin(2*np.pi*f*k*t*(1+0.0004*k*k))*np.exp(-t*(1.2+k*0.9))/k**1.3 for k in range(1,8))
    s+=0.3*np.sin(2*np.pi*f*t)*np.exp(-t*0.6)
    env=np.minimum(t/0.003,1)*np.where(t>d,np.clip(1-(t-d)/0.5,0,1),1)
    return s*env*0.12*v
def strings(notes,d,v=1):
    t=tt(d+1.2); s=np.zeros(len(t))
    for m in notes:
        for det in (-0.006,0,0.005):
            f=mid(m)*(1+det)*(1+0.003*np.sin(2*np.pi*5.2*t+rng.random()*6))
            ph=2*np.pi*np.cumsum(f)/SR+rng.random()*6
            s+=sum(np.sin(k*ph)/k for k in range(1,9))
    env=np.minimum(t/0.9,1)*np.where(t>d,np.clip(1-(t-d)/1.1,0,1),1)
    return s*env*0.012*v
def bell(m,d,v=1):
    f=mid(m); t=tt(d+2)
    s=np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*2)+.25*np.sin(2*np.pi*f*5.4*t)*np.exp(-t*4)
    return s*np.exp(-t*1.4)*np.minimum(t/0.002,1)*0.07*v
music=np.zeros((N,2)); pads=np.zeros((N,2))
CH={'C':[48,55,60,64],'G/B':[47,55,59,62],'Am':[45,52,57,60],'F':[41,53,57,60],'G':[43,55,59,62],'Dm':[38,53,57,62],'Bb':[46,53,58,62],'A':[45,52,57,61],'E':[40,52,56,59],'Gm':[43,55,58,62],'Em':[40,52,55,59]}
sections=[ # (start scene idx, end scene idx, chords, bar seconds, piano pattern, extra)
 (0,3,['C','G/B','Am','F','C','G','F','C','Am','Em','F','G'],2.6,'arp_up','warm'),
 (3,4,['Am','F','C','G'],2.5,'sparse','night'),
 (4,6,['Dm','Dm','Bb','A','Dm','Dm','Bb','A'],2.4,'pulse','tension'),
 (6,9,['Dm','Bb','F','A','Gm','Bb','A','Dm','Dm','Bb','F','A'],3.0,'slow','sad'),
 (9,11,['F','C','Dm','Bb','F','C','Bb','C'],2.8,'bells','dawn'),
 (11,12,['C','G','Am','F','C','G','C'],2.2,'arp_up','warm'),
]
pat={'arp_up':[(0,0),(0.5,1),(1,2),(1.5,3),(2,2),(2.5,1),(3,3),(3.5,2)],
     'sparse':[(0,2),(1.5,3),(2.5,1)],
     'slow':[(0,3),(2,2)],
     'bells':[(0,3),(1,2),(2,3),(3,1)],
     'pulse':[]}
for a,b,chs,bar,p,kind in sections:
    t0=SC[a]; t1=SC[b]; t=t0; k=0
    while t<t1-0.3:
        ch=CH[chs[k%len(chs)]]; d=min(bar,t1-t)
        place(pads,strings([n+12 for n in ch[1:]],d,1.0 if kind!='night' else .7),t,0,1)
        if kind!='dawn': place(pads,strings([ch[0]],d,0.8),t,0,1)
        if p=='pulse':
            for e in range(int(d/(bar/8))):
                tt0=t+e*bar/8; f=mid(ch[0]-12+(12 if e%4==3 else 0)); x=tt(0.25)
                s=(np.sin(2*np.pi*f*x)+0.5*np.sin(4*np.pi*f*x))*np.exp(-x*9)*0.22*(1.0 if e%2==0 else .7)
                place(music,s,tt0,0,1)
            if k%2==1: place(music,piano(ch[2]+24,0.5,0.5),t+bar*0.75,0.3)
        else:
            for off,ix in pat[p]:
                tt0=t+off*bar/4
                if tt0>=t1-0.2: continue
                v=0.7+0.3*rng.random()
                if p=='bells': place(music,bell(ch[ix]+24,1.5,v),tt0+rng.normal(0,.01),0.4*np.sin(off))
                else: place(music,piano(ch[ix]+12+(12 if (k%4==2 and ix==3) else 0),bar/4*1.5,v),tt0+rng.normal(0,.01),0.3*np.sin(off*1.7))
            if kind=='warm' and k%2==0: place(music,piano(ch[0],bar*0.9,0.8),t,0)
        t+=bar; k+=1
# final ring
place(music,piano(48,3,1),DUR-3.2); place(music,piano(60,3,.8),DUR-3.2); place(music,piano(64,3,.7),DUR-3.15); place(music,piano(67,3,.7),DUR-3.1)
music=reverb(music,2.2,.3); pads=reverb(pads,3.0,.35)
mix=music+pads*0.9
mix=filt(mix,40,15000)
Tm=np.arange(N)/SR; fade=np.clip(Tm/1.0,0,1)*np.clip((DUR-Tm)/2.5,0,1); mix*=fade[:,None]
mix=mix/np.abs(mix).max()*0.85
def save(x,fn):
    with wave.open(fn,'wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(x,-1,1)*32767).astype('<i2').tobytes())
save(mix,'score.wav')
# ---------- FX ----------
fx=np.zeros((N,2))
def waves(t0,t1,g=1):
    d=t1-t0; n=int(d*SR); t=np.arange(n)/SR
    w=filt(np.stack([rng.standard_normal(n),rng.standard_normal(n)],1),80,900)
    sw=0.55+0.45*np.sin(2*np.pi*0.11*t+1)[:,None]*np.sin(2*np.pi*0.047*t)[:,None]**2
    foam=filt(np.stack([rng.standard_normal(n),rng.standard_normal(n)],1),1500,6000)*(np.maximum(np.sin(2*np.pi*0.11*t+1),0)**4)[:,None]*0.4
    s=(w*sw+foam)*np.minimum(np.minimum(t/1.5,1),np.minimum((d-t)/1.5,1))[:,None]
    i=int(t0*SR); fx[i:i+n]+=s[:N-i]*0.05*g
waves(0,SC[5],1); waves(SC[7],SC[9],0.8); waves(SC[9],SC[10],1); waves(SC[11],DUR,1)
# ship horn at departure
def horn(d=2.6):
    t=tt(d+1); s=np.zeros(len(t))
    for f in (87.3,110.0,130.8):
        ph=2*np.pi*f*t*(1+0.002*np.sin(2*np.pi*3*t)); s+=sum(np.sin(k*ph)*(0.9**k) for k in range(1,14))
    s+=filt(rng.standard_normal(len(t)),200,1200)*0.6
    env=np.minimum(t/0.25,1)*np.where(t>d,np.clip(1-(t-d)/0.7,0,1),1)
    return filt(s*env,None,1600)*0.025
hs=segs[2]['start']+0.3; place(fx,horn(2.4),hs,0,1); place(fx,horn(1.4),hs+3.2,0,0.8)
# morse beeps during ice warnings
ms=segs[3]['start']+3.0; code=".-.. --.- ..- -.-. . .-. .. -.-. .".replace(" ","/")
t=ms
for c in code:
    if c=='/': t+=0.18; continue
    d=0.07 if c=='.' else 0.2; x=tt(d); s=np.sin(2*np.pi*680*x)*np.minimum(np.minimum(x/0.005,1),np.minimum((d-x)/0.005,1))*0.08
    place(fx,s,t,0.4,1); t+=d+0.07
# metal groan + rumble at break
bs=segs[7]['start']+3.6
t=tt(3.0); f=70+25*np.sin(2*np.pi*0.7*t)*np.exp(-t*0.5); ph=2*np.pi*np.cumsum(f)/SR
groan=sum(np.sin(k*ph+np.sin(2*np.pi*11*t)*0.3)/k for k in range(1,10))*np.exp(-t*0.9)*np.minimum(t/0.3,1)
place(fx,filt(groan,None,1200)*0.08,bs-1.2,0,1)
rum=filt(rng.standard_normal(int(SR*3.5)),30,250)*np.exp(-tt(3.5)*1.0)*0.5
place(fx,rum,bs,0,1)
# bubbles in deep-sea scene
for k in range(26):
    t0=SC[10]+0.5+rng.random()*(SC[11]-SC[10]-1.5); d=0.06+rng.random()*0.05; x=tt(d)
    f=500+rng.random()*900; s=np.sin(2*np.pi*np.cumsum(f*(1+x/d*1.5))/SR)*np.exp(-x*30)*0.05
    place(fx,s,t0,rng.uniform(-.7,.7),1)
fx=reverb(fx,1.6,.2); fx*=np.clip((DUR-Tm)/2.0,0,1)[:,None]
save(fx/max(1,np.abs(fx).max()/0.9),'fx.wav')
print('ok', SC)
