# Erzeugt einen eigenen, lizenzfreien Beat (120 BPM, 58 s) - keine fremde Musik.
import numpy as np, wave, sys
SR=44100; DUR=58; BPM=120; beat=60/BPM
n=SR*DUR; t=np.arange(n)/SR; out=np.zeros(n)
def add(start,sig):
    i=int(start*SR); j=min(n,i+len(sig)); out[i:j]+=sig[:j-i]
k_t=np.arange(int(.35*SR))/SR
kick=np.sin(2*np.pi*(55+120*np.exp(-k_t*30))*k_t)*np.exp(-k_t*9)
h_t=np.arange(int(.06*SR))/SR
rng=np.random.default_rng(1)
hat=rng.standard_normal(len(h_t))*np.exp(-h_t*70)*0.25
clap=rng.standard_normal(int(.15*SR))*np.exp(-np.arange(int(.15*SR))/SR*30)*0.4
bass_notes=[55,55,65.4,49]  # A1 A1 C2 G1, ein Takt je Note
for b in range(int(DUR/beat)):
    s=b*beat
    sec=s
    intro = sec<4
    add(s,kick*(0.5 if intro else 0.9))
    if not intro:
        add(s+beat/2,hat)
        if b%2==1: add(s,clap)
for bar in range(DUR//2):
    f=bass_notes[bar%4]; s=bar*2.0
    bt=np.arange(int(1.9*SR))/SR
    sig=(np.sin(2*np.pi*f*bt)+0.3*np.sin(2*np.pi*2*f*bt))*np.exp(-bt*1.2)*0.35*(0.0 if s<4 else 1)
    add(s,sig)
    # sanfter Pad
    pt=np.arange(int(2*SR))/SR
    pad=sum(np.sin(2*np.pi*f*m*pt) for m in (4,5,6))*0.04*np.minimum(1,pt*4)*np.minimum(1,(2-pt)*4)
    add(s,pad)
fade=np.minimum(1,(DUR-t)/2.5); out*=fade
out/=np.max(np.abs(out))*1.15
data=(out*32767).astype(np.int16)
with wave.open(sys.argv[1],'wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())
