import numpy as np, wave, sys
SR=44100
def lp(x,fc):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/SR); return np.fft.irfft(X/np.sqrt(1+(f/fc)**4),len(x))
def bp(x,lo,hi):
    X=np.fft.rfft(x); f=np.fft.rfftfreq(len(x),1/SR); X[(f<lo)|(f>hi)]=0; return np.fft.irfft(X,len(x))
def buzz(dur,pan_path,vol_path,pitch_path,seed=1):
    rng=np.random.default_rng(seed); n=int(dur*SR); t=np.arange(n)/SR; u=t/dur
    f0=225*np.interp(u,*pitch_path)*(1+0.012*np.sin(2*np.pi*6.3*t)+0.006*np.sin(2*np.pi*13.7*t))
    ph=2*np.pi*np.cumsum(f0)/SR
    s=sum(np.sin(k*ph+rng.random()*6)/k**0.9 for k in range(1,28))
    s=np.tanh(s*0.8)
    s=lp(s,2600)+0.25*bp(s,900,1800)
    s+=0.06*lp(rng.standard_normal(n),3000)*(1+np.sin(ph))
    am=0.8+0.2*np.sin(ph*0.5)
    s*=am
    v=np.interp(u,*vol_path); fade=np.minimum(np.minimum(t/0.08,1),np.minimum((dur-t)/0.15,1))
    s=s/np.abs(s).max()*v*fade
    p=np.interp(u,*pan_path)
    L=s*np.sqrt(0.5*(1-p)); R=s*np.sqrt(0.5*(1+p))
    return np.stack([L,R],1)
def save(x,fn):
    x=x/np.abs(x).max()*0.85
    with wave.open(fn,'wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((x*32767).astype('<i2').tobytes())
# A: left->right across intro
save(buzz(2.2,([0,1],[-0.9,0.9]),([0,.45,.55,1],[.15,1,1,.15]),([0,.5,1],[1.04,1.0,0.95]),1),'buzzA.wav')
# B: across headline
save(buzz(2.3,([0,1],[-0.9,0.9]),([0,.4,.6,1],[.15,1,1,.12]),([0,.5,1],[1.05,1.0,0.94]),2),'buzzB.wav')
# C: from right, then hover
save(buzz(3.6,([0,.4,1],[0.9,0.35,0.3]),([0,.35,1],[.2,1,.75]),([0,.35,.4,1],[1.03,1.0,0.97,0.97]),3),'buzzC.wav')
