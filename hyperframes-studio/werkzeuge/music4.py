import numpy as np, wave, sys
SR=44100; BPM=120; B=60/BPM; DUR=15.0; N=int(SR*DUR)
rng=np.random.default_rng(11)
def buf(): return np.zeros((N,2))
def tt(d): return np.arange(int(SR*d))/SR
def place(dst,sig,t,pan=0.0,g=1.0):
    i=int(round(t*SR)); 
    if i>=N: return
    s=sig[:N-i] if i>=0 else sig[-i:][:N]; i=max(i,0)
    dst[i:i+len(s),0]+=s*g*np.sqrt(0.5*(1-pan)); dst[i:i+len(s),1]+=s*g*np.sqrt(0.5*(1+pan))
def lp(x,fc,order=2):
    X=np.fft.rfft(x,axis=0); f=np.fft.rfftfreq(x.shape[0],1/SR)
    H=1/np.sqrt(1+(f/fc)**(2*order)); return np.fft.irfft(X*(H[:,None] if x.ndim>1 else H),x.shape[0],axis=0)
def hp(x,fc,order=2):
    X=np.fft.rfft(x,axis=0); f=np.fft.rfftfreq(x.shape[0],1/SR)
    H=1/np.sqrt(1+(fc/np.maximum(f,1))**(2*order)); return np.fft.irfft(X*(H[:,None] if x.ndim>1 else H),x.shape[0],axis=0)
def reverb(x,decay=1.6,mix=0.25):
    L=int(SR*decay); t=np.arange(L)/SR
    ir=np.stack([rng.standard_normal(L),rng.standard_normal(L)],1)*np.exp(-t*6.9/decay)[:,None]
    ir=lp(ir,6000); ir/=np.sqrt((ir**2).sum(0))
    n=x.shape[0]+L; F=1<<(n-1).bit_length()
    y=np.fft.irfft(np.fft.rfft(x,F,axis=0)*np.fft.rfft(ir,F,axis=0),F,axis=0)[:x.shape[0]]
    return x*(1-mix)+y*mix*3
mid=lambda m:440*2**((m-69)/12)
def saw(f,t,det=0): ph=(f*(1+det)*t+rng.random())%1; return 2*ph-1
# --- drums
drums=buf(); kicks=[]
def kick():
    t=tt(0.45); f=42+140*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR
    body=np.sin(ph)*np.exp(-t*7.5); click=lp(rng.standard_normal(len(t)),4000)*np.exp(-t*300)*0.5
    return np.tanh((body+click)*1.6)*0.9
def hat(o=False):
    t=tt(0.3 if o else 0.06); n=hp(rng.standard_normal(len(t)),7000,3)
    return n*np.exp(-t*(14 if o else 80))*0.25
def clap():
    t=tt(0.35); n=hp(lp(rng.standard_normal(len(t)),5000),800)
    env=np.zeros(len(t))
    for k,d in enumerate([0,0.011,0.022]): env+=np.exp(-np.maximum(t-d,0)*120)*(t>=d)
    env+=0.7*np.exp(-np.maximum(t-0.03,0)*14)*(t>=0.03)
    return n*env*0.4
def snareroll(): pass
DROP=2.0; END=13.0
for b in range(int(DROP/B),int(END/B)):
    t=b*B; place(drums,kick(),t); kicks.append(t)
    place(drums,hat(),t+B/2,0.25,1.0); place(drums,hat(),t+B/4,-0.3,0.35); place(drums,hat(),t+3*B/4,0.3,0.35)
    if b%2==1: place(drums,clap(),t,0,1.0)
    if b%4==3: place(drums,hat(True),t+B/2,0.15,0.8)
# intro: soft filtered hats building
for k in range(8):
    t=k*B/2; place(drums,hat(),t,(-1)**k*0.3,0.15+0.06*k)
# snare build in last half second of intro
for k in range(8):
    t=1.5+k*B/8; place(drums,clap(),t,0,0.15+0.1*k)
# final hit
place(drums,kick(),END); place(drums,hat(True),END,0,1.2)
# --- sidechain env
side=np.ones(N); T=np.arange(N)/SR
for k in kicks:
    i=int(k*SR); m=T[i:]-k; side[i:]=np.minimum(side[i:],1-0.65*np.exp(-m*9))
# --- chords (supersaw pad)
prog=[(0,(57,60,64,69)),(2,(57,60,64,69)),(4,(53,57,60,65)),(6,(48,55,60,64)),(8,(55,59,62,67)),(10,(57,60,64,69)),(12,(53,57,60,65)),(13,(48,55,60,64))]
bassn={0:45,2:45,4:41,6:36,8:43,10:45,12:41,13:36}
pad=buf()
for i,(t0,notes) in enumerate(prog):
    t1=prog[i+1][0] if i+1<len(prog) else DUR
    d=t1-t0+0.3; t=tt(d)
    s=sum(saw(mid(n),t,dt) for n in notes for dt in (-0.008,0,0.009))/12
    env=np.minimum(t/0.05,1)*np.minimum(np.maximum(d-t,0)/0.3,1)
    place(pad,s*env,t0,-0.2,0.5); place(pad,np.roll(s,300)*env,t0,0.2,0.5)
pad=lp(pad,1200 ,2)
# intro filter sweep: crude — attenuate intro highs by mixing with heavier lp
padlo=lp(pad,350,2); w=np.clip((T-0.0)/DROP,0,1)[:,None]
pad=np.where((T<DROP)[:,None],padlo*(0.6+0.4*w)+pad*0.25*w,pad)
pad*=np.where(T<DROP,1,side)[:,None]
# --- bass
bass=buf()
for i,(t0,_) in enumerate(prog):
    if t0<DROP: continue
    t1=prog[i+1][0] if i+1<len(prog) else END
    f=mid(bassn[t0]-12)
    nb=int(round((t1-t0)/(B/2)))
    for k in range(nb):
        t=tt(B/2*0.9); s=np.sin(2*np.pi*f*t)+0.4*np.tanh(3*np.sin(2*np.pi*f*t))
        place(bass,s*np.minimum(t*200,1)*np.exp(-t*4)*0.45,t0+k*B/2)
bass[:,0]*=side; bass[:,1]*=side
# --- pluck arp (16ths) from drop
arp=buf()
for i,(t0,notes) in enumerate(prog):
    if t0<DROP: continue
    t1=prog[i+1][0] if i+1<len(prog) else END
    pat=[0,2,1,3,2,1,3,2]
    for k in range(int(round((t1-t0)/(B/4)))):
        n=notes[pat[k%8]]+12; t=tt(0.25)
        s=(np.sin(2*np.pi*mid(n)*t)+0.3*np.sin(4*np.pi*mid(n)*t)+0.1*saw(mid(n),t))*np.exp(-t*18)
        place(arp,s*0.14,t0+k*B/4,(-0.5 if k%2 else 0.5))
arp=reverb(arp,1.2,0.35)
# outro bell chord at END
bell=buf()
for n in (60,64,67,72,76):
    t=tt(2.0); s=(np.sin(2*np.pi*mid(n)*t)+0.4*np.sin(2*np.pi*mid(n)*2.01*t))*np.exp(-t*2.2)
    place(bell,s*0.12,END,0)
bell=reverb(bell,2.0,0.4)
mix=drums*1.0+pad*0.9+bass*1.0+arp*1.0+bell
mix=reverb(mix,0.8,0.08)
mix=hp(mix,30,2)
fade=np.ones(N); f0=int(14.2*SR); fade[f0:]=np.linspace(1,0,N-f0)
mix*=fade[:,None]
mix=np.tanh(mix/np.abs(mix).max()*1.3)/np.tanh(1.3)*0.89
pcm=(np.clip(mix,-1,1)*32767).astype('<i2')
with wave.open(sys.argv[1],'wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
print('ok')
