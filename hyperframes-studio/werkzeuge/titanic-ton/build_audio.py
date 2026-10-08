import numpy as np, wave, json, subprocess, re
SR=22050
exec(open('script.py').read())
def readwav(fn):
    with wave.open(fn) as w:
        sr=w.getframerate(); x=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(float)/32768
    return x,sr
LEAD=0.8; GAP=0.75
segs=[];t=LEAD
voice=[]
for i in range(len(SEG)):
    x,sr=readwav(f'seg{i:02d}.wav'); assert sr==SR
    d=len(x)/SR; segs.append({'start':round(t,3),'dur':round(d,3)}); t+=d+GAP
TOTAL=round(t+1.6,2)
N=int(TOTAL*SR); v=np.zeros(N)
for i,s in enumerate(segs):
    x,_=readwav(f'seg{i:02d}.wav'); a=int(s['start']*SR); v[a:a+len(x)]+=x
# lipsync envelope at 30 fps
fps=30; hop=SR//fps; env=[]
for k in range(int(TOTAL*fps)):
    w=v[k*hop:(k+1)*hop]; env.append(np.sqrt((w**2).mean()) if len(w) else 0)
env=np.array(env); env=env/np.percentile(env[env>0.005],95); env=np.clip(env,0,1)
env=np.where(env<0.08,0,env)
sm=np.copy(env)
for k in range(1,len(sm)): sm[k]=max(env[k],sm[k-1]*0.55)
lip=[round(float(e),2) for e in sm]
# captions: split each segment caption into chunks, time by char proportion
caps=[]
for i,(sp,cap) in enumerate(SEG):
    sents=re.split(r'(?<=[.!?:])\s+',cap)
    chunks=[]
    for s in sents:
        words=s.split()
        while words:
            take=words[:9] if len(words)>11 else words
            chunks.append(" ".join(take)); words=words[len(take):]
    L=sum(len(c) for c in chunks); t0=segs[i]['start']
    for c in chunks:
        d=segs[i]['dur']*len(c)/L; caps.append({'t':round(t0,2),'d':round(d,2),'text':c}); t0+=d
# write voice 44.1k
v44=np.interp(np.arange(int(TOTAL*44100))/44100,np.arange(N)/SR,v)
with wave.open('voice.wav','wb') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(44100);w.writeframes((np.clip(v44,-1,1)*32767*0.95).astype('<i2').tobytes())
json.dump({'total':TOTAL,'segs':segs,'lip':lip,'caps':caps},open('timing.json','w'))
print(TOTAL,[ (s['start'],s['dur']) for s in segs])
