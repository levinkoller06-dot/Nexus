const FPS = 30, DURATION = TL.duration, C = TL.cues;
const clamp = (x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const prog = (t,a,b)=>clamp((t-a)/(b-a));
const eo3 = x=>1-Math.pow(1-x,3);
const eob = x=>{const c=1.70158,d=c+1;return 1+d*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const lerp=(a,b,x)=>a+(b-a)*x;
const $ = id=>document.getElementById(id);
const scenes = TL.scenes;

function pop(el,t,start,{dx=0,dy=40}={}){
  const p = eo3(prog(t,start,start+0.5));
  el.style.opacity = p;
  el.style.transform = `translate(${(1-p)*dx}px,${(1-p)*dy}px)`;
}

function render(t){
  $('prog').style.width = (t/DURATION*100)+'%';
  for(const [a,b,id] of scenes){
    const el=$(id), lt=t-a;
    const fi=prog(lt,0,.35), fo=1-prog(lt,b-a-.35,b-a);
    el.style.opacity = (t>=a&&t<b) ? Math.min(fi,fo) : 0;
    el.style.display = (t>=a-.01&&t<b+.01) ? 'block':'none';
  }
  let lt;
  // S1
  if(t<4){
    $('bg1').style.transform=`scale(${1+t*0.03})`;
    $('s1a').style.transform=`translateX(${(1-eob(prog(t,0.0,0.7)))*-900}px)`;
    $('s1b').style.transform=`translateX(${(1-eob(prog(t,0.5,1.2)))*900}px)`;
    $('s1q').style.opacity=prog(t,1.5,1.6); const qp=eob(prog(t,1.5,2.1)); $('s1q').style.transform=`scale(${qp}) rotate(${(1-qp)*-40}deg)`;
    pop($('s1c'),t,2,{dy:30});
  }
  // S2 Waage: Kippen passend zum Sprecher
  if(t>=4&&t<14){
    lt=t-4; const tb=C.s2b-4-0.1, te=C.s2c-4-0.1, tc=C.s2d-4-0.1;
    pop($('s2h'),lt,0.2,{dy:-30});
    const ang = lt<tb?0: lt<te? -9*eob(prog(lt,tb,tb+.6)) : lt<tc? lerp(-9,0,eo3(prog(lt,te,te+.6))) : lerp(0,9,eob(prog(lt,tc,tc+.6)));
    $('beam').setAttribute('transform',`translate(0,560) rotate(${ang} 960 9)`);
    $('panL').setAttribute('transform',`rotate(${-ang} 400 18)`);
    $('panR').setAttribute('transform',`rotate(${-ang} 1520 18)`);
    const lbl=$('s2lbl'), sub=$('s2sub'); let ts=0;
    if(lt<tb){lbl.textContent='';sub.textContent='';}
    else if(lt<te){lbl.textContent='Überschuss'; lbl.style.color='var(--bulk)'; sub.textContent='mehr rein als raus  →  BULK'; ts=tb;}
    else if(lt<tc){lbl.textContent='Gleichgewicht'; lbl.style.color='#fff'; sub.textContent='gleich viel  →  Gewicht halten'; ts=te;}
    else {lbl.textContent='Defizit'; lbl.style.color='var(--cut)'; sub.textContent='weniger rein als raus  →  CUT'; ts=tc;}
    lbl.style.transform=`scale(${1+(1-eo3(prog(lt-ts,0,.3)))*0.15})`;
  }
  // S3 Bulk
  if(t>=14&&t<34){
    lt=t-14; pop($('s3t'),lt,0.1,{dx:-100,dy:0}); pop($('s3st'),lt,0.6,{dy:20});
    ['s3a','s3b','s3c','s3d'].forEach((k,i)=>pop($('s3b'+(i+1)),t,C[k]-0.2,{dx:-80,dy:0}));
    const g=eo3(prog(t,C.s3a+0.5,C.s3a+3)), g2=eo3(prog(t,C.s3d+0.4,C.s3d+2.6));
    const H=480, m1=H*0.30*g, f1=H*0.12*g, m2=H*0.30*g2, f2=H*0.52*g2;
    $('m1').setAttribute('y',640-m1); $('m1').setAttribute('height',m1);
    $('f1').setAttribute('y',640-m1-f1); $('f1').setAttribute('height',f1);
    $('m2').setAttribute('y',640-m2); $('m2').setAttribute('height',m2);
    $('f2').setAttribute('y',640-m2-f2); $('f2').setAttribute('height',f2);
  }
  // S4 Cut
  if(t>=34&&t<52){
    lt=t-34; pop($('s4t'),lt,0.1,{dx:-100,dy:0});
    ['s4a','s4b','s4c','s4d'].forEach((k,i)=>pop($('s4b'+(i+1)),t,C[k]-0.2,{dx:-80,dy:0}));
    const p=eo3(prog(t,C.s4a,C.s4d+1.5)), N=40; let dF='',dM='';
    for(let i=0;i<=N*p;i++){ const x=lerp(80,620,i/N), u=i/N;
      const yF=lerp(240,520,eo3(u)*0.9+u*0.1), yM=360+Math.sin(u*9)*5+u*6;
      dF+=(i?'L':'M')+x+' '+yF+' '; dM+=(i?'L':'M')+x+' '+yM+' '; }
    $('cutFat').setAttribute('d',dF); $('cutMus').setAttribute('d',dM);
  }
  // S5 Protein
  if(t>=52&&t<68){
    pop($('s5h'),t,C.s5a-0.2,{dy:-30});
    const n=lerp(1.6,2.2,eo3(prog(t,C.s5b,C.s5b+2.8)));
    const txt = t<C.s5b?'1,6': t<C.s5b+3 ? n.toFixed(1).replace('.',',') : '1,6–2,2';
    $('s5n').textContent=txt; $('s5n').style.fontSize = t>=C.s5b+3 ? '200px':'260px';
    pop($('s5n'),t,C.s5a+0.3,{dy:30});
    pop($('s5u'),t,C.s5a+0.8,{dy:20}); pop($('s5c'),t,C.s5c-0.2,{dy:40});
  }
  // S6 Zyklus
  if(t>=68&&t<80){
    pop($('s6h'),t,C.s6a-0.2,{dy:-30});
    $('band1').setAttribute('width',830*eo3(prog(t,C.s6a,C.s6a+1.6)));
    $('band2').setAttribute('width',590*eo3(prog(t,C.s6a+2.8,C.s6a+4.2)));
    const pts=[[160,700],[400,640],[700,520],[1000,430],[1150,500],[1350,590],[1600,640]];
    const total=prog(t,C.s6a+0.3,C.s6a+4.9); let d='';
    const segs=pts.length-1, f=total*segs;
    for(let i=0;i<=Math.floor(f)&&i<pts.length;i++){ d+=(i?'L':'M')+pts[i][0]+' '+pts[i][1]+' '; }
    const i=Math.min(Math.floor(f),segs-1), r=f-i;
    if(total<1&&i<segs){ d+='L'+lerp(pts[i][0],pts[i+1][0],r)+' '+lerp(pts[i][1],pts[i+1][1],r); }
    $('wave').setAttribute('d',d);
    const so=(id,s)=>$(id).setAttribute('opacity',prog(t,s,s+0.5));
    so('l1',C.s6a+0.8);so('l1b',C.s6a+1.6);so('l2',C.s6a+3.0);so('l2b',C.s6a+3.8);
    pop($('s6c'),t,C.s6b-0.2,{dy:40});
  }
  // S7 Outro
  if(t>=80){
    pop($('s7a'),t,C.s7a,{dx:-100,dy:0}); pop($('s7b'),t,C.s7a+1.2,{dx:-100,dy:0});
    pop($('s7c'),t,C.s7b,{dy:30}); pop($('s7d'),t,C.s7b+1.2,{dy:20});
  }
}
window.render = render; window.FPS=FPS; window.DURATION=DURATION;
render(0);
if(!navigator.webdriver){ const t0=performance.now(); (function loop(){ const t=((performance.now()-t0)/1000)%DURATION; render(t); requestAnimationFrame(loop);})(); }
