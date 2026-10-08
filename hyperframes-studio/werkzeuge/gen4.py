import math,sys
out=sys.argv[1]
CREAM,DARK,CLAY,KRAFT,INK2="#F0EEE6","#191919","#D97757","#D4A27F","#262624"
lens=[200,150,185,120,200,140,190,125,195,145,180,130]
def spark(id_,col,size,cls="spark"):
    p=[]
    for i,l in enumerate(lens):
        a=2*math.pi*i/12
        p.append(f'<line x1="{220+28*math.cos(a):.1f}" y1="{220+28*math.sin(a):.1f}" x2="{220+l*math.cos(a):.1f}" y2="{220+l*math.sin(a):.1f}" stroke="{col}" stroke-width="34" stroke-linecap="round"/>')
    return f'<svg id="{id_}" class="{cls}" viewBox="0 0 440 440" width="{size}" height="{size}">{"".join(p)}</svg>'
def chars(txt,cls): return "".join(f'<span class="{cls}">{"&nbsp;" if c==" " else c}</span>' for c in txt)
S=[]  # (start,dur,theme,html,js)
def scene(s,d,th,html,js): S.append((s,d,th,html,js))

# 1 cursor typing
scene(0,1.0,"dark",f'<div class="term"><span class="pr">&gt;</span>{chars("Hallo?","c1")}<i id="cur1" class="cur"></i></div>',
 'tl.fromTo(".c1",{opacity:0},{opacity:1,duration:.01,stagger:.09},S+.18);'
 'for(let k=0;k<6;k++){tl.set("#cur1",{opacity:k%2?1:0},S+k*.16);}')
# 2 spark awakens
scene(1.0,1.0,"dark",f'<i id="glow2" class="glow"></i><i id="ring2" class="ring"></i>{spark("sp2",CLAY,220)}',
 'tl.fromTo("#sp2",{scale:.1,rotation:-160,opacity:0},{scale:1,rotation:0,opacity:1,duration:.9,ease:"power2.in"},S);'
 'tl.fromTo("#glow2",{scale:.2,opacity:0},{scale:1.6,opacity:1,duration:1,ease:"power2.in"},S);'
 'tl.fromTo("#ring2",{scale:3,opacity:0},{scale:.4,opacity:.9,duration:.95,ease:"power3.in"},S);')
# 3 drop: Ich bin Claude
scene(2.0,1.0,"cream",f'<div id="w3" class="stack">{spark("sp3",CLAY,230)}<h1 class="serif s200">Ich bin <b class="c-clay">Claude.</b></h1></div>',
 'tl.fromTo("#w3",{scale:1.25},{scale:1,duration:.6,ease:"expo.out"},S);'
 'tl.fromTo("#sp3",{rotation:-90},{rotation:30,duration:1,ease:"power2.out"},S);')
# 4 KI
scene(3.0,0.5,"clay",'<h1 id="k4" class="sans s560">KI</h1>',
 'tl.fromTo("#k4",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:.22,ease:"expo.out"},S);')
# 5 Assistent
scene(3.5,0.5,"dark",'<div class="mask"><h1 id="a5" class="serif s260"><i>Assistent.</i></h1></div>',
 'tl.fromTo("#a5",{y:320},{y:0,duration:.28,ease:"expo.out"},S);')
# 6 chat
scene(4.0,1.0,"cream",f'<div class="chat"><div id="u6" class="bub user">Kannst du mir helfen?</div><div id="c6" class="bub bot">{spark("sp6",CLAY,64,"spark mini")}<span>{chars("Klar! Lass uns loslegen.","c6")}</span></div></div>',
 'tl.fromTo("#u6",{scale:.6,opacity:0,y:40},{scale:1,opacity:1,y:0,duration:.25,ease:"back.out(2)"},S+.05);'
 'tl.fromTo("#c6",{scale:.6,opacity:0,y:40},{scale:1,opacity:1,y:0,duration:.25,ease:"back.out(2)"},S+.42);'
 'tl.fromTo(".c6",{opacity:0},{opacity:1,duration:.01,stagger:.018},S+.5);'
 'tl.fromTo("#sp6",{rotation:0},{rotation:120,duration:.6,ease:"power2.out"},S+.42);')
# 7 glitch Anthropic
scene(5.0,1.0,"dark",'<div class="stack"><p id="k7" class="kick">Gebaut von</p><div class="gl"><h1 id="g7a" class="serif s250 gcopy c-clay" data-layout-allow-overlap>Anthropic</h1><h1 id="g7b" class="serif s250 gcopy c-kraft" data-layout-allow-overlap>Anthropic</h1><h1 id="g7" class="serif s250 c-cream" data-layout-allow-overlap>Anthropic</h1></div></div>',
 'const J=[[-28,22,0],[34,-18,.06],[-12,40,.12],[22,-30,.18],[-40,10,.24],[8,-6,.3],[0,0,.36]];'
 'for(const [a,b,t] of J){tl.set("#g7a",{x:a,opacity:a?1:0},S+.02+t);tl.set("#g7b",{x:b,opacity:b?1:0},S+.02+t);tl.set("#g7",{x:-a*.3},S+.02+t);}'
 'tl.fromTo("#k7",{opacity:0,y:20},{opacity:1,y:0,duration:.25,ease:"expo.out"},S+.45);')
# 8 fact cards
cards=[("2021","gegründet"),("San Francisco","Hauptsitz"),("KI-Sicherheit","Forschung & Produkte")]
scene(6.0,1.0,"cream",'<div class="cards">'+"".join(f'<div class="card8"><span class="serif cnum">{a}</span><span class="clab">{b}</span></div>' for a,b in cards)+'</div>',
 'tl.fromTo(".card8",{y:500,rotation:(i)=>[-6,4,-3][i]},{y:0,rotation:0,duration:.35,ease:"expo.out",stagger:.15},S+.02);')
# 9-11 values
scene(7.0,0.5,"clay",'<h1 id="v9" class="serif s300">Hilfreich.</h1>','tl.fromTo("#v9",{x:-1200},{x:0,duration:.22,ease:"expo.out"},S);')
scene(7.5,0.5,"dark",'<h1 id="v10" class="serif s300 c-cream">Ehrlich.</h1>','tl.fromTo("#v10",{y:500},{y:0,duration:.22,ease:"expo.out"},S);')
scene(8.0,0.5,"cream",'<h1 id="v11" class="serif s300 c-clay">Harmlos.</h1>','tl.fromTo("#v11",{scale:.3,opacity:0},{scale:1,opacity:1,duration:.22,ease:"back.out(2)"},S);')
# 12 code editor
code=[('<span class="kw">const</span> claude = <span class="kw">new</span> Assistent();',None),
      ('claude.hilf(<span class="st">"dir"</span>);',None),
      ('<span class="cm">// → Gerne. Womit fangen wir an?</span>',None)]
def typed(htmlline,cls):
    # wrap only visible text chars, keep tags
    out="";i=0
    while i<len(htmlline):
        if htmlline[i]=="<":
            j=htmlline.index(">",i); out+=htmlline[i:j+1]; i=j+1
        else:
            c=htmlline[i]
            if c=="&":
                j=htmlline.index(";",i); c=htmlline[i:j+1]; i=j+1
            else: i+=1
            out+=f'<span class="{cls}">{"&nbsp;" if c==" " else c}</span>'
    return out
lines="".join(f'<div class="cl"><span class="ln">{n+1}</span>{typed(l,"t12")}</div>' for n,(l,_) in enumerate(code))
scene(8.5,1.0,"dark",f'<div id="win12" class="win"><div class="bar"><i></i><i></i><i></i><span>claude.js</span></div><div class="code">{lines}</div></div>',
 'tl.fromTo("#win12",{scale:.85,opacity:0},{scale:1,opacity:1,duration:.2,ease:"expo.out"},S);'
 'tl.fromTo(".t12",{opacity:0},{opacity:1,duration:.001,stagger:.0085},S+.12);')
# 13 slot machine
words=["Schreiben","Analysieren","Coden","Übersetzen","Recherchieren"]
scene(9.5,1.0,"clay",'<div class="slot"><p class="kick lbl">Claude kann</p><div class="win13"><div id="list13">'+"".join(f'<div class="w13 serif">{w}</div>' for w in words)+'</div></div></div>',
 'for(let k=1;k<5;k++){tl.to("#list13",{y:-200*k,duration:.14,ease:"back.out(2)"},S+.08+(k-1)*.2);}')
# 14 zoom through spark
scene(10.5,1.0,"cream",f'{spark("sp14",DARK,300)}<h1 id="t14" class="sans s90 z14">Bereit?</h1>',
 'tl.fromTo("#t14",{opacity:0,y:30},{opacity:1,y:0,duration:.2,ease:"expo.out"},S+.02);'
 'tl.to("#t14",{opacity:0,duration:.1},S+.4);'
 'tl.fromTo("#sp14",{scale:1,rotation:0},{scale:28,rotation:140,duration:.85,ease:"power4.in"},S+.1);')
# 15 everywhere
scene(11.5,1.0,"dark",'<div class="rows"><h1 class="r15 serif s170 c-cream">Im Browser.</h1><h1 class="r15 serif s170 c-clay">Auf dem Handy.</h1><h1 class="r15 serif s170 c-kraft">In deinem Code.</h1></div>',
 'tl.fromTo(".r15",{x:-900,opacity:0},{x:0,opacity:1,duration:.25,ease:"expo.out",stagger:.15},S+.03);')
# 16 slam
scene(12.5,0.5,"clay",'<h1 id="c16" class="serif s420"><b>Claude</b></h1>',
 'tl.fromTo("#c16",{scale:1.7,opacity:0},{scale:1,opacity:1,duration:.2,ease:"expo.out"},S);')
# 17 final
scene(13.0,2.0,"cream",f'<div class="stack">{spark("sp17",CLAY,240)}<h1 id="t17" class="serif s280"><b>Claude</b></h1><p id="k17" class="kick">von Anthropic</p><p id="m17" class="sub">Hilfreich · Ehrlich · Harmlos</p></div>',
 'tl.fromTo("#sp17",{scale:0,rotation:-200},{scale:1,rotation:0,duration:.6,ease:"back.out(1.8)"},S+.02);'
 'tl.to("#sp17",{rotation:60,duration:1.4,ease:"none"},S+.6);'
 'tl.fromTo("#t17",{opacity:0,y:60},{opacity:1,y:0,duration:.45,ease:"expo.out"},S+.15);'
 'tl.fromTo("#k17",{opacity:0,y:20},{opacity:1,y:0,duration:.35,ease:"expo.out"},S+.4);'
 'tl.fromTo("#m17",{opacity:0},{opacity:1,duration:.4,ease:"power1.out"},S+.65);')

# SFX: (id,file,start,mediaStart,dur,vol)
SFX=[("typing1","typing",0.08,0.4,0.85,0.8),
 ("riser","riser",0.0,2.15,2.0,0.55),
 ("impact3","impact-bass-2",2.0,0,0.8,0.5),
 ("spark3","sparkle",2.02,0,1.2,0.45),
 ("wh4","whoosh-short",2.86,0,0.55,0.7),
 ("wh5","whoosh",3.36,0,0.55,0.55),
 ("pop6a","pop",3.95,0,0.6,0.55),
 ("note6","notification",4.38,0,1.0,0.35),
 ("key6","key-press",4.55,0,0.4,0.8),
 ("glitch7","glitch-1",4.86,0,0.6,0.45),
 ("click8a","click",6.0,0,0.36,0.7),("click8b","click-soft",6.15,0,0.36,0.7),("click8c","click",6.30,0,0.36,0.6),
 ("wh9","whoosh-short",6.86,0,0.5,0.6),("wh10","whoosh",7.36,0,0.5,0.45),("pop11","pop",7.9,0,0.6,0.5),
 ("type12","typing",8.55,0.4,0.9,0.7),
 ("tick13a","click-soft",9.54,0,0.3,0.7),("tick13b","click-soft",9.74,0,0.3,0.7),("tick13c","click-soft",9.94,0,0.3,0.7),("tick13d","click-soft",10.14,0,0.3,0.7),
 ("ping13","ping",9.92,0,1.0,0.35),
 ("zoom14","whoosh-cinematic",9.4,0.4,2.3,0.5),
 ("pop15a","pop",11.42,0,0.5,0.4),("pop15b","pop",11.57,0,0.5,0.45),("pop15c","pop",11.72,0,0.5,0.5),
 ("impact16","impact-bass-1",12.5,0,0.5,0.4),
 ("chime17","chime",12.6,0,2.4,0.6),("spark17","sparkle",13.05,0,1.5,0.35)]

css=f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:{DARK}}}
#root{{width:100%;height:100%;position:relative;overflow:hidden;background:{DARK};font-family:Inter,ui-sans-serif,system-ui,sans-serif}}
.scene{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.bg{{position:absolute;inset:0}}
.cream .bg{{background:{CREAM}}}.cream{{color:{DARK}}}
.dark .bg{{background:{DARK}}}.dark{{color:{CREAM}}}
.clay .bg{{background:{CLAY}}}.clay{{color:{DARK}}}
.serif{{font-family:"EB Garamond",Georgia,serif;font-weight:400;letter-spacing:-0.03em;line-height:1}}
.sans{{font-family:Inter,sans-serif;font-weight:800;letter-spacing:-0.03em;line-height:1}}
b{{font-weight:700}}
.c-clay{{color:#C6613F}}.dark .c-clay{{color:{CLAY}}}.c-kraft{{color:{KRAFT}}}.c-cream{{color:{CREAM}}}
.s90{{font-size:90px}}.s130{{font-size:130px}}.s170{{font-size:170px}}.s200{{font-size:200px}}.s250{{font-size:250px}}.s260{{font-size:260px}}.s280{{font-size:280px}}.s300{{font-size:300px}}.s420{{font-size:420px}}.s560{{font-size:560px}}
.stack{{position:relative;display:flex;flex-direction:column;align-items:center;gap:28px;text-align:center}}
.kick{{font-size:40px;font-weight:600;letter-spacing:.26em;text-transform:uppercase;color:#C6613F}}
.dark .kick{{color:{CLAY}}}
.sub{{font-size:46px;color:#55544d}}
.spark{{display:block}}
.term{{position:relative;display:flex;align-items:center;font-family:"JetBrains Mono",monospace;font-size:150px;color:{CREAM}}}
.pr{{color:{CLAY};margin-right:50px}}
.cur{{display:block;width:80px;height:150px;background:{CLAY};margin-left:14px}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(217,119,87,.55),rgba(217,119,87,0) 65%)}}
.ring{{position:absolute;width:700px;height:700px;border-radius:50%;border:6px solid {CLAY}}}
.mask{{position:relative;overflow:hidden;padding:30px 60px 60px}}
.chat{{position:relative;width:1300px;display:flex;flex-direction:column;gap:40px}}
.bub{{font-size:64px;padding:34px 50px;border-radius:44px;max-width:1100px;display:flex;align-items:center;gap:30px}}
.user{{align-self:flex-end;background:{DARK};color:{CREAM};border-bottom-right-radius:10px}}
.bot{{align-self:flex-start;background:#FFFFFF;color:{DARK};border-bottom-left-radius:10px;box-shadow:0 20px 60px rgba(0,0,0,.12)}}
.mini{{flex:none}}
.gl{{position:relative;display:flex;align-items:center;justify-content:center;width:1500px;height:300px}}
.gl h1{{position:absolute}}
.gcopy{{opacity:0}}
.cards{{display:flex;gap:40px}}
.card8{{width:520px;height:440px;background:{DARK};border-radius:36px;padding:50px;display:flex;flex-direction:column;justify-content:flex-end;gap:18px}}
.cnum{{font-size:96px;color:{KRAFT};line-height:1.02}}
.clab{{font-size:36px;color:#b9b6aa;font-weight:500}}
.win{{width:1500px;background:{INK2};border-radius:28px;overflow:hidden;box-shadow:0 40px 120px rgba(0,0,0,.5)}}
.bar{{display:flex;align-items:center;gap:16px;padding:26px 34px;background:#30302e}}
.bar i{{display:block;width:22px;height:22px;border-radius:50%;background:#55544d}}
.bar i:first-child{{background:{CLAY}}}
.bar span{{margin-left:20px;font-family:"JetBrains Mono",monospace;font-size:28px;color:#9a988f}}
.code{{padding:50px 50px 60px;font-family:"JetBrains Mono",monospace;font-size:54px;color:{CREAM};display:flex;flex-direction:column;gap:22px}}
.cl{{display:flex;white-space:pre}}
.ln{{color:#6b6a63;width:70px;flex:none}}
.kw{{color:{CLAY}}}.st{{color:{KRAFT}}}.cm{{color:#8f8d84}}
.slot{{position:relative;display:flex;flex-direction:column;align-items:center;gap:30px}}
.clay .lbl{{color:{DARK}}}
.win13{{height:200px;overflow:hidden;width:1600px}}
.w13{{height:200px;font-size:180px;line-height:200px;font-weight:700;color:{DARK};text-align:center}}
.z14{{position:absolute;bottom:200px}}
.rows{{display:flex;flex-direction:column;gap:20px;align-items:flex-start}}
'''
body=""; js=""
for k,(s,d,th,html,j) in enumerate(S):
    body+=f'      <section id="s{k+1}" class="scene clip {th}" data-start="{s}" data-duration="{d}" data-track-index="{k%3}">\n        <div class="bg"></div>\n        {html}\n      </section>\n'
    js+=f'      {{const S={s};{j}}}\n'
aud=f'      <audio id="music" src="assets/music.mp3" data-start="0" data-duration="15" data-track-index="10" data-volume="0.75"></audio>\n'
for n,(i,f,s,ms,d,v) in enumerate(SFX):
    aud+=f'      <audio id="sfx-{i}" src="assets/sfx/{f}.mp3" data-start="{s}" data-media-start="{ms}" data-duration="{d}" data-track-index="{11+n}" data-volume="{v}"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="15" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>
'''
open(out,'w').write(html)
