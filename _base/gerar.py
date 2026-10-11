"""Gera um carrossel no estilo "print de tweet" do @marquinhosmilhas.

Uso: python -I gerar.py roteiro.json
roteiro.json = {"nome": "2026-10-13-cinco-erros", "slides": [{"html": "<p class=\"big\">...</p>", "swipe": true}, ...]}
Classes: big (título), hl (marca-texto), box/row/k/v (tabela), formula/eq (conta), cta (palavra-chave).
As imagens saem em ../carrosseis/<nome>/01.png, 02.png ... (1080x1350).
"""
import io, json, os, subprocess, sys, pathlib

BASE = pathlib.Path(__file__).resolve().parent
AVATAR = (BASE / "avatar.png").as_uri()
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=block');
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden;background:#fff}
body{font-family:'Inter','Segoe UI','Segoe UI Emoji',system-ui,sans-serif;color:#0F1419;-webkit-font-smoothing:antialiased}
.s{width:1080px;height:1350px;padding:96px 92px 84px;display:flex;flex-direction:column}
.head{display:flex;align-items:center;gap:28px}
.head img{width:128px;height:128px;border-radius:50%;object-fit:cover}
.name{font-size:46px;font-weight:800;letter-spacing:-.01em}
.handle{font-size:36px;color:#536471;font-weight:500;margin-top:4px}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px;font-size:54px;line-height:1.36;letter-spacing:-.005em}
.body p{font-weight:500}
.body b{font-weight:800}
.body .big{font-size:66px;line-height:1.22;font-weight:800;letter-spacing:-.015em}
.hl{background:linear-gradient(transparent 58%, #FFD9C2 58%);padding:0 4px}
.box{background:#F7F9F9;border:2px solid #E6ECF0;border-radius:32px;padding:40px 46px;font-size:50px;line-height:1.4}
.box .row{display:flex;justify-content:space-between;gap:24px}
.box .row + .row{margin-top:14px}
.box .k{color:#536471;font-weight:500}
.box .v{font-weight:800}
.formula{background:#0F1419;color:#fff;border-radius:32px;padding:44px 50px;font-size:54px;line-height:1.4;font-weight:700}
.formula .eq{color:#FFB37A}
.body .cta{font-size:96px;font-weight:800;letter-spacing:-.02em}
.foot{display:flex;gap:16px;align-items:center}
.pill{font-size:30px;font-weight:700;border-radius:999px;padding:12px 26px}
.pill.g{color:#fff;background:linear-gradient(90deg,#833AB4,#E1306C 55%,#F77737)}
.pill.d{color:#fff;background:#26313D}
.body .swipe{font-size:40px;font-weight:700;color:#536471}
"""

def slide(body, swipe=False):
    sw = '<p class="swipe">arrasta pro lado ➡️</p>' if swipe else ''
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">
<div class="head"><img src="{AVATAR}"><div><div class="name">Marquinhos Milhas</div><div class="handle">@marquinhosmilhas</div></div></div>
<div class="body">{body}{sw}</div>
<div class="foot"><span class="pill g">Marquinhos Milhas</span><span class="pill d">@marquinhosmilhas</span></div>
</div></body></html>"""


spec = json.load(io.open(sys.argv[1], encoding="utf-8"))
out = BASE.parent / "carrosseis" / spec["nome"]
tmp = BASE / "_html" / spec["nome"]
out.mkdir(parents=True, exist_ok=True); tmp.mkdir(parents=True, exist_ok=True)
for f in out.glob("*.png"): f.unlink()
for i, s in enumerate(spec["slides"], 1):
    hp = tmp / f"{i:02d}.html"
    hp.write_text(slide(s["html"], s.get("swipe", False)), encoding="utf-8")
    png = out / f"{i:02d}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=8000", f"--screenshot={png}", hp.as_uri()], check=True, capture_output=True)
    print(png)
