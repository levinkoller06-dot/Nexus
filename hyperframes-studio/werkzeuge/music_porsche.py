import numpy as np, wave
SR=44100; DUR=45.0; N=int(DUR*SR); B=0.5; BAR=2.0
rng=np.random.default_rng(911)
def tt(d): return np.arange(int(SR*d))/SR
def buf(): return np.zeros((N,2))
def place(b,s,t,pan=0,g=1):
    i=int(round(t*SR))
    if i>=N: return
    if i<0: s=s[-i:]; i=0
    s=s[:N-i]; b[i:i+len(s),0]+=s*g*np.sqrt(.5*(1-pan)); b[i:i+len(s),1]+=s*g*np.sqrt(.5*(1+pan))
def filt(x,lo=None,hi=None,o=2):
    X=np.fft.rfft(x,axis=0); f=np.fft.rfftfreq(x.shape[0],1/SR); H=np.ones_like(f)
    if hi: H/=np.sqrt(1+(f/hi)**(2*o))
    if lo: H/=np.sqrt(1+(lo/np.maximum(f,1))**(2*o))
    return np.fft.irfft(X*(H[:,None] if x.ndim>1 else H),x.shape[0],axis=0)
def reverb(x,decay=2.0,mix=.25):
    L=int(SR*decay); t=np.arange(L)/SR
    ir=np.stack([rng.standard_normal(L),rng.standard_normal(L)],1)*np.exp(-t*6.9/decay)[:,None]
    ir=filt(ir,200,7000); ir/=np.sqrt((ir**2).sum(0))
    n=x.shape[0]+L; F=1<<(n-1).bit_length()
    y=np.fft.irfft(np.fft.rfft(x,F,axis=0)*np.fft.rfft(ir,F,axis=0),F,axis=0)[:x.shape[0]]
    return x*(1-mix)+y*mix*2.5
mid=lambda m:440*2**((m-69)/12)
def saw(f,t): ph=np.cumsum(np.broadcast_to(f,t.shape))/SR; return 2*(ph%1)-1
T=np.arange(N)/SR
# ---------- drums
dr=buf()
def kick(v=1,big=False):
    t=tt(0.6 if big else 0.35); f=40+(160 if big else 120)*np.exp(-t*(18 if big else 30)); ph=2*np.pi*np.cumsum(f)/SR
    return np.tanh(np.sin(ph)*np.exp(-t*(4 if big else 8))*1.8+filt(rng.standard_normal(len(t)),2000,8000)*np.exp(-t*250)*.4)*.9*v
def clap(v=1):
    t=tt(.3); n=filt(rng.standard_normal(len(t)),900,7000); e=sum(np.exp(-np.maximum(t-d,0)*140)*(t>=d) for d in (0,.009,.018))+.6*np.exp(-np.maximum(t-.025,0)*16)*(t>=.025)
    return n*e*.35*v
def hat(v=1,op=False):
    t=tt(.25 if op else .05); return filt(rng.standard_normal(len(t)),7500,None)*np.exp(-t*(16 if op else 90))*.22*v
def heartbeat(v=1):
    t=tt(.5); f=38+30*np.exp(-t*20); s=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9); return s*v*.9
for t0 in [0.6,1.0,2.6,3.0,4.4,4.75]: place(dr,heartbeat(0.8 if t0%1<.5 else .55),t0)
def groove(t0,t1,kpat,clap_on=True,hat16=False,openh=True):
    b=t0;k=0
    while b<t1-1e-6:
        beat=int(round((b-t0)/B))
        if beat%4 in kpat or (beat%4==3 and k%2==1 and 3.5 in kpat): place(dr,kick(.95+.1*rng.random()),b)
        if clap_on and beat%2==1: place(dr,clap(.9+.2*rng.random()),b,.05)
        steps=4 if hat16 else 2
        for s in range(steps):
            h=b+s*B/steps; acc=1 if (s==steps//2) else .5
            place(dr,hat(acc*(.7+.4*rng.random())),h+rng.normal(0,.003),.3)
        if openh and beat%4==3: place(dr,hat(.8,True),b+B/2,-.2)
        b+=B; k+=1
groove(8,20,[0,2],True,False); groove(20,32,[0,2,2.5],True,True); groove(32,38,[0],False,False,False)
# fill before 20 and 38
for i in range(8): place(dr,clap(.3+.09*i),19.0+i*.125,0)
for i in range(16): place(dr,clap(.2+.05*i),37.0+i*.0625,0)
place(dr,kick(1.2,True),8.0); place(dr,kick(1.0,True),20.0); place(dr,kick(1.25,True),38.0); place(dr,kick(1.1,True),42.0)
# ---------- harmony
CH={'Dm':[50,53,57,62],'Bb':[46,53,58,62],'F':[41,53,57,60],'C':[48,52,55,60],'Gm':[43,55,58,62],'A':[45,52,57,61],'Dm9':[50,53,57,64]}
pads=buf(); bass=buf(); lead=buf(); arp=buf()
def pad(notes,d,v=1,bright=1):
    t=tt(d+1.5); s=np.zeros(len(t))
    for m in notes:
        for det in (-.007,0,.006): s+=saw(mid(m)*(1+det),t)
    env=np.minimum(t/.4,1)*np.where(t>d,np.clip(1-(t-d)/1.4,0,1),1)
    return s*env*.03*v
def bassnote(m,d,v=1):
    t=tt(d); f=mid(m); s=np.tanh(2.2*(saw(f,t)*.6+np.sin(2*np.pi*f/2*t)*.8))
    return s*np.minimum(t/.005,1)*np.clip(1-(t-d+.03)/.03,0,1)*.32*v
def pluck(m,d,v=1):
    t=tt(d+.3); f=mid(m); s=saw(f,t)*.5+np.sin(2*np.pi*f*2*t)*.3
    return s*np.exp(-t*9)*np.minimum(t/.002,1)*.13*v
# intro drone
t=tt(8.2); drone=(saw(mid(26),t)+saw(mid(26)*1.004,t)+.5*saw(mid(38),t))*np.minimum(t/3,1)*.05
dr2=np.stack([drone,drone],1); dr2=filt(dr2,None,320); place(pads,dr2[:,0],0,-.1); place(pads,dr2[:,1],0,.1)
progA=['Dm','Bb','F','C','Gm','A']; progB=['Dm','Bb','F','C','Dm','Bb']; progC=['Bb','F','C']
def section(t0,prog,bar,bpat,arp_on,lead_notes=None,padv=1):
    for i,c in enumerate(prog):
        tb=t0+i*bar; ch=CH[c]
        place(pads,pad([n+12 for n in ch[1:]],bar,padv),tb,0)
        for o,iv,ln in bpat:
            place(bass,bassnote(ch[0]-12+iv,ln*B),tb+o*B)
        if arp_on:
            seq=[ch[1]+24,ch[2]+24,ch[3]+24,ch[2]+24] if i%2==0 else [ch[3]+24,ch[2]+24,ch[1]+24,ch[2]+36]
            for s in range(int(bar/(B/2))): place(arp,pluck(seq[s%4],.18,.6+.4*((s%4)==0)),tb+s*B/2,.5*(-1)**s)
bA=[(o,0 if o%2==0 else 12,.45) for o in [0,.5,1,1.5,2,2.5,3,3.5]]
bB=[(0,0,.9),(1,0,.45),(1.5,12,.45),(2,0,.9),(3,7,.45),(3.5,12,.45)]
section(8,progA,2.0,bA,False,padv=.8)
section(20,progB,2.0,bB,True,padv=1.0)
section(32,progC,2.0,[(0,0,3.5)],True,padv=.7)
# lead melody in B
mel=[(20,74,1),(21,77,.5),(21.5,76,.5),(22,74,1.5),(24,77,1),(25,79,.5),(25.5,77,.5),(26,81,2),(28,79,1),(29,77,1),(30,76,.5),(30.5,74,.5),(31,72,1)]
for t0,m,ln in mel:
    t=tt(ln*B*2+.4); f=mid(m)*(1+.004*np.sin(2*np.pi*5*t)); s=(saw(f,t)*.5+saw(f*1.005,t)*.5)
    env=np.minimum(t/.02,1)*np.where(t>ln,np.clip(1-(t-ln)/.4,0,1),1)
    place(lead,filt(s,None,3000)*env*.05,t0,.15)
# final chord
place(pads,pad([50,57,62,64,69],5.5,1.3),38,0)
place(bass,bassnote(26,4.5,1.1),38)
# ---------- transitions fx (each unique)
fx=buf()
def swoosh(d,f0,f1,v,rev=False,pan0=-.8,pan1=.8):
    n=int(d*SR); t=np.arange(n)/SR; x=rng.standard_normal(n)
    out=np.zeros(n); bands=np.geomspace(f0,f1,10)
    for k in range(len(bands)-1):
        c=(k+.5)/(len(bands)-1); env=np.exp(-((t/d-c)**2)/.02)
        out+=filt(x,bands[k],bands[k+1])*env
    out*=np.sin(np.pi*np.clip(t/d,0,1))**.7
    if rev: out=out[::-1]
    pan=np.linspace(pan0,pan1,n)
    s=np.stack([out*np.sqrt(.5*(1-pan)),out*np.sqrt(.5*(1+pan))],1)*v
    return s
def put(s,t):
    i=int(t*SR); s=s[:N-i]; fx[i:i+len(s)]+=s
put(swoosh(1.8,80,9000,.5,False,0,0),6.2)           # riser-ish air into title
put(swoosh(.45,300,6000,.35,False,-.9,.9),9.75)     # car changes, all different
put(swoosh(.55,200,4500,.33,False,.9,-.9),11.72)
put(swoosh(.35,500,9000,.30,False,-.6,.8),13.8)
put(swoosh(.6,150,3500,.36,True,.8,-.8),15.65)
put(swoosh(.4,400,7000,.31,False,-.9,.4),17.78)
put(swoosh(.7,250,8000,.4,False,-.5,.5),19.45)
put(swoosh(.5,300,5000,.3,True,.6,-.6),22.6)
put(swoosh(.42,600,10000,.28,False,-.8,.8),25.7)
put(swoosh(.55,180,4000,.32,False,.8,-.8),28.6)
put(swoosh(.9,100,6000,.3,True,0,0),31.2)
put(swoosh(.5,250,6000,.25,False,-.7,.7),33.8); put(swoosh(.5,350,7000,.22,False,.7,-.7),35.8)
put(swoosh(2.0,60,12000,.55,False,0,0),36.0)
# shimmer at end
t=tt(4.5); sh=sum(np.sin(2*np.pi*mid(m)*t)*np.exp(-t*(.8+.2*k)) for k,m in enumerate([86,88,93,98]))*.02
place(fx,sh,38.05,.3)
mix=dr*1.0+filt(pads,None,5000)*1.0+bass*1.0+arp*.9+lead*.9
mix=reverb(mix,1.4,.12)+reverb(fx,1.6,.2)*0+fx
mix=filt(mix,30,16000)
fade=np.clip(T/.3,0,1)*np.clip((DUR-T)/2.2,0,1); mix*=fade[:,None]
mix=np.tanh(mix/np.abs(mix).max()*1.4)/np.tanh(1.4)*.9
with wave.open('porsche_music.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(mix,-1,1)*32767).astype('<i2').tobytes())
print('ok')
