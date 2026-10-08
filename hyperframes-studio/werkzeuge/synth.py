import numpy as np, wave, sys
SR=44100; BPM=128; B=60/BPM; DUR=15.0
N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,pan=0.0,gain=1.0):
    i=int(t*SR)
    if i>=N or i+len(sig)<=0: return
    s=sig[max(0,-i):]; i=max(i,0); s=s[:N-i]
    L[i:i+len(s)]+=s*gain*(1-max(pan,0)); R[i:i+len(s)]+=s*gain*(1+min(pan,0))
def tt(d): return np.arange(int(SR*d))/SR
def fft_filter(x,lo,hi):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/SR)
    X[(f<lo)|(f>hi)]=0; return np.fft.irfft(X,len(x))
def kick():
    t=tt(0.32); f=45+110*np.exp(-t*28); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*9)*1.0 + 0.3*np.exp(-t*200)*rng.standard_normal(len(t))
def hat(open_=False):
    d=0.22 if open_ else 0.05; t=tt(d)
    return fft_filter(rng.standard_normal(len(t)),6500,16000)*np.exp(-t*(18 if open_ else 90))*0.35
def clap():
    t=tt(0.22); n=fft_filter(rng.standard_normal(len(t)),900,6000)
    env=np.exp(-t*22)+0.6*np.exp(-((t-0.012)%0.02)*60)*np.exp(-t*8)
    return n*env*0.55
def bass(freq,d):
    t=tt(d); s=np.sin(2*np.pi*freq*t)+0.35*np.sin(4*np.pi*freq*t)
    return s*np.minimum(t*80,1)*np.exp(-t*3.2)*0.55
def pluck(freq,d=0.28):
    t=tt(d); s=sum(np.sin(2*np.pi*freq*k*t)/k for k in (1,2,3))*np.exp(-t*14)
    return s*0.22
def pad(freqs,d):
    t=tt(d); s=sum(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*1.004*t) for f in freqs)
    env=np.minimum(t*6,1)*np.minimum((d-t)*6,1)
    return s*env*0.035
def whoosh(d=0.3):
    t=tt(d); n=rng.standard_normal(len(t)); out=np.zeros(len(t))
    # rising band: crossfade a few fixed bands
    for k,(lo,hi) in enumerate([(300,900),(900,2500),(2500,6000),(6000,12000)]):
        c=(k+0.5)/4; env=np.exp(-((t/d-c)**2)/0.03)
        out+=fft_filter(n,lo,hi)*env
    return out*np.minimum(t*40,1)*0.6
def thump():
    t=tt(0.22); f=70*np.exp(-t*10)+35; ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*12)*0.9
def crash():
    t=tt(1.2); return fft_filter(rng.standard_normal(len(t)),3000,16000)*np.exp(-t*3.5)*0.6
mid=lambda m:440*2**((m-69)/12)
chords=[(57,60,64),(53,57,60),(48,52,55),(55,59,62),(57,60,64),(53,57,60),(55,59,62),(52,56,59)] # Am F C G Am F G E
bass_root=[33,29,36,31,33,29,31,28]
for bar in range(8):
    t0=bar*4*B; ch=chords[bar]
    add(pad([mid(n) for n in ch],4*B),t0,0,1.0)
    for e in range(8):
        te=t0+e*B/2
        r=mid(bass_root[bar]+(12 if e in(3,7) else 0))
        add(bass(r,B/2*0.95),te,0,1.0)
        n=ch[[0,1,2,1,0,2,1,2][e]]+12
        add(pluck(mid(n)),te,[-0.4,0.4][e%2],1.0)
for beat in range(32):
    t=beat*B
    add(kick(),t,0,1.0)
    add(hat(),t+B/2,0.3,1.0)
    add(hat(),t+B/4,-0.3,0.45); add(hat(),t+3*B/4,0.3,0.45)
    if beat%2==1: add(clap(),t,0,1.0)
    if beat%4==3: add(hat(True),t+B/2,0.2,0.8)
# scene cuts every 2 beats: rising whoosh into cut + thump
for s in range(16):
    t=s*2*B
    if s>0: add(whoosh(0.28),t-0.28,0.0,0.9)
    add(thump(),t,0,0.8)
add(crash(),0.0,0,0.5); add(crash(),14*B*2/2*2/2*1.0 if False else 15*B-0.0,0,0.0)
# final crash at last scene
add(crash(),15*(2*B),0,0.0)
add(crash(),(32-2)*B,0,0.8)
# master
m=np.maximum(np.abs(L).max(),np.abs(R).max()); g=0.89/m
fade=np.ones(N); f0=int((DUR-0.35)*SR); fade[f0:]=np.linspace(1,0,N-f0)
L*=g*fade; R*=g*fade
x=np.stack([L,R],1); x=np.clip(x,-1,1)
pcm=(x*32767).astype('<i2')
with wave.open(sys.argv[1],'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("ok",m,g)
