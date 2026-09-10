#!/usr/bin/env python3
"""Render a Markdown document as a blipbox-styled page fragment.

Usage: python3 scripts/md-to-page.py IN.md OUT.html [masthead label]
The output has no <html>/<head>/<body> shell: a <title>, the font link, a
<style>, and the content. Hosts that need a full document can wrap it.
"""
import pathlib
import re
import sys

import markdown

src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
label = sys.argv[3] if len(sys.argv) > 3 else ""
text = src.read_text(encoding="utf-8")

title_match = re.match(r"#\s+(.+)", text)
doc_title = title_match.group(1).strip() if title_match else src.stem
body_md = text[title_match.end():] if title_match else text

html = markdown.markdown(body_md, extensions=["tables", "sane_lists", "smarty"])

# Wrap tables so wide ones scroll inside their own container.
html = html.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")

# The first section after the title is the summary: put it in a box.
parts = re.split(r"(?=<h2>)", html, maxsplit=2)
if len(parts) == 3:
    html = parts[0] + '<section class="box">' + parts[1] + "</section>" + parts[2]

STYLE = """
:root {
  color-scheme: light;
  --paper: #FCFBF9; --paper-2: #F3F1EC; --ink: #0D0D0B; --ink-2: #4A4744; --ink-3: #706A64;
  --line: rgba(13,13,11,.14); --red: #EF2720; --yellow: #FFCB25; --on-ink: #FCFBF9;
  --stroke: 3px; --radius: 12px; --radius-lg: 20px;
  --font-sans: "Archivo", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-mono: "Azeret Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --paper: #131211; --paper-2: #1D1B19; --ink: #F4F2EE; --ink-2: #BBB5AE; --ink-3: #8F8982;
    --line: rgba(244,242,238,.16); --red: #F5342C; --on-ink: #131211;
  }
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --paper: #131211; --paper-2: #1D1B19; --ink: #F4F2EE; --ink-2: #BBB5AE; --ink-3: #8F8982;
  --line: rgba(244,242,238,.16); --red: #F5342C; --on-ink: #131211;
}
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--font-sans); font-size: 1.0625rem; line-height: 1.6; -webkit-font-smoothing: antialiased; }
::selection { background: var(--yellow); color: #0D0D0B; }
:focus-visible { outline: var(--stroke) solid var(--yellow); outline-offset: 3px; }
.page { max-width: 76ch; margin-inline: auto; padding: 40px clamp(20px, 4vw, 48px) 96px; }
.masthead { display: flex; align-items: center; gap: 12px; font-weight: 800; font-stretch: 112%; font-size: 1.25rem; letter-spacing: -.02em; margin-bottom: 40px; }
.masthead svg { width: 34px; height: 34px; display: block; }
.masthead span { color: var(--ink-3); font-weight: 600; font-stretch: 90%; font-size: .9375rem; letter-spacing: 0; margin-left: 4px; }
h1 { font-size: clamp(2.2rem, 1.4rem + 3vw, 3.4rem); line-height: 1; letter-spacing: -.03em; font-weight: 800; font-stretch: 112%; margin: 0 0 16px; text-wrap: balance; }
h1 + p em { color: var(--ink-2); font-style: normal; }
h2 { font-size: 1.75rem; line-height: 1.1; letter-spacing: -.025em; font-weight: 800; font-stretch: 112%; margin: 64px 0 20px; padding-top: 28px; border-top: var(--stroke) solid var(--ink); text-wrap: balance; }
h3 { font-size: 1.2rem; font-weight: 700; margin: 32px 0 8px; }
p { margin: 0 0 18px; text-wrap: pretty; }
strong { font-weight: 700; }
a { color: inherit; text-decoration-color: var(--line); text-underline-offset: .18em; }
a:hover { text-decoration-color: var(--yellow); text-decoration-thickness: 2px; }
code { font-family: var(--font-mono); font-size: .86em; background: var(--paper-2); padding: 2px 6px; border-radius: 6px; }
ul, ol { padding-left: 0; margin: 0 0 20px; }
ul { list-style: none; }
ul li { position: relative; padding-left: 24px; margin-bottom: 10px; }
ul li::before { content: ""; position: absolute; left: 0; top: .6em; width: 10px; height: 10px; border-radius: 2px; background: var(--yellow); }
ol { list-style: none; counter-reset: n; }
ol li { position: relative; padding-left: 52px; margin-bottom: 14px; counter-increment: n; }
ol li::before { content: counter(n); position: absolute; left: 0; top: .05em; width: 36px; height: 36px; display: grid; place-items: center; border: var(--stroke) solid var(--ink); border-radius: 10px; font-weight: 800; font-stretch: 112%; font-size: 1.05rem; line-height: 1; }
.box { border: var(--stroke) solid var(--ink); border-radius: var(--radius-lg); padding: 28px clamp(20px, 3vw, 36px) 12px; margin: 8px 0 24px; }
.box h2 { border-top: 0; padding-top: 0; margin-top: 0; font-size: 1.4rem; }
.box ol li::before { background: var(--red); border-color: var(--red); color: #FCFBF9; }
.table-wrap { overflow-x: auto; margin: 0 0 24px; }
table { border-collapse: collapse; width: 100%; font-size: .9375rem; line-height: 1.45; }
th, td { text-align: left; vertical-align: top; padding: 12px 14px 12px 0; border-bottom: 1px solid var(--line); }
th { font-weight: 600; font-stretch: 90%; color: var(--ink-3); border-bottom: var(--stroke) solid var(--ink); }
td:first-child { font-weight: 600; min-width: 11ch; }
h2 + ul, h2 + ol { margin-top: 20px; }
.sources { font-size: .9375rem; color: var(--ink-2); }
.sources ul li { margin-bottom: 8px; }
@media (max-width: 600px) { h2 { margin-top: 48px; } ol li { padding-left: 46px; } }
"""

MARK = """<svg viewBox="0 0 1024 1024" aria-hidden="true"><g stroke="#0D0D0B" stroke-width="34" stroke-linejoin="round"><polygon fill="#FFCB25" points="651,335 791,239 791,671 651,767"/><polygon fill="#FFCB25" points="225,335 651,335 791,239 365,239"/><rect fill="#EF2720" x="225" y="335" width="426" height="432" rx="18"/></g><g fill="#FFCB25" stroke="#FFCB25" stroke-width="14" stroke-linejoin="round"><path d="M380 441 H470 V549 H409 V613 H323 V502 H380 Z"/><rect x="497" y="611" width="46" height="56" rx="4"/></g></svg>"""

# Give the sources section a lighter treatment.
html = html.replace("<h2>Sources</h2>", '<h2 id="sources">Sources</h2><div class="sources">') + ("</div>" if "<h2>Sources</h2>" in html or 'id="sources"' in html else "")

page = f"""<title>{doc_title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@90..112,400..800&family=Azeret+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{STYLE}</style>
<main class="page">
  <div class="masthead">{MARK}blipbox{f"<span>{label}</span>" if label else ""}</div>
  <h1>{doc_title}</h1>
  {html}
</main>
"""
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page)} bytes)")
