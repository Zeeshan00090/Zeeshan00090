import base64
import urllib.request
import os

os.makedirs('/Users/zeeshanrahman/Zeeshan00090/assets', exist_ok=True)

import urllib.request
import base64
import os

os.makedirs('/Users/zeeshanrahman/Zeeshan00090/assets', exist_ok=True)

try:
    url = "https://avatars.githubusercontent.com/Zeeshan00090?size=400"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        b64 = base64.b64encode(response.read()).decode('utf-8')
    img_href = f"data:image/png;base64,{b64}"
except Exception:
    img_href = ""

header_svg = f"""<svg width="850" height="280" viewBox="0 0 850 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>

    <!-- 3D Glassmorphism -->
    <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0.12)" />
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0.02)" />
    </linearGradient>

    <filter id="drop-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="15" dy="15" stdDeviation="15" flood-color="#000" flood-opacity="0.9"/>
    </filter>

    <filter id="glow">
      <feGaussianBlur stdDeviation="6" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="circleProfile">
      <circle cx="150" cy="140" r="85" />
    </clipPath>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" fill="url(#bg)" rx="20" />

  <!-- 3D Glass Card Container -->
  <rect x="25" y="25" width="800" height="230" rx="25" fill="url(#glass)" stroke="rgba(255, 255, 255, 0.2)" stroke-width="2" filter="url(#drop-shadow)" />

  <!-- Photo Glow Ring -->
  <circle cx="150" cy="140" r="88" fill="none" stroke="#00FF9C" stroke-width="4" filter="url(#glow)"/>
  
  <!-- Embedded Base64 Profile Picture -->
  <image href="{img_href}" x="65" y="55" height="170" width="170" clip-path="url(#circleProfile)" preserveAspectRatio="xMidYMid slice" />

  <!-- Text Content with 3D shadow -->
  <text x="270" y="95" font-family="Arial, sans-serif" font-size="48" font-weight="900" fill="#ffffff" filter="url(#drop-shadow)">Zeeshan Rahman</text>
  
  <text x="270" y="140" font-family="Arial, sans-serif" font-size="16" fill="#00FF9C" font-weight="700" letter-spacing="3">STUDENT | AGI RESEARCHER | AI ENGINEER</text>
  
  <text x="270" y="185" font-family="Arial, sans-serif" font-size="16" fill="#cbd5e1">Building the Future of Artificial General Intelligence.</text>
  <text x="270" y="215" font-family="Arial, sans-serif" font-size="16" fill="#cbd5e1">Pioneering Semantic State Evolution &amp; Continuous-Time Reasoning.</text>
</svg>
"""

with open('/Users/zeeshanrahman/Zeeshan00090/assets/header.svg', 'w') as f:
    f.write(header_svg)


vision_svg = f"""<svg width="850" height="250" viewBox="0 0 850 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>

    <linearGradient id="glass2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0.08)" />
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0.01)" />
    </linearGradient>

    <filter id="shadow2" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="15" dy="15" stdDeviation="15" flood-color="#000" flood-opacity="0.9"/>
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="url(#bg2)" rx="20" />

  <rect x="25" y="25" width="800" height="200" rx="25" fill="url(#glass2)" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.5" filter="url(#shadow2)" />

  <text x="60" y="75" font-family="Arial, sans-serif" font-size="30" font-weight="900" fill="#00FF9C">🧠 The AGI Vision</text>
  
  <text x="60" y="125" font-family="Arial, sans-serif" font-size="20" fill="#ffffff" font-weight="bold">Transformers predict. Manas thinks.</text>
  
  <text x="60" y="165" font-family="Arial, sans-serif" font-size="16" fill="#cbd5e1">Scaling Next-Token Prediction is a dead end for true intelligence.</text>
  <text x="60" y="195" font-family="Arial, sans-serif" font-size="16" fill="#cbd5e1">Engineering Cognitive Fluid Dynamics &amp; Continuous-Time Reasoning.</text>
</svg>
"""

with open('/Users/zeeshanrahman/Zeeshan00090/assets/vision.svg', 'w') as f:
    f.write(vision_svg)
