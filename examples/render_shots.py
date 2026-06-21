#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 examples/slide-*.svg 渲染成 PNG 截图（用于 README 预览墙）。
依赖：playwright（pip install playwright && python3 -m playwright install chromium）。
浏览器渲染 → Inter/JetBrains 走 Google Fonts、CJK 走系统 PingFang，2x 高清。
运行：python3 examples/render_shots.py  → 写出 assets/shots/slide-*.png
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "assets" / "shots"
SHOTS.mkdir(parents=True, exist_ok=True)
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">')

svgs = sorted((ROOT / "examples").glob("slide-*.svg"))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 720}, device_scale_factor=2)
    for s in svgs:
        html = (f'<!doctype html><html><head><meta charset="utf-8">{FONTS}'
                '<style>html,body{margin:0;padding:0}svg{display:block}</style></head>'
                f'<body>{s.read_text(encoding="utf-8")}</body></html>')
        pg.set_content(html, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(450)
        out = SHOTS / (s.stem + ".png")
        pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1280, "height": 720})
        print("shot:", out.relative_to(ROOT))
    b.close()
print("done →", SHOTS.relative_to(ROOT))
