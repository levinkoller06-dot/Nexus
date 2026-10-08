import numpy as np, wave, sys
SR=44100; BPM=96; B=60/BPM; BAR=4*B; DUR=30.0; N=int(SR*DUR)
rng=np.random.default_rng(21)
mix=np.zeros((N,2))
def tt(d): return np.arange(int(SR*d))/SR
def place(buf,sig,t,pan=0.0,g=1.0):
    i=int(round(t*SR))
    if i>=N: return
    if i<0: sig=sig[-i:]; i=0
    s=sig[:N-i]; buf[i:i+len(s),0]+=s*g*np.sqrt(0.5*(1-pan)); buf[i:i+len(s),1]+=s*g*np.sqrt(0.5*(1+pan))
def filt(x,lo=None,hi=None,order=2):
    X=np.fft.rfft(x,axis=0); f=np.fft.rfftfreq(x.shape[0],1/SR); H=np.ones_like(f)
    if hi: H/=np.sqrt(1+(f/hi)**(2*order))
    if lo: H/=np.sqrt(1+(lo/np.maximum(f,1))**(2*order))
    return np.fft.irfft(X*(H[:,None] if x.ndim>1 else H),x.shape[0],axis=0)
def reverb(x,decay=2.2,mix_=0.3):
    L=int(SR*decay); t=np.arange(L)/SR
    ir=np.stack([rng.standard_normal(L),rng.standard_normal(L)],1)*np.exp(-t*6.9/decay)[:,None]
    ir=filt(ir,200,5000); ir/=np.sqrt((ir**2).sum(0))
    n=x.shape[0]+L; F=1<<(n-1).bit_length()
    y=np.fft.irfft(np.fft.rfft(x,F,axis=0)*np.fft.rfft(ir,F,axis=0),F,axis=0)[:x.shape[0]]
    return x*(1-mix_)+y*mix_*2.5
mid=lambda m:440*2**((m-69)/12)
def epiano(m,d,vel=1.0):
    f=mid(m); t=tt(d+1.2); I=2.2*vel*np.exp(-t*5)
    s=np.sin(2*np.pi*f*t+I*np.sin(2*np.pi*f*t))+0.25*np.sin(2*np.pi*2*f*t)*np.exp(-t*3)
    s+=0.12*np.sin(2*np.pi*f*14*t)*np.exp(-t*40)*vel  # tine click
    env=np.exp(-t*(1.1+f/900))*np.minimum(t/0.004,1)
    rel=np.clip(1-(t-d)/0.35,0,1); env*=np.where(t>d,rel,1)
    trem=1+0.08*np.sin(2*np.pi*4.5*t)
    return s*env*trem*0.16*vel
def hum(): return rng.normal(0,0.012)
# chords (bar index -> notes), voicings
C={'Fmaj7':[53,57,60,64],'Em7':[52,55,59,62],'Dm7':[50,53,57,60],'Cmaj7':[48,52,55,59],'Am7':[45,52,55,60],'G7':[43,53,59,62],'Gsus':[43,50,55,60],'Bbmaj7':[46,53,57,62]}
prog=[['Fmaj7'],['Em7'],['Dm7'],['Cmaj7'],['Fmaj7'],['Em7'],['Am7'],['Dm7','G7'],['Bbmaj7'],['Am7'],['Dm7','Gsus'],['Cmaj7']]
bass_root={'Fmaj7':41,'Em7':40,'Dm7':38,'Cmaj7':36,'Am7':33,'G7':31,'Gsus':31,'Bbmaj7':34}
keys=np.zeros((N,2)); bass=np.zeros((N,2)); drums=np.zeros((N,2)); mel=np.zeros((N,2))
# comping rhythms vary per bar (beat offsets, length)
comp=[[(0,3.8)],[(0,3.8)],[(0,1.5),(2.5,1.4)],[(0,3.8)],
      [(0,1.4),(1.5,0.9),(3,1)],[(0,2),(2.5,1.4)],[(0,1.4),(1.5,0.9),(3.5,0.5)],[(0,1.8),(2,1.9)],
      [(0.5,1.4),(2,0.9),(3,1)],[(0,1.4),(1.75,1),(3,1)],[(0,1.8),(2,1.9)],[(0,8)]]
for bar,chs in enumerate(prog):
    t0=bar*BAR
    for k,(off,ln) in enumerate(comp[bar]):
        ch=chs[0] if len(chs)==1 or off<2 else chs[1]
        vel=0.75+0.25*rng.random()
        for j,n in enumerate(C[ch]):
            place(keys,epiano(n+12,ln*B,vel*(0.9 if j else 1)),t0+off*B+j*0.012+hum(),(-0.25+0.17*j),1)
# bass from bar 2 (5s), walking variations
bpat=[None,None,[(0,0,1.5),(1.5,7,0.5),(2,0,1.8)],[(0,0,2),(2.5,7,1),(3.5,12,0.4)],
      [(0,0,1.5),(1.5,0,0.4),(2,7,1.8)],[(0,0,1),(1.5,3,0.5),(2,7,1.5),(3.5,10,0.4)],[(0,0,1.5),(2,7,1),(3,5,0.8)],[(0,0,1.8),(2,0,1.8)],
      [(0,0,1.5),(1.5,0,0.4),(2,7,1),(3,9,0.8)],[(0,0,2),(2.5,7,0.5),(3,5,0.9)],[(0,0,1.8),(2,0,1.5),(3.5,2,0.4)],[(0,0,6)]]
for bar,chs in enumerate(prog):
    if bpat[bar] is None: continue
    for off,iv,ln in bpat[bar]:
        ch=chs[0] if len(chs)==1 or off<2 else chs[1]
        f=mid(bass_root[ch]+iv); d=ln*B; t=tt(d+0.2)
        s=(np.sin(2*np.pi*f*t)+0.3*np.sin(4*np.pi*f*t)+0.1*np.sin(6*np.pi*f*t))
        env=np.minimum(t/0.01,1)*np.exp(-t*1.8)*np.where(t>d,np.clip(1-(t-d)/0.15,0,1),1)
        place(bass,s*env*0.42*(0.85+0.15*rng.random()),bar*BAR+off*B+hum())
# drums: soft, from bar 3 (7.5s); variations
def kick(v):
    t=tt(0.4); f=48+70*np.exp(-t*25); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*9)*0.7*v
def rim(v):
    t=tt(0.12); n=filt(rng.standard_normal(len(t)),1500,6000)
    return (n*np.exp(-t*60)*0.3+np.sin(2*np.pi*1700*t)*np.exp(-t*90)*0.15)*v
def shaker(v):
    t=tt(0.09); n=filt(rng.standard_normal(len(t)),5000,12000)
    env=np.minimum(t/0.02,1)*np.exp(-t*45)
    return n*env*0.12*v
def ohat(v):
    t=tt(0.4); return filt(rng.standard_normal(len(t)),6000,14000)*np.exp(-t*9)*0.08*v
for bar in range(3,12):
    t0=bar*BAR
    if bar==11:
        place(drums,kick(1),t0); place(drums,ohat(1.2),t0,0.2); continue
    kp=[0,2.5] if bar%2 else [0,1.75,2.5]
    if bar==7: kp=[0,2.5,3.5]
    for o in kp: place(drums,kick(0.85+0.15*rng.random()),t0+o*B+hum()*0.3)
    for o in [1,3]: place(drums,rim(0.8+0.3*rng.random()),t0+o*B+hum()*0.5,0.1)
    step=0.25 if bar>=8 else 0.5
    for k in range(int(4/step)):
        o=k*step; acc=1.0 if (o%1)==0.5 else 0.55
        place(drums,shaker(acc*(0.7+0.5*rng.random())),t0+o*B+0.012*rng.standard_normal(),0.35)
    if bar in (6,10): place(drums,ohat(1),t0+3.5*B,-0.2)
# melody (vibes-like bell), phrases vary: bars 4-11
def bell(m,d,v):
    f=mid(m); t=tt(d+1.0)
    s=np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*f*3.99*t)*np.exp(-t*4)+0.15*np.sin(2*np.pi*f*2*t)
    env=np.minimum(t/0.003,1)*np.exp(-t*2.4)
    return s*env*0.11*v
phr={4:[(0,72,1),(1,76,0.5),(1.5,77,1),(3,76,1)],
     5:[(0,74,1.5),(2,71,0.5),(2.5,72,1.5)],
     6:[(0.5,76,0.5),(1,79,1),(2,77,0.5),(2.5,76,0.5),(3,72,1)],
     7:[(0,74,2),(2,74,0.5),(2.5,77,0.5),(3,79,1)],
     8:[(0,81,1.5),(1.5,79,0.5),(2,77,1),(3,74,1)],
     9:[(0,76,1),(1,72,0.5),(1.5,76,0.5),(2,79,2)],
     10:[(0,77,0.5),(0.5,76,0.5),(1,74,1),(2,71,0.5),(2.5,74,1.5)],
     11:[(0,79,1),(1,76,1),(2,72,4)]}
for bar,notes in phr.items():
    for o,m,ln in notes:
        place(mel,bell(m,ln*B,0.8+0.25*rng.random()),bar*BAR+o*B+hum(),0.15*np.sin(o))
keys=reverb(keys,2.0,0.28); mel=reverb(mel,2.6,0.38); drums=reverb(drums,0.9,0.12)
# gentle intro swell: lowpass keys in first 5s
lo=filt(keys,None,1500); T=np.arange(N)/SR; w=np.clip(T/5,0,1)[:,None]
keys=np.where((T<5)[:,None],lo*(1-w)+keys*w,keys)
mix=keys*1.0+bass*1.0+drums*0.9+mel*0.9
mix=filt(mix,35,16000)
fi=np.minimum(T/0.6,1); fo=np.clip((30-T)/1.8,0,1); mix*=(fi*fo)[:,None]
mix=np.tanh(mix/np.abs(mix).max()*1.15)/np.tanh(1.15)*0.85
with wave.open(sys.argv[1],'wb') as wv: wv.setnchannels(2);wv.setsampwidth(2);wv.setframerate(SR);wv.writeframes((np.clip(mix,-1,1)*32767).astype('<i2').tobytes())
print('ok')
