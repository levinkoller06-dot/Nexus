import math,sys
out=sys.argv[1]
NAVY,NAVY2,Y,LIGHT,INK,RED,GREY="#08192F","#051024","#F8B91E","#F8F9FB","#0F1E3A","#D92D20","#4B5563"
# honeycomb svg
def honey(id_):
    r=120; w=math.sqrt(3)*r; lines=[]
    for row in range(-1,8):
        for col in range(-1,13):
            cx=col*w+(w/2 if row%2 else 0); cy=row*1.5*r
            pts=[(cx+r*math.cos(math.radians(60*k-30)),cy+r*math.sin(math.radians(60*k-30))) for k in range(6)]
            lines.append("M"+" L".join(f"{x:.0f},{y:.0f}" for x,y in pts)+"Z")
    return f'<svg id="{id_}" class="honey" viewBox="0 0 2300 1400" width="2300" height="1400"><path d="{" ".join(lines)}" fill="none" stroke="{Y}" stroke-opacity=".28" stroke-width="3"/></svg>'
ICON={
 "doc":'<path d="M14 4h14l8 8v28a2 2 0 0 1-2 2H14a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="M24 16v10M24 32v.5"/>',
 "sync":'<path d="M38 18a14 14 0 0 0-26-4M10 30a14 14 0 0 0 26 4"/><path d="M12 6v8h8M36 42v-8h-8"/>',
 "db":'<ellipse cx="24" cy="11" rx="13" ry="5"/><path d="M11 11v26c0 3 6 5 13 5s13-2 13-5V11M11 24c0 3 6 5 13 5s13-2 13-5"/>',
 "warn":'<path d="M24 6 4 40h40z"/><path d="M24 18v10M24 34v.5"/>',
 "dollar":'<path d="M24 4v40M33 13c-2-3-5-4-9-4-5 0-9 2-9 6 0 9 18 5 18 14 0 4-4 7-9 7-4 0-8-2-10-5"/>',
 "clock":'<circle cx="24" cy="24" r="18"/><path d="M24 13v11l7 5"/>'}
def icon(k): return f'<svg viewBox="0 0 48 48" width="70" height="70" fill="none" stroke="{RED}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'
def chars(t,cls): return "".join(f'<span class="{cls}">{"&nbsp;" if c==" " else c}</span>' for c in t)
S=[]
def scene(s,d,th,html,js,hc=False):
    bgx=f'{honey("hc"+str(len(S)+1))}<i class="vig"></i>' if hc else ''
    S.append((s,d,th,bgx+html,js,hc))
HCJS=lambda n,s,d:f'tl.fromTo("#hc{n}",{{x:-120,y:-60}},{{x:-40,y:-20,duration:{d},ease:"none"}},{s});'

# 1 logo reveal
scene(0,3,"navy",'<i id="gl1" class="glowY"></i><div class="stack"><img id="lg1" class="logo" src="assets/logo.png" width="380" height="436" alt="HABEE Logo"/><h1 id="wm1" class="H wm">'+chars("HA","wa")+'<span class="yb">'+chars("BEE","wb")+'</span></h1></div>',
 'tl.fromTo("#hc1",{opacity:0},{opacity:1,duration:1.2,ease:"power1.out"},S);'
 'tl.fromTo("#gl1",{scale:.3,opacity:0},{scale:1.2,opacity:1,duration:1.6,ease:"power2.out"},S+.6);'
 'tl.fromTo("#lg1",{scale:0,rotation:-25,opacity:0},{scale:1,rotation:0,opacity:1,duration:.7,ease:"back.out(1.7)"},S+.9);'
 'tl.fromTo(".wa,.wb",{y:120,opacity:0},{y:0,opacity:1,duration:.4,ease:"expo.out",stagger:.08},S+1.7);',True)
# 2 pill
scene(3,2,"navy",'<div class="stack"><div id="p2" class="pill">KI-Automatisierung für Schweizer KMU</div><p id="s2" class="H sub2">Massgeschneidert. Modular. Bezahlbar.</p></div>',
 'tl.fromTo("#p2",{scale:2.2,opacity:0},{scale:1,opacity:1,duration:.45,ease:"expo.out"},S);'
 'tl.fromTo("#s2",{opacity:0,y:30},{opacity:1,y:0,duration:.4,ease:"expo.out"},S+.6);',True)
# 3 problem headline
scene(5,2,"light",'<div class="stack"><p id="k3" class="tag">Das Problem</p><div class="mask"><h1 id="h3a" class="H s150">Zu viel Administration.</h1></div><div class="mask"><h1 id="h3b" class="H s150">Zu wenig Zeit.</h1></div></div>',
 'tl.fromTo("#k3",{opacity:0,scale:.6},{opacity:1,scale:1,duration:.3,ease:"back.out(2)"},S);'
 'tl.fromTo("#h3a",{y:220},{y:0,duration:.45,ease:"expo.out"},S+.12);'
 'tl.fromTo("#h3b",{y:220},{y:0,duration:.45,ease:"expo.out"},S+.75);')
# 4 stat
scene(7,2.5,"light",'<div id="c4" class="statcard"><div class="H bignum"><span id="n4a">0</span>–<span id="n4b">0</span>%</div><p class="stxt">der Arbeitszeit von KMU-Mitarbeitenden fliesst in repetitive, manuelle Aufgaben, die automatisierbar wären.</p></div>',
 'tl.fromTo("#c4",{y:200,opacity:0},{y:0,opacity:1,duration:.5,ease:"expo.out"},S);'
 'const o4={a:0,b:0};tl.to(o4,{a:20,b:30,duration:1.1,ease:"power2.out",onUpdate:()=>{document.getElementById("n4a").textContent=Math.round(o4.a);document.getElementById("n4b").textContent=Math.round(o4.b);}},S+.2);')
# 5 pain cards
pains=[("doc","Manuelles Reporting, das Ihren Tag auffrisst"),("sync","Doppelte Datenerfassung in verschiedenen Systemen"),("db","Isolierte Tools, die nicht miteinander kommunizieren"),
       ("warn","Fehleranfällige, manuelle Prozesse"),("dollar","Teure Standardsoftware, die nicht passt"),("clock","Angst vor kostspieligen, endlosen IT-Projekten")]
scene(9.5,3.5,"light",'<div class="grid5">'+"".join(f'<div class="pc"><span class="ib">{icon(k)}</span><span class="pt">{t}</span></div>' for k,t in pains)+'</div>',
 'tl.fromTo(".pc",{y:120,opacity:0,scale:.9},{y:0,opacity:1,scale:1,duration:.4,ease:"back.out(1.6)",stagger:.3},S+.15);'
 'tl.fromTo(".grid5",{scale:1},{scale:1.04,duration:3.5,ease:"none"},S);')
# 6 better way
scene(13,1.5,"navy",'<div class="stack"><h1 class="H s130 cw nw">'+" ".join(f'<span class="w6">{w}</span>' for w in "Es gibt einen besseren Weg.".split())+'</h1><i id="u6" class="uline"></i></div>',
 'tl.fromTo(".w6",{y:80,opacity:0},{y:0,opacity:1,duration:.35,ease:"expo.out",stagger:.12},S+.05);'
 'tl.fromTo("#u6",{width:0},{width:900,duration:.5,ease:"power3.inOut"},S+.8);')
# 7 headline
scene(14.5,3,"navy",'<div class="lines7">'+"".join(f'<div class="mask"><h1 class="H s150 l7 {c}">{t}</h1></div>' for t,c in [("Automatisierung","cw"),("nach Mass.","cw"),("Mit KI effizient","cy"),("umgesetzt.","cy")])+'</div>',
 'tl.fromTo(".l7",{y:200},{y:0,duration:.5,ease:"expo.out",stagger:.18},S+.05);',True)
# 8 steps
steps=[("01","Engpass finden."),("02","Agent bauen."),("03","Zeit sparen.")]
scene(17.5,3,"navy",'<div class="steps"><i id="ln8" class="ln8"></i>'+"".join(f'<div class="st8"><span class="H num8">{n}</span><span class="H lab8">{t}</span></div>' for n,t in steps)+'</div>',
 'tl.fromTo("#ln8",{width:0},{width:1240,duration:1.8,ease:"power1.inOut"},S+.1);'
 'tl.fromTo(".st8",{scale:0,opacity:0},{scale:1,opacity:1,duration:.45,ease:"back.out(2)",stagger:.7},S+.1);',True)
# 9 solution
scene(20.5,2.5,"light",'<div class="stack"><p id="k9" class="tag">Die Lösung</p><h1 id="h9" class="H s110 nw">Massgeschneiderte KI-Agenten</h1><p id="t9" class="lead">die Ihre administrativen Prozesse automatisieren</p><div class="chips9"><span class="chip9">Modulare Architektur</span><span class="chip9">Endlich auch für KMU bezahlbar</span></div></div>',
 'tl.fromTo("#k9",{opacity:0,scale:.6},{opacity:1,scale:1,duration:.3,ease:"back.out(2)"},S);'
 'tl.fromTo("#h9",{opacity:0,y:60},{opacity:1,y:0,duration:.45,ease:"expo.out"},S+.1);'
 'tl.fromTo("#t9",{opacity:0},{opacity:1,duration:.4},S+.5);'
 'tl.fromTo(".chip9",{scale:0,opacity:0},{scale:1,opacity:1,duration:.35,ease:"back.out(2)",stagger:.2},S+.75);')
# 10 stats
scene(23,3,"navy",'<div class="stats">'
 '<div class="sc"><span class="H snum"><span id="n10a">0</span>+</span><span class="slab">KMU automatisiert</span></div>'
 '<div class="sc"><span class="H snum">Ø <span id="n10b">0</span> h</span><span class="slab">gespart pro Woche</span></div>'
 '<div class="sc"><span class="H snum">&lt; <span id="n10c">12</span> Wo.</span><span class="slab">bis erste Ergebnisse</span></div></div>',
 'tl.fromTo(".sc",{y:150,opacity:0},{y:0,opacity:1,duration:.5,ease:"expo.out",stagger:.15},S+.05);'
 'const o10={a:0,b:0,c:12};tl.to(o10,{a:16,b:12,c:4,duration:1.4,ease:"power2.out",onUpdate:()=>{document.getElementById("n10a").textContent=Math.round(o10.a);document.getElementById("n10b").textContent=Math.round(o10.b);document.getElementById("n10c").textContent=Math.round(o10.c);}},S+.2);',True)
# 11 checks
scene(26,2,"light",'<div class="checks">'+"".join(f'<div class="ck"><span class="dot"><svg viewBox="0 0 24 24" width="56" height="56" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 10 17.5 19 7"/></svg></span><span class="H ckt">{t}</span></div>' for t in ["Schweizer Anbieter","Kein Vendor Lock-in","Faire KMU-Preise"])+'</div>',
 'tl.fromTo(".ck",{x:-300,opacity:0},{x:0,opacity:1,duration:.4,ease:"expo.out",stagger:.35},S+.08);'
 'tl.fromTo(".dot",{scale:0},{scale:1,duration:.35,ease:"back.out(2.5)",stagger:.35},S+.2);')
# 12 CTA
scene(28,4,"navy",'<i id="gl12" class="glowY"></i><div class="stack"><img id="lg12" class="logo" src="assets/logo.png" width="250" height="287" alt="HABEE Logo"/><h1 id="wm12" class="H wm12">HA<span class="yb">BEE</span></h1><div id="b12" class="btn">Kostenloses Erstgespräch anfragen <span class="arr">→</span></div><p id="u12" class="url">habee.solutions</p></div>',
 'tl.fromTo("#gl12",{scale:.4,opacity:0},{scale:1.1,opacity:1,duration:1.2,ease:"power2.out"},S);'
 'tl.fromTo("#lg12",{scale:0,rotation:-20},{scale:1,rotation:0,duration:.6,ease:"back.out(1.8)"},S+.05);'
 'tl.fromTo("#wm12",{opacity:0,y:40},{opacity:1,y:0,duration:.4,ease:"expo.out"},S+.35);'
 'tl.fromTo("#b12",{opacity:0,y:60},{opacity:1,y:0,duration:.45,ease:"expo.out"},S+.7);'
 'tl.to("#b12",{scale:.94,duration:.08,ease:"power1.in"},S+2.25);tl.to("#b12",{scale:1,duration:.3,ease:"back.out(3)"},S+2.33);'
 'tl.fromTo(".arr",{x:0},{x:14,duration:.3,ease:"power2.inOut",yoyo:true,repeat:3},S+1.3);'
 'tl.fromTo("#u12",{opacity:0},{opacity:1,duration:.5},S+1.1);',True)

SFX=[("riser","riser",0,1.15,3.0,.5),("spark1","sparkle",.9,0,1.5,.5)]+\
 [(f"ltr{k}","click-soft",1.66+.08*k,0,.3,.35) for k in range(5)]+\
 [("imp2","impact-bass-2",3.0,0,.9,.5),("pop2","pop",2.9,0,.6,.5),("wh2","whoosh-short",3.45,0,.5,.35),
  ("wh3a","whoosh-short",4.98,0,.5,.5),("wh3b","whoosh",5.62,0,.5,.45),("err4","error",6.55,0,1.4,.4)]+\
 [(f"card{k}","click",9.61+.3*k,0,.36,.5) for k in range(6)]+\
 [("cine6","whoosh-cinematic",10.45,0,3.2,.4),("chime7","chime",14.1,0,2.4,.5),("wh7","whoosh",14.46,0,.5,.4),("spk7","sparkle",14.95,0,1.5,.3)]+\
 [(f"ping8{k}","ping",17.29+.7*k,0,1.2,.4) for k in range(3)]+\
 [("pop9a","pop",20.4,0,.6,.45),("pop9b","pop",21.15,0,.6,.4),("pop9c","pop",21.35,0,.6,.45),("wh10","whoosh",22.88,0,.5,.45)]+\
 [(f"tick10{k}","click-soft",23.2+.14*k,0,.3,.25) for k in range(8)]+\
 [(f"chk{k}","pop",26.1+.35*k,0,.6,.45) for k in range(3)]+\
 [("imp12","impact-bass-1",28.0,0,.6,.35),("spk12","sparkle",28.08,0,1.6,.4),("press12","click",30.21,0,.36,.75),("note12","notification",30.28,0,1.6,.35)]

css=f'''
@font-face{{font-family:"DM Sans";font-weight:500;font-style:normal;src:url("assets/fonts/dm-sans-latin-500-normal.woff2") format("woff2")}}
@font-face{{font-family:"DM Sans";font-weight:600;font-style:normal;src:url("assets/fonts/dm-sans-latin-600-normal.woff2") format("woff2")}}
@font-face{{font-family:"DM Sans";font-weight:700;font-style:normal;src:url("assets/fonts/dm-sans-latin-700-normal.woff2") format("woff2")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:{NAVY}}}
#root{{width:100%;height:100%;position:relative;overflow:hidden;background:{NAVY};font-family:Inter,ui-sans-serif,system-ui,sans-serif}}
.scene{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.bg{{position:absolute;inset:0}}
.navy .bg{{background:radial-gradient(ellipse at 50% 40%,#0d2347 0%,{NAVY} 55%,{NAVY2} 100%)}}.navy{{color:#FFFFFF}}
.light .bg{{background:{LIGHT}}}.light{{color:{INK}}}
.honey{{position:absolute;left:0;top:0;display:block}}
.vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(8,25,47,.55) 0%,rgba(5,16,36,.2) 45%,rgba(5,16,36,.85) 100%)}}
.H{{font-family:"DM Sans",Inter,sans-serif;font-weight:700;letter-spacing:-0.025em;line-height:1.05}}
.stack{{position:relative;display:flex;flex-direction:column;align-items:center;gap:34px;text-align:center}}
.cw{{color:#FFFFFF}}.cy{{color:{Y}}}.yb{{color:{Y}}}
.s110{{font-size:110px}}.s130{{font-size:130px}}.nw{{white-space:nowrap}}.s150{{font-size:150px}}
.glowY{{position:absolute;width:1100px;height:1100px;border-radius:50%;background:radial-gradient(circle,rgba(248,185,30,.32),rgba(248,185,30,0) 62%)}}
.logo{{display:block}}
.wm{{font-size:190px;display:flex;color:#FFFFFF}}.wm span{{display:block}}.wm .yb{{display:flex}}
.pill{{font-size:70px;font-weight:600;color:{Y};padding:30px 64px;border:3px solid rgba(248,185,30,.75);border-radius:999px;background:rgba(248,185,30,.14)}}
.sub2{{font-size:64px;color:#E5E7EB;font-weight:500}}
.tag{{font-size:44px;font-weight:600;color:{INK};background:#FBEFD2;padding:16px 44px;border-radius:999px}}
.mask{{position:relative;overflow:hidden;padding:4px 20px 18px}}
.statcard{{width:1760px;display:flex;align-items:center;gap:60px;padding:80px 70px;border:3px solid #F3C4BF;border-radius:48px;background:#FFFFFF}}
.bignum{{font-size:190px;color:{RED};white-space:nowrap;flex:none}}
.stxt{{font-size:50px;color:{GREY};line-height:1.35;width:760px;flex:none}}
.grid5{{display:grid;grid-template-columns:repeat(3,560px);gap:30px}}
.pc{{height:230px;background:#FFFFFF;border:2px solid #E5E7EB;border-radius:36px;padding:34px 36px;display:flex;align-items:center;gap:30px;box-shadow:0 18px 40px rgba(15,30,58,.06)}}
.ib{{flex:none;width:104px;height:104px;border-radius:24px;background:#FDE8E7;display:flex;align-items:center;justify-content:center}}
.ib svg{{display:block}}
.pt{{font-size:36px;font-weight:600;line-height:1.3;color:{INK}}}
.uline{{display:block;height:10px;width:0;background:{Y};border-radius:5px}}
.lines7{{display:flex;flex-direction:column;align-items:flex-start;position:relative}}
.lines7 .mask{{padding:0 20px 6px}}
.steps{{position:relative;width:1500px;display:flex;justify-content:space-between}}
.ln8{{position:absolute;left:130px;top:100px;height:6px;width:0;background:{Y};border-radius:3px;display:block}}
.st8{{position:relative;width:420px;display:flex;flex-direction:column;align-items:center;gap:40px}}
.num8{{width:200px;height:200px;border-radius:50%;background:{Y};color:{NAVY};font-size:84px;display:flex;align-items:center;justify-content:center}}
.lab8{{font-size:72px;color:#FFFFFF;white-space:nowrap}}
.lead{{font-size:54px;color:{GREY}}}
.chips9{{display:flex;gap:30px}}
.chip9{{display:block;font-size:52px;font-weight:700;color:{NAVY};background:{Y};padding:24px 50px;border-radius:999px}}
.stats{{display:flex;gap:110px;position:relative}}
.sc{{display:flex;flex-direction:column;gap:22px}}
.snum{{font-size:170px;color:{Y};white-space:nowrap}}
.slab{{font-size:50px;color:#FFFFFF;font-weight:500}}
.checks{{display:flex;flex-direction:column;gap:46px}}
.ck{{display:flex;align-items:center;gap:44px}}
.dot{{width:110px;height:110px;border-radius:50%;background:{Y};display:flex;align-items:center;justify-content:center;flex:none}}
.dot svg{{display:block}}
.ckt{{font-size:110px;color:{INK}}}
.wm12{{font-size:150px;color:#FFFFFF}}
.btn{{font-size:58px;font-weight:700;color:{NAVY};background:{Y};padding:34px 70px;border-radius:24px;display:flex;align-items:center;gap:24px}}
.arr{{display:block}}
.url{{font-size:46px;color:#CBD5E1;letter-spacing:.04em}}
'''
body="";js=""
for k,(s,d,th,html,j,hc) in enumerate(S):
    n=k+1
    body+=f'      <section id="s{n}" class="scene clip {th}" data-start="{s}" data-duration="{d}" data-track-index="{k%3}">\n        <div class="bg"></div>\n        {html}\n      </section>\n'
    js+=f'      {{const S={s};{j}{HCJS(n,s,d) if hc else ""}}}\n'
aud='      <audio id="music" src="assets/music.mp3" data-start="0" data-duration="32" data-track-index="10" data-volume="0.7"></audio>\n'
for n,(i,f,s,ms,d,v) in enumerate(SFX):
    aud+=f'      <audio id="sfx-{i}" src="assets/sfx/{f}.mp3" data-start="{s:.2f}" data-media-start="{ms}" data-duration="{d}" data-track-index="{11+n}" data-volume="{v}"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="32" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>
'''
open(out,'w').write(html)
