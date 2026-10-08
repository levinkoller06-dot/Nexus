import sys, math
sys.path.insert(0,'/tmp/claude-0/-home-user-Nexus/78db4e45-757a-5460-8fc1-0f9e8d2fdc56/scratchpad/iphone')
from phone import phone, PHONE_CSS, wallpaper
out=sys.argv[1]
TOTAL=71.88
PER=0.5042; BAR=4*PER; D0=0.874
D=lambda n: round(D0+BAR*n,3)        # Taktanfang n
Bt=lambda n: round(0.37+PER*n,3)     # Schlag n
LIGHT,DARK,INK,SUB,SUBD='#F5F5F7','#000000','#1D1D1F','#6E6E73','#A1A1A6'
def grad20(gid,size,txt='20'):
    w=size*1.25*len(txt)/2
    return (f'<svg class="g20" viewBox="0 0 {w:.0f} {size:.0f}" width="{w:.0f}" height="{size:.0f}"><defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="#7B5CFF"/><stop offset=".5" stop-color="#FF5FA8"/><stop offset="1" stop-color="#FF9F43"/></linearGradient></defs>'
            f'<text x="50%" y="84%" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{size:.0f}" letter-spacing="-{size*0.04:.0f}" fill="url(#{gid})">{txt}</text></svg>')
LOCK=('<div class="lock" data-layout-allow-overlap><p class="ldate">Dienstag, 14. September</p><p class="ltime">9:41</p>'
      '<div class="lwid"><span class="wi" data-layout-allow-overlap>21°<small>Zürich</small></span><span class="wi" data-layout-allow-overlap>☀︎<small>Sonnig</small></span></div></div>')
def notif(i,t,s): return f'<div class="note n{i}" data-layout-allow-overlap><b>{t}</b><span>{s}</span></div>'
S=[]
def scene(a,b,bg,html,js,cls=''): S.append((a,b,bg,html,js,cls))
# S0 Intro: Silhouette zeichnet sich
scene(0,D(1),DARK,
 '<svg class="abs" style="left:0;top:0" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><linearGradient id="og" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7B5CFF"/><stop offset=".5" stop-color="#FF5FA8"/><stop offset="1" stop-color="#FF9F43"/></linearGradient><filter id="glw"><feGaussianBlur stdDeviation="6"/></filter></defs>'
 '<rect id="o0b" x="810" y="230" width="300" height="620" rx="52" fill="none" stroke="url(#og)" stroke-width="8" filter="url(#glw)" opacity=".8"/>'
 '<rect id="o0" x="810" y="230" width="300" height="620" rx="52" fill="none" stroke="#FFFFFF" stroke-width="3"/></svg>'
 '<p class="yr" id="yr0">2007 — 2027</p>',
 'for(const id of ["o0","o0b"]){const r=document.getElementById(id);const L=r.getTotalLength();gsap.set(r,{strokeDasharray:L,strokeDashoffset:L});tl.to(r,{strokeDashoffset:0,duration:2.1,ease:"power2.inOut"},S+.25);}'
 'tl.fromTo("#yr0",{opacity:0,y:16},{opacity:1,y:0,duration:.8,ease:"power2.out"},S+1.0);')
# S1 Reveal
scene(D(1),D(3),DARK,
 '<svg class="abs halo" id="h1" style="left:330px;top:40px;width:900px;height:1000px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_halo"><stop offset="0" stop-color="#7B5CFF" stop-opacity="0.35"/><stop offset="0.45" stop-color="#FF5FA8" stop-opacity="0.12"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_halo)"/></svg>'f'<div class="stage">{phone("ph1",360,"mitternacht",LOCK,screen_on=False)}</div>'
 f'<div class="ttl" id="t1"><h1 class="hero">iPhone {grad20("g1",190)}</h1><p class="sub d">Zwanzig Jahre. Ein neues Kapitel.</p></div>',
 'gsap.set("#ph1",{x:430,y:170,rotationY:-24,rotationX:4});'
 'tl.fromTo("#ph1",{scale:.86,rotationY:-34},{scale:1,rotationY:-14,duration:4.0,ease:"power2.out"},S);'
 'tl.fromTo("#ph1 .scroff",{opacity:1},{opacity:0,duration:.35,ease:"power2.out"},S+.02);'
 'tl.fromTo("#h1",{opacity:0,scale:.5},{opacity:1,scale:1,duration:1.4,ease:"power2.out"},S);'
 f'tl.fromTo("#t1 .hero",{{opacity:0,x:60}},{{opacity:1,x:0,duration:.7,ease:"expo.out"}},{D(2)}-0.02);'
 f'tl.fromTo("#t1 .sub",{{opacity:0}},{{opacity:1,duration:.6}},{Bt(10)});')
# S2 Spin
scene(D(3),D(5),LIGHT,
 f'<p class="kick" id="k2">Ganz aus Glas.</p><div class="stage">{phone("ph2",330,"mitternacht",LOCK)}</div><p class="foot" id="f2">Vorne. Hinten. Rundum.</p>',
 'gsap.set("#ph2",{x:795,y:200,rotationX:-6});'
 'tl.fromTo("#ph2",{rotationY:-20},{rotationY:340,duration:3.9,ease:"power2.inOut"},S);'
 'tl.fromTo("#k2",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.05);'
 f'tl.fromTo("#f2",{{opacity:0}},{{opacity:1,duration:.5}},{Bt(14)});')
# S3 Profil
scene(D(5),D(7),DARK,
 '<div class="abs" id="pf3" style="left:210px;top:470px"><svg width="1500" height="150" viewBox="0 0 1500 150"><defs><linearGradient id="ti" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9EAEE"/><stop offset=".35" stop-color="#8E9097"/><stop offset=".6" stop-color="#5D5F66"/><stop offset="1" stop-color="#2A2B30"/></linearGradient></defs>'
 '<rect x="0" y="40" width="1500" height="56" rx="28" fill="url(#ti)"/><rect x="40" y="26" width="300" height="16" rx="8" fill="#3B3D44"/>'
 '<rect x="600" y="92" width="120" height="10" rx="5" fill="#4A4C53"/><rect x="760" y="92" width="80" height="10" rx="5" fill="#4A4C53"/>'
 '<rect x="1470" y="58" width="16" height="20" rx="6" fill="#111"/></svg></div>'
 '<div class="dim" id="dm3"><i></i><span>5,2 mm</span></div><p class="kick dk" id="k3">Unfassbar dünn.</p>',
 'tl.fromTo("#pf3",{x:-260,opacity:0},{x:0,opacity:1,duration:1.2,ease:"expo.out"},S);tl.to("#pf3",{x:-60,duration:2.8,ease:"none"},S+1.2);'
 f'tl.fromTo("#dm3",{{opacity:0,scaleY:.2}},{{opacity:1,scaleY:1,duration:.5,ease:"back.out(1.6)"}},{Bt(22)});'
 f'tl.fromTo("#k3",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,ease:"power3.out"}},{Bt(24)});')
# S4 20 Jahre
gens=[('2007',38,True,False),('2017',16,False,'notch'),('2022',16,False,'island'),('2027',8,False,None)]
gh=''
for i,(yr,bez,home,cut) in enumerate(gens):
    x=430+i*300
    extra=''
    if home: extra='<circle cx="80" cy="292" r="14" fill="none" stroke="#1D1D1F" stroke-width="3"/>'
    if cut=='notch': extra='<path d="M52,%d h56 a8,8 0 0 1 -8,10 h-40 a8,8 0 0 1 -8,-10z" fill="#1D1D1F"/>'%(bez)
    if cut=='island': extra='<rect x="58" y="26" width="44" height="14" rx="7" fill="#1D1D1F"/>'
    top=bez+ (30 if home else 0); bot=bez+(30 if home else 0)
    gh+=(f'<div class="gen" id="gn{i}" style="left:{x}px"><svg width="160" height="320" viewBox="0 0 160 320"><rect x="2" y="2" width="156" height="316" rx="{24 if home else 30}" fill="none" stroke="#1D1D1F" stroke-width="4"/>'
         f'<rect x="{2+ (10 if home else bez/2)}" y="{2+top}" width="{156-2*(10 if home else bez/2)}" height="{316-top-bot}" rx="{6 if home else 24}" fill="{"#D2D2D7" if i<3 else "url(#ag)"}"/>{extra}'
         '<defs><linearGradient id="ag" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7B5CFF"/><stop offset=".55" stop-color="#FF5FA8"/><stop offset="1" stop-color="#FF9F43"/></linearGradient></defs></svg><p>'+yr+'</p></div>')
scene(D(7),D(9),LIGHT,
 f'<p class="kick" id="k4">Zwanzig Jahre iPhone.</p><p class="cnt4" id="c4">2007</p>{gh}',
 'tl.fromTo("#k4",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.02);'
 'const o4={v:2007};tl.to(o4,{v:2027,duration:3.4,ease:"power2.inOut",onUpdate:()=>{document.getElementById("c4").textContent=Math.round(o4.v)}},S+.3);'
 + ''.join(f'tl.fromTo("#gn{i}",{{opacity:0,y:40}},{{opacity:1,y:0,duration:.45,ease:"back.out(1.6)"}},{Bt(30+i*2)});' for i in range(4)))
# S5 Display
scene(D(9),D(11),DARK,
 f'<div class="stage">{phone("ph5",520,"mitternacht",LOCK+notif(1,"Nachricht","Bis gleich 👋"))}</div>'
 '<svg class="abs" id="eg5" style="left:1080px;top:-2px" width="540" height="1080" viewBox="0 0 540 1080"><defs><linearGradient id="eg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7B5CFF"/><stop offset=".5" stop-color="#FF5FA8"/><stop offset="1" stop-color="#FF9F43"/></linearGradient></defs>'
 '<rect id="egr" x="10" y="20" width="520" height="1076" rx="88" fill="none" stroke="url(#eg)" stroke-width="6"/></svg>'
 '<div class="side" id="t5"><h2 class="h2 d">Display bis an<br>jeden Rand.</h2><p class="sub d">Rundum gekrümmt. Ohne Notch.<br>Ohne Insel. Nur Bild.</p></div>',
 'gsap.set("#ph5",{x:1080,y:20});'
 'tl.fromTo("#ph5",{y:160},{y:20,duration:4,ease:"power2.out"},S);'
 'tl.fromTo("#eg5",{y:140},{y:0,duration:4,ease:"power2.out"},S);'
 '{const r=document.getElementById("egr");const L=r.getTotalLength();gsap.set(r,{strokeDasharray:(L*0.18)+" "+L});tl.fromTo(r,{strokeDashoffset:0},{strokeDashoffset:-L*1.18,duration:3.6,ease:"power1.inOut"},S+.2);}'
 'tl.fromTo("#t5 .h2",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"expo.out"},S+.05);tl.fromTo("#t5 .sub",{opacity:0},{opacity:1,duration:.6},S+1.0);'
 'tl.fromTo("#ph5 .n1",{opacity:0,y:-30},{opacity:1,y:0,duration:.4,ease:"back.out(1.8)"},S+2.0);')
# S6 Kamera
scene(D(11),D(13),'#0A0A0C',
 f'<div class="stage">{phone("ph6",900,"mitternacht")}</div>'
 '<div class="side r" id="t6"><h2 class="h2 d">Kamera.<br>Neu gedacht.</h2><ul class="specs d"><li><b>200 MP</b> Hauptkamera</li><li><b>8×</b> optischer Zoom</li><li><b>8K</b> Video</li></ul></div>',
 'gsap.set("#ph6",{x:120,y:-180,rotationY:180,rotationZ:-8});'
 'tl.fromTo("#ph6",{scale:1.08,rotationY:196},{scale:1,rotationY:186,duration:4,ease:"power2.out"},S);'
 'tl.fromTo("#t6 .h2",{opacity:0,x:40},{opacity:1,x:0,duration:.7,ease:"expo.out"},S+.1);'
 + ''.join(f'tl.fromTo("#t6 li:nth-child({i+1})",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.4,ease:"power3.out"}},{Bt(46+i*2)});' for i in range(3))
 + 'tl.fromTo("#ph6 .lgl",{opacity:.3},{opacity:1,duration:.12,yoyo:true,repeat:5,ease:"none"},S+.9);')
# S7 Chip
traces=''.join(f'<path class="tr7" d="M{960+math.cos(a)*170:.0f},{540+math.sin(a)*170:.0f} L{960+math.cos(a)*(330+40*(k%3)):.0f},{540+math.sin(a)*(330+40*(k%3)):.0f} L{960+math.cos(a+0.12)*(520+60*(k%2)):.0f},{540+math.sin(a+0.12)*(520+60*(k%2)):.0f}" fill="none" stroke="url(#tg)" stroke-width="3" stroke-linecap="round"/>' for k,a in enumerate([i*math.pi/8 for i in range(16)]))
scene(D(13),D(15),DARK,
 f'<svg class="abs" style="left:0;top:0" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><linearGradient id="tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7B5CFF"/><stop offset="1" stop-color="#FF5FA8"/></linearGradient>'
 '<linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5A5C63"/><stop offset=".45" stop-color="#1C1D21"/><stop offset="1" stop-color="#3E4047"/></linearGradient></defs>'
 f'{traces}<rect id="chip7" x="810" y="390" width="300" height="300" rx="46" fill="url(#cg)" stroke="#8A8C93" stroke-width="3"/>'
 '<text x="960" y="560" text-anchor="middle" font-family="Inter" font-weight="700" font-size="92" fill="#F5F5F7" letter-spacing="-3">A21</text>'
 '<text x="960" y="622" text-anchor="middle" font-family="Inter" font-weight="600" font-size="44" fill="#A1A1A6">PRO</text></svg>'
 '<div class="stats7"><p><b>2 nm</b>Fertigung</p><p><b>+40 %</b>Leistung</p><p><b>−30 %</b>Energie</p></div>',
 'tl.fromTo("#chip7",{scale:.6,opacity:0,transformOrigin:"50% 50%"},{scale:1,opacity:1,duration:.7,ease:"expo.out"},S);'
 '{const ts=document.querySelectorAll(".tr7");ts.forEach((p,i)=>{const L=p.getTotalLength();gsap.set(p,{strokeDasharray:L,strokeDashoffset:L});tl.to(p,{strokeDashoffset:0,duration:.9,ease:"power2.out"},S+.3+(i%4)*0.504);});}'
 + ''.join(f'tl.fromTo(".stats7 p:nth-child({i+1})",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.45,ease:"power3.out"}},{Bt(54+i*2)});' for i in range(3)))
# S8 Akku
scene(D(15),D(17),LIGHT,
 '<svg class="abs" style="left:660px;top:190px" width="600" height="600" viewBox="0 0 600 600"><circle cx="300" cy="300" r="240" fill="none" stroke="#E3E3E8" stroke-width="40"/>'
 '<circle id="bt8" cx="300" cy="300" r="240" fill="none" stroke="#34C759" stroke-width="40" stroke-linecap="round" transform="rotate(-90 300 300)"/></svg>'
 '<p class="pct8" id="p8">0 %</p><p class="kick b8" id="k8">Bis zu zwei Tage Akku.</p><p class="foot" id="f8">In 15 Minuten auf 80 % geladen.</p>',
 '{const c=document.getElementById("bt8");const L=2*Math.PI*240;gsap.set(c,{strokeDasharray:L,strokeDashoffset:L});tl.to(c,{strokeDashoffset:0,duration:3.2,ease:"power2.inOut"},S+.2);'
 'const o8={v:0};tl.to(o8,{v:100,duration:3.2,ease:"power2.inOut",onUpdate:()=>{document.getElementById("p8").textContent=Math.round(o8.v)+" %"}},S+.2);}'
 'tl.fromTo("#k8",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.1);'
 f'tl.fromTo("#f8",{{opacity:0}},{{opacity:1,duration:.5}},{Bt(66)});')
# S9 Farben
cols=[('polar','Polarweiss'),('mitternacht','Mitternacht'),('gletscher','Gletscherblau'),('sand','Sandstein'),('salbei','Salbei')]
ph9=''.join(f'<div class="stage">{phone("ph9_"+str(i),210,f)}</div>' for i,(f,n) in enumerate(cols))
nm9=''.join(f'<p class="cn" id="cn{i}" style="left:{230+i*300}px">{n}</p>' for i,(f,n) in enumerate(cols))
scene(D(17),D(21),LIGHT,
 f'<p class="kick" id="k9">Fünf neue Farben.</p>{ph9}{nm9}',
 'tl.fromTo("#k9",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.05);'
 + ''.join(f'gsap.set("#ph9_{i}",{{x:{290+i*300},y:300,rotationY:180}});tl.fromTo("#ph9_{i}",{{y:620,opacity:0,rotationY:150}},{{y:300,opacity:1,rotationY:200,duration:.8,ease:"expo.out"}},{Bt(68+i*2)});tl.fromTo("#cn{i}",{{opacity:0}},{{opacity:1,duration:.4}},{Bt(68+i*2)+0.25});' for i in range(5))
 + ''.join(f'tl.to("#ph9_{i}",{{rotationY:160,duration:3.0,ease:"sine.inOut"}},{Bt(78)});' for i in range(5)))
# S10 Kinetic
words=['Leichter.','Heller.','Schneller.','Smarter.']
scene(D(21),D(23),'#FFFFFF',
 ''.join(f'<p class="kw" id="kw{i}">{w}</p>' for i,w in enumerate(words)),
 ''.join(f'tl.fromTo("#kw{i}",{{opacity:0,scale:1.25}},{{opacity:1,scale:1,duration:.32,ease:"expo.out"}},{Bt(84+i*2)});'+(f'tl.to("#kw{i}",{{opacity:0,duration:.12}},{Bt(86+i*2)}-0.13);' if i<3 else '') for i in range(4)))
# S11 Lockscreen
nots=notif(1,'Kalender','Keynote · 19:00')+notif(2,'Wetter','21° und sonnig in Zürich')+notif(3,'Fotos','Neue Erinnerung: Sommer 2027')
scene(D(23),D(25),'#ECECF1',
 '<svg class="abs blob" style="left:700px;top:-120px;width:700px;height:700px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_blob1"><stop offset="0" stop-color="#7B5CFF" stop-opacity="0.35"/><stop offset="1" stop-color="#7B5CFF" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_blob1)"/></svg><svg class="abs blob" style="left:1100px;top:500px;width:800px;height:800px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_blob2"><stop offset="0" stop-color="#FF5FA8" stop-opacity="0.28"/><stop offset="1" stop-color="#FF5FA8" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_blob2)"/></svg>'f'<div class="stage">{phone("ph11",400,"polar",LOCK+nots)}</div><div class="side" id="t11"><h2 class="h2">Neu gestaltet.<br>Bis ins Detail.</h2></div>',
 'gsap.set("#ph11",{x:1180,y:120,rotationY:-10,rotationX:4});tl.fromTo("#ph11",{rotationY:-22},{rotationY:-6,duration:4,ease:"power2.out"},S);'
 'tl.fromTo("#t11 .h2",{opacity:0,y:30},{opacity:1,y:0,duration:.7,ease:"expo.out"},S+.05);'
 + ''.join(f'tl.fromTo("#ph11 .n{i+1}",{{opacity:0,y:-40,scale:.9}},{{opacity:1,y:0,scale:1,duration:.4,ease:"back.out(1.8)"}},{Bt(93+i*2)});' for i in range(3))
 + 'tl.fromTo(".blob",{x:0},{x:120,duration:4,ease:"none"},S);')
# S12 Viewfinder
scene(D(25),D(27),DARK,
 '<div class="abs vf" id="vf12"><svg width="1920" height="1080" viewBox="0 0 1920 1080"><defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2B2F6E"/><stop offset=".45" stop-color="#C2547A"/><stop offset=".7" stop-color="#F6A35B"/><stop offset="1" stop-color="#FFD9A0"/></linearGradient>'
 '<linearGradient id="lake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E88A62"/><stop offset="1" stop-color="#2A2440"/></linearGradient></defs>'
 '<rect width="1920" height="760" fill="url(#sky)"/><circle cx="1180" cy="640" r="120" fill="#FFE7B8"/>'
 '<path d="M0,700 L240,520 L420,640 L640,430 L900,650 L1100,560 L1350,690 L1560,500 L1920,660 L1920,780 L0,780Z" fill="#3B2A55"/>'
 '<path d="M0,760 L300,640 L560,720 L820,600 L1120,740 L1400,650 L1700,730 L1920,690 L1920,800 L0,800Z" fill="#231B38"/>'
 '<rect y="790" width="1920" height="290" fill="url(#lake)"/><ellipse cx="1180" cy="860" rx="160" ry="16" fill="#FFE7B8" opacity=".6"/></svg></div>'
 '<div class="vfui"><div class="zoom"><span>0,5×</span><span class="on">1×</span><span>2×</span><span>8×</span></div><i class="shutter"></i><p class="vft">FOTO</p></div><i class="flash12" id="fl12"></i>'
 '<p class="ovt" id="o12">Fotos, die leuchten.</p>',
 'tl.fromTo("#vf12",{scale:1.0},{scale:1.06,duration:1.0,ease:"power2.out"},S);'
 f'tl.to("#vf12",{{scale:1.35,duration:.4,ease:"power3.out"}},{Bt(100)});tl.to("#vf12",{{scale:2.2,transformOrigin:"61% 62%",duration:.45,ease:"power3.out"}},{Bt(102)});'
 f'tl.set(".zoom span",{{className:""}},{Bt(100)});'
 f'tl.fromTo("#fl12",{{opacity:0}},{{opacity:.9,duration:.05}},{Bt(105)});tl.to("#fl12",{{opacity:0,duration:.35}},{Bt(105)}+0.05);'
 'tl.fromTo("#o12",{opacity:0,y:20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.3);')
# S13 Glas-Widgets
scene(D(27),D(29),'#120E2A',
 '<svg class="abs aur a1" style="left:200px;top:300px;width:800px;height:700px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_a1"><stop offset="0" stop-color="#7B5CFF" stop-opacity="1"/><stop offset="1" stop-color="#7B5CFF" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_a1)"/></svg><svg class="abs aur a2" style="left:1000px;top:100px;width:800px;height:800px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_a2"><stop offset="0" stop-color="#FF5FA8" stop-opacity="1"/><stop offset="1" stop-color="#FF5FA8" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_a2)"/></svg><svg class="abs aur a3" style="left:700px;top:600px;width:700px;height:600px" viewBox="0 0 100 100" preserveAspectRatio="none"><defs><radialGradient id="rg_a3"><stop offset="0" stop-color="#21C3FF" stop-opacity="1"/><stop offset="1" stop-color="#21C3FF" stop-opacity="0"/></radialGradient></defs><ellipse cx="50" cy="50" rx="50" ry="50" fill="url(#rg_a3)"/></svg>'
 '<div class="gw w1"><b>21°</b><span>Zürich · Sonnig</span></div>'
 '<div class="gw w2"><svg width="150" height="150" viewBox="0 0 150 150"><circle cx="75" cy="75" r="62" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="14"/><circle cx="75" cy="75" r="62" fill="none" stroke="#FF375F" stroke-width="14" stroke-linecap="round" stroke-dasharray="389" stroke-dashoffset="90" transform="rotate(-90 75 75)"/><circle cx="75" cy="75" r="44" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="14"/><circle cx="75" cy="75" r="44" fill="none" stroke="#A4FF4F" stroke-width="14" stroke-linecap="round" stroke-dasharray="276" stroke-dashoffset="70" transform="rotate(-90 75 75)"/><circle cx="75" cy="75" r="26" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="14"/><circle cx="75" cy="75" r="26" fill="none" stroke="#4FD8FF" stroke-width="14" stroke-linecap="round" stroke-dasharray="163" stroke-dashoffset="30" transform="rotate(-90 75 75)"/></svg></div>'
 '<div class="gw w3"><b>Di 14</b><span>Keynote · 19:00</span></div>'
 '<p class="ovt c" id="o13">Glas, das lebt.</p>',
 'tl.fromTo(".a1",{x:0,y:0},{x:220,y:80,duration:4,ease:"sine.inOut"},S);tl.fromTo(".a2",{x:0,y:0},{x:-260,y:-60,duration:4,ease:"sine.inOut"},S);tl.fromTo(".a3",{x:0},{x:160,duration:4,ease:"sine.inOut"},S);'
 + ''.join(f'tl.fromTo(".w{i+1}",{{opacity:0,y:80,scale:.9}},{{opacity:1,y:0,scale:1,duration:.6,ease:"expo.out"}},{Bt(109+i*2)});tl.to(".w{i+1}",{{y:-30*({i}-1),duration:3,ease:"none"}},{Bt(109+i*2)}+0.6);' for i in range(3))
 + 'tl.fromTo("#o13",{opacity:0,scale:.92},{opacity:1,scale:1,duration:.7,ease:"expo.out"},S+.1);')
# S14 Build mit 20
scene(D(29),D(33),DARK,
 f'<div class="abs big20" id="b20" data-layout-allow-overlap>{grad20("g14",820)}</div><div class="stage">{phone("ph14",360,"gletscher")}</div><i class="streak s1"></i><i class="streak s2"></i>',
 'gsap.set("#ph14",{x:780,y:150,rotationX:-4});'
 'tl.fromTo("#b20",{opacity:0,scale:.8},{opacity:.95,scale:1,duration:1.6,ease:"power2.out"},S);tl.to("#b20",{scale:1.12,duration:6.5,ease:"none"},S+1.6);'
 + ''.join(f'tl.to("#ph14",{{rotationY:{(k+1)*90},duration:.42,ease:"expo.out"}},{Bt(116+k*2)});' for k in range(8))
 + ''.join(f'tl.to("#ph14",{{rotationY:{720+(k+1)*45},duration:.2,ease:"expo.out"}},{Bt(132+k)});' for k in range(3))
 + 'tl.fromTo(".s1",{x:-1400},{x:2200,duration:.6,ease:"power2.in"},S+2.0);tl.fromTo(".s2",{x:2200},{x:-1400,duration:.6,ease:"power2.in"},S+6.0);')
# S15 End
scene(D(33),TOTAL,LIGHT,
 f'<div class="stage">{phone("ph15",300,"mitternacht",LOCK)}</div><div class="end" id="e15"><h1 class="hero dk2">iPhone {grad20("g15",170)}</h1><p class="when">Herbst 2027.</p></div><p class="disc" id="d15">Fan-Konzept · Kein offizielles Apple-Produkt</p>',
 'gsap.set("#ph15",{x:420,y:200,rotationY:-16,rotationX:3});tl.fromTo("#ph15",{rotationY:-40,opacity:0},{rotationY:-16,opacity:1,duration:1.4,ease:"expo.out"},S);'
 'tl.fromTo("#e15 .hero",{opacity:0,y:40},{opacity:1,y:0,duration:.8,ease:"expo.out"},S+.25);tl.fromTo("#e15 .when",{opacity:0},{opacity:1,duration:.6},S+1.1);'
 'tl.fromTo("#d15",{opacity:0},{opacity:1,duration:.6},S+1.8);')
css=PHONE_CSS+f'''
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#000}}
#root{{width:100%;height:100%;position:relative;overflow:hidden;background:#000;font-family:Inter,sans-serif}}
.scene{{position:absolute;inset:0;overflow:hidden}}
.abs{{position:absolute;display:block}}
.g20{{display:inline-block;vertical-align:baseline;overflow:visible}}
.yr{{position:absolute;left:0;right:0;top:900px;text-align:center;font-size:30px;font-weight:500;letter-spacing:.3em;color:#86868B}}
.ttl{{position:absolute;left:1000px;top:330px;width:880px}}
.hero{{font-size:190px;font-weight:700;letter-spacing:-0.045em;line-height:1;color:#F5F5F7;white-space:nowrap;display:flex;align-items:flex-end;gap:30px}}
.hero.dk2{{color:#1D1D1F;font-size:170px}}
.sub{{font-size:44px;font-weight:500;letter-spacing:-0.01em;color:{SUB};margin-top:26px;line-height:1.3}}
.sub.d{{color:{SUBD}}}
.kick{{position:absolute;left:0;right:0;top:90px;text-align:center;font-size:84px;font-weight:700;letter-spacing:-0.035em;color:{INK}}}
.kick.dk{{color:#F5F5F7;top:240px}}
.foot{{position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:40px;font-weight:500;color:{SUB}}}
.dim{{position:absolute;left:1700px;top:400px;display:flex;align-items:center;gap:18px;transform-origin:50% 50%}}
.dim i{{display:block;width:4px;height:200px;background:linear-gradient(#FF9F43,#FF5FA8)}}
.dim span{{font-size:56px;font-weight:700;color:#F5F5F7;letter-spacing:-0.02em}}
.cnt4{{position:absolute;left:0;right:0;top:220px;text-align:center;font-size:150px;font-weight:700;letter-spacing:-0.04em;color:{INK}}}
.gen{{position:absolute;top:470px;width:160px;text-align:center}}
.gen svg{{display:block}}
.gen p{{font-size:34px;font-weight:600;color:{SUB};margin-top:16px}}
.side{{position:absolute;left:150px;top:300px;width:820px}}
.side.r{{left:1100px}}
.h2{{font-size:110px;font-weight:700;letter-spacing:-0.04em;line-height:1.02;color:{INK}}}
.h2.d{{color:#F5F5F7}}
.specs{{list-style:none;margin-top:40px;display:flex;flex-direction:column;gap:14px}}
.specs li{{font-size:42px;color:{SUBD};font-weight:500}}
.specs b{{color:#F5F5F7;font-weight:700}}
.stats7{{position:absolute;left:0;right:0;bottom:90px;display:flex;justify-content:center;gap:120px}}
.stats7 p{{display:flex;flex-direction:column;align-items:center;font-size:32px;color:{SUBD};font-weight:500}}
.stats7 b{{font-size:64px;color:#F5F5F7;font-weight:700;letter-spacing:-0.03em}}
.pct8{{position:absolute;left:0;right:0;top:420px;text-align:center;font-size:120px;font-weight:700;letter-spacing:-0.04em;color:{INK}}}
.kick.b8{{top:60px}}
.cn{{position:absolute;top:800px;width:240px;text-align:center;font-size:34px;font-weight:600;color:{INK}}}
.kw{{position:absolute;left:0;right:0;top:390px;text-align:center;font-size:240px;font-weight:700;letter-spacing:-0.05em;color:{INK};opacity:0}}
.lock{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;padding-top:14%;color:#fff}}
.ldate{{font-size:1.15em;font-weight:500;opacity:.9}}
.ltime{{font-size:4.6em;font-weight:600;letter-spacing:-0.03em;line-height:1}}
.lwid{{display:flex;gap:.8em;margin-top:.8em}}
.wi{{display:flex;flex-direction:column;align-items:center;font-size:1.1em;font-weight:600;background:rgba(0,0,0,.42);border:1px solid rgba(255,255,255,.3);border-radius:1em;padding:.5em .9em}}
.wi small{{font-size:.6em;font-weight:500;opacity:.85}}
.note{{position:absolute;left:6%;right:6%;background:rgba(0,0,0,.42);border:1px solid rgba(255,255,255,.35);border-radius:1.1em;padding:.7em .9em;display:flex;flex-direction:column;color:#fff;font-size:.95em}}
.note b{{font-weight:700}}.note span{{opacity:.9}}
.n1{{top:58%}}.n2{{top:70%}}.n3{{top:82%}}
.vf{{left:0;top:0;width:1920px;height:1080px;transform-origin:61% 62%}}
.vfui{{position:absolute;inset:0}}
.zoom{{position:absolute;left:50%;bottom:210px;margin-left:-190px;width:380px;display:flex;justify-content:space-around;background:rgba(0,0,0,.35);border-radius:999px;padding:12px 18px}}
.zoom span{{font-size:30px;font-weight:600;color:#fff}}
.zoom span.on{{color:#FFD60A}}
.shutter{{position:absolute;left:50%;bottom:60px;margin-left:-62px;width:124px;height:124px;border-radius:50%;border:8px solid #fff;background:rgba(255,255,255,.9);box-shadow:0 0 0 6px rgba(0,0,0,.25);display:block}}
.vft{{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:22px;font-weight:700;letter-spacing:.2em;color:#FFD60A}}
.flash12{{position:absolute;inset:0;background:#fff;opacity:0;display:block}}
.ovt{{position:absolute;left:120px;top:110px;font-size:96px;font-weight:700;letter-spacing:-0.04em;color:#fff;text-shadow:0 4px 30px rgba(0,0,0,.35)}}
.ovt.c{{left:0;right:0;top:120px;text-align:center}}
.gw{{position:absolute;display:flex;flex-direction:column;justify-content:center;gap:8px;padding:34px 40px;border-radius:44px;background:rgba(255,255,255,.14);border:1.5px solid rgba(255,255,255,.38);box-shadow:inset 0 1px 0 rgba(255,255,255,.5),0 30px 60px rgba(0,0,0,.25);color:#fff}}
.gw b{{font-size:72px;font-weight:700;letter-spacing:-0.03em}}.gw span{{font-size:30px;font-weight:500;opacity:.9}}
.w1{{left:260px;top:420px;width:420px;height:260px}}
.w2{{left:820px;top:380px;width:280px;height:280px;align-items:center}}
.w3{{left:1240px;top:440px;width:420px;height:260px}}
.big20{{left:0;top:0;width:1920px;height:1080px;display:flex;align-items:center;justify-content:center}}
.streak{{position:absolute;top:520px;width:900px;height:6px;border-radius:3px;display:block;background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.9),rgba(255,255,255,0))}}
.s2{{top:600px}}
.end{{position:absolute;left:820px;top:360px;width:1000px}}
.when{{font-size:56px;font-weight:600;color:{SUB};margin-top:24px;letter-spacing:-0.01em}}
.disc{{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-size:24px;font-weight:500;color:#86868B;letter-spacing:.02em}}
'''
body='';js=''
for k,(a,b,bg,html,j,cls) in enumerate(S):
    d=round(b-a,3)
    body+=f'      <section id="s{k}" class="scene clip" data-start="{a}" data-duration="{d}" data-track-index="{k%2}" style="background:{bg}">\n        {html}\n      </section>\n'
    js+=f'      {{const S={a};{j}}}\n'
aud=f'      <audio id="music" src="assets/audio/song.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="10" data-volume="1"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>'''
open(out,'w').write(html); print('ok',len(S),'scenes')
