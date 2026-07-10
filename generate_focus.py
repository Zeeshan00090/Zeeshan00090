import base64
import urllib.request
import os

os.makedirs('/Users/zeeshanrahman/Zeeshan00090/assets', exist_ok=True)

# Fetch skill icons SVG
try:
    url = "https://skillicons.dev/icons?i=python,pytorch,tensorflow,c,cpp,git,docker,linux,aws,gcp&theme=dark&perline=5"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
        b64_icons = base64.b64encode(img_data).decode('utf-8')
    icons_href = f"data:image/svg+xml;base64,{b64_icons}"
except Exception as e:
    icons_href = ""

svg_content = f"""<svg width="850" height="320" viewBox="0 0 850 320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>

    <!-- Glassmorphism -->
    <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0.08)" />
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0.02)" />
    </linearGradient>

    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="10" dy="15" stdDeviation="15" flood-color="#000" flood-opacity="0.8"/>
    </filter>

    <!-- Glowing animated border -->
    <linearGradient id="glow-border" x1="0%" y1="0%" x2="200%" y2="200%">
      <stop offset="0%" stop-color="#00FF9C" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#00FF9C" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#00FF9C" stop-opacity="0.8" />
      <animate attributeName="x1" values="0%;200%;0%" dur="10s" repeatCount="indefinite" />
      <animate attributeName="y1" values="0%;200%;0%" dur="10s" repeatCount="indefinite" />
    </linearGradient>
    
    <filter id="text-glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <rect width="100%" height="100%" fill="url(#bg)" rx="20" />

  <!-- Left Panel: Focus -->
  <rect x="20" y="20" width="400" height="280" rx="20" fill="url(#glass)" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" filter="url(#shadow)" />
  
  <text x="50" y="65" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#00FF9C" filter="url(#text-glow)">🚀 Current Focus</text>
  
  <circle cx="45" cy="115" r="4" fill="#00FF9C">
    <animate attributeName="r" values="4;6;4" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="65" y="120" font-family="Arial, sans-serif" font-size="16" fill="#ffffff" font-weight="bold">Building Manas</text>
  <text x="65" y="145" font-family="Arial, sans-serif" font-size="14" fill="#cbd5e1">Continuous-time cognitive AGI engine.</text>

  <circle cx="45" cy="180" r="4" fill="#00FF9C">
    <animate attributeName="r" values="4;6;4" dur="2.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.4;1" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <text x="65" y="185" font-family="Arial, sans-serif" font-size="16" fill="#ffffff" font-weight="bold">Semantic State Evolution</text>
  <text x="65" y="210" font-family="Arial, sans-serif" font-size="14" fill="#cbd5e1">Replacing Next-Token Prediction.</text>

  <circle cx="45" cy="245" r="4" fill="#00FF9C">
    <animate attributeName="r" values="4;6;4" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.4;1" dur="3s" repeatCount="indefinite"/>
  </circle>
  <text x="65" y="250" font-family="Arial, sans-serif" font-size="16" fill="#ffffff" font-weight="bold">ZULIC Mathematics</text>
  <text x="65" y="275" font-family="Arial, sans-serif" font-size="14" fill="#cbd5e1">Non-linear reasoning dynamics for AI.</text>

  <!-- Right Panel: Tech Stack -->
  <rect x="430" y="20" width="400" height="280" rx="20" fill="url(#glass)" stroke="url(#glow-border)" stroke-width="2" filter="url(#shadow)" />
  
  <text x="560" y="65" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#00FF9C" filter="url(#text-glow)">🛠️ Tech Stack</text>

  <!-- Floating animated icon group -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="0,0; 0,-8; 0,0" dur="4s" repeatCount="indefinite" />
    <image href="{icons_href}" x="475" y="90" width="310" height="155" preserveAspectRatio="xMidYMid meet" />
  </g>

</svg>
"""

with open('/Users/zeeshanrahman/Zeeshan00090/assets/focus_stack.svg', 'w') as f:
    f.write(svg_content)
