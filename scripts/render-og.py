#!/usr/bin/env python3
"""Render brand/social-card.html to assets/og.png at 1200x630 with headless Chrome."""
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "brand" / "social-card.html"
OUT = ROOT / "assets" / "og.png"

CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "chromium",
    "chromium-browser",
]
chrome = next((c for c in CANDIDATES if shutil.which(c) or pathlib.Path(c).exists()), None)
if not chrome:
    sys.exit("Chrome or Chromium not found; install one or pass the path in CANDIDATES.")

with tempfile.TemporaryDirectory() as profile:
    if OUT.exists():
        OUT.unlink()
    args = [
        chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--no-first-run", "--no-default-browser-check",
        f"--user-data-dir={profile}",
        "--force-device-scale-factor=1",
        "--run-all-compositor-stages-before-draw",
        "--window-size=1200,630",
        f"--screenshot={OUT}",
        SRC.as_uri(),
    ]
    # Headless Chrome does not always exit after writing the screenshot, so wait
    # a bounded time, then kill it and judge by the output file instead.
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        proc.wait(timeout=30)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

if not OUT.exists() or OUT.stat().st_size == 0:
    sys.exit("Chrome did not write the screenshot; check that brand/social-card.html opens in a browser.")
print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")
