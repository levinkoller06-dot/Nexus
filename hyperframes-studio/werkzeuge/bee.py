import math, random
def bee_svg(uid, w=320):
    R=random.Random(4)
    p=uid
    fuzz=[]
    for i in range(140):
        a=R.uniform(0,2*math.pi); r0=R.uniform(52,66); L=R.uniform(10,22)
        x0=370+r0*math.cos(a); y0=190+r0*math.sin(a)
        x1=370+(r0+L)*math.cos(a+R.uniform(-.25,.25)); y1=190+(r0+L)*math.sin(a+R.uniform(-.25,.25))
        col=R.choice(["#C9962E","#B07E22","#8A5E18","#E0B04A"])
        fuzz.append(f'<path d="M{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f}" stroke="{col}" stroke-width="{R.uniform(1.6,3):.1f}" stroke-linecap="round" opacity="{R.uniform(.55,.95):.2f}"/>')
    hfuzz=[]
    for i in range(50):
        a=R.uniform(-2.6,-0.4); r0=R.uniform(44,50); L=R.uniform(6,12)
        x0=455+r0*math.cos(a); y0=205+r0*math.sin(a)
        hfuzz.append(f'<path d="M{x0:.1f},{y0:.1f} l{L*math.cos(a):.1f},{L*math.sin(a):.1f}" stroke="#A97A24" stroke-width="1.6" stroke-linecap="round" opacity=".7"/>')
    veins='<path d="M0,0 C60,-30 140,-80 230,-95 M40,-20 C90,-60 150,-70 200,-60 M100,-55 C130,-45 170,-40 210,-30" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="2"/>'
    wing_d="M0,0 C30,-70 140,-150 250,-130 C320,-118 300,-60 230,-35 C150,-8 60,10 0,0Z"
    wing2_d="M0,0 C40,-40 120,-80 190,-70 C240,-62 230,-25 180,-12 C120,4 50,10 0,0Z"
    return f'''<svg class="beesvg" viewBox="80 20 520 340" width="{w}" height="{w*340/520:.0f}" overflow="visible">
<defs>
 <radialGradient id="{p}abd" cx="45%" cy="30%" r="75%"><stop offset="0" stop-color="#FFE08A"/><stop offset=".35" stop-color="#FDBA21"/><stop offset=".75" stop-color="#D98A06"/><stop offset="1" stop-color="#7A4300"/></radialGradient>
 <linearGradient id="{p}str" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B2A12"/><stop offset=".4" stop-color="#1C1309"/><stop offset="1" stop-color="#0A0603"/></linearGradient>
 <radialGradient id="{p}shade" cx="40%" cy="25%" r="80%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
 <radialGradient id="{p}tho" cx="38%" cy="30%" r="75%"><stop offset="0" stop-color="#6E4E1E"/><stop offset=".5" stop-color="#3A2610"/><stop offset="1" stop-color="#140C04"/></radialGradient>
 <radialGradient id="{p}head" cx="40%" cy="30%" r="75%"><stop offset="0" stop-color="#4A341A"/><stop offset=".6" stop-color="#22160A"/><stop offset="1" stop-color="#0B0703"/></radialGradient>
 <radialGradient id="{p}eye" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#3C4A5A"/><stop offset=".45" stop-color="#11161C"/><stop offset="1" stop-color="#000"/></radialGradient>
 <linearGradient id="{p}wing" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".75"/><stop offset=".5" stop-color="#CFE6FF" stop-opacity=".4"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".18"/></linearGradient>
 <clipPath id="{p}clip"><ellipse cx="235" cy="220" rx="135" ry="98" transform="rotate(-12 235 220)"/></clipPath>
 <filter id="{p}blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
 <filter id="{p}soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2"/></filter>
</defs>
<g class="bwingB"><g transform="translate(385,150) scale(-1,1) rotate(-48)"><path d="{wing2_d}" fill="url(#{p}wing)" stroke="rgba(255,255,255,.55)" stroke-width="2"/></g></g>
<g fill="none" stroke="#1A1208" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
 <path d="M345,245 L330,290 L300,318"/><path d="M380,250 L385,300 L365,335"/><path d="M415,240 L440,285 L455,320"/>
</g>
<path d="M98,248 L130,232 L132,252Z" fill="#1A1208"/>
<g>
 <ellipse cx="235" cy="220" rx="135" ry="98" transform="rotate(-12 235 220)" fill="url(#{p}abd)"/>
 <g clip-path="url(#{p}clip)">
  <path d="M150,90 C120,170 120,280 165,350 L205,350 C165,280 165,170 192,90Z" fill="url(#{p}str)"/>
  <path d="M235,80 C205,160 205,290 250,350 L292,350 C250,290 250,160 278,80Z" fill="url(#{p}str)"/>
  <path d="M90,120 C70,190 70,270 105,330 L125,330 C95,270 95,190 118,120Z" fill="url(#{p}str)"/>
  <ellipse cx="235" cy="220" rx="135" ry="98" transform="rotate(-12 235 220)" fill="url(#{p}shade)"/>
 </g>
 <ellipse cx="225" cy="160" rx="70" ry="22" transform="rotate(-12 225 160)" fill="#FFFFFF" opacity=".45" filter="url(#{p}blur)"/>
 <ellipse cx="205" cy="158" rx="22" ry="7" transform="rotate(-14 205 158)" fill="#FFFFFF" opacity=".8" filter="url(#{p}soft)"/>
</g>
<g>{''.join(fuzz)}<circle cx="370" cy="190" r="62" fill="url(#{p}tho)"/>
 <ellipse cx="352" cy="165" rx="24" ry="12" fill="#FFFFFF" opacity=".22" filter="url(#{p}blur)"/></g>
<g fill="none" stroke="#1A1208" stroke-width="4.5" stroke-linecap="round">
 <path d="M462,162 C470,120 495,95 525,88"/><path d="M475,168 C495,135 525,122 555,125"/>
</g>
<circle cx="526" cy="88" r="6" fill="#1A1208"/><circle cx="556" cy="125" r="6" fill="#1A1208"/>
<g>{''.join(hfuzz)}<circle cx="455" cy="205" r="48" fill="url(#{p}head)"/>
 <ellipse cx="468" cy="193" rx="22" ry="30" fill="url(#{p}eye)"/>
 <ellipse cx="461" cy="181" rx="7" ry="9" fill="#FFFFFF" opacity=".85"/><circle cx="475" cy="205" r="3" fill="#FFFFFF" opacity=".6"/>
 <path d="M490,228 q10,8 4,18" stroke="#0B0703" stroke-width="4" fill="none" stroke-linecap="round"/></g>
<g class="bwingF"><g transform="translate(372,142) scale(-1,1) rotate(-22)"><path d="{wing_d}" fill="url(#{p}wing)" stroke="rgba(255,255,255,.8)" stroke-width="2.5"/>{veins}</g></g>
</svg>'''
