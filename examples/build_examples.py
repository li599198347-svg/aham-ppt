#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aham UI v6.1 · PPT 示例生成器
所有页用技能自身的 40px 网格 + 标准 Chrome（grid-system.md / svg-skeleton-common.md）。
运行：python3 examples/build_examples.py  → 写出 examples/slide-*.svg
"""
from pathlib import Path

SANS = "Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"
INK1, INK2, INK3, INK4 = "#262626", "#6E6E6E", "#9B9B9B", "#C4C4C4"
LINE, PANEL, ACC = "#E7E7E7", "#F3F3F3", "#336EE8"
OK, WARN, RISK = "#5A7A60", "#8A7333", "#9E3D31"
BAR, BAR2 = "#9B9B9B", "#C8C8C8"

def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def T(x, y, s, size=14, fill=INK1, w=None, anchor=None, ff=SANS, ls=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    wt = f' font-weight="{w}"' if w else ""
    ls = f' letter-spacing="{ls}"' if ls else ""
    return f'<text x="{x}" y="{y}" font-family="{ff}" font-size="{size}"{wt}{a}{ls} fill="{fill}">{esc(s)}</text>'

def M(x, y, s, size=14, fill=INK1, w=None, anchor=None):  # mono
    return T(x, y, s, size, fill, w, anchor, ff=MONO)

def L(x1, y1, x2, y2, stroke=LINE, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def R(x, y, w, h, fill, rx=None, stroke=None, sw=None):
    r = f' rx="{rx}"' if rx is not None else ""
    st = f' stroke="{stroke}" stroke-width="{sw or 1}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r} fill="{fill}"{st}/>'

def CIR(cx, cy, r, fill):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'

def status(x, y, color, label, size=14):
    return CIR(x, y - 4, 4, color) + T(x + 14, y, label, size, INK2)

def chrome(section, title, page, total, bluebar=False):
    e = [R(0, 0, 1280, 720, "#FFFFFF")]
    e += [T(40, 24, section, 11, INK3, ls=1),
          R(1188, 16, 9, 9, ACC, rx=2),
          T(1240, 24, "Aham", 12, INK1, w=600, anchor="end"),
          L(40, 32, 1240, 32)]
    e += [T(40, 78, title, 32, INK1, w=700), L(40, 94, 1240, 94)]
    if bluebar:
        e.append(R(40, 672, 84, 2, ACC))
    e += [L(40, 690, 1240, 690),
          T(40, 709, f"来源：{section_src.get(page,'内部测算')}", 11, INK3),
          M(1240, 709, f"{page:02d} / {total:02d}", 11, INK3, anchor="end")]
    return e

section_src = {}
def svg(body):
    return ('<svg width="1280" height="720" viewBox="0 0 1280 720" '
            'xmlns="http://www.w3.org/2000/svg">\n' + "\n".join(body) + "\n</svg>\n")

OUT = Path(__file__).parent
slides = {}

# ── 01 封面 ──────────────────────────────────────────────
def cover():
    e = [R(0, 0, 1280, 720, "#FFFFFF")]
    e += [R(40, 60, 12, 12, ACC, rx=2),
          T(62, 76, "Aham", 19, INK1, w=700),
          T(118, 76, "·　运营改善咨询", 15, INK3)]
    e += [T(40, 320, "三条产线运营诊断", 48, INK1, w=700),
          T(40, 384, "与改善实施方案", 48, INK1, w=700),
          R(42, 410, 116, 4, ACC)]
    e += [f'<text x="40" y="458" font-family="{SANS}" font-size="20" fill="{INK2}">综合效率 '
          f'<tspan font-family="{MONO}" fill="{INK1}">71%</tspan> → '
          f'<tspan font-family="{MONO}" fill="{INK1}">85%</tspan> 的 90 天改善路径</text>']
    # 右侧目录
    e.append(L(856, 286, 856, 500))
    e.append(T(892, 304, "目录　CONTENTS", 13, INK3, ls=2))
    toc = ["现状诊断与基准对标", "停机与不良根因分析", "改善方案选型对照", "90 天实施与责任矩阵"]
    for i, t in enumerate(toc):
        y = 352 + i * 42
        e.append(M(892, y, f"{i+1:02d}", 16, INK3))
        e.append(T(936, y, t, 17, INK1))
    e.append(L(40, 648, 1240, 648))
    e.append(f'<text x="40" y="682" font-family="{SANS}" font-size="13" fill="{INK3}">受众：工厂管理层　·　日期：'
             f'<tspan font-family="{MONO}">2026-06-21</tspan>　·　编号：<tspan font-family="{MONO}">OPS-2026-014</tspan></text>')
    e.append(T(1240, 682, "机密 · 仅限内部", 13, INK3, anchor="end"))
    return svg(e)
slides["slide-01-cover.svg"] = cover()

# ── 02 KPI 看板 ──────────────────────────────────────────
def dashboard():
    section_src[2] = "MES 系统 · 2026-Q1 现场测算"
    e = chrome("产线运营诊断　·　第一部分 现状", "综合效率 71.2%，低于行业基准 14 个百分点", 2, 11)
    # KPI 带
    cols = [40, 340, 640, 940]
    for x in (316, 616, 916):
        e.append(L(x, 120, x, 214))
    kpis = [("综合效率 OEE", "71.2", "%", RISK, "同比 −3.1 pt"),
            ("计划达成率", "86.4", "%", WARN, "环比 −1.8 pt"),
            ("平均停机时长", "4.7", "h/日", RISK, "环比 +0.9 h"),
            ("一次良率 FPY", "93.5", "%", OK, "环比 +0.4 pt")]
    for x, (lab, val, unit, col, delta) in zip(cols, kpis):
        e.append(T(x, 140, lab, 15, INK3))
        e.append(M(x, 190, val, 48, INK1, w=700))
        e.append(T(x + 11 + len(val) * 28, 190, unit, 20, INK3))
        e.append(status(x + 5, 210, col, delta))
    e.append(L(40, 232, 1240, 232))
    # 左表
    e.append(T(40, 274, "三条产线效率明细", 20, INK1, w=600))
    e.append(T(420, 274, "基准 OEE 目标 85%", 13, INK3, anchor="end"))
    hx = [(40, "产线", "start"), (340, "节拍达成", "end"), (456, "停机(h)", "end"),
          (560, "不良率", "end"), (600, "状态", "start")]
    for x, lab, an in hx:
        e.append(T(x, 314, lab, 14, INK2, w=600, anchor=None if an == "start" else "end"))
    e.append(L(40, 326, 700, 326, LINE, 1.2))
    rows = [("冲压线 A", "82.0%", "3.2", "2.1%", WARN, "预警"),
            ("焊装线 B", "68.4%", "5.9", "4.8%", RISK, "风险"),
            ("总装线 C", "73.0%", "4.9", "3.0%", WARN, "预警")]
    ry = 362
    for name, p, h, ng, col, st in rows:
        e.append(T(40, ry, name, 15, INK1))
        e.append(M(340, ry, p, 15, INK1, anchor="end"))
        e.append(M(456, ry, h, 15, INK1, anchor="end"))
        e.append(M(560, ry, ng, 15, INK1, anchor="end"))
        e.append(status(601, ry, col, st))
        e.append(L(40, ry + 18, 700, ry + 18, LINE, 0.75))
        ry += 54
    e.append(L(40, ry - 36 + 2, 700, ry - 36 + 2, INK4, 1.2))  # totals top line
    ty = ry + 16
    e.append(T(40, ty, "综合 / 均值", 15, INK1, w=700))
    e.append(M(340, ty, "71.2%", 15, INK1, w=700, anchor="end"))
    e.append(M(456, ty, "4.7", 15, INK1, w=700, anchor="end"))
    e.append(M(560, ty, "3.3%", 15, INK1, w=700, anchor="end"))
    e.append(T(600, ty, "—", 14, INK3))
    # 右栏
    e.append(L(728, 256, 728, 648))
    e.append(T(756, 274, "关键发现", 20, INK1, w=600))
    finds = [["焊装线 B 为主瓶颈：停机 5.9 h、不良 4.8%，", "单线拉低综合 OEE 约 6 个百分点。"],
             ["非计划停机集中在换型与待料，二者", "合计占比 64%，是改善的第一抓手。"],
             ["一次良率 93.5%，质量端稳定，重心", "应放在设备综合效率而非工艺。"]]
    fy = 310
    for lines in finds:
        e.append(CIR(760, fy - 4, 3, INK3))
        for i, ln in enumerate(lines):
            e.append(T(776, fy + i * 24, ln, 15, INK1))
        fy += 64
    e.append(T(756, 540, "非计划停机构成 · Top 3", 17, INK1, w=600))
    top3 = [("换型等待", 285, "38%", ACC), ("物料待料", 195, "26%", BAR), ("设备故障", 128, "17%", BAR2)]
    by = 568
    for lab, w, pct, col in top3:
        e.append(T(756, by, lab, 14, INK2))
        e.append(R(856, by - 12, w, 16, col, rx=2))
        e.append(M(1240, by, pct, 14, INK1, anchor="end"))
        by += 30
    return svg(e)
slides["slide-02-dashboard.svg"] = dashboard()

# ── 03 方案选型对照 ──────────────────────────────────────
def options():
    section_src[3] = "方案投入产出测算 · 2026-06"
    e = chrome("改善方案　·　第三部分 选型", "方案 B 系统升级综合性价比最高，建议优先实施", 3, 11)
    e.append(R(654, 150, 300, 452, PANEL, rx=12))  # 推荐列灰底
    e.append(T(804, 178, "推荐", 14, ACC, w=600, anchor="middle"))
    e.append(R(784, 186, 40, 2, ACC))
    heads = [(500, "方案 A", "快速改善", 600), (804, "方案 B", "系统升级", 700), (1090, "方案 C", "产线重构", 600)]
    for x, a, b, w in heads:
        e.append(T(x, 214, a, 20, INK1, w=w, anchor="middle"))
        e.append(T(x, 238, b, 14, INK2, anchor="middle"))
    e.append(L(40, 262, 1240, 262, LINE, 1.2))
    rows = [("投入预算", ("¥80 万", "¥260 万", "¥720 万"), "mono"),
            ("实施周期", ("6 周", "12 周", "28 周"), "mono"),
            ("预期 OEE 提升", ("+4 pt", "+12 pt", "+18 pt"), "mono"),
            ("实施风险", ((OK, "低"), (WARN, "中"), (RISK, "高")), "status"),
            ("产线停产", ("不停产", "周末窗口", "停产 4 周"), "text"),
            ("方案可逆性", ("高", "中", "低"), "text")]
    cx = [500, 804, 1090]
    ry = 300
    for i, (lab, vals, kind) in enumerate(rows):
        e.append(T(40, ry, lab, 15, INK2))
        for j, (x, v) in enumerate(zip(cx, vals)):
            bold = 700 if (kind == "mono" and j == 1 and i == 2) else (600 if j == 1 else None)
            if kind == "mono":
                e.append(M(x, ry, v, 15, INK1, w=bold, anchor="middle"))
            elif kind == "text":
                e.append(T(x, ry, v, 15, INK1, w=bold, anchor="middle"))
            else:
                col, txt = v
                e.append(CIR(x - 14, ry - 5, 4, col))
                e.append(T(x + 2, ry, txt, 15, INK1, anchor="middle"))
        if i < len(rows) - 1:
            e.append(L(40, ry + 22, 654, ry + 22, LINE, 0.75))
            e.append(L(954, ry + 22, 1240, ry + 22, LINE, 0.75))
        ry += 52
    e.append(L(40, ry - 22, 1240, ry - 22, INK4, 1.2))
    e.append(CIR(44, ry + 9, 3, ACC))
    e.append(f'<text x="60" y="{ry+15}" font-family="{SANS}" font-size="15" fill="{INK1}">'
             f'以中等投入、<tspan font-family="{MONO}">12</tspan> 周换取 <tspan font-family="{MONO}">+12</tspan> 个百分点 OEE，'
             f'并保留向方案 C 升级的可逆性。</text>')
    return svg(e)
slides["slide-03-options.svg"] = options()

# ── 04 证据 · 趋势图 ────────────────────────────────────
def evidence():
    section_src[4] = "MES OEE 月报 2025-11 至 2026-06"
    e = chrome("根因分析　·　第二部分 证据", "OEE 连续 8 个月低于 75%，自然爬坡无法收敛缺口", 4, 11)
    e.append(T(110, 138, "月度综合效率 OEE（%）", 14, INK3))
    base, top = 560, 180  # y for 60% and 90%
    def yv(v): return base - (v - 60) * (base - top) / 30.0
    for g in (60, 70, 80, 90):
        e.append(L(110, yv(g), 720, yv(g), PANEL, 1))
        e.append(M(98, yv(g) + 4, str(g), 12, INK3, anchor="end"))
    e.append(L(110, top - 4, 110, base, LINE, 1))
    e.append(L(110, base, 720, base, LINE, 1))
    e.append(L(110, yv(85), 720, yv(85), INK3, 1, dash="5,4"))
    e.append(T(116, yv(85) - 7, "行业基准 85%", 12, INK2))
    data = [("11月", 73), ("12月", 72), ("1月", 70), ("2月", 69), ("3月", 71), ("4月", 70), ("5月", 71), ("6月", 71.2)]
    x0, slot, bw = 130, 70, 44
    for i, (mon, v) in enumerate(data):
        cx = x0 + i * slot + slot / 2 - 22
        col = ACC if i == len(data) - 1 else BAR2
        e.append(R(cx, yv(v), bw, base - yv(v), col))
        e.append(M(cx + bw / 2, yv(v) - 8, str(v), 12, ACC if i == len(data)-1 else INK2,
                   w=600 if i == len(data)-1 else None, anchor="middle"))
        e.append(M(cx + bw / 2, 582, mon, 12, INK1 if i == len(data)-1 else INK2, anchor="middle"))
    # 右栏
    e.append(L(748, 150, 748, 632))
    e.append(T(780, 168, "趋势研判", 20, INK1, w=600))
    bs = [["近 8 个月在 69–73% 区间震荡，", "无趋势性改善，长期低于基准。"],
          ["波谷集中在 1–2 月，换型批次", "增多，与换型停机高度相关。"],
          ["缺口约 14 个百分点，靠自然", "爬坡无法收敛，需结构性介入。"]]
    by = 205
    for lines in bs:
        e.append(CIR(784, by - 4, 3, INK3))
        for i, ln in enumerate(lines):
            e.append(T(800, by + i * 24, ln, 15, INK1))
        by += 72
    e.append(L(768, 420, 1240, 420))
    e.append(T(768, 462, "改善后 6 个月目标", 14, INK3))
    e.append(M(768, 522, "85%+", 50, ACC, w=700))
    e.append(T(768, 556, "约 +14 pt，回到行业基准水平", 15, INK2))
    return svg(e)
slides["slide-04-evidence.svg"] = evidence()

# ── 05 实施路线 + 责任矩阵 ──────────────────────────────
def roadmap():
    section_src[5] = "改善项目实施计划 v2 · 2026-06"
    e = chrome("实施路径　·　第四部分 落地", "90 天三阶段推进：先治瓶颈、再稳系统、后固标准", 5, 11)
    e.append(L(242, 158, 1038, 158, LINE, 2))
    for cx, on in ((242, True), (640, False), (1038, False)):
        e.append(CIR(cx, 158, 6, ACC if on else INK4))
    for cx, d in ((242, "Day 1–30"), (640, "Day 31–60"), (1038, "Day 61–90")):
        e.append(M(cx, 190, d, 13, INK2, anchor="middle"))
    e.append(L(441, 222, 441, 476))
    e.append(L(839, 222, 839, 476))
    phases = [(40, "01", "治瓶颈", True,
               ["焊装线 B 换型 SMED 改造", "待料看板与配送节拍对齐", "关键设备点检上线"], "B 线 OEE 68→76%"),
              (454, "02", "稳系统", False,
               ["SMED 与点检标准三线推广", "MES 停机自动采集 + 日清会", "备件与工装预置"], "综合 OEE →80%"),
              (852, "03", "固标准", False,
               ["标准作业固化与培训认证", "OEE 纳入班组考核看板", "月度改善例会机制"], "综合 OEE →85% 可持续")]
    for x, num, name, cur, items, deliver in phases:
        e.append(M(x, 252, num, 28, INK4, w=700))
        e.append(T(x + 48, 252, name, 22, INK1, w=600))
        if cur:
            e.append(status(x + 124, 245, INK2, "进行中", 13))
        iy = 296
        for it in items:
            e.append(CIR(x + 4, iy - 4, 3, INK3))
            e.append(T(x + 20, iy, it, 15, INK1))
            iy += 36
        e.append(L(x, 420, x + 372, 420, LINE, 0.75))
        e.append(T(x, 454, "交付", 13, INK3))
        e.append(T(x + 48, 454, deliver, 16, INK1, w=600))
    # 责任矩阵
    e.append(L(40, 496, 1240, 496))
    e.append(T(40, 530, "责任矩阵", 17, INK1, w=600))
    cols = [(40, "关键举措"), (620, "责任方"), (840, "截止"), (980, "验收 KPI")]
    for x, lab in cols:
        e.append(T(x, 558, lab, 14, INK2, w=600))
    e.append(L(40, 570, 1240, 570, LINE, 1.2))
    rrows = [("SMED 换型改造", "工艺 · 李工", "Day 30", "换型 ≤ 20 min"),
             ("停机自动采集", "IT · 王工", "Day 45", "采集率 ≥ 95%"),
             ("标准作业固化", "生产 · 张工", "Day 90", "稽核 ≥ 90 分")]
    ry = 600
    for i, (a, b, c, d) in enumerate(rrows):
        e.append(T(40, ry, a, 15, INK1))
        e.append(T(620, ry, b, 15, INK1))
        e.append(M(840, ry, c, 15, INK1))
        e.append(T(980, ry, d, 15, INK1))
        if i < len(rrows) - 1:
            e.append(L(40, ry + 14, 1240, ry + 14, LINE, 0.75))
        ry += 28
    return svg(e)
slides["slide-05-roadmap.svg"] = roadmap()

# ── 06 大数字冲击（I-04）──────────────────────────────────
def bignum():
    e = [R(0, 0, 1280, 720, "#FFFFFF")]
    e.append(T(40, 40, "根因分析　·　停机损失量化", 11, INK3, ls=2))
    e.append(R(40, 660, 84, 2, ACC))
    e.append(T(40, 200, "非计划停机每年吃掉", 22, INK2))
    e.append(M(36, 380, "¥420", 168, INK1, w=700))
    e.append(T(450, 380, "万", 56, INK3))
    e.append(L(40, 410, 520, 410, INK1, 1.5))
    e.append(T(40, 452, "相当于焊装线 B 全年利润的 31%", 22, INK1, w=600))
    e.append(T(40, 492, "按 2026-Q1 停机工时 × 边际贡献测算", 15, INK3))
    # 右侧三条拆解
    e.append(L(800, 150, 800, 590))
    e.append(T(840, 174, "损失拆解", 13, RISK, ls=2))
    e.append(R(840, 188, 120, 2, RISK))
    items = [("换型等待", "¥160 万", "占 38% · 换型频次高、单次 45 min"),
             ("物料待料", "¥109 万", "占 26% · 配送节拍与产线不齐"),
             ("设备故障", "¥71 万", "占 17% · 点检缺失、突发停机")]
    iy = 236
    for lab, val, desc in items:
        e.append(T(840, iy, lab, 15, INK1, w=600))
        e.append(M(1240, iy, val, 17, INK1, w=600, anchor="end"))
        e.append(T(840, iy + 24, desc, 13, INK2))
        e.append(L(840, iy + 44, 1240, iy + 44, LINE, 0.75))
        iy += 84
    e.append(CIR(844, iy + 6, 3, ACC))
    e.append(T(860, iy + 12, "三项合计可改善空间 ¥340 万 / 年", 15, INK1))
    e.append(T(40, 700, "来源：停机工时台账 × 边际贡献测算 · 2026-Q1", 11, INK3))
    e.append(M(1240, 700, "06 / 11", 11, INK3, anchor="end"))
    return svg(e)
slides["slide-06-bignumber.svg"] = bignum()

# ── 07 架构层次图（E-04）· 三层 + 模块面板，层间中性箭头 ──
def architecture2():
    section_src[7] = "改善体系设计 · 2026-06"
    e = chrome("改善方案　·　体系架构", "三层改善体系：目标对齐、过程管理、现场执行", 7, 11)
    layers = [("战略层", "目标与对标", ["OEE 目标 85%", "对标行业基准", "投入产出测算"]),
              ("管理层", "过程与机制", ["日清会机制", "OEE 看板", "标准作业体系", "月度改善例会"]),
              ("执行层", "现场与动作", ["SMED 换型", "设备点检", "配送节拍", "备件预置", "培训认证"])]
    y = 120
    for li, (name, sub, mods) in enumerate(layers):
        h = 150
        e.append(T(40, y + 38, name, 22, INK1, w=600))
        e.append(T(40, y + 64, sub, 14, INK2))
        e.append(M(40, y + 116, f"L{li+1}", 30, INK4, w=700))
        mx = 240
        mw = (1240 - 240 - (len(mods) - 1) * 16) / len(mods)
        for m in mods:
            e.append(R(mx, y, mw, h, PANEL, rx=12))
            e.append(T(mx + mw / 2, y + h / 2 + 5, m, 15, INK1, w=600, anchor="middle"))
            mx += mw + 16
        if li < 2:
            # 层间下行箭头（中性）
            ax = 1140
            e.append(L(ax, y + h + 4, ax, y + h + 16, INK3, 2))
            e.append(f'<polygon points="{ax-5},{y+h+12} {ax},{y+h+20} {ax+5},{y+h+12}" fill="{INK3}"/>')
        y += h + 22
    return svg(e)
slides["slide-07-architecture.svg"] = architecture2()

# ── 08 2×2 优先级矩阵（S-02）────────────────────────────
def matrix():
    section_src[8] = "改善举措排序 · 2026-06"
    e = chrome("改善方案　·　优先级", "先做高影响低投入：SMED 与停机采集是首选", 8, 11)
    ox, oy, w, h = 200, 120, 880, 540
    cx, cy = ox + w / 2, oy + h / 2
    # 轴
    e.append(L(ox, cy, ox + w, cy, INK3, 1))
    e.append(L(cx, oy, cx, oy + h, INK3, 1))
    e.append(T(ox - 16, oy + 10, "高", 13, INK3, anchor="end"))
    e.append(T(ox - 16, oy + h, "低", 13, INK3, anchor="end"))
    # y 轴含义放左上角（避免旋转文字在 PPTX 里错位）
    e.append(T(40, oy - 4, "↑ 改善影响", 13, INK2, w=600))
    e.append(T(ox, oy + h + 30, "低投入", 13, INK3))
    e.append(T(ox + w, oy + h + 30, "高投入", 13, INK3, anchor="end"))
    e.append(T(cx, oy + h + 30, "实施投入 →", 13, INK2, anchor="middle"))
    quad = [(ox + 30, oy + 28, "优先实施", "Quick Wins", ACC,
             [("SMED 换型改造", "影响高 · 6 周"), ("停机自动采集", "影响高 · 投入低")]),
            (cx + 30, oy + 28, "重点投入", "Big Bets", INK1,
             [("MES 系统升级", "影响高 · 12 周"), ("产线节拍重排", "影响高 · 投入大")]),
            (ox + 30, cy + 28, "顺手做", "Fill-ins", INK2,
             [("点检表电子化", "影响中 · 投入低"), ("看板可视化", "影响中 · 投入低")]),
            (cx + 30, cy + 28, "暂缓", "Money Pits", INK3,
             [("整线产线重构", "影响中 · 投入巨"), ("全厂 MES 替换", "投入大 · 周期长")])]
    for qx, qy, title, en, col, items in quad:
        e.append(T(qx, qy, title, 16, col if col == ACC else INK1, w=600))
        e.append(M(qx, qy + 20, en.upper(), 11, INK3, w=None))
        iy = qy + 56
        for nm, meta in items:
            dot = ACC if col == ACC else INK3
            e.append(CIR(qx + 4, iy - 4, 3, dot))
            e.append(T(qx + 18, iy, nm, 15, INK1, w=600))
            e.append(T(qx + 18, iy + 20, meta, 13, INK2))
            iy += 50
    return svg(e)
slides["slide-08-matrix.svg"] = matrix()

# ── 09 流程闭环（E-03）──────────────────────────────────
def flow():
    e = chrome("改善方案　·　运行机制", "改善以四步闭环推进，月度复盘驱动持续迭代", 9, 11)
    steps = [("01", "测量", "Measure", "OEE/停机/不良采集", "采集率 ≥95%"),
             ("02", "诊断", "Diagnose", "根因定位、瓶颈识别", "锁定 Top3"),
             ("03", "改善", "Improve", "SMED/点检/看板", "换型 −25min"),
             ("04", "标准化", "Standardize", "标准作业+培训", "稽核 ≥90"),
             ("05", "复盘", "Review", "月度例会+迭代", "OEE 月升")]
    bw, gap, by, bh = 192, 60, 200, 150
    cxs = []
    for i, (num, zh, en, sub, metric) in enumerate(steps):
        x = 40 + i * (bw + gap); cxs.append(x + bw / 2)
        e.append(R(x, by, bw, bh, PANEL, rx=12))
        e.append(M(x + 18, by + 40, num, 22, INK4, w=700))
        e.append(T(x + 18, by + 80, zh, 18, INK1, w=600))
        e.append(T(x + 18, by + 102, en, 12, INK3))
        e.append(T(x + 18, by + 130, sub, 13, INK2))
        e.append(T(x + 18, by + bh + 30, "交付", 11, INK3))
        e.append(M(x + 18, by + bh + 52, metric, 14, INK1, w=600))
        if i < len(steps) - 1:
            ax = x + bw
            e.append(L(ax + 10, by + bh / 2, ax + gap - 14, by + bh / 2, INK3, 2))
            e.append(f'<polygon points="{ax+gap-14},{by+bh/2-5} {ax+gap-6},{by+bh/2} {ax+gap-14},{by+bh/2+5}" fill="{INK3}"/>')
    loopy = by + bh + 92
    e.append(L(cxs[-1], by + bh + 66, cxs[-1], loopy, INK3, 1.5))
    e.append(L(cxs[-1], loopy, cxs[0], loopy, INK3, 1.5))
    e.append(L(cxs[0], loopy, cxs[0], by + bh + 66, INK3, 1.5))
    e.append(f'<polygon points="{cxs[0]-5},{by+bh+74} {cxs[0]},{by+bh+66} {cxs[0]+5},{by+bh+74}" fill="{INK3}"/>')
    e.append(T((cxs[0] + cxs[-1]) / 2, loopy + 22, "每月复盘 · 持续迭代，避免回潮", 14, INK2, anchor="middle"))
    e.append(CIR(44, 626, 3, ACC))
    e.append(T(60, 632, "闭环每月跑一轮：数据驱动诊断、诊断驱动改善、改善沉淀为标准。", 15, INK1))
    return svg(e)
slides["slide-09-flow.svg"] = flow()

# ── 10 VS 对照（S-08）──────────────────────────────────
def versus():
    e = chrome("改善方案　·　决策", "维持现状年损 ¥420 万，立即改善 12 周回本", 10, 11)
    e.append(R(660, 150, 580, 432, PANEL, rx=12))
    e.append(T(70, 198, "维持现状", 22, INK1, w=700))
    e.append(T(70, 222, "DO NOTHING", 12, INK3))
    e.append(T(700, 198, "立即改善", 22, INK1, w=700))
    e.append(T(820, 198, "推荐", 14, ACC, w=600))
    e.append(R(820, 206, 40, 2, ACC))
    e.append(T(700, 222, "ACT NOW", 12, INK3))
    e.append(f'<circle cx="640" cy="206" r="26" fill="#FFFFFF" stroke="{LINE}" stroke-width="1.5"/>')
    e.append(T(640, 213, "VS", 16, INK3, w=700, anchor="middle"))
    rows = [("综合 OEE", "71%", "85%+", RISK, OK, True),
            ("年停机损失", "¥420 万", "省 ¥340 万", RISK, OK, False),
            ("效率趋势", "持续下滑", "12 周回本", RISK, OK, False),
            ("实施风险", "风险累积", "中等可控", WARN, OK, False),
            ("12 个月后", "进一步恶化", "进入良性循环", RISK, OK, False)]
    ry = 296
    for lab, lv, rv, lc, rc, isnum in rows:
        e.append(T(70, ry, lab, 14, INK2))
        e.append(CIR(286, ry - 5, 4, lc))
        e.append((M if isnum else T)(302, ry, lv, 17, INK1))
        e.append(T(700, ry, lab, 14, INK2))
        e.append(CIR(916, ry - 5, 4, rc))
        e.append((M if isnum else T)(932, ry, rv, 17, INK1))
        e.append(L(70, ry + 18, 600, ry + 18, LINE, 0.75))
        e.append(L(700, ry + 18, 1216, ry + 18, LINE, 0.75))
        ry += 56
    e.append(CIR(44, 626, 3, ACC))
    e.append(T(60, 632, "同样 12 周：要么继续亏 ¥420 万/年，要么省下 ¥340 万——选择显而易见。", 15, INK1))
    return svg(e)
slides["slide-10-versus.svg"] = versus()

# ── 11 深色过渡（T-01）· 章节切换，暗色提案调色板 ──
def darktransition():
    BG, D1, D2, D3, DACC = "#1C1C1C", "#F5F5F5", "#A8A8A8", "#767676", "#5C8BED"
    e = [R(0, 0, 1280, 720, BG)]
    e.append(T(40, 80, "PART 03　—　改善方案", 13, D3, ls=3))
    e.append(T(40, 332, "已经看清问题在哪，", 44, D1, w=700))
    e.append(T(40, 402, "接下来是怎么把它解决。", 44, D1, w=700))
    e.append(R(42, 432, 116, 3, DACC))
    e.append(T(40, 480, "从根因到闭环：方案选型、体系架构、90 天落地。", 18, D2))
    e.append(T(40, 700, "Aham · 运营改善咨询", 11, D3))
    e.append(M(1240, 700, "11 / 11", 11, D3, anchor="end"))
    return svg(e)
slides["slide-11-dark.svg"] = darktransition()

for name, content in slides.items():
    (OUT / name).write_text(content, encoding="utf-8")
print("wrote:", ", ".join(sorted(slides)))

# 浏览器高保真预览（加载 Inter / JetBrains Mono 网络字体）
CAPS = {"slide-01-cover.svg": "01 · 封面 Cover", "slide-02-dashboard.svg": "02 · KPI 看板",
        "slide-03-options.svg": "03 · 方案选型对照", "slide-04-evidence.svg": "04 · 证据 · 趋势图",
        "slide-05-roadmap.svg": "05 · 实施路线 + 责任矩阵", "slide-06-bignumber.svg": "06 · 大数字冲击",
        "slide-07-architecture.svg": "07 · 三层架构图", "slide-08-matrix.svg": "08 · 2×2 优先级矩阵",
        "slide-09-flow.svg": "09 · 流程闭环 Flow", "slide-10-versus.svg": "10 · VS 对照",
        "slide-11-dark.svg": "11 · 深色过渡"}
figs = "\n".join(f'<figure class="slide"><figcaption>{c}</figcaption><div class="canvas">{slides[f]}</div></figure>'
                 for f, c in CAPS.items())
deck = ('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Aham PPT · v6.1 设计示例</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">'
        "<style>*{box-sizing:border-box}body{margin:0;background:#FAFAFA;font-family:'Inter','PingFang SC','Microsoft YaHei',sans-serif;color:#262626;-webkit-font-smoothing:antialiased;padding:32px 16px 64px}"
        ".wrap{max-width:1080px;margin:0 auto}h1{font-size:20px;font-weight:600;margin:0 0 4px}.sub{font-size:13px;color:#9B9B9B;margin:0 0 28px}"
        ".slide{margin:0 0 28px;background:#fff;border:1px solid #E7E7E7;border-radius:12px;overflow:hidden}"
        "figcaption{font:500 12px/1 'JetBrains Mono',monospace;color:#9B9B9B;padding:12px 16px;border-bottom:1px solid #F0F0F0}"
        ".canvas svg{display:block;width:100%;height:auto}</style></head><body><div class=\"wrap\">"
        "<h1>Aham PPT · v6.1 设计示例（技能自身 40px 网格）</h1>"
        "<p class=\"sub\">三层灰 · 蓝是点缀 · 文档式表格 · 留白分隔 · 数字 mono · 状态点+文字 · 底永远纯白 16:9</p>"
        + figs + "</div></body></html>")
(OUT / "preview").mkdir(exist_ok=True)
(OUT / "preview" / "deck.html").write_text(deck, encoding="utf-8")
print("wrote: preview/deck.html")
