#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统一社交 banner 生成器（Aham 四仓库，1280×640）。
同一模板 + 单一 #336EE8 平涂（无渐变）+ 统一色板/类型标 —— 一眼是一个系列。
渲染 2x PNG 到桌面 aham-门面统一-提案/banner统一/。依赖 playwright。
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

SANS = "Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
INK1, INK2, INK3 = "#262626", "#6E6E6E", "#9B9B9B"
LINE, PANEL, ACC, INK = "#E7E7E7", "#F3F3F3", "#336EE8", "#262626"
W, H = 1280, 640
LX, LY, LS = 96, 212, 168  # logo box

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def T(x, y, s, size, fill, w=None, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wt = f' font-weight="{w}"' if w else ""
    return f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}"{wt}{a} fill="{fill}">{esc(s)}</text>'
def R(x, y, w, h, fill, rx=None):
    r = f' rx="{rx}"' if rx is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"/>'

# ── 四个 logo 字形（白色，平涂蓝底；无渐变无阴影）──
def logo_box(glyph):
    return R(LX, LY, LS, LS, ACC, rx=40) + glyph
def g_ui():       # 两条圆角线
    return (R(LX+38, LY+64, 92, 14, "#FFFFFF", rx=7) +
            R(LX+38, LY+92, 58, 14, "#FFFFFF", rx=7))
def g_ppt():      # 柱状图
    return (R(LX+34, LY+96, 24, 38, "#FFFFFF", rx=4) +
            R(LX+72, LY+70, 24, 64, "#FFFFFF", rx=4) +
            R(LX+110, LY+44, 24, 90, "#FFFFFF", rx=4))
def g_voice():    # 波形
    hs = [44, 74, 104, 128, 104, 74, 44]; out = []
    bw, gap = 12, 11; x0 = LX + (LS - (len(hs)*bw + (len(hs)-1)*gap)) / 2; cy = LY + LS/2
    for i, h in enumerate(hs):
        x = x0 + i*(bw+gap); out.append(R(x, cy - h/2, bw, h, "#FFFFFF", rx=6))
    return "".join(out)
def g_survey():   # 文档 + 放大镜
    doc = R(LX+30, LY+32, 78, 100, "#FFFFFF", rx=9)
    lines = "".join(R(LX+44, LY+54 + i*18, 46, 6, ACC, rx=3) for i in range(3))
    mag = (f'<circle cx="{LX+112}" cy="{LY+106}" r="25" fill="none" stroke="#FFFFFF" stroke-width="11"/>'
           f'<line x1="{LX+129}" y1="{LY+123}" x2="{LX+146}" y2="{LY+140}" stroke="#FFFFFF" stroke-width="11" stroke-linecap="round"/>')
    return doc + lines + mag

def banner(name, tagline, detail, type_label, glyph):
    e = [R(0, 0, W, H, "#FFFFFF"), R(0, 0, W, 6, ACC)]            # 底白 + 顶部 6px 蓝条
    e.append(logo_box(glyph))
    e.append(T(312, 300, name, 84, INK1, w=700))
    e.append(T(314, 348, tagline, 30, INK2))
    e.append(T(316, 396, detail, 20, INK3))
    # 统一色板：蓝 + 三层灰 + 墨
    sw = [ACC, "#FFFFFF", PANEL, LINE, INK1]
    for i, c in enumerate(sw):
        x = 96 + i*50
        e.append(R(x, 458, 40, 40, c, rx=6))
        if c == "#FFFFFF":
            e.append(f'<rect x="{x}" y="458" width="40" height="40" rx="6" fill="none" stroke="{LINE}" stroke-width="1"/>')
    e.append(T(96, 560, "把灵光一现，做成能用的 AI 工具。", 22, INK2))
    e.append(T(1184, 560, type_label, 22, ACC, w=700, anchor="end"))
    return (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'
            + "".join(e) + "</svg>")

BANNERS = {
    "ui": banner("Aham UI", "供 AI 消费的设计系统",
                 "单一事实源 · 八层规范 · 亮/暗双色", "Design System", g_ui()),
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
