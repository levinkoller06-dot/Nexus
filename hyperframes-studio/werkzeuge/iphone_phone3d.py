# 3D iPhone-20-Konzept aus CSS-3D-Ebenen
FINISH={
 'mitternacht':dict(back1='#2B2D33',back2='#14151A',rim1='#5A5D66',rim2='#23252B',glow='#7D8BFF'),
 'polar':dict(back1='#F4F3EF',back2='#DAD8D2',rim1='#F2F1EC',rim2='#B9B7B0',glow='#FFFFFF'),
 'gletscher':dict(back1='#CFE0EE',back2='#9DBBD3',rim1='#D9E6F0',rim2='#8FA9BD',glow='#BFE3FF'),
 'sand':dict(back1='#E8D9C4',back2='#C9B497',rim1='#EDE0CC',rim2='#A8916F',glow='#FFE1B8'),
 'salbei':dict(back1='#C9D3C2',back2='#9AA894',rim1='#D2DACB',rim2='#7F8C79',glow='#DFF5D3'),
}
def wallpaper_svg(pid):
    blobs=[(25,20,48,'#7B5CFF'),(80,35,45,'#FF5FA8'),(40,80,52,'#21C3FF'),(85,90,42,'#FF9F43')]
    defs=''.join(f'<radialGradient id="{pid}w{i}"><stop offset="0" stop-color="{c}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for i,(x,y,r,c) in enumerate(blobs))
    cs=''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*0.55}" fill="url(#{pid}w{i})"/>' for i,(x,y,r,c) in enumerate(blobs))
    return f'<svg class="wp" viewBox="0 0 100 100" preserveAspectRatio="none"><defs>{defs}</defs><rect width="100" height="100" fill="#0B0B18"/>{cs}</svg>'
def wallpaper(kind='aurora'):
    if kind=='aurora':
        return ('radial-gradient(circle at 25% 20%,#7B5CFF 0%,rgba(123,92,255,0) 45%),'
                'radial-gradient(circle at 80% 35%,#FF5FA8 0%,rgba(255,95,168,0) 42%),'
                'radial-gradient(circle at 40% 80%,#21C3FF 0%,rgba(33,195,255,0) 48%),'
                'radial-gradient(circle at 85% 90%,#FF9F43 0%,rgba(255,159,67,0) 40%),#0B0B18')
    return kind
def phone(pid,w=420,finish='mitternacht',screen='',wall='aurora',slices=22,screen_on=True):
    f=FINISH[finish]; h=round(w*2.07); t=round(w*0.085); r=round(w*0.17)
    sl=''.join(f'<i class="sl" style="transform:translateZ({-t/2+t*i/(slices-1):.2f}px);background:linear-gradient(90deg,{f["rim1"]},{f["rim2"]} 45%,{f["rim1"]} 55%,{f["rim2"]});border-radius:{r}px"></i>' for i in range(slices))
    bw=w-2*round(w*0.06); bh=round(w*0.30); bx=round(w*0.06); by=round(w*0.06)
    cam=(f'<div class="cbar" style="left:{bx}px;top:{by}px;width:{bw}px;height:{bh}px;border-radius:{round(bh*0.42)}px;background:linear-gradient(180deg,{f["rim1"]},{f["back2"]})">'
         f'<svg class="lsv" viewBox="0 0 {bw} {bh}" width="{bw}" height="{bh}"><defs>'
         f'<radialGradient id="{pid}L" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#2E4590"/><stop offset=".5" stop-color="#0C1028"/><stop offset="1" stop-color="#020205"/></radialGradient>'
         f'<linearGradient id="{pid}R" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6B6E77"/><stop offset=".5" stop-color="#17181C"/><stop offset="1" stop-color="#4E5059"/></linearGradient></defs>'
         + ''.join(f'<circle cx="{cx:.1f}" cy="{bh*0.5:.1f}" r="{bh*0.32:.1f}" fill="url(#{pid}R)"/><circle cx="{cx:.1f}" cy="{bh*0.5:.1f}" r="{bh*0.25:.1f}" fill="#07080C"/><circle cx="{cx:.1f}" cy="{bh*0.5:.1f}" r="{bh*0.19:.1f}" fill="url(#{pid}L)"/><circle class="lgl" cx="{cx-bh*0.06:.1f}" cy="{bh*0.43:.1f}" r="{bh*0.045:.1f}" fill="#FFFFFF" opacity=".7"/>' for cx in (bh*0.52,bh*1.22,bh*1.92))
         + f'<circle cx="{bw-bh*0.31:.1f}" cy="{bh*0.35:.1f}" r="{bh*0.11:.1f}" fill="#F3E7C8"/><circle cx="{bw-bh*0.31:.1f}" cy="{bh*0.66:.1f}" r="{bh*0.08:.1f}" fill="#15161A"/></svg></div>')
    scr_bg=wallpaper(wall)
    front=(f'<div class="face front" style="transform:translateZ({t/2:.1f}px);border-radius:{r}px">'
           f'<div class="scr" style="inset:{max(2,round(w*0.012))}px;border-radius:{r-3}px;background:#0B0B18;font-size:{w*0.045:.1f}px">{wallpaper_svg(pid)}<div class="scrc">{screen}</div>'
           f'<i class="scroff" style="opacity:{0 if screen_on else 1}"></i><i class="curve"></i><i class="gl"></i></div></div>')
    back=(f'<div class="face back" style="transform:rotateY(180deg) translateZ({t/2:.1f}px);border-radius:{r}px;background:linear-gradient(160deg,{f["back1"]},{f["back2"]})">'
          f'{cam}<i class="bgl"></i></div>')
    return (f'<div class="ph3d" id="{pid}" style="width:{w}px;height:{h}px">{sl}{back}{front}</div>')
PHONE_CSS='''
.stage{position:absolute;inset:0;perspective:2600px;perspective-origin:50% 45%}
.ph3d{position:absolute;transform-style:preserve-3d}
.ph3d .sl{position:absolute;inset:0;display:block;backface-visibility:visible}
.ph3d .face{position:absolute;inset:0;overflow:hidden;backface-visibility:hidden}
.ph3d .front{background:#050506;box-shadow:inset 0 0 0 2px rgba(255,255,255,.18)}
.ph3d .scr{position:absolute;overflow:hidden}
.ph3d .scrc{position:absolute;inset:0}
.ph3d .scroff{position:absolute;inset:0;background:#030304;display:block}
.ph3d .curve{position:absolute;inset:0;display:block;border-radius:inherit;box-shadow:inset 0 0 18px 6px rgba(0,0,0,.55),inset 0 0 2px 1px rgba(255,255,255,.35)}
.ph3d .gl{position:absolute;inset:-40%;display:block;background:linear-gradient(115deg,rgba(255,255,255,0) 40%,rgba(255,255,255,.16) 48%,rgba(255,255,255,0) 56%)}
.ph3d .bgl{position:absolute;inset:-40%;display:block;background:linear-gradient(115deg,rgba(255,255,255,0) 38%,rgba(255,255,255,.28) 47%,rgba(255,255,255,0) 58%)}
.ph3d .cbar{position:absolute;overflow:hidden;box-shadow:0 6px 18px rgba(0,0,0,.25),inset 0 1px 0 rgba(255,255,255,.5)}
.ph3d .wp{position:absolute;inset:0;width:100%;height:100%;display:block}
.ph3d .lsv{position:absolute;left:0;top:0;display:block}
'''
