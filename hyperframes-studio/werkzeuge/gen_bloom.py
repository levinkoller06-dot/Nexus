import sys
out=sys.argv[1]
TQ,TQD,TXT,GRY,BG,BG2="#77C8D2","#2F8C99","#1C1C1C","#5E616B","#FFFFFF","#F4F5F9"
S=[]
def scene(s,d,bg,html,js): S.append((s,d,bg,html,js))
# 1 logo
scene(0,3.75,BG,'<i class="ring r1"></i><i class="ring r2"></i><i class="ring r3"></i><div class="stack"><img id="lg1" class="logo" src="assets/img/logo.png" width="420" height="420" alt="Bloom Logo"/><p id="t1" class="lab">Coiffeur · Hair &amp; Nails</p></div>',
 'tl.fromTo("#lg1",{scale:.6,opacity:0},{scale:1,opacity:1,duration:1.2,ease:"expo.out"},S+.3);'
 'tl.fromTo(".ring",{scale:.5,opacity:.0},{scale:2.4,opacity:.0,duration:2.6,ease:"power2.out",keyframes:{opacity:[0,.55,0]},stagger:.35},S+.35);'
 'tl.fromTo("#t1",{opacity:0,y:20},{opacity:1,y:0,duration:.9,ease:"power3.out"},S+1.3);')
# 2 hero welcome
scene(3.75,3.75,BG,'<div class="heroWrap"><img id="hi2" class="heroImg" src="assets/img/hero.png" width="2020" height="814" alt="Salon Bloom"/></div><div id="p2" class="panel"><p class="lab">Fehraltorf</p><h1 class="G h1">Willkommen<br/>bei Bloom</h1><i class="bar"></i></div>',
 'tl.fromTo("#hi2",{scale:1.0,x:0},{scale:1.1,x:-40,duration:3.75,ease:"none"},S);'
 'tl.fromTo("#p2",{opacity:0,x:60},{opacity:1,x:0,duration:.9,ease:"power3.out"},S+.4);'
 'tl.fromTo("#p2 .bar",{width:0},{width:160,duration:.8,ease:"power2.inOut"},S+1.1);')
# 3 about
scene(7.5,3.75,BG2,'<div class="split"><div class="circ"><img id="ai3" src="assets/img/about.png" width="582" height="388" alt="Dominique Koller"/></div><div class="txt3"><p class="lab">Über mich</p><h2 class="G h2">Dominique Koller</h2><ul class="tl3"><li><b>Mit 14</b> die Ausbildung zur Coiffeuse</li><li><b>Coiffure Valentino</b> in Zürich</li><li><b>Seit 2009</b> selbstständig</li></ul></div></div>',
 'tl.fromTo(".circ",{scale:.7,opacity:0},{scale:1,opacity:1,duration:.9,ease:"expo.out"},S+.15);'
 'tl.fromTo("#ai3",{scale:1.15},{scale:1.0,duration:3.6,ease:"none"},S);'
 'tl.fromTo(".txt3 .lab,.txt3 .h2",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"power3.out",stagger:.15},S+.4);'
 'tl.fromTo(".tl3 li",{opacity:0,x:40},{opacity:1,x:0,duration:.6,ease:"power3.out",stagger:.35},S+1.0);')
# 4 paul mitchell
scene(11.25,3.15,BG,'<div class="stack"><p class="lab">Produkte</p><h2 class="G h2">Paul Mitchell</h2><div class="pills"><span class="pill">ohne Tierversuche</span><span class="pill">meist vegan</span><span class="pill">mehrfach ausgezeichnet</span></div><p class="note">Eine Firma mit Herz – für Professionalität und Umweltschutz.</p></div>',
 'tl.fromTo("#s4 .lab,#s4 .h2",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"power3.out",stagger:.15},S+.15);'
 'tl.fromTo("#s4 .pill",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.5,ease:"back.out(1.6)",stagger:.25},S+.8);'
 'tl.fromTo("#s4 .note",{opacity:0},{opacity:1,duration:.6},S+1.8);')
# 5 prices
rows=[("Damen","Waschen · Schneiden · Föhnen","ab 80.–"),("Herren","Waschen · Schneiden · Föhnen","ab 62.–"),("Balayage","","ab 100.–"),("Highlights","ganzer Kopf","ab 100.–"),("Kinder","je nach Alter","ab 15.–")]
scene(14.4,5.0,BG2,'<div class="price"><div class="ph"><p class="lab">Preise</p><h2 class="G h2">Ehrlich &amp; fair</h2></div><div class="plist">'+"".join(f'<div class="pr"><span class="pn">{a}<small>{b}</small></span><i class="dots"></i><span class="pp">{c}</span></div>' for a,b,c in rows)+'</div><p class="stud">Studenten erhalten 10 % auf Erwachsenenpreise</p></div>',
 'tl.fromTo("#s5 .ph",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"power3.out"},S+.15);'
 'tl.fromTo(".pr",{opacity:0,y:24},{opacity:1,y:0,duration:.5,ease:"power3.out",stagger:.3},S+.6);'
 'tl.fromTo(".dots",{scaleX:0},{scaleX:1,duration:.5,ease:"power2.out",stagger:.3,transformOrigin:"left center"},S+.75);'
 'tl.fromTo(".stud",{opacity:0},{opacity:1,duration:.6},S+2.6);')
# 6 impressions
scene(19.4,3.1,BG,'<div class="gal"><div class="gi g1"><img src="assets/img/salon.png" width="582" height="388" alt="Salon"/></div><div class="gi g2"><img src="assets/img/hero.png" width="2020" height="814" alt="Beim Schneiden"/></div><div class="gi g3"><img src="assets/img/cards.png" width="582" height="388" alt="Karten"/></div></div><p id="t6" class="lab cap6">Impressionen</p>',
 'tl.fromTo(".gi",{opacity:0,y:80},{opacity:1,y:0,duration:.9,ease:"power3.out",stagger:.2},S+.1);'
 'tl.fromTo(".gi img",{scale:1.12},{scale:1,duration:3.1,ease:"none"},S);'
 'tl.fromTo("#t6",{opacity:0},{opacity:1,duration:.6},S+.7);')
# 7 contact
scene(22.5,3.75,BG2,'<div class="stack"><p class="lab">Kontakt</p><h2 class="G h2">Allmendstrasse 1</h2><p class="sub">8320 Fehraltorf</p><div class="info"><span>Parkplätze vor dem Haus</span><i></i><span>Bus «Undermüli» in 2 Minuten</span></div></div>',
 'tl.fromTo("#s7 .lab,#s7 .h2,#s7 .sub",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"power3.out",stagger:.15},S+.15);'
 'tl.fromTo("#s7 .info",{opacity:0,y:20},{opacity:1,y:0,duration:.7,ease:"power3.out"},S+1.0);')
# 8 CTA
scene(26.25,3.75,BG,'<div class="stack"><img id="lg8" class="logo" src="assets/img/logo.png" width="300" height="300" alt="Bloom Logo"/><h2 class="G h2s">Jetzt Termin vereinbaren</h2><div id="b8" class="btn">078 238 44 79</div><p class="url">mybloom.ch</p></div>',
 'tl.fromTo("#lg8",{scale:.7,opacity:0},{scale:1,opacity:1,duration:1,ease:"expo.out"},S+.1);'
 'tl.fromTo("#s8 .h2s",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"power3.out"},S+.5);'
 'tl.fromTo("#b8",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},S+.85);'
 'tl.fromTo("#s8 .url",{opacity:0},{opacity:1,duration:.6},S+1.2);')

SFX=[("spk1","sparkle",0.3,0,1.8,.22),("wh2","whoosh-short",3.62,0,.5,.18),("wh3","whoosh-short",7.37,0,.5,.15),("wh5","whoosh-short",14.27,0,.5,.15),("wh7","whoosh-short",22.37,0,.5,.15),("chime8","chime",25.95,0,2.5,.28)]

css=f'''
@font-face{{font-family:"Julius Sans One";font-weight:400;src:url("assets/fonts/julius-sans-one-latin-400-normal.woff2") format("woff2")}}
@font-face{{font-family:"Noto Sans";font-weight:400;src:url("assets/fonts/noto-sans-latin-400-normal.woff2") format("woff2")}}
@font-face{{font-family:"Noto Sans";font-weight:600;src:url("assets/fonts/noto-sans-latin-600-normal.woff2") format("woff2")}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#fff}}
#root{{width:100%;height:100%;position:relative;overflow:hidden;background:#fff;font-family:"Noto Sans",sans-serif;color:{TXT}}}
.scene{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}}
.bg{{position:absolute;inset:0}}
.fade{{position:absolute;inset:0;background:#fff;pointer-events:none;opacity:0}}
.G{{font-family:"EB Garamond",Georgia,serif;font-weight:400;letter-spacing:-0.01em;line-height:1.05;color:{TQD}}}
.lab{{font-family:"Julius Sans One",sans-serif;font-size:34px;letter-spacing:.3em;text-transform:uppercase;color:{GRY}}}
.stack{{position:relative;display:flex;flex-direction:column;align-items:center;gap:30px;text-align:center}}
.logo{{display:block}}
.ring{{position:absolute;width:440px;height:440px;border-radius:50%;border:3px solid {TQ};display:block}}
.heroWrap{{position:absolute;inset:0;overflow:hidden}}
.heroImg{{position:absolute;left:0;top:0;width:2680px;height:1080px;object-fit:cover;object-position:30% 50%;display:block}}
.panel{{position:absolute;right:120px;top:270px;width:760px;padding:70px 70px 80px;background:rgba(255,255,255,.94);display:flex;flex-direction:column;gap:26px;box-shadow:0 30px 80px rgba(0,0,0,.08)}}
.h1{{font-size:130px}}
.bar{{display:block;height:5px;width:0;background:{TQ}}}
.split{{display:flex;align-items:center;gap:110px}}
.circ{{width:560px;height:560px;border-radius:50%;overflow:hidden;border:10px solid #fff;box-shadow:0 0 0 4px {TQ};flex:none;position:relative}}
.circ img{{position:absolute;left:-130px;top:-10px;width:840px;height:580px;object-fit:cover;display:block}}
.txt3{{display:flex;flex-direction:column;gap:24px;width:860px}}
.h2{{font-size:120px}}
.h2s{{font-size:96px}}
.tl3{{list-style:none;display:flex;flex-direction:column;gap:20px;margin-top:10px}}
.tl3 li{{font-size:44px;color:{GRY};padding-left:40px;position:relative}}
.tl3 li::before{{content:"";position:absolute;left:0;top:24px;width:16px;height:16px;border-radius:50%;background:{TQ}}}
.tl3 b{{color:{TXT};font-weight:600}}
.pills{{display:flex;gap:24px}}
.pill{{display:block;font-size:42px;padding:20px 44px;border-radius:999px;border:3px solid {TQ};color:{TXT}}}
.note{{font-size:40px;color:{GRY};font-family:"EB Garamond",serif;font-style:italic}}
.price{{display:flex;flex-direction:column;align-items:center;gap:36px;width:1300px}}
.ph{{display:flex;flex-direction:column;align-items:center;gap:14px}}
.plist{{width:100%;display:flex;flex-direction:column;gap:18px}}
.pr{{display:flex;align-items:flex-end;gap:24px;font-size:50px}}
.pn{{display:flex;align-items:baseline;gap:22px;font-family:"EB Garamond",serif;font-size:62px;color:{TXT};white-space:nowrap}}
.pn small{{font-family:"Noto Sans",sans-serif;font-size:30px;color:{GRY}}}
.dots{{flex:1;display:block;height:0;border-bottom:3px dotted {TQ};margin-bottom:16px}}
.pp{{font-size:54px;font-weight:600;color:{TQD};white-space:nowrap}}
.stud{{font-size:36px;color:{GRY}}}
.gal{{position:relative;width:1700px;height:760px}}
.gi{{position:absolute;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.12);border:10px solid #fff}}
.gi img{{width:100%;height:100%;object-fit:cover;display:block}}
.g1{{left:0;top:120px;width:620px;height:430px}}
.g2{{left:560px;top:0;width:640px;height:700px;z-index:2}}
.g2 img{{object-position:22% 50%}}
.g3{{left:1120px;top:180px;width:580px;height:410px}}
.cap6{{position:absolute;bottom:70px}}
.sub{{font-size:56px;color:{GRY}}}
.info{{display:flex;align-items:center;gap:30px;font-size:38px;color:{GRY}}}
.info i{{display:block;width:12px;height:12px;border-radius:50%;background:{TQ}}}
.btn{{font-size:64px;font-weight:600;color:{TXT};background:{TQ};padding:28px 80px;border-radius:999px;letter-spacing:.02em}}
.url{{font-family:"Julius Sans One",sans-serif;font-size:40px;letter-spacing:.2em;color:{GRY}}}
'''
body="";js=""
for k,(s,d,bg,html,j) in enumerate(S):
    n=k+1
    body+=f'      <section id="s{n}" class="scene clip" data-start="{s}" data-duration="{d}" data-track-index="{k%2}">\n        <div class="bg" style="background:{bg}"></div>\n        {html}\n        <i class="fade" id="f{n}"></i>\n      </section>\n'
    fin='' if n==1 else f'tl.fromTo("#f{n}",{{opacity:1}},{{opacity:0,duration:.35,ease:"power1.out"}},S);'
    fout=f'tl.fromTo("#f{n}",{{opacity:0}},{{opacity:1,duration:.3,ease:"power1.in",immediateRender:false}},S+{d}-.3);' if n<len(S) else f'tl.fromTo("#f{n}",{{opacity:0}},{{opacity:1,duration:.8,ease:"power1.in",immediateRender:false}},S+{d}-.8);'
    js+=f'      {{const S={s};{fin}{j}{fout}}}\n'
aud='      <audio id="music" src="assets/music.mp3" data-start="0" data-duration="30" data-track-index="10" data-volume="0.85"></audio>\n'
for n,(i,f,s,ms,d,v) in enumerate(SFX):
    aud+=f'      <audio id="sfx-{i}" src="assets/sfx/{f}.mp3" data-start="{s}" data-media-start="{ms}" data-duration="{d}" data-track-index="{11+n}" data-volume="{v}"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="30" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>
'''
open(out,'w').write(html)
