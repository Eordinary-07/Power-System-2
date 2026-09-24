#!/usr/bin/env python3
"""Build a static HTML site + combined PDF from the Power Systems-II notes."""

import os
import re
import sys
import markdown
from pathlib import Path
from xhtml2pdf import pisa

ROOT = Path(__file__).parent
NOTES = ROOT / "notes"
OUT = ROOT / "site"
OUT.mkdir(exist_ok=True)
(OUT / "figures").mkdir(exist_ok=True)

# File order + display metadata
CHAPTERS = [
    ("README.md",                          "Home",                "🏠"),
    ("00-outline.md",                      "Subject outline",     "🗺️"),
    ("01-intro-and-prerequisites.md",      "Prerequisites",       "📘"),
    ("02-unit-i-symmetrical-components.md","Unit I · Symmetrical components", "🔵"),
    ("03-unit-ii-fault-analysis.md",       "Unit II · Fault analysis",        "🔴"),
    ("04-unit-iii-stability.md",           "Unit III · Stability",            "🟡"),
    ("05-unit-iv-economic-operation.md",   "Unit IV · Economic operation",    "💰"),
    ("06-unit-v-control.md",               "Unit V · Control",                "🎛️"),
    ("07-quick-reference.md",              "Quick reference card",            "📇"),
    ("08-glossary-and-symbols.md",         "Glossary & symbols",              "📖"),
    ("09-exam-prep.md",                    "Exam prep",                       "🎯"),
    ("diagram_log.md",                     "Diagram log (ref)",               "🖼️"),
]

CSS = r"""
:root{
  --bg:#fdfcf7; --fg:#1d2430; --accent:#1d4ed8; --accent2:#b91c1c;
  --muted:#5b6473; --line:#d8d3c3; --card:#ffffff; --code-bg:#f4efe0;
  --warn-bg:#fff4e5; --warn-bd:#e2a339; --ok-bg:#e8f3ee; --ok-bd:#2f855a;
  --red:#b91c1c;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:var(--bg);color:var(--fg);
  font-family:Georgia,"Iowan Old Style","Times New Roman",serif;
  font-size:16.5px;line-height:1.65;}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
code,pre{font-family:"JetBrains Mono",SFMono-Regular,Consolas,Menlo,monospace;
  font-size:0.92em;background:var(--code-bg);border-radius:4px}
code{padding:1px 5px}
pre{padding:12px 14px;overflow:auto;border:1px solid var(--line);border-radius:6px;
  line-height:1.45}
img{max-width:100%;height:auto;display:block;margin:18px auto;
  border:1px solid var(--line);border-radius:4px;background:#fff;padding:6px}
h1,h2,h3,h4{font-family:Inter,"Segoe UI",system-ui,sans-serif;line-height:1.3;
  color:#0f172a;margin-top:1.8em;scroll-margin-top:20px}
h1{font-size:2em;border-bottom:2px solid var(--accent);padding-bottom:8px;margin-top:0}
h2{font-size:1.4em;border-bottom:1px solid var(--line);padding-bottom:4px}
h3{font-size:1.15em;color:#1e3a8a}
h4{font-size:1.05em;color:#334155}
hr{border:0;border-top:1px dashed var(--line);margin:28px 0}
table{border-collapse:collapse;margin:18px 0;width:100%;font-size:0.95em}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#eef1f7;font-family:Inter,sans-serif}
blockquote{border-left:4px solid var(--accent);margin:18px 0;padding:6px 16px;
  background:#eef3fb;border-radius:0 6px 6px 0;color:#1e293b}
blockquote blockquote{border-left-color:var(--warn-bd);background:var(--warn-bg)}
/* Layout */
.layout{display:grid;grid-template-columns:260px 1fr;min-height:100vh}
nav.sidebar{background:#0f1e3a;color:#e5e7eb;padding:18px 14px;position:sticky;top:0;
  height:100vh;overflow-y:auto;border-right:1px solid #1e293b}
nav.sidebar a{color:#cbd5e1;display:block;padding:6px 8px;border-radius:5px;
  font-family:Inter,sans-serif;font-size:0.9em}
nav.sidebar a.active,nav.sidebar a:hover{background:#1d4ed8;color:#fff;text-decoration:none}
nav.sidebar h3{color:#fff;font-family:Inter,sans-serif;margin:12px 6px 6px;font-size:0.75em;
  text-transform:uppercase;letter-spacing:1px;opacity:0.6;border:0}
nav .brand{font-family:Inter,sans-serif;font-weight:700;color:#fff;font-size:1.1em;
  padding:10px 8px 14px;border-bottom:1px solid #1e3a8a;margin-bottom:8px}
main{padding:30px 48px 80px;max-width:920px}
.download-bar{background:#fff8e1;border:1px solid var(--warn-bd);border-radius:8px;
  padding:12px 18px;margin-bottom:24px;display:flex;justify-content:space-between;
  align-items:center;flex-wrap:wrap;gap:12px}
.download-bar strong{color:#92400e}
.btn{display:inline-block;padding:8px 16px;border-radius:6px;background:var(--accent);
  color:#fff;font-family:Inter,sans-serif;font-size:0.9em;font-weight:600;border:0;cursor:pointer}
.btn:hover{background:#1e40af;text-decoration:none;color:#fff}
.btn.green{background:#15803d}
.btn.green:hover{background:#166534}
/* Signposts */
.checkpoint{background:var(--ok-bg);border-left:4px solid var(--ok-bd);padding:8px 14px;
  margin:14px 0;border-radius:0 6px 6px 0}
.misconception{background:var(--warn-bg);border-left:4px solid var(--warn-bd);padding:8px 14px;
  margin:14px 0;border-radius:0 6px 6px 0}
.why{background:#eef3fb;border-left:4px solid var(--accent);padding:8px 14px;margin:14px 0;
  border-radius:0 6px 6px 0;font-style:italic}
.pace{font-family:Inter,sans-serif;font-size:0.8em;padding:2px 8px;border-radius:10px;
  background:#e5e7eb;color:#374151;margin-left:6px;vertical-align:middle}
.note{font-size:0.95em;color:var(--muted)}
sub,sup{line-height:0}
@media(max-width:820px){
  .layout{grid-template-columns:1fr}
  nav.sidebar{position:static;height:auto}
  main{padding:20px}
}
/* Print / PDF */
@page{size:A4;margin:18mm 16mm;@bottom-center{content:"Power Systems-II · page " counter(page) " of " counter(pages);
  font-family:Inter,sans-serif;font-size:9pt;color:#888}}
@media print{
  nav.sidebar{display:none}
  .layout{display:block}
  main{padding:0;max-width:none}
  .download-bar{display:none}
  a{color:inherit;text-decoration:none}
  img{max-height:20cm;page-break-inside:avoid}
  h2,h3{page-break-after:avoid}
  pre,table,blockquote{page-break-inside:avoid}
}
"""

def md_to_html(md_text: str, source_path: str) -> str:
    """Convert markdown to HTML with small special-case formatting."""
    # Pre-process: convert --- divider lines (sparingly — only between major sections, not every HR)
    # Convert ❓ checkpoints and ⚠️ misconception paragraphs that start with those markers.
    # We'll use a simple extension: fenced code blocks via fenced_code, tables, etc.
    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "sane_lists", "toc", "attr_list"],
        output_format="html5",
    )
    body = md.convert(md_text)

    # Wrap checkpoint / misconception / why callouts
    # Pattern: a <p> starting with ❓ becomes a checkpoint. We do this naively.
    body = re.sub(
        r"<p>\*\*❓ Understanding checkpoint:\*\*(.*?)</p>",
        r'<div class="checkpoint"><strong>❓ Understanding checkpoint:</strong>\1</div>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<p>\*\*❓(.*?)</p>",
        r'<div class="checkpoint"><strong>❓ \1</strong></div>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<p>([ \t]*)- \*Answer:(.*?)</p>",
        r'<p class="answer"> — <em>\2</em></p>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<p>([ \t]*)\*Answer:(.*?)</p>",
        r'<p class="answer"><em>\2</em></p>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<blockquote>\s*<p>⚠️(.*?)</p>\s*</blockquote>",
        r'<div class="misconception">⚠️\1</div>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<p>⚠️(.*?)</p>",
        r'<div class="misconception">⚠️\1</div>',
        body, flags=re.DOTALL,
    )
    body = re.sub(
        r"<blockquote>\s*<p>🟡 \*Why[^*]*\*(.*?)</p>\s*</blockquote>",
        r'<div class="why"><strong>Why:</strong>\1</div>',
        body, flags=re.DOTALL,
    )
    return body


def build_page(filename: str, html_body: str, idx: int, is_home: bool = False) -> str:
    nav = ['<div class="brand">⚡ Power Systems-II<br><span style="font-size:0.7em;opacity:0.7">Complete notes (Kothari &amp; Nagrath)</span></div>',
           '<h3>Contents</h3>']
    for i, (fn, title, icon) in enumerate(CHAPTERS):
        cls = "active" if fn == filename else ""
        nav.append(f'<a class="{cls}" href="{page_name(fn)}">{icon} {title}</a>')
    nav_html = "\n".join(nav)

    dl_bar = ""
    if not is_home:
        dl_bar = """
        <div class="download-bar">
          <div><strong>Download:</strong> The full notes as a single PDF (print-ready, A4, with all diagrams).</div>
          <a class="btn green" href="Power-Systems-II-notes.pdf">⬇  Download PDF</a>
        </div>
        """

    title = next(t for (f, t, _) in CHAPTERS if f == filename)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — Power Systems-II Notes</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="layout">
  <nav class="sidebar">{nav_html}</nav>
  <main>
    {dl_bar}
    {html_body}
  </main>
</div>
</body>
</html>
"""


def page_name(filename: str) -> str:
    if filename == "README.md":
        return "index.html"
    return filename.replace(".md", ".html")


def build_pdf(pdf_html: str, out_path: Path, font_dir_uri: str):
    """Render PDF using xhtml2pdf (pure Python/reportlab, no system libs)."""
    # Use plain format() rather than f-string to avoid needing braces doubled everywhere
    print_css = """
    @page { size: A4; margin: 2.0cm 1.8cm 2.2cm 1.8cm; }
    @font-face { font-family: "Body"; src: url("__FD__DejaVuSans.ttf"); }
    @font-face { font-family: "Body"; font-weight: bold; src: url("__FD__DejaVuSans-Bold.ttf"); }
    @font-face { font-family: "Mono"; src: url("__FD__DejaVuSansMono.ttf"); }
    @font-face { font-family: "Mono"; font-weight: bold; src: url("__FD__DejaVuSansMono-Bold.ttf"); }
    html, body { font-family: "Body", sans-serif; font-size: 10.5pt; color: #1a1a1a; line-height: 1.45; }
    h1 { font-size: 20pt; color: #0f1e3a; border-bottom: 2px solid #1d4ed8; padding-bottom: 4pt; margin-top: 0; }
    h2 { font-size: 14pt; color: #1e3a8a; border-bottom: 1px solid #c5c5c5; padding-bottom: 2pt; margin-top: 18pt; page-break-after: avoid; }
    h3 { font-size: 12pt; color: #334155; margin-top: 14pt; page-break-after: avoid; }
    h4 { font-size: 11pt; color: #475569; margin-top: 10pt; }
    p { margin: 6pt 0; text-align: justify; }
    pre, code { font-family: "Mono", monospace; font-size: 9pt; }
    pre { background: #f4efe0; border: 1px solid #c5c5c5; padding: 8pt; overflow: hidden; white-space: pre-wrap; page-break-inside: avoid; }
    code { background: #f4efe0; padding: 1pt 3pt; }
    img { max-width: 100%; display: block; margin: 10pt auto; page-break-inside: avoid; }
    blockquote { border-left: 3pt solid #1d4ed8; background: #eef3fb; padding: 6pt 10pt; margin: 8pt 0; font-size: 10pt; page-break-inside: avoid; }
    table { border-collapse: collapse; width: 100%; margin: 10pt 0; font-size: 9.5pt; page-break-inside: avoid; }
    th, td { border: 1px solid #999; padding: 5pt 7pt; text-align: left; vertical-align: top; }
    th { background: #eef1f7; }
    hr { border: 0; border-top: 1px dashed #aaa; margin: 12pt 0; }
    ul, ol { margin: 6pt 0 6pt 22pt; padding: 0; }
    li { margin: 2pt 0; }
    a { color: #1d4ed8; text-decoration: none; }
    .cover { text-align: center; padding-top: 60pt; page-break-after: always; }
    .cover h1 { font-size: 30pt; color: #0f1e3a; border: 0; margin-bottom: 10pt; }
    .cover p { color: #555; font-size: 12pt; margin: 6pt 0; text-align: center; }
    .checkpoint { background: #e8f3ee; border-left: 3pt solid #2f855a; padding: 6pt 10pt; margin: 8pt 0; font-size: 10pt; page-break-inside: avoid; }
    .misconception { background: #fff4e5; border-left: 3pt solid #e2a339; padding: 6pt 10pt; margin: 8pt 0; font-size: 10pt; page-break-inside: avoid; }
    .why { background: #eef3fb; border-left: 3pt solid #1d4ed8; padding: 6pt 10pt; margin: 8pt 0; font-size: 10pt; font-style: italic; page-break-inside: avoid; }
    .answer { color: #2f5c2f; margin-left: 12pt; font-size: 10pt; }
    sub, sup { font-size: 0.7em; }
    """.replace("__FD__", font_dir_uri)
    # Inject print CSS in <head>
    if "<head>" in pdf_html:
        pdf_html = pdf_html.replace("<head>", f"<head><style>{print_css}</style>")
    else:
        pdf_html = f"<html><head><style>{print_css}</style></head><body>" + pdf_html + "</body></html>"

    with open(out_path, "wb") as f:
        result = pisa.CreatePDF(pdf_html, dest=f, path=str(OUT))
    if result.err:
        print(f"  xhtml2pdf reported errors: {result.err}")
    else:
        size = out_path.stat().st_size / (1024*1024)
        print(f"  PDF written: {out_path.name} ({size:.1f} MB)")


def build_site():
    # Copy figures
    import shutil
    for fig in (NOTES / "figures").glob("*.png"):
        shutil.copy(fig, OUT / "figures" / fig.name)

    # Write CSS
    (OUT / "style.css").write_text(CSS, encoding="utf-8")

    all_html_for_pdf = []
    pages = {}

    for idx, (fname, title, icon) in enumerate(CHAPTERS):
        md_text = (NOTES / fname).read_text(encoding="utf-8")
        # Fix image paths (notes/figures/x.png → figures/x.png in the built site)
        md_text = md_text.replace("](figures/", "](figures/")
        body = md_to_html(md_text, fname)
        # Wrap with a title h1 if the file doesn't start with # (README etc do)
        if not md_text.lstrip().startswith("#"):
            body = f"<h1>{title}</h1>\n" + body
        is_home = fname == "README.md"
        html = build_page(fname, body, idx, is_home=is_home)
        out_name = page_name(fname)
        (OUT / out_name).write_text(html, encoding="utf-8")
        pages[fname] = body
        # For PDF: concatenate body content with a page break between chapters
        if idx > 0:
            all_html_for_pdf.append('<div style="page-break-before:always"></div>')
        all_html_for_pdf.append(f'<h1 class="pdf-chapter">{icon} {title}</h1>')
        all_html_for_pdf.append(body)
        print(f"  built {out_name}")

    # Build combined PDF with xhtml2pdf (pure-Python)
    # Copy fonts locally so xhtml2pdf can read them (its resource policy limits to cwd)
    fonts_dir = OUT / "_fonts"
    fonts_dir.mkdir(exist_ok=True)
    import shutil
    for f in ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSansMono.ttf", "DejaVuSansMono-Bold.ttf"]:
        src = Path("/usr/share/fonts/truetype/dejavu") / f
        if src.exists():
            shutil.copy(src, fonts_dir / f)
    # Rewrite image paths to absolute file:// URLs so xhtml2pdf can find them
    fig_dir_uri = OUT.as_uri() + "/figures/"
    font_dir_uri = fonts_dir.as_uri() + "/"
    pdf_html_for_render = ''.join(all_html_for_pdf)
    pdf_html_for_render = pdf_html_for_render.replace('src="figures/', f'src="{fig_dir_uri}')
    # Strip emoji / rare glyphs that DejaVu may not cover
    emoji_map = {
        '\u26a1':'*',        # ⚡
        '\U0001f3e0':'',      # 🏠
        '\U0001f5fa\ufe0f':'',# 🗺️
        '\U0001f4d8':'',      # 📘
        '\U0001f535':'',      # 🔵
        '\U0001f534':'',      # 🔴
        '\U0001f7e1':'',      # 🟡
        '\U0001f4b0':'',      # 💰
        '\U0001f39b\ufe0f':'',# 🎛️
        '\U0001f4c7':'',      # 📇
        '\U0001f4d6':'',      # 📖
        '\U0001f3af':'',      # 🎯
        '\U0001f5bc\ufe0f':'',# 🖼️
        '\u2705':'[OK]',      # ✅
        '\u2753':'Q.',        # ❓
        '\u26a0\ufe0f':'Note:', # ⚠️
        '\u2b07\ufe0f':'',    # ⬇
        '\U0001f7e2':'',      # 🟢
        '\u27f9':'=>',        # ⟹
    }
    for k,v in emoji_map.items():
        pdf_html_for_render = pdf_html_for_render.replace(k, v)
    # Strip all remaining non-bmp characters (>U+FFFF) and rare symbols to boxes
    pdf_html_for_render = ''.join(c for c in pdf_html_for_render if ord(c) < 0x10000)
    # Also add chapter-break class to h1.pdf-chapter
    pdf_html_for_render = pdf_html_for_render.replace('<h1 class="pdf-chapter">',
        '<div class="chapter-page"></div><h1>')
    # Add cover page
    cover = f"""
    <div class="cover">
      <h1>&#9889; Power Systems-II</h1>
      <p><b>Complete first-time notes for a zero-background reader</b></p>
      <p>Primary text: Kothari &amp; Nagrath, <i>Modern Power System Analysis</i>, 3rd ed.<br>
      Supporting: Bergen &amp; Vittal; Saadat (cross-checks only)</p>
      <p>B.Tech. Electrical Engineering · Semester V<br>
      Rashtrasant Tukadoji Maharaj Nagpur University (BEL5T15)</p>
      <p style="margin-top:30pt;color:#888;font-size:10pt">
      {len(CHAPTERS)-1} chapters · 6 narrated worked examples · 25 practice problems ·
      40 diagrams from K&amp;N · ~2,450 lines of notes</p>
    </div>
    """
    pdf_html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Power Systems-II Notes</title></head><body>
{cover}
{pdf_html_for_render}
</body></html>"""
    (OUT / "all.html").write_text(pdf_html, encoding="utf-8")
    print("Rendering PDF...")
    build_pdf(pdf_html, OUT / "Power-Systems-II-notes.pdf", font_dir_uri)


if __name__ == "__main__":
    build_site()
    print("\nSite built in:", OUT)
