import sys,json
out=sys.argv[1]
ARROW='<span class="arr"><svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg></span>'
SM_MACAN="Macan: Stromverbrauch kombiniert: 19.4 – 16.8 kWh/100km, Elektrische Reichweite kombiniert (WLTP): 547 – 638 km, CO₂-Emissionen kombiniert: 0 g/km, Effizienzklasse: B - C"
SM_CAY="Cayenne Turbo Electric: Stromverbrauch kombiniert: 22.5 – 20.5 kWh/100km, Elektrische Reichweite kombiniert (WLTP): 557 – 620 km, CO₂-Emissionen kombiniert: 0 g/km, Effizienzklasse: C - D"
S=[]  # (start,dur,html,js,bg)
def scene(s,d,html,js,bg="#000"): S.append((s,d,html,js,bg))
# hero video
scene(0,6.0,'<video id="hv" class="clip vid" src="assets/video/hero.mp4" muted playsinline data-start="0" data-duration="6.0" data-playback-rate="0.6" data-track-index="9"></video><i class="vig"></i>',
 'tl.fromTo("#vz0",{scale:1.0},{scale:1.08,duration:6,ease:"none"},S);','#000')
# title
scene(6.0,2.0,'<i class="redglow" id="rg1"></i><div class="t1"><div class="mask"><h1 id="t1a" class="F hero">Aus Liebe zum</h1></div><div class="mask"><h1 id="t1b" class="F hero">Sportwagen.</h1></div></div>',
 'tl.fromTo("#rg1",{opacity:0,scale:.6},{opacity:1,scale:1.1,duration:2,ease:"power2.out"},S);'
 'tl.fromTo("#t1a",{y:200},{y:0,duration:.6,ease:"expo.out"},S+.1);tl.fromTo("#t1b",{y:200},{y:0,duration:.6,ease:"expo.out"},S+.35);'
 'tl.to(".t1",{scale:1.06,duration:2,ease:"none"},S);','#000')
cars=[('718','car_718','Benzin','Präziser Sportwagen mit Mittelmotor.'),('911','car_911','Benzin','Ikonischer Sportwagen mit Heckmotor.'),('Taycan','car_taycan','Elektro','Elektrischer Sportwagen.'),('Panamera','car_panamera','Hybrid,Benzin','Luxuslimousine mit hohem Komfort.'),('Macan','car_xab','Elektro','Sportlicher Kompakt-SUV.'),('Cayenne','car_macan','Elektro,Hybrid,Benzin','Vielseitiger SUV.')]
for i,(n,img,tags,desc) in enumerate(cars):
    s=8.0+i*2.0; k=len(S)
    pills="".join(f'<span class="pill">{t}</span>' for t in tags.split(','))
    scene(s,2.0,f'<div class="card"></div><p class="cnt">0{i+1} / 06</p><h2 class="F mname" id="mn{k}">{n}</h2><p class="mdesc" id="md{k}">{desc}</p><div class="carwrap" id="cw{k}"><img class="car" src="assets/img/{img}.png" alt="{n}"/><i class="floor"></i></div><div class="pills" id="pl{k}">{pills}</div>',
     f'tl.fromTo("#cw{k}",{{x:1500,skewX:-8}},{{x:0,skewX:0,duration:.55,ease:"expo.out"}},S);tl.to("#cw{k}",{{x:-40,duration:1.15,ease:"none"}},S+.55);tl.to("#cw{k}",{{x:-1900,skewX:8,duration:.3,ease:"power3.in"}},S+1.7);'
     f'tl.fromTo("#mn{k}",{{opacity:0,x:-60}},{{opacity:1,x:0,duration:.45,ease:"expo.out"}},S+.08);tl.fromTo("#md{k}",{{opacity:0}},{{opacity:1,duration:.4}},S+.3);'
     f'tl.fromTo("#pl{k} .pill",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.35,ease:"back.out(1.6)",stagger:.08}},S+.4);','#EEEFF2')
life=[('p911','911.','Ikonischer Sportwagen mit Heckmotor.',None,(1.14,1.0,-40,0)),('pmacan','Macan Electric.','Sportlicher Kompakt-SUV.',SM_MACAN,(1.0,1.12,0,-30)),('pcayenne','Cayenne Turbo Electric.','Vielseitiger SUV.',SM_CAY,(1.12,1.0,40,0)),('pnorway','Motorsport – Events &amp; Strecken.','Ihr Porsche Abenteuer beginnt jetzt.',None,(1.0,1.1,0,0))]
for i,(img,tit,sub,sm,(a,b,x0,y0)) in enumerate(life):
    s=20.0+i*3.0; k=len(S)
    smh=f'<p class="small">{sm}</p>' if sm else ''
    scene(s,3.0,f'<img class="full" id="ph{k}" src="assets/img/{img}.jpg" alt=""/><i class="grad"></i><div class="ltxt"><h2 class="F ltit" id="lt{k}">{tit}</h2><p class="lsub" id="ls{k}">{sub}</p></div><div class="larr" id="la{k}">{ARROW}</div>{smh}',
     f'tl.fromTo("#ph{k}",{{scale:{a},x:{x0},y:{y0}}},{{scale:{b},x:0,y:0,duration:3,ease:"none"}},S);'
     f'tl.fromTo("#lt{k}",{{opacity:0,y:50}},{{opacity:1,y:0,duration:.55,ease:"expo.out"}},S+.15);tl.fromTo("#ls{k}",{{opacity:0}},{{opacity:1,duration:.5}},S+.5);'
     f'tl.fromTo("#la{k}",{{opacity:0,scale:.5}},{{opacity:1,scale:1,duration:.4,ease:"back.out(2)"}},S+.6);','#000')
cards=[('pcard','Porsche Kreditkarte aus Metall'),('pswiss','Swiss Benefits'),('ptaycan','E-Performance')]
k=len(S)
scene(32.0,6.0,'<h2 class="F ent" id="en'+str(k)+'">Entdecken</h2><div class="cards">'+"".join(f'<div class="dc"><img src="assets/img/{im}.jpg" alt=""/><i class="cg"></i><p>{t}</p>{ARROW}</div>' for im,t in cards)+'</div><p class="shop" id="sh'+str(k)+'">Fahrzeugzubehör · Bekleidung · Home &amp; Lifestyle — im Porsche Online Shop</p>',
 f'tl.fromTo("#en{k}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.6,ease:"expo.out"}},S+.1);'
 f'tl.fromTo("#s{k} .dc",{{opacity:0,y:240}},{{opacity:1,y:0,duration:.7,ease:"expo.out",stagger:.25}},S+.3);'
 f'tl.fromTo("#s{k} .dc img",{{scale:1.15}},{{scale:1.0,duration:5.5,ease:"none"}},S+.3);'
 f'tl.fromTo("#sh{k}",{{opacity:0}},{{opacity:1,duration:.6}},S+2.4);','#0B0B0E')
k=len(S)
scene(38.0,7.0,f'<img class="full" id="cr{k}" src="assets/img/pcrest.jpg" alt=""/><i class="grad2"></i><div class="end"><h2 class="F endt" id="et{k}">Ihr Porsche Abenteuer beginnt jetzt.</h2><p class="url" id="eu{k}">porsche.com/swiss</p></div>',
 f'tl.fromTo("#cr{k}",{{scale:1.18}},{{scale:1.0,duration:7,ease:"power1.out"}},S);'
 f'tl.fromTo("#et{k}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.9,ease:"expo.out"}},S+1.0);tl.fromTo("#eu{k}",{{opacity:0}},{{opacity:1,duration:.8}},S+1.8);','#000')

css='''
@font-face{font-family:"BSC";font-weight:300;src:url("assets/fonts/barlow-semi-condensed-latin-300-normal.woff2") format("woff2")}
@font-face{font-family:"BSC";font-weight:400;src:url("assets/fonts/barlow-semi-condensed-latin-400-normal.woff2") format("woff2")}
@font-face{font-family:"BSC";font-weight:500;src:url("assets/fonts/barlow-semi-condensed-latin-500-normal.woff2") format("woff2")}
@font-face{font-family:"BSC";font-weight:600;src:url("assets/fonts/barlow-semi-condensed-latin-600-normal.woff2") format("woff2")}
*{margin:0;padding:0;box-sizing:border-box}
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#000}
#root{width:100%;height:100%;position:relative;overflow:hidden;background:#000;font-family:"BSC",sans-serif;color:#fff}
.scene{position:absolute;inset:0;overflow:hidden}
.sw{position:absolute;inset:0}
.fade{position:absolute;inset:0;background:#000;opacity:0;display:block}
.F{font-family:"BSC",sans-serif;font-weight:400;letter-spacing:-0.01em;line-height:1.02}
.vzw{position:absolute;inset:0;overflow:hidden}
.vid{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover;display:block}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,0) 40%,rgba(0,0,0,.65) 100%);display:block}
.redglow{position:absolute;left:460px;top:40px;width:1000px;height:1000px;border-radius:50%;background:radial-gradient(circle,rgba(200,20,10,.42),rgba(200,20,10,0) 65%);display:block}
.t1{position:absolute;left:0;top:0;width:1920px;height:1080px;display:flex;flex-direction:column;justify-content:center;padding-left:160px}
.mask{overflow:hidden;padding:0 20px 14px 0}
.hero{font-size:190px;font-weight:400;color:#fff}
.card{position:absolute;inset:0;background:radial-gradient(ellipse at 55% 75%,#FFFFFF 0%,#EEEFF2 55%,#E2E4E9 100%)}
.cnt{position:absolute;right:120px;top:110px;font-size:34px;color:#6B6D70;letter-spacing:.08em}
.mname{position:absolute;left:120px;top:90px;font-size:200px;color:#0E0E12;font-weight:400}
.mdesc{position:absolute;left:126px;top:320px;font-size:46px;color:#4C4E52}
.carwrap{position:absolute;left:250px;top:400px;width:1500px;height:520px;display:flex;align-items:flex-end;justify-content:center}
.car{display:block;max-width:1500px;max-height:500px;position:relative;z-index:2}
.floor{position:absolute;left:120px;right:120px;bottom:-10px;height:46px;border-radius:50%;background:radial-gradient(ellipse,rgba(0,0,0,.38),rgba(0,0,0,0) 70%);display:block}
.pills{position:absolute;left:120px;bottom:90px;display:flex;gap:20px}
.pill{display:block;font-size:40px;color:#0E0E12;background:#FFFFFF;padding:14px 38px;border-radius:999px;box-shadow:0 4px 18px rgba(0,0,0,.06)}
.full{position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover;display:block}
.grad{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.78) 100%);display:block}
.grad2{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15) 0%,rgba(0,0,0,0) 40%,rgba(0,0,0,.75) 100%);display:block}
.ltxt{position:absolute;left:120px;bottom:150px;width:1450px}
.ltit{font-size:130px;color:#fff}
.lsub{font-size:42px;color:#E3E4E6;margin-top:10px}
.larr{position:absolute;right:120px;bottom:170px}
.arr{display:flex;width:96px;height:96px;border-radius:50%;background:rgba(80,80,84,.75);align-items:center;justify-content:center}
.small{position:absolute;left:120px;right:120px;bottom:44px;font-size:21px;line-height:1.35;color:rgba(255,255,255,.78)}
.ent{position:absolute;left:0;right:0;top:70px;text-align:center;font-size:110px;color:#fff}
.cards{position:absolute;left:120px;top:240px;width:1680px;display:flex;gap:40px}
.dc{position:relative;width:533px;height:640px;border-radius:44px;overflow:hidden;background:#222}
.dc img{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;display:block}
.cg{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.8) 100%);display:block}
.dc p{position:absolute;left:40px;bottom:46px;width:330px;font-size:44px;line-height:1.1;color:#fff}
.dc .arr{position:absolute;right:34px;bottom:40px;width:84px;height:84px}
.shop{position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:38px;color:#C9CACD}
.end{position:absolute;left:0;right:0;bottom:120px;text-align:center}
.endt{font-size:104px;color:#fff}
.url{font-size:46px;color:#D6D7D9;letter-spacing:.06em;margin-top:22px}
'''
body="";js=""
for k,(s,d,html,j,bg) in enumerate(S):
    inner=html
    if k==0:
        inner='<div class="vzw" id="vz0">'+html+'</div>'
    body+=f'      <section id="s{k}" class="scene clip" data-start="{s}" data-duration="{d}" data-track-index="{k%2}" style="background:{bg}">\n        <div class="sw">{inner}</div>\n        <i class="fade" id="f{k}"></i>\n      </section>\n'
    fin=f'tl.fromTo("#f{k}",{{opacity:1}},{{opacity:0,duration:{0.8 if k==0 else 0.12},ease:"power1.out"}},S);' if k in (0,1,len(S)-2,len(S)-1) or k==8 else ''
    fout=f'tl.fromTo("#f{k}",{{opacity:0}},{{opacity:1,duration:1.4,ease:"power1.in",immediateRender:false}},S+{d}-1.4);' if k==len(S)-1 else ''
    js+=f'      {{const S={s};{fin}{j}{fout}}}\n'
# move hero video out of section for lint (video_nested_in_timed_element): keep video top-level instead
vid='<video id="hv" class="clip vid" src="assets/video/hero.mp4" muted playsinline data-start="0" data-duration="6.0" data-playback-rate="0.6" data-track-index="9"></video>'
body=body.replace(vid,'')
body=f'      {vid}\n'+body.replace('<section id="s0" class="scene clip" data-start="0" data-duration="6.0" data-track-index="0" style="background:#000">','<section id="s0" class="scene clip" data-start="0" data-duration="6.0" data-track-index="0" style="background:transparent">')
js=js.replace('tl.fromTo("#vz0",{scale:1.0},{scale:1.08,duration:6,ease:"none"},S);','tl.fromTo("#hv",{scale:1.0},{scale:1.08,duration:6,ease:"none"},S);')
aud='      <audio id="music" src="assets/audio/music.mp3" data-start="0" data-duration="45" data-track-index="20" data-volume="1"></audio>\n'
for n,(i,f,s,ms,d,v) in enumerate([("riser","riser",3.85,0,4.25,.32),("drop","impact-bass-2",8.0,0,1.6,.42),("endhit","impact-bass-2",38.0,0,1.8,.38)]):
    aud+=f'      <audio id="sfx-{i}" src="assets/sfx/{f}.mp3" data-start="{s}" data-media-start="{ms}" data-duration="{d}" data-track-index="{21+n}" data-volume="{v}"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="45" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>'''
open(out,'w').write(html); print('ok',len(S))
