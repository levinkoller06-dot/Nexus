def kurt_svg(w=420):
    return f'''<svg id="kurtsvg" viewBox="0 0 420 640" width="{w}" height="{w*640/420:.0f}" overflow="visible">
<defs>
 <radialGradient id="kSkin" cx="45%" cy="38%" r="65%"><stop offset="0" stop-color="#FFDDBE"/><stop offset=".7" stop-color="#F1BE93"/><stop offset="1" stop-color="#D9976C"/></radialGradient>
 <linearGradient id="kCoat" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2C4C7A"/><stop offset="1" stop-color="#14284A"/></linearGradient>
 <radialGradient id="kBeard" cx="45%" cy="30%" r="75%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".75" stop-color="#ECEBE6"/><stop offset="1" stop-color="#C9C6BD"/></radialGradient>
 <linearGradient id="kCap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCDAD3"/></linearGradient>
 <radialGradient id="kNose" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFB49A"/><stop offset="1" stop-color="#DE7F62"/></radialGradient>
</defs>
<g id="kBody">
 <ellipse cx="210" cy="628" rx="150" ry="14" fill="#000" opacity=".18"/>
 <rect x="140" y="560" width="50" height="62" rx="10" fill="#1A2236"/><rect x="230" y="560" width="50" height="62" rx="10" fill="#1A2236"/>
 <ellipse cx="160" cy="622" rx="42" ry="16" fill="#111"/><ellipse cx="262" cy="622" rx="42" ry="16" fill="#111"/>
 <path d="M95,600 C80,470 95,380 140,340 L280,340 C325,380 340,470 325,600 Z" fill="url(#kCoat)"/>
 <path d="M175,340 L210,420 L245,340 Z" fill="#F5F3EE"/>
 <path d="M210,345 L210,600" stroke="#0F1E38" stroke-width="3"/>
 <circle cx="185" cy="445" r="9" fill="#E8B54A"/><circle cx="185" cy="495" r="9" fill="#E8B54A"/><circle cx="185" cy="545" r="9" fill="#E8B54A"/>
 <circle cx="235" cy="445" r="9" fill="#E8B54A"/><circle cx="235" cy="495" r="9" fill="#E8B54A"/><circle cx="235" cy="545" r="9" fill="#E8B54A"/>
 <path d="M100,370 l40,-12 M320,370 l-40,-12" stroke="#E8B54A" stroke-width="10" stroke-linecap="round"/>
 <g id="kArmL"><path d="M128,360 C95,400 80,460 92,520" stroke="url(#kCoat)" stroke-width="44" fill="none" stroke-linecap="round"/><circle cx="94" cy="528" r="26" fill="url(#kSkin)"/></g>
 <g id="kArmR"><path d="M292,360 C325,400 340,460 328,520" stroke="url(#kCoat)" stroke-width="44" fill="none" stroke-linecap="round"/><circle cx="326" cy="528" r="26" fill="url(#kSkin)"/></g>
</g>
<g id="kHead">
 <ellipse cx="96" cy="215" rx="22" ry="30" fill="url(#kSkin)"/><ellipse cx="324" cy="215" rx="22" ry="30" fill="url(#kSkin)"/>
 <ellipse cx="210" cy="210" rx="120" ry="128" fill="url(#kSkin)"/>
 <ellipse cx="140" cy="240" rx="24" ry="14" fill="#F08C7A" opacity=".45"/><ellipse cx="280" cy="240" rx="24" ry="14" fill="#F08C7A" opacity=".45"/>
 <path d="M95,215 C90,300 130,370 210,378 C290,370 330,300 325,215 C300,250 280,262 255,262 C240,250 180,250 165,262 C140,262 120,250 95,215 Z" fill="url(#kBeard)"/>
 <g id="kMouth"><path d="M178,278 C185,300 235,300 242,278 Z" fill="#5B1D22"/><ellipse cx="210" cy="292" rx="16" ry="6" fill="#E26B6B"/></g>
 <path d="M150,262 C170,244 200,252 210,262 C220,252 250,244 270,262 C258,282 228,276 210,270 C192,276 162,282 150,262 Z" fill="#F7F6F2"/>
 <ellipse cx="210" cy="232" rx="26" ry="22" fill="url(#kNose)"/><ellipse cx="202" cy="224" rx="8" ry="5" fill="#fff" opacity=".55"/>
 <g id="kEyes">
  <ellipse cx="165" cy="190" rx="22" ry="25" fill="#fff"/><ellipse cx="255" cy="190" rx="22" ry="25" fill="#fff"/>
  <circle cx="170" cy="194" r="12" fill="#2A2F3A"/><circle cx="250" cy="194" r="12" fill="#2A2F3A"/>
  <circle cx="174" cy="189" r="4" fill="#fff"/><circle cx="254" cy="189" r="4" fill="#fff"/>
  <g id="kLids"><rect x="140" y="163" width="50" height="54" rx="22" fill="url(#kSkin)"/><rect x="230" y="163" width="50" height="54" rx="22" fill="url(#kSkin)"/></g>
 </g>
 <path d="M138,158 C150,142 180,140 192,152" stroke="#F4F2EC" stroke-width="12" fill="none" stroke-linecap="round"/>
 <path d="M228,152 C240,140 270,142 282,158" stroke="#F4F2EC" stroke-width="12" fill="none" stroke-linecap="round"/>
 <g id="kCapG">
  <path d="M92,118 C90,60 140,28 210,28 C280,28 330,60 328,118 Z" fill="url(#kCap)"/>
  <rect x="96" y="104" width="228" height="38" rx="12" fill="#1C3159"/>
  <path d="M100,138 C140,166 280,166 320,138 L322,150 C280,184 140,184 98,150 Z" fill="#101010"/>
  <circle cx="210" cy="114" r="20" fill="#E8B54A"/>
  <path d="M210,100 v26 M202,108 h16 M198,120 c4,8 20,8 24,0" stroke="#1C3159" stroke-width="3.5" fill="none" stroke-linecap="round"/>
 </g>
</g>
</svg>'''
