#!/usr/bin/env python3
"""Bundle index.html with its CSS, JS, and favicon into single files.

Writes dist/index.html (a full document) and dist/artifact.html (the same
page as a fragment: title, font link, styles, body content, and script).
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
html = (ROOT / "index.html").read_text(encoding="utf-8")

def inline_css(match: re.Match) -> str:
    path = ROOT / match.group(1)
    return "<style>\n" + path.read_text(encoding="utf-8") + "\n</style>"

def inline_js(match: re.Match) -> str:
    path = ROOT / match.group(1)
    return "<script>\n" + path.read_text(encoding="utf-8") + "\n</script>"

def inline_icon(match: re.Match) -> str:
    path = ROOT / match.group(1)
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<link rel="icon" href="data:image/svg+xml;base64,{data}" type="image/svg+xml">'

html = re.sub(r'<link rel="stylesheet" href="((?:brand|assets)/[^"]+\.css)">', inline_css, html)
html = re.sub(r'<script src="(assets/[^"]+\.js)"></script>', inline_js, html)
html = re.sub(r'<link rel="icon" href="(assets/[^"]+\.svg)" type="image/svg\+xml">', inline_icon, html)

dist = ROOT / "dist"
dist.mkdir(exist_ok=True)
(dist / "index.html").write_text(html, encoding="utf-8")

# Fragment for artifact hosts: <title> + font link + styles, then body inner, then script.
head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
title = re.search(r"<title>.*?</title>", head, re.S).group(0)
font_link = re.search(r'<link href="https://fonts\.googleapis\.com[^>]*>', head).group(0)
styles = "\n".join(m.group(0) for m in re.finditer(r"<style>.*?</style>", head, re.S))
fragment = f"{title}\n{font_link}\n{styles}\n{body}\n"
(dist / "artifact.html").write_text(fragment, encoding="utf-8")

print(f"dist/index.html    {len(html):>7} bytes")
print(f"dist/artifact.html {len(fragment):>7} bytes")
