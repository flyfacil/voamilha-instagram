"""Gera um Reel vertical (1080x1920) com o texto surgindo frase por frase, no estilo "print de tweet".

Uso: python -I video.py roteiro-video.json
roteiro = {"nome": "asia-china", "telas": [["frase 1", "frase 2", ...], ["frase da tela 2", ...]]}
Cada tela começa limpa e as frases vão aparecendo uma a uma (ficam as anteriores).
Frase que começa com "# " vira título (negrito, maior). "**x**" vira negrito.
Saída: ../videos/<nome>.mp4 (30 fps, H.264, com faixa de áudio muda para colocar a música no app).
"""
import io, json, os, re, subprocess, sys, pathlib, html as H

BASE = pathlib.Path(__file__).resolve().parent
AVATAR = (BASE / "avatar.png").as_uri()
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FFMPEG = next(pathlib.Path(os.environ["LOCALAPPDATA"], "Microsoft", "WinGet", "Packages").glob("Gyan.FFmpeg*/*/bin/ffmpeg.exe"))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&display=block');
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#fff}
body{font-family:'Inter','Segoe UI','Segoe UI Emoji',system-ui,sans-serif;color:#0F1419;-webkit-font-smoothing:antialiased}
.s{width:1080px;height:1920px;padding:150px 92px 230px;display:flex;flex-direction:column}
.head{display:flex;align-items:center;gap:28px}
.head img{width:132px;height:132px;border-radius:50%}
.name{font-size:48px;font-weight:800}
.handle{font-size:38px;color:#536471;font-weight:500;margin-top:4px}
.body{flex:1;display:flex;flex-direction:column;justify-content:center;gap:46px}
.l{font-size:70px;line-height:1.3;font-weight:500;letter-spacing:-.005em}
.l.t{font-size:92px;line-height:1.12;font-weight:800;letter-spacing:-.02em}
.l b{font-weight:800}
.hl{background:linear-gradient(transparent 62%, #FFD9C2 62%);-webkit-box-decoration-break:clone;box-decoration-break:clone}
"""

def fmt(line):
    t = line[2:] if line.startswith("# ") else line
    t = H.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return ("l t" if line.startswith("# ") else "l"), t

def page(lines):
    ps = []
    for i, ln in enumerate(lines):
        cls, t = fmt(ln)
        if i == len(lines) - 1 and len(lines) > 1 and "t" not in cls.split(): t = f'<span class="hl">{t}</span>'
        ps.append(f'<p class="{cls}">{t}</p>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">
<div class="head"><img src="{AVATAR}"><div><div class="name">Marquinhos Milhas</div><div class="handle">@marquinhosmilhas</div></div></div>
<div class="body">{''.join(ps)}</div></div></body></html>"""

def dur(line):
    words = len(re.sub(r"[#*]", "", line).split())
    return max(1.3, min(3.2, 0.7 + words * 0.22))

spec = json.load(io.open(sys.argv[1], encoding="utf-8"))
tmp = BASE / "_html" / ("video-" + spec["nome"])
tmp.mkdir(parents=True, exist_ok=True)
for f in tmp.glob("*.png"): f.unlink()
frames = []
n = 0
for tela in spec["telas"]:
    for i in range(1, len(tela) + 1):
        n += 1
        hp = tmp / f"{n:03d}.html"
        hp.write_text(page(tela[:i]), encoding="utf-8")
        png = tmp / f"{n:03d}.png"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        "--window-size=1080,1920", "--virtual-time-budget=6000", f"--screenshot={png}", hp.as_uri()], check=True, capture_output=True)
        frames.append((png, dur(tela[i - 1])))
frames[-1] = (frames[-1][0], frames[-1][1] + 2.5)   # segura o CTA no fim

lst = tmp / "lista.txt"
with io.open(lst, "w", encoding="utf-8") as f:
    for png, d in frames:
        f.write(f"file '{png.as_posix()}'\nduration {d:.2f}\n")
    f.write(f"file '{frames[-1][0].as_posix()}'\n")
out = BASE.parent / "videos" / f"{spec['nome']}.mp4"
out.parent.mkdir(exist_ok=True)
total = sum(d for _, d in frames)
subprocess.run([str(FFMPEG), "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-c:a", "aac", "-shortest", "-t", f"{total:.2f}", "-movflags", "+faststart", str(out)], check=True)
print(out, f"{total:.1f}s", f"{len(frames)} quadros")
