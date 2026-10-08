import json, math, random, sys
sys.path.insert(0,'/tmp/claude-0/-home-user-Nexus/78db4e45-757a-5460-8fc1-0f9e8d2fdc56/scratchpad')
from kurt import kurt_svg
out=sys.argv[1]; T=json.load(open(sys.argv[2]))
TOTAL=T['total']; segs=T['segs']; SC=[0]+[round(s['start']-0.4,3) for s in segs[1:]]+[TOTAL]
R=random.Random(7)
def ship(uid,w,night=False,face=1,hull="#15171C",funnel="#E3A13A",funnels=4,length=1000):
    ports="".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="{"#FFD27A" if night else "#C9C2B0"}"/>' for y in (158,178) for x in range(90,930,22))
    ports+="".join(f'<rect x="{x}" y="118" width="10" height="7" fill="{"#FFE3A0" if night else "#9AA7B4"}"/>' for x in range(200,820,26))
    fx=[300,410,520,630] if funnels==4 else [470]
    fun="".join(f'<g transform="skewX(-8)"><rect x="{x+18}" y="18" width="50" height="76" fill="{funnel}"/><rect x="{x+18}" y="18" width="50" height="20" fill="#111"/></g>' for x in fx)
    boats="".join(f'<rect x="{x}" y="96" width="26" height="8" rx="4" fill="#F4F1EA" stroke="#9C9586" stroke-width="1"/>' for x in range(230,800,52))
    glow=f'<ellipse cx="500" cy="170" rx="460" ry="60" fill="#FFC86B" opacity=".10"/>' if night else ''
    tr=f'transform="translate(1000,0) scale(-1,1)"' if face<0 else ''
    return f'''<svg id="{uid}" class="ship" viewBox="0 -60 1000 330" width="{w}" height="{w*330/1000:.0f}" overflow="visible"><g {tr}>
{glow}<path d="M120,-40 L120,140 M905,-50 L905,140" stroke="#2B2B2B" stroke-width="5"/><path d="M120,-40 L905,-50" stroke="#2B2B2B" stroke-width="1.5"/>
<rect x="150" y="104" width="700" height="40" fill="#F2EEE4"/><rect x="215" y="86" width="560" height="22" fill="#E9E4D6"/>{boats}{fun}
<path d="M18,138 C30,138 950,134 985,128 C975,175 955,215 925,232 L80,232 C50,210 30,180 18,138 Z" fill="{hull}"/>
<path d="M60,210 L940,210 C935,220 930,226 925,232 L80,232 C72,226 66,218 60,210Z" fill="#8E2A22"/>
<path d="M22,146 C200,142 800,140 982,134" stroke="#F2EEE4" stroke-width="4" fill="none"/>{ports}</g></svg>'''
def stars(n,h=700):
    return "".join(f'<circle cx="{R.uniform(0,1920):.0f}" cy="{R.uniform(0,h):.0f}" r="{R.uniform(.8,2.4):.1f}" fill="#fff" opacity="{R.uniform(.35,1):.2f}"/>' for _ in range(n))
def sea(y,c1,c2,uid,front=False):
    wv=" ".join(f"Q{x+60},{y-14} {x+120},{y} T{x+240},{y}" for x in range(-240,2400,240))
    return f'<svg class="sea" viewBox="0 0 1920 1080" width="1920" height="1080"><defs><linearGradient id="sg{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs><path id="wv{uid}" d="M-240,{y} {wv} L2400,1080 L-240,1080Z" fill="url(#sg{uid})"/></svg>'
S=[]
def scene(html,js,bg): S.append((html,js,bg))
# ---- S0 title
scene(f'''<div class="sky" style="background:linear-gradient(#1F2B55 0%,#7A4A6E 38%,#E7835B 62%,#F6C28B 70%)"></div>
<i class="sun" id="sun0"></i>{sea(700,"#2C3E66","#0E1A33","0")}
<div class="abs" id="sh0" style="left:1050px;top:560px">{ship("ship0",520,True)}</div>
<div class="title0"><h1 id="tt0">TITANIC</h1><p id="ts0">Wie das berühmteste Schiff der Welt sank</p></div>''',
 'tl.fromTo("#sun0",{y:0},{y:120,duration:10,ease:"none"},S);tl.fromTo("#sh0",{x:-80},{x:120,duration:10,ease:"none"},S);'
 'tl.fromTo("#tt0",{opacity:0,y:60,scale:.9},{opacity:1,y:0,scale:1,duration:1.4,ease:"expo.out"},S+.6);tl.fromTo("#ts0",{opacity:0,y:20},{opacity:1,y:0,duration:1,ease:"power3.out"},S+1.6);',"#1F2B55")
# ---- S1 ship size
fields="".join(f'<g transform="translate({i*508},0)"><rect x="0" y="0" width="{508 if i<2 else 254}" height="120" fill="{"#4E9A4A" if i%2==0 else "#5BAA56"}" stroke="#fff" stroke-width="4"/>{"<line x1=\'254\' y1=\'0\' x2=\'254\' y2=\'120\' stroke=\'#fff\' stroke-width=\'4\'/><circle cx=\'254\' cy=\'60\' r=\'34\' fill=\'none\' stroke=\'#fff\' stroke-width=\'4\'/>" if i<2 else ""}</g>' for i in range(3))
scene(f'''<div class="sky" style="background:linear-gradient(#5DA9DA,#BFE3F4 70%)"></div>
<i class="cloud" style="left:300px;top:110px"></i><i class="cloud" style="left:1350px;top:70px;transform:scale(.7)"></i>{sea(560,"#2E7FB0","#14496E","1")}
<div class="abs" id="sh1" style="left:500px;top:300px">{ship("ship1",1300)}</div>
<div class="abs cmp" id="cmp1" style="left:500px;top:700px"><div class="ruler"><i></i><span>269 m</span></div><svg width="1300" height="124" viewBox="0 0 1300 124">{fields}</svg><p class="clab">≈ 2,5 Fußballfelder</p></div>
<div class="stamp" id="st1">„UNSINKBAR“</div>''',
 'tl.fromTo("#sh1",{x:-1600},{x:0,duration:3,ease:"power2.out"},S);tl.fromTo("#sh1",{y:0},{y:8,duration:1.2,ease:"sine.inOut",yoyo:true,repeat:5},S);'
 'tl.fromTo("#cmp1 .ruler",{opacity:0,scaleX:0},{opacity:1,scaleX:1,duration:.9,ease:"power3.out",transformOrigin:"left center"},S+3.2);'
 'tl.fromTo("#cmp1 svg g",{opacity:0,y:30},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)",stagger:.35},S+3.8);tl.fromTo("#cmp1 .clab",{opacity:0},{opacity:1,duration:.5},S+5);'
 'tl.fromTo("#st1",{opacity:0,scale:2.4,rotation:-14},{opacity:1,scale:1,rotation:-8,duration:.35,ease:"power4.in"},S+8.0);',"#5DA9DA")
# ---- S2 map
scene(f'''<div class="sky" style="background:#A9D1E2"></div>
<svg class="abs" style="left:0;top:0" width="1920" height="1080" viewBox="0 0 1920 1080">
<defs><pattern id="grid2" width="120" height="120" patternUnits="userSpaceOnUse"><path d="M120 0H0V120" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/></pattern></defs>
<rect width="1920" height="1080" fill="url(#grid2)"/>
<path d="M0,120 C120,140 260,220 330,330 C380,400 430,420 470,470 C500,520 470,600 420,660 C380,720 400,820 360,900 C320,980 200,1040 0,1080Z" fill="#E6D8B4" stroke="#B9A77A" stroke-width="4"/>
<path d="M1590,170 C1630,140 1690,150 1700,200 C1720,250 1700,290 1720,320 C1700,350 1640,360 1600,340 C1620,300 1580,280 1600,250 C1570,220 1570,190 1590,170Z" fill="#E6D8B4" stroke="#B9A77A" stroke-width="4"/>
<path d="M1530,240 C1555,230 1570,260 1555,290 C1540,310 1515,290 1520,265Z" fill="#E6D8B4" stroke="#B9A77A" stroke-width="4"/>
<path d="M1760,300 C1800,260 1920,250 1920,250 L1920,700 C1860,690 1800,640 1790,560 C1780,480 1740,420 1760,300Z" fill="#E6D8B4" stroke="#B9A77A" stroke-width="4"/>
<path id="route2" d="M1660,335 C1450,420 1000,560 760,560 C600,560 520,500 440,455" fill="none" stroke="#C0392B" stroke-width="7" stroke-dasharray="18 14"/>
<circle cx="1660" cy="335" r="13" fill="#1C3159"/><circle cx="440" cy="455" r="13" fill="#1C3159"/>
<g id="xmark2" opacity="0"><path d="M995,535 l30,30 M1025,535 l-30,30" stroke="#0E2240" stroke-width="7" stroke-linecap="round"/></g>
</svg>
<p class="mapl" style="left:1500px;top:380px">SOUTHAMPTON</p><p class="mapl" style="left:330px;top:490px">NEW YORK</p><p class="mapl sm" style="left:1720px;top:600px">EUROPA</p><p class="mapl sm" style="left:120px;top:300px">NORDAMERIKA</p><p class="mapl sm sea2" style="left:520px;top:700px">NORDATLANTIK</p>
<div class="abs" id="mk2" style="left:0;top:0">{ship("ship2",150,False,-1)}</div>
<div class="card2" id="c2"><p class="cdate">10. April 1912</p><p class="cnum">≈ <span id="n2">0</span></p><p class="ctext">Menschen an Bord</p></div>''',
 '''const rp=document.getElementById("route2");const L=rp.getTotalLength();gsap.set(rp,{strokeDasharray:L+" "+L,strokeDashoffset:L});
 tl.fromTo(rp,{strokeDashoffset:L},{strokeDashoffset:L*0.38,duration:9,ease:"none"},S+.8);
 const o2={u:0};const mk=document.getElementById("mk2");
 const pl=(u)=>{const p=rp.getPointAtLength(L*u);gsap.set(mk,{x:p.x-75,y:p.y-62});};pl(0);
 tl.to(o2,{u:.62,duration:9,ease:"none",onUpdate:()=>pl(o2.u)},S+.8);
 tl.fromTo("#c2",{opacity:0,y:40},{opacity:1,y:0,duration:.7,ease:"power3.out"},S+.4);
 const n2={v:0};tl.to(n2,{v:2200,duration:2,ease:"power2.out",onUpdate:()=>{document.getElementById("n2").textContent=Math.round(n2.v).toLocaleString("de-CH")}},S+6.5);''',"#A9D1E2")
# ---- S3 night warnings
warn="".join(f'<div class="warn"><b>FUNKSPRUCH</b><span>Eis gesichtet!</span></div>' for i in range(4))
scene(f'''<div class="sky" style="background:linear-gradient(#030814,#0D2142 75%)"></div><svg class="abs" width="1920" height="700" style="left:0;top:0">{stars(170)}</svg>{sea(690,"#0B1D36","#020812","3")}
<div class="abs" id="sh3" style="left:380px;top:470px">{ship("ship3",900,True)}</div>
<div class="warns" id="w3">{warn}</div>
<div class="gauge" id="g3"><svg width="300" height="190" viewBox="0 0 300 190"><path d="M30,170 A120,120 0 0 1 270,170" fill="none" stroke="#2A4A72" stroke-width="22"/><path id="ga3" d="M30,170 A120,120 0 0 1 270,170" fill="none" stroke="#F0B44C" stroke-width="22" stroke-dasharray="377" stroke-dashoffset="377"/><g id="nd3"><line x1="150" y1="170" x2="60" y2="170" stroke="#fff" stroke-width="7" stroke-linecap="round"/></g><circle cx="150" cy="170" r="12" fill="#fff"/></svg><p><b>≈ 22</b> Knoten</p></div>''',
 'tl.fromTo("#sh3",{x:-200},{x:150,duration:10,ease:"none"},S);'
 'tl.fromTo("#w3 .warn",{opacity:0,x:80},{opacity:1,x:0,duration:.45,ease:"back.out(1.6)",stagger:.7},S+3.0);'
 'tl.fromTo("#g3",{opacity:0},{opacity:1,duration:.5},S+6.5);tl.fromTo("#ga3",{strokeDashoffset:377},{strokeDashoffset:377*0.18,duration:1.4,ease:"power2.out"},S+6.8);'
 'tl.fromTo("#nd3",{rotation:0},{rotation:148,svgOrigin:"150 170",duration:1.4,ease:"power2.out"},S+6.8);',"#030814")
# ---- S4 iceberg
scene(f'''<div class="sky" style="background:linear-gradient(#020610,#0A1A35 75%)"></div><svg class="abs" width="1920" height="700" style="left:0;top:0">{stars(140)}</svg>
<div class="abs" id="ice4" style="left:1180px;top:250px"><svg width="640" height="560" viewBox="0 0 640 560"><defs><linearGradient id="ig" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4FBFF"/><stop offset=".6" stop-color="#BFDDEA"/><stop offset="1" stop-color="#6E9DB5"/></linearGradient></defs><path d="M40,520 L120,300 L190,330 L260,120 L330,60 L380,150 L450,140 L520,330 L600,520Z" fill="url(#ig)"/><path d="M330,60 L300,250 L260,120Z M450,140 L420,330 L380,150Z" fill="#fff" opacity=".6"/><path d="M120,300 L160,520 L40,520Z" fill="#7FA9BF" opacity=".6"/></svg></div>
{sea(700,"#0B1D36","#020812","4")}
<div class="abs" id="sh4" style="left:120px;top:480px">{ship("ship4",820,True)}</div>
<div class="bubble" id="bb4">„Eisberg direkt voraus!“</div>
<div class="clock" id="ck4">23:40</div><i class="flash" id="fl4"></i>''',
 'tl.fromTo("#ice4",{opacity:0,scale:.75,y:40},{opacity:1,scale:1,y:0,duration:3,ease:"power2.out"},S);'
 'tl.fromTo("#sh4",{x:0},{x:420,duration:8.5,ease:"power1.in"},S);tl.fromTo("#sh4",{rotation:0},{rotation:-2.5,duration:2,ease:"sine.inOut"},S+5.2);'
 'tl.fromTo("#ck4",{opacity:0,y:-30},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.6);'
 'tl.fromTo("#bb4",{opacity:0,scale:.4},{opacity:1,scale:1,duration:.45,ease:"back.out(2)"},S+2.4);tl.to("#bb4",{opacity:0,duration:.4},S+6.2);'
 '{const H=S+8.3;tl.fromTo("#fl4",{opacity:0},{opacity:.55,duration:.06},H);tl.to("#fl4",{opacity:0,duration:.5},H+.06);'
 'const sh=[[14,-6],[-12,8],[10,4],[-8,-6],[6,3],[-3,-2],[0,0]];sh.forEach((p,i)=>tl.set("#sc4wrap",{x:p[0],y:p[1]},H+i*.05));}',"#020610")
# ---- S5 compartments
comp="".join(f'<g><rect x="{40+i*86}" y="60" width="86" height="260" fill="none" stroke="#9FD3F5" stroke-width="3"/><rect class="wf5" id="wf5_{i}" x="{42+i*86}" y="318" width="82" height="0" fill="#3EA6E8" opacity=".8"/><text x="{83+i*86}" y="350" fill="#9FD3F5" font-size="24" text-anchor="middle" font-family="Montserrat">{i+1}</text></g>' for i in range(16))
scene(f'''<div class="sky" style="background:#0F2A44"></div><div class="bp"></div>
<p class="h5" id="h5"><b>16</b> wasserdichte Abteilungen</p>
<div class="abs" id="hull5" style="left:330px;top:300px"><svg width="1520" height="420" viewBox="0 0 1500 400"><path d="M20,60 L1460,60 C1490,130 1470,260 1420,320 L80,320 C40,260 20,160 20,60Z" fill="#163A5C" stroke="#CFE9FB" stroke-width="5"/>{comp}<path d="M1500,40 L1500,40" /></svg></div>
<div class="verd" id="ok5">4 geflutet → schwimmt noch ✔</div><div class="verd bad" id="bad5">5 geflutet → sinkt ✘</div>''',
 'tl.fromTo("#h5",{opacity:0,y:-30},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.3);'
 'tl.fromTo("#hull5",{opacity:0,y:40},{opacity:1,y:0,duration:.8,ease:"power3.out"},S+.2);'
 '[15,14,13,12].forEach((c,i)=>tl.fromTo("#wf5_"+c,{attr:{y:318,height:0}},{attr:{y:62,height:256},duration:.9,ease:"power1.inOut"},S+3.2+i*.6));'
 'tl.fromTo("#ok5",{opacity:0,y:20},{opacity:1,y:0,duration:.5,ease:"back.out(1.6)"},S+5.6);tl.to("#ok5",{opacity:0,duration:.3},S+6.9);'
 'tl.fromTo("#wf5_11",{attr:{y:318,height:0}},{attr:{y:62,height:256},duration:.9,ease:"power1.inOut"},S+6.9);'
 'tl.fromTo("#bad5",{opacity:0,scale:1.4},{opacity:1,scale:1,duration:.4,ease:"power3.out"},S+7.8);'
 'tl.to("#hull5",{rotation:4,y:30,duration:2.4,ease:"power2.in"},S+7.8);',"#0F2A44")
# ---- S6 lifeboats
boat='<svg viewBox="0 0 100 44" width="96" height="42"><path d="M4,8 L96,8 C90,30 74,40 50,40 C26,40 10,30 4,8Z" fill="#F4F1EA" stroke="#7A6E5A" stroke-width="3"/><path d="M8,16 L92,16" stroke="#C0392B" stroke-width="3"/></svg>'
scene(f'''<div class="sky" style="background:linear-gradient(#DCEFF7,#A9D1E2)"></div>
<p class="h6" id="h6">Nur <b>20</b> Rettungsboote</p>
<div class="boats" id="bt6">{"".join(f'<i class="bt">{boat}</i>' for _ in range(20))}</div>
<div class="bars" id="bars6"><div class="brow"><span class="bl">Menschen an Bord</span><div class="btrack"><i class="bfill b1"></i></div><span class="bv">≈ 2200</span></div>
<div class="brow"><span class="bl">Plätze in Booten</span><div class="btrack"><i class="bfill b2"></i></div><span class="bv">1178</span></div></div>
<div class="half6" id="hf6">→ nur gut die Hälfte!</div>''',
 'tl.fromTo("#h6",{opacity:0,y:-30},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+.3);'
 'tl.fromTo(".bt",{scale:0,opacity:0},{scale:1,opacity:1,duration:.35,ease:"back.out(2)",stagger:.09},S+1.6);'
 'tl.fromTo(".b1",{width:0},{width:900,duration:1.0,ease:"power2.out"},S+4.6);tl.fromTo(".b2",{width:0},{width:482,duration:1.0,ease:"power2.out"},S+5.6);'
 'tl.fromTo("#bars6 .brow",{opacity:0},{opacity:1,duration:.4,stagger:1},S+4.4);'
 'tl.fromTo("#hf6",{opacity:0,x:-30},{opacity:1,x:0,duration:.5,ease:"back.out(1.6)"},S+7.2);',"#DCEFF7")
# ---- S7 sinking
scene(f'''<div class="sky" style="background:linear-gradient(#01040B,#0A1A35 75%)"></div><svg class="abs" width="1920" height="700" style="left:0;top:0">{stars(150)}</svg>
<div class="abs" id="sh7" style="left:420px;top:420px;width:1100px;height:363px">
 <div class="abs half" id="st7" style="left:0;top:0;width:1100px;height:363px;clip-path:inset(0 46% 0 0)">{ship("ship7a",1100,True)}</div>
 <div class="abs half" id="bw7" style="left:0;top:0;width:1100px;height:363px;clip-path:inset(0 0 0 54%)">{ship("ship7b",1100,True)}</div>
</div>
{sea(720,"#0B1D36","#020812","7")}
<div class="clock" id="ck7">02:20</div>''',
 'tl.fromTo("#sh7",{rotation:0,y:0},{rotation:9,y:60,duration:3.6,ease:"power1.in",transformOrigin:"55% 60%"},S+.4);'
 'tl.fromTo("#bw7",{rotation:0,y:0,x:0},{rotation:24,y:520,x:120,duration:3.5,ease:"power2.in",transformOrigin:"54% 50%"},S+4.0);'
 'tl.fromTo("#st7",{rotation:0,y:0},{rotation:-62,y:-60,duration:1.6,ease:"power2.out",transformOrigin:"54% 60%"},S+4.0);'
 'tl.to("#st7",{y:620,duration:2.8,ease:"power2.in"},S+5.6);'
 'tl.fromTo("#ck7",{opacity:0,y:-30},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+7.0);',"#01040B")
# ---- S8 cold / victims
scene(f'''<div class="sky" style="background:linear-gradient(#0A1424,#05080F)"></div>
<div class="therm" id="th8"><svg width="160" height="620" viewBox="0 0 160 620"><rect x="55" y="20" width="50" height="500" rx="25" fill="#1E2C44" stroke="#9FB3CC" stroke-width="5"/><circle cx="80" cy="550" r="55" fill="#3EA6E8" stroke="#9FB3CC" stroke-width="5"/><rect id="mc8" x="67" y="40" width="26" height="480" rx="13" fill="#3EA6E8"/>{"".join(f'<line x1="110" y1="{60+k*45}" x2="130" y2="{60+k*45}" stroke="#9FB3CC" stroke-width="3"/>' for k in range(10))}</svg><p id="tv8">−2 °C</p></div>
<div class="vict" id="v8"><p class="vnum">≈ 1500</p><p class="vtxt">Menschen verloren in dieser Nacht ihr Leben</p></div>''',
 'tl.fromTo("#th8",{opacity:0},{opacity:1,duration:.8},S+.2);tl.fromTo("#mc8",{attr:{y:40,height:480}},{attr:{y:330,height:190},duration:2.2,ease:"power2.out"},S+.6);'
 'tl.fromTo("#tv8",{opacity:0},{opacity:1,duration:.6},S+2.2);tl.fromTo("#v8",{opacity:0,y:20},{opacity:1,y:0,duration:1.4,ease:"power2.out"},S+2.8);',"#0A1424")
# ---- S9 Carpathia
scene(f'''<div class="sky" style="background:linear-gradient(#5B6E9A,#F2A97E 55%,#F8D7A8 68%)"></div>{sea(690,"#4F7FA6","#1F4363","9")}
<div class="abs" id="cp9" style="left:900px;top:470px">{ship("ship9",760,False,-1,"#1B1B1B","#D4502A",1)}</div>
<div class="abs boats9" id="lb9">{"".join(f'<i class="lb" style="left:{x}px;top:{y}px">{boat}</i>' for x,y in [(80,0),(260,30),(430,8),(600,40)])}</div>
<div class="tag9" id="t9"><b>RMS Carpathia</b><span>ca. 4:00 Uhr</span></div><div class="res9" id="r9">≈ 700 Überlebende gerettet</div>''',
 'tl.fromTo("#cp9",{x:900},{x:0,duration:4.5,ease:"power2.out"},S);tl.fromTo(".lb",{y:0},{y:10,duration:1.1,ease:"sine.inOut",yoyo:true,repeat:6,stagger:.3},S);'
 'tl.fromTo("#t9",{opacity:0,y:-20},{opacity:1,y:0,duration:.6,ease:"power3.out"},S+1.6);tl.fromTo("#r9",{opacity:0,scale:.8},{opacity:1,scale:1,duration:.6,ease:"back.out(1.6)"},S+4.6);',"#5B6E9A")
# ---- S10 deep sea / wreck
bub="".join(f'<i class="bub" style="left:{R.uniform(500,1700):.0f}px;top:{R.uniform(200,1000):.0f}px;width:{(s:=R.uniform(8,22)):.0f}px;height:{s:.0f}px"></i>' for _ in range(22))
scene(f'''<div class="abs deep" id="dp10"></div>{bub}
<div class="abs" id="wr10" style="left:760px;top:560px"><svg width="900" height="380" viewBox="0 0 900 380"><path d="M0,330 C200,310 700,320 900,330 L900,380 L0,380Z" fill="#1C1A16"/><g transform="rotate(-6 450 250)"><path d="M120,170 C300,150 650,140 800,120 C790,180 760,240 720,270 L160,290 C130,250 120,210 120,170Z" fill="#5B3B2A"/><path d="M200,150 L240,90 L260,150Z M520,140 L540,95 L560,140Z" fill="#4A2F22"/>{"".join(f'<circle cx="{x}" cy="{R.uniform(185,215):.0f}" r="5" fill="#2A1A12"/>' for x in range(200,720,34))}{"".join(f'<path d="M{x},{R.uniform(250,275):.0f} l4,{R.uniform(18,40):.0f}" stroke="#8A5A3A" stroke-width="4" stroke-linecap="round"/>' for x in range(190,700,28))}</g></svg></div>
<i class="beam" id="bm10"></i><div class="abs" id="sub10" style="left:1520px;top:420px"><svg width="170" height="110" viewBox="0 0 170 110"><ellipse cx="85" cy="60" rx="70" ry="38" fill="#F2C230"/><circle cx="40" cy="55" r="16" fill="#9FD3F5" stroke="#555" stroke-width="4"/><rect x="140" y="50" width="26" height="14" fill="#555"/></svg></div>
<div class="depth" id="dg10"><span id="dv10">0</span> m</div><div class="tag10" id="t10"><b>1985</b><span>Robert Ballard findet das Wrack</span></div>''',
 'tl.fromTo("#dp10",{y:0},{y:-1800,duration:6,ease:"power2.inOut"},S);'
 'tl.fromTo("#wr10",{opacity:0,y:200},{opacity:1,y:0,duration:3,ease:"power2.out"},S+4);'
 'tl.fromTo("#sub10",{opacity:0,x:200},{opacity:1,x:0,duration:3,ease:"power2.out"},S+4.5);tl.fromTo("#bm10",{opacity:0},{opacity:1,duration:1.2},S+6.5);'
 'tl.fromTo(".bub",{y:0},{y:-260,duration:11,ease:"none"},S);'
 'const d10={v:0};tl.to(d10,{v:3800,duration:6,ease:"power2.inOut",onUpdate:()=>{document.getElementById("dv10").textContent=Math.round(d10.v).toLocaleString("de-CH")}},S);'
 'tl.fromTo("#t10",{opacity:0,y:20},{opacity:1,y:0,duration:.7,ease:"power3.out"},S+4.2);',"#0E4A6B")
# ---- S11 outro
scene(f'''<div class="sky" style="background:linear-gradient(#69B5E3,#CDEBF7 70%)"></div><i class="cloud" style="left:1300px;top:90px"></i>{sea(640,"#2E7FB0","#14496E","11")}
<div class="abs" id="sh11" style="left:880px;top:390px">{ship("ship11",820)}</div>
<div class="rule11" id="r11"><p class="rt">Neue Regeln nach dem Unglück</p><p class="rb">🛟 Rettungsboote für <b>alle</b> an Bord</p><p class="rs">Internationale Konvention SOLAS, 1914</p></div>
<div class="bye" id="by11">Tschüss!</div>''',
 'tl.fromTo("#sh11",{x:200},{x:-120,duration:14,ease:"none"},S);'
 'tl.fromTo("#r11",{opacity:0,y:40},{opacity:1,y:0,duration:.8,ease:"power3.out"},S+1.2);'
 'tl.fromTo("#by11",{opacity:0,scale:.5},{opacity:1,scale:1,duration:.6,ease:"back.out(2)"},S+10.3);',"#69B5E3")

# Kurt poses per scene: (left,top,width,armR rotation, armL rot)
BIG=(70,250,470); SMALL=(10,700,250)
pose=[BIG,SMALL,SMALL,SMALL,SMALL,SMALL,SMALL,SMALL,SMALL,SMALL,SMALL,BIG]
css=open('/tmp/claude-0/-home-user-Nexus/78db4e45-757a-5460-8fc1-0f9e8d2fdc56/scratchpad/titanic.css').read()
body="";js=""
for k,(html,j,bg) in enumerate(S):
    s=SC[k]; d=round(SC[k+1]-SC[k],3)
    wrap=f'<div id="sc{k}wrap" class="abs" style="inset:0">{html}</div>'
    body+=f'      <section id="s{k}" class="scene clip" data-start="{s}" data-duration="{d}" data-track-index="{k%2}" style="background:{bg}">\n        {wrap}\n        <i class="fade" id="f{k}"></i>\n      </section>\n'
    fin='' if k==0 else f'tl.fromTo("#f{k}",{{opacity:1}},{{opacity:0,duration:.4,ease:"power1.out"}},S);'
    fout=f'tl.fromTo("#f{k}",{{opacity:0}},{{opacity:1,duration:.35,ease:"power1.in",immediateRender:false}},S+{d}-.35);' if k<len(S)-1 else f'tl.fromTo("#f{k}",{{opacity:0}},{{opacity:1,duration:1.2,ease:"power1.in",immediateRender:false}},S+{d}-1.2);'
    js+=f'      {{const S={s};{fin}{j}{fout}}}\n'
# Kurt element spanning whole film
body+=f'      <div id="kurt" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="5">{kurt_svg(470)}</div>\n'
body+=f'      <div id="capbox" class="clip" data-start="0.6" data-duration="{round(TOTAL-1.8,2)}" data-track-index="6"><p id="cap"></p></div>\n'
# Kurt moves between poses
kjs=""
for k in range(len(S)):
    l,t,w=pose[k]; sc=w/470
    if k==0: kjs+=f'gsap.set("#kurt",{{x:{l},y:{t},scale:{sc}}});'
    elif pose[k]!=pose[k-1]: kjs+=f'tl.to("#kurt",{{x:{l},y:{t},scale:{sc},duration:.8,ease:"power3.inOut"}},{SC[k]-.2});'
# gestures
kjs+='tl.fromTo("#kArmR",{rotation:0},{rotation:-135,svgOrigin:"292 360",duration:.5,ease:"back.out(1.6)"},0.9);'
kjs+='tl.fromTo("#kArmR",{rotation:-135},{rotation:-110,svgOrigin:"292 360",duration:.35,ease:"sine.inOut",yoyo:true,repeat:5,immediateRender:false},1.4);'
kjs+='tl.to("#kArmR",{rotation:0,svgOrigin:"292 360",duration:.6,ease:"power2.inOut"},3.7);'
for k in range(1,11):
    a=SC[k]+1.0
    kjs+=f'tl.to("#kArmR",{{rotation:-75,svgOrigin:"292 360",duration:.5,ease:"back.out(1.6)"}},{a});tl.to("#kArmR",{{rotation:0,svgOrigin:"292 360",duration:.6,ease:"power2.inOut"}},{a+2.6});'
e=SC[11]+10.0
kjs+=f'tl.to("#kArmR",{{rotation:-135,svgOrigin:"292 360",duration:.5,ease:"back.out(1.6)"}},{e});tl.fromTo("#kArmR",{{rotation:-135}},{{rotation:-110,svgOrigin:"292 360",duration:.35,ease:"sine.inOut",yoyo:true,repeat:5,immediateRender:false}},{e+.5});'
# breathing / idle bob
kjs+=f'tl.fromTo("#kHead",{{y:0}},{{y:3,duration:1.6,ease:"sine.inOut",yoyo:true,repeat:{int(TOTAL/1.6)-1}}},0);'
# master driver: lipsync, blink, captions
lip=json.dumps(T['lip']); caps=json.dumps(T['caps'],ensure_ascii=False)
blinks=[]; t=1.7
while t<TOTAL-1: blinks.append(round(t,2)); t+=2.6+R.random()*2.4
kjs+=f'''const LIP={lip};const CAPS={caps};const BL={json.dumps(blinks)};
const mouth=document.querySelector("#kMouth");const lids=document.querySelector("#kLids");const capEl=document.getElementById("cap");let lastCap=-2;
const drive=(t)=>{{const i=Math.min(LIP.length-1,Math.max(0,Math.floor(t*30)));const o=LIP[i];
 gsap.set(mouth,{{scaleY:0.18+1.25*o,scaleX:0.9+0.15*o,svgOrigin:"210 278"}});
 let b=0;for(const x of BL){{if(t>=x&&t<x+0.13){{b=1;break;}}}} gsap.set(lids,{{scaleY:b,svgOrigin:"210 163"}});
 let ci=-1;for(let k=0;k<CAPS.length;k++){{if(t>=CAPS[k].t&&t<CAPS[k].t+CAPS[k].d+0.25){{ci=k;}}}}
 if(ci!==lastCap){{capEl.textContent=ci>=0?CAPS[ci].text:"";capEl.style.opacity=ci>=0?1:0;lastCap=ci;}}}};
const M={{t:0}};drive(0);tl.to(M,{{t:{TOTAL},duration:{TOTAL},ease:"none",onUpdate:()=>drive(M.t)}},0);
'''
SFX=[("impact4","impact-bass-1",round(SC[4]+8.3,2),0,1.2,.55),("break7","impact-bass-2",round(segs[7]['start']+3.6,2),0,1.2,.45),("whcine10","whoosh-cinematic",round(SC[10]-1.8,2),0,3.5,.25),("chime11","chime",round(TOTAL-4.5,2),0,2.5,.3)]
aud=f'      <audio id="voice" src="assets/audio/voice.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="1"></audio>\n'
aud+=f'      <audio id="score" src="assets/audio/score.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="21" data-volume="0.32"></audio>\n'
aud+=f'      <audio id="fx" src="assets/audio/fx.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="22" data-volume="0.9"></audio>\n'
for n,(i,f,s,ms,d,v) in enumerate(SFX):
    aud+=f'      <audio id="sfx-{i}" src="assets/sfx/{f}.mp3" data-start="{s}" data-media-start="{ms}" data-duration="{d}" data-track-index="{23+n}" data-volume="{v}"></audio>\n'
html=f'''<!doctype html>
<html lang="de"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1920, height=1080"/>
<script src="assets/gsap.min.js"></script>
<style>{css}</style></head>
<body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1920" data-height="1080">
{body}{aud}    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{js}      {kjs}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
</body></html>'''
open(out,'w').write(html)
print("ok",TOTAL)
