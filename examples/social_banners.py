#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统一社交 banner 生成器（Aham 四仓库，1280×640）。
模板锚定 aham-ui 原版（顶条 + logo + 名称96/定位40/细节26 + 色板 + slogan + 类型标）。
单一 #336EE8 平涂、无渐变。渲染 2x PNG + 同名 SVG 到桌面 banner统一/。依赖 playwright。
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

SANS = "'Inter','PingFang SC','Microsoft YaHei',system-ui,-apple-system,sans-serif"
INK1, INK2, INK3 = "#262626", "#6E6E6E", "#9B9B9B"
LINE, PANEL, ACC = "#E7E7E7", "#F3F3F3", "#336EE8"
W, H = 1280, 640

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def T(x, y, s, size, fill, w=None, anchor=None, ls=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wt = f' font-weight="{w}"' if w else ""
    lss = f' letter-spacing="{ls}"' if ls else ""
    return f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}"{wt}{a}{lss} fill="{fill}">{esc(s)}</text>'
def R(x, y, w, h, fill, rx=None):
    r = f' rx="{rx}"' if rx is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"/>'

# ── 四个 logo 字形（白，平涂蓝底；坐标在 translate(96,212) 的 168 盒内）──
def g_ui():
    return (R(48, 60, 74, 14, "#FFFFFF", 7) + R(48, 94, 52, 14, "#FFFFFF", 7))
def g_ppt():
    return (R(44, 98, 22, 36, "#FFFFFF", 4) + R(73, 74, 22, 60, "#FFFFFF", 4) + R(102, 46, 22, 88, "#FFFFFF", 4))
def g_voice():
    hs = [40, 68, 96, 120, 96, 68, 40]; bw, gap = 11, 10
    x0 = (168 - (len(hs) * bw + (len(hs) - 1) * gap)) / 2; cy = 84
    return "".join(R(x0 + i * (bw + gap), cy - h / 2, bw, h, "#FFFFFF", 6) for i, h in enumerate(hs))
def g_survey():
    doc = R(32, 34, 74, 96, "#FFFFFF", 9)
    lines = "".join(R(46, 56 + i * 18, 46, 6, ACC, 3) for i in range(3))
    mag = (f'<circle cx="108" cy="108" r="24" fill="none" stroke="#FFFFFF" stroke-width="10"/>'
           f'<line x1="125" y1="125" x2="141" y2="141" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round"/>')
    return doc + lines + mag

def banner(name, tagline, detail, type_label, glyph):
    e = [R(0, 0, W, H, "#FFFFFF")]
    e.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" fill="none" stroke="{LINE}" stroke-width="2"/>')
    e.append(R(0, 0, W, 6, ACC))
    # logo
    e.append(f'<g transform="translate(96,212)"><rect width="168" height="168" rx="42" fill="{ACC}"/>{glyph}</g>')
    # 文案
    e.append(T(312, 268, name, 96, INK1, w=700, ls=-1))
    e.append(T(316, 332, tagline, 40, INK2, w=500))
    e.append(T(316, 382, detail, 26, INK3))
    # 色板：蓝 + 三层灰 + 墨
    sw = [ACC, "#FFFFFF", PANEL, LINE, INK1]
    g = ['<g transform="translate(96,456)">']
    for i, c in enumerate(sw):
        x = i * 50
        g.append(R(x, 0, 38, 38, c, 8))
        if c == "#FFFFFF":
            g.append(f'<rect x="{x}" y="0" width="38" height="38" rx="8" fill="none" stroke="{LINE}" stroke-width="1.5"/>')
    g.append('</g>'); e.append("".join(g))
    # slogan + 类型标
    e.append(T(98, 560, "把灵光一现，做成能用的 AI 工具。", 26, INK2))
    e.append(T(1182, 560, type_label, 26, ACC, w=700, anchor="end"))
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">' + "".join(e) + "</svg>"

BANNERS = {
    "ui": banner("Aham UI", "供 AI 消费的设计系统",
                 "单一事实源 · 八层规范 · 亮/暗双色 · 内容优先", "Design System", g_ui()),
    "ppt": banner("Aham PPT", "咨询级 AI 演示制作技能",
                  "对标麦肯锡/德勤 · 八阶段流程 · 原生 PPTX", "Claude Skill", g_ppt()),
    "survey": banner("Aham Survey", "现场调研工具 · macOS",
                     "项目制调研 · 行业模板 · 本地语音 · AI 追问", "macOS App", g_survey()),
    "voice": banner("Aham Voice", "录音转写与会议纪要 · macOS",
                    "本地离线转写 · 说话人分离 · AI 会议纪要", "macOS App", g_voice()),
}

OUT = Path.home() / "Desktop" / "aham-门面统一-提案" / "banner统一"
OUT.mkdir(parents=True, exist_ok=True)
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Inter:wght@400;500;600;700&display=swap">')
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, s in BANNERS.items():
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg.set_content(f'<!doctype html><html><head><meta charset="utf-8">{FONTS}'
                       '<style>html,body{margin:0}svg{display:block}</style></head>'
                       f'<body>{s}</body></html>', wait_until="networkidle")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(OUT / f"{name}.png"), clip={"x": 0, "y": 0, "width": W, "height": H})
        (OUT / f"{name}.svg").write_text(s, encoding="utf-8")
        pg.close(); print("banner:", name)
    b.close()
print("→", OUT)
