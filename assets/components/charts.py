# -*- coding: utf-8 -*-
"""图表组件库 charts.py（自包含，通用）。

把 chart-impl.md 的手画图表固化成参数化函数：一行调用 = 一张合规专业图表，
不再逐坐标手画。供 V 系（证据/图表版式）与任意需要数据可视化的内容页调用。

—— 严格遵守 brand.md §7.5 / §2.4 图表画法（硬约束）：
   · 数据元素灰阶 #9B9B9B(主) / #C8C8C8(次)，至多一个 #336EE8 高亮“当前/重点项”
   · 坐标轴 #E7E7E7、刻度标签 #6E6E6E / #9B9B9B
   · 无 3D / 阴影 / 渐变 / 饼图 / 环形图；绝不多色（不用红绿区分正负）
   · 正负、阈值靠 “浮动位置 + 数值符号(+/-) + 文字” 区分（双通道），不靠颜色
   · 所有数字等宽 mono；柱状图 Y 轴从 0 起
—— PPTX 兼容：只用 <rect>/<line>/<text>，箭头(如需)用 <polygon>；不用 <marker>/<g rotate>。
   坐标自包含：传入图表外框 (x,y,w,h)，函数内部自动留轴/标签边距。
—— 复用 components.py 的原子函数与颜色常量，不在本文件写死品牌色。
"""
from components import T, L, MONO, ACC, INK1, INK2, INK3, INK4, LINE

BAR_MAIN = INK3        # 数据柱默认灰
BAR_SUB = "#C8C8C8"    # 次级灰（§2.4 允许的次灰）
BAR_TOTAL = INK1       # 瀑布图总量柱（深墨，作锚点）


def _fmt(v, money=False):
    """数值格式：整数加千分位；非整保留 1 位小数。货币加 ¥。"""
    if money:
        return f"\u00a5{v:,.0f}"
    if abs(v - round(v)) < 1e-9:
        return f"{int(round(v)):,}"
    return f"{v:,.1f}"


def waterfall(x, y, w, h, items, hi_index=None, unit="", money=False, title=None):
    """瀑布图：展示某指标从起点到终点的逐项增减拆解。

    items: [(label, value, kind), ...]
        kind='total' → 绝对总量柱（从 0 基线起，深墨；用于期初/期末/小计锚点）
        kind='delta' → 增量柱（浮动；value 带正负号，正=上增、负=下减）
    hi_index: 用唯一蓝(#336EE8)高亮第 i 根柱（强调关键贡献项），None 则全灰。
    unit:   左上角单位说明（如“综合产能指数(基准=100)”）。
    money:  数值是否按 ¥ 千分位格式。
    title:  图表小标题（可选）。
    """
    pad_l = 58
    pad_b = 34
    pad_t = 30 if title else 16
    px = x + pad_l
    pyt = y + pad_t
    pw = w - pad_l - 14
    ph = h - pad_t - pad_b
    n = len(items)
    if n == 0:
        return ""

    # 逐柱累计，得到每根柱的底/顶绝对值 (b0, b1)
    cum = 0.0
    bars = []  # (label, kind, b0, b1, val)
    vmax = 0.0
    for (label, val, kind) in items:
        if kind == "total":
            b0, b1 = 0.0, float(val)
            cum = float(val)
        else:  # delta
            b0, b1 = cum, cum + float(val)
            cum = cum + float(val)
        vmax = max(vmax, b0, b1)
        bars.append((label, kind, b0, b1, float(val)))
    if vmax <= 0:
        vmax = 1.0

    def vy(v):  # 值 -> 像素 y
        return pyt + ph - (v / vmax) * ph

    s = []
    if title:
        s.append(T(x, y + 16, title, 15, INK1, 700))
    if unit:
        s.append(T(px, pyt - 4, unit, 10, INK3))

    # 水平网格 + Y 刻度（3 档）
    for g in range(1, 4):
        gv = vmax * g / 3.0
        gy = vy(gv)
        s.append(L(px, gy, px + pw, gy, LINE, 0.5, dash="2,2"))
        s.append(T(px - 8, gy + 4, _fmt(gv, money), 10, INK3, anchor="end", fam=MONO))

    # Y 轴 + 0 基线
    s.append(L(px, pyt, px, pyt + ph, INK3, 0.6))
    s.append(L(px, pyt + ph, px + pw, pyt + ph, INK3, 0.6))

    slot = pw / n
    bw = slot * 0.56
    gap = slot * 0.44

    prev_b1_py = None
    prev_x_right = None
    for i, (label, kind, b0, b1, val) in enumerate(bars):
        bx = px + i * slot + gap / 2
        ytop = vy(max(b0, b1))
        ybot = vy(min(b0, b1))
        bh = max(ybot - ytop, 1.5)
        if i == hi_index:
            fill = ACC
        elif kind == "total":
            fill = BAR_TOTAL
        else:
            fill = BAR_MAIN
        s.append(f'<rect x="{bx:.1f}" y="{ytop:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{fill}"/>')

        # 浮动连接虚线：从上一柱的“结束累计”高度，水平连到当前柱左侧
        if prev_b1_py is not None:
            s.append(L(prev_x_right, prev_b1_py, bx, prev_b1_py, INK4, 0.6, dash="3,2"))

        # 数值标注（delta 带符号；total 无符号）
        if kind == "delta":
            txt = ("+" if val >= 0 else "-") + _fmt(abs(val), money)
        else:
            txt = _fmt(val, money)
        s.append(T(bx + bw / 2, ytop - 6, txt, 11, INK1, 700, anchor="middle", fam=MONO))

        # X 轴标签（过长自动两行：以空格或全角空格简单折）
        s.append(T(bx + bw / 2, pyt + ph + 18, label, 11, INK2, anchor="middle"))

        prev_b1_py = vy(b1)
        prev_x_right = bx + bw

    return "".join(s)


def bar(x, y, w, h, data, hi_index=None, unit="", money=False, title=None, target=None):
    """纵向柱状图（分类对比/排名，Y 轴从 0 起）。data=[(label,value),...]。
    hi_index 用蓝高亮一项；target 画目标参考虚线（深灰，不用绿）。"""
    pad_l, pad_b, pad_t = 52, 34, (30 if title else 16)
    px = x + pad_l; pyt = y + pad_t; pw = w - pad_l - 14; ph = h - pad_t - pad_b
    n = len(data)
    if n == 0: return ""
    vmax = max([v for _, v in data] + ([target] if target else []))
    if vmax <= 0: vmax = 1.0
    def vy(v): return pyt + ph - (v / vmax) * ph
    s = []
    if title: s.append(T(x, y + 16, title, 15, INK1, 700))
    if unit: s.append(T(px, pyt - 4, unit, 10, INK3))
    for g in range(1, 4):
        gv = vmax * g / 3.0; gy = vy(gv)
        s.append(L(px, gy, px + pw, gy, LINE, 0.5, dash="2,2"))
        s.append(T(px - 8, gy + 4, _fmt(gv, money), 10, INK3, anchor="end", fam=MONO))
    s.append(L(px, pyt, px, pyt + ph, INK3, 0.6))
    s.append(L(px, pyt + ph, px + pw, pyt + ph, INK3, 0.6))
    slot = pw / n; bw = slot * 0.56; gap = slot * 0.44
    for i, (label, val) in enumerate(data):
        bx = px + i * slot + gap / 2; ytop = vy(val); bh = max(pyt + ph - ytop, 1.5)
        fill = ACC if i == hi_index else BAR_MAIN
        s.append(f'<rect x="{bx:.1f}" y="{ytop:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{fill}"/>')
        s.append(T(bx + bw / 2, ytop - 6, _fmt(val, money), 11, INK1, 700, anchor="middle", fam=MONO))
        s.append(T(bx + bw / 2, pyt + ph + 18, label, 11, INK2, anchor="middle"))
    if target:
        ty = vy(target)
        s.append(L(px, ty, px + pw, ty, INK2, 1, dash="5,3"))
        s.append(T(px + pw, ty - 5, f"目标 {_fmt(target, money)}", 10, INK2, anchor="end"))
    return "".join(s)


def hbar(x, y, w, h, data, hi_index=None, money=False, title=None):
    """横向柱状图（排名/长标签，≤8项）。data=[(label,value),...] 自上而下。"""
    pad_l = 140; pad_t = (30 if title else 8); pad_r = 70
    px = x + pad_l; pyt = y + pad_t; pw = w - pad_l - pad_r; ph = h - pad_t - 8
    n = len(data)
    if n == 0: return ""
    vmax = max(v for _, v in data) or 1.0
    s = []
    if title: s.append(T(x, y + 16, title, 15, INK1, 700))
    rowh = ph / n; bh = min(rowh * 0.5, 26)
    for i, (label, val) in enumerate(data):
        cy = pyt + i * rowh + rowh / 2; bw = (val / vmax) * pw
        fill = ACC if i == hi_index else BAR_MAIN
        s.append(T(x + pad_l - 12, cy + 4, label, 12.5, INK2, anchor="end"))
        s.append(f'<rect x="{px:.1f}" y="{cy - bh/2:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{fill}"/>')
        s.append(T(px + bw + 8, cy + 4, _fmt(val, money), 12, INK1, 700, fam=MONO))
    return "".join(s)


def line(x, y, w, h, values, xlabels, hi_last=True, unit="", money=False, title=None, target=None, ymin=None):
    """折线趋势图（时间序列）。values 单系列；折线用 <line> 段（转换器明确支持）。
    数据点用 <circle>；hi_last 末点高亮蓝；target 画目标虚线。默认 Y 从 0。"""
    pad_l = 52; pad_b = 30; pad_t = (30 if title else 16)
    px = x + pad_l; pyt = y + pad_t; pw = w - pad_l - 16; ph = h - pad_t - pad_b
    n = len(values)
    if n < 2: return ""
    vmax = max(values + ([target] if target else []))
    vlo = 0 if ymin is None else ymin
    rng = (vmax - vlo) or 1.0
    def vy(v): return pyt + ph - ((v - vlo) / rng) * ph
    def vx(i): return px + pw * (i / (n - 1))
    s = []
    if title: s.append(T(x, y + 16, title, 15, INK1, 700))
    if unit: s.append(T(px, pyt - 4, unit, 10, INK3))
    for g in range(0, 4):
        gv = vlo + rng * g / 3.0; gy = vy(gv)
        s.append(L(px, gy, px + pw, gy, LINE, 0.5, dash="2,2"))
        s.append(T(px - 8, gy + 4, _fmt(gv, money), 10, INK3, anchor="end", fam=MONO))
    s.append(L(px, pyt, px, pyt + ph, INK3, 0.6))
    s.append(L(px, pyt + ph, px + pw, pyt + ph, INK3, 0.6))
    for i in range(n - 1):
        s.append(L(vx(i), vy(values[i]), vx(i + 1), vy(values[i + 1]), INK1, 2))
    if target:
        ty = vy(target); s.append(L(px, ty, px + pw, ty, INK2, 1, dash="5,3"))
        s.append(T(px + pw, ty - 5, f"目标 {_fmt(target, money)}", 10, INK2, anchor="end"))
    for i, v in enumerate(values):
        cx = vx(i); cy = vy(v); last = (i == n - 1)
        col = ACC if (hi_last and last) else INK1
        s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{col}"/>')
        if last or i == 0:
            s.append(T(cx, cy - 10, _fmt(v, money), 11, col, 700, anchor="middle", fam=MONO))
        s.append(T(cx, pyt + ph + 18, xlabels[i], 10, INK2, anchor="middle"))
    return "".join(s)


def funnel(x, y, w, h, stages, hi_index=None, money=False, title=None):
    """漏斗图（转化/收窄流程）。stages=[(label,value),...] 自上而下递减。
    用居中梯形(polygon)逐级收窄；级间标转化率。灰阶交替 + 可一个蓝高亮。"""
    pad_t = 30 if title else 8
    py0 = y + pad_t
    ph = h - pad_t - 8
    n = len(stages)
    if n == 0:
        return ""
    vmax = max(v for _, v in stages) or 1.0
    seg_h = ph / n * 0.7
    gap = ph / n * 0.3
    cx = x + w * 0.40
    maxw = w * 0.50
    s = []
    if title:
        s.append(T(x, y + 16, title, 15, INK1, 700))
    prev_val = None
    for i, (label, val) in enumerate(stages):
        topw = (val / vmax) * maxw
        nxtval = stages[i + 1][1] if i + 1 < n else val
        botw = (nxtval / vmax) * maxw
        yt = py0 + i * (seg_h + gap)
        yb = yt + seg_h
        fill = ACC if i == hi_index else (BAR_MAIN if i % 2 == 0 else BAR_SUB)
        pts = (f"{cx-topw/2:.1f},{yt:.1f} {cx+topw/2:.1f},{yt:.1f} "
               f"{cx+botw/2:.1f},{yb:.1f} {cx-botw/2:.1f},{yb:.1f}")
        s.append(f'<polygon points="{pts}" fill="{fill}"/>')
        s.append(T(x + w * 0.70, yt + seg_h / 2 - 3, label, 12.5, INK1, 600))
        s.append(T(x + w * 0.70, yt + seg_h / 2 + 15, _fmt(val, money), 13, INK1, 700, fam=MONO))
        if prev_val is not None and prev_val > 0:
            rate = val / prev_val * 100
            s.append(T(cx, yt - gap / 2 + 4, f"{rate:.0f}%", 10.5, INK3, anchor="middle", fam=MONO))
        prev_val = val
    return "".join(s)


def gantt(x, y, w, h, tasks, total_units, today=None, unit_label="", title=None):
    """甘特图（分期排期）。tasks=[(name,start,dur[,hi]),...]，start/dur 以 total_units 为轴总长。
    hi=True 高亮蓝；today 画今日竖虚线。只用 rect/line/text。"""
    pad_l = 150
    pad_t = 30 if title else 8
    pad_b = 24
    px = x + pad_l
    pyt = y + pad_t
    pw = w - pad_l - 16
    ph = h - pad_t - pad_b
    n = len(tasks)
    if n == 0 or total_units <= 0:
        return ""
    def ux(u):
        return px + (u / total_units) * pw
    s = []
    if title:
        s.append(T(x, y + 16, title, 15, INK1, 700))
    rowh = ph / n
    barh = min(rowh * 0.52, 22)
    grid = max(1, round(total_units / 6))
    u = 0
    while u <= total_units + 0.01:
        gx = ux(u)
        s.append(L(gx, pyt - 4, gx, pyt + ph, LINE, 0.5, dash="2,2"))
        s.append(T(gx, pyt - 8, f"{int(u)}", 9.5, INK3, anchor="middle", fam=MONO))
        u += grid
    for i, t in enumerate(tasks):
        name, start, dur = t[0], t[1], t[2]
        hi = t[3] if len(t) > 3 else False
        cy = pyt + i * rowh + rowh / 2
        bx = ux(start)
        bw = (dur / total_units) * pw
        fill = ACC if hi else BAR_MAIN
        s.append(T(x + pad_l - 12, cy + 4, name, 12, INK2, anchor="end"))
        s.append(f'<rect x="{bx:.1f}" y="{cy-barh/2:.1f}" width="{bw:.1f}" height="{barh:.1f}" rx="3" fill="{fill}"/>')
        s.append(T(bx + bw + 6, cy + 4, f"{dur}{unit_label}", 10, INK3, fam=MONO))
    if today is not None:
        tx = ux(today)
        s.append(L(tx, pyt - 6, tx, pyt + ph, INK1, 1.2, dash="4,2"))
        s.append(T(tx, pyt + ph + 14, "今日", 9.5, INK1, 600, anchor="middle"))
    return "".join(s)


def bullet(x, y, w, h, metrics, hi_index=None, money=False, title=None):
    """子弹图（多指标 实际 vs 目标）。metrics=[(label,actual,target,max),...]。
    背景=max(浅灰)，实际条=灰(或蓝高亮重点行)，目标=黑竖线。达标与否靠条末是否过目标线(双通道)，不用红绿。"""
    pad_l = 150
    pad_t = 30 if title else 8
    pad_r = 72
    px = x + pad_l
    pyt = y + pad_t
    pw = w - pad_l - pad_r
    ph = h - pad_t - 8
    n = len(metrics)
    if n == 0:
        return ""
    s = []
    if title:
        s.append(T(x, y + 16, title, 15, INK1, 700))
    rowh = ph / n
    barh = min(rowh * 0.42, 18)
    for i, (label, actual, target, mx) in enumerate(metrics):
        cy = pyt + i * rowh + rowh / 2
        mx = mx or 1.0
        s.append(f'<rect x="{px:.1f}" y="{cy-barh/2:.1f}" width="{pw:.1f}" height="{barh:.1f}" fill="{LINE}"/>')
        aw = min(actual / mx, 1.0) * pw
        fill = ACC if i == hi_index else BAR_MAIN
        s.append(f'<rect x="{px:.1f}" y="{cy-barh/2:.1f}" width="{aw:.1f}" height="{barh:.1f}" fill="{fill}"/>')
        tx = px + min(target / mx, 1.0) * pw
        s.append(L(tx, cy - barh / 2 - 4, tx, cy + barh / 2 + 4, INK1, 1.8))
        s.append(T(x + pad_l - 12, cy + 4, label, 12, INK2, anchor="end"))
        s.append(T(px + pw + 8, cy + 4, _fmt(actual, money), 11.5, INK1, 700, fam=MONO))
    return "".join(s)


def stacked(x, y, w, h, data, seriesnames, hi_series=None, unit="", money=False, title=None):
    """堆叠柱状图（构成随时间变化，≤4段）。data=[(label,[v1,v2,...]),...]；seriesnames=[...]。
    段用灰阶明度区分，可一个蓝高亮某 series。Y 从 0，柱顶标合计，底部图例。"""
    pad_l = 52; pad_b = 46; pad_t = 30 if title else 16
    px = x + pad_l; pyt = y + pad_t; pw = w - pad_l - 14; ph = h - pad_t - pad_b
    n = len(data)
    if n == 0: return ""
    totals = [sum(vals) for _, vals in data]
    vmax = max(totals) or 1.0
    def vy(v): return pyt + ph - (v / vmax) * ph
    grays = ["#C8C8C8", INK3, INK2, INK1]   # 4 级灰阶（白名单内：#C8C8C8/#9B9B9B/#6E6E6E/#262626）
    s = []
    if title: s.append(T(x, y + 16, title, 15, INK1, 700))
    if unit: s.append(T(px, pyt - 4, unit, 10, INK3))
    for g in range(1, 4):
        gv = vmax * g / 3.0; gy = vy(gv)
        s.append(L(px, gy, px + pw, gy, LINE, 0.5, dash="2,2"))
        s.append(T(px - 8, gy + 4, _fmt(gv, money), 10, INK3, anchor="end", fam=MONO))
    s.append(L(px, pyt, px, pyt + ph, INK3, 0.6))
    s.append(L(px, pyt + ph, px + pw, pyt + ph, INK3, 0.6))
    slot = pw / n; bw = slot * 0.56; gap = slot * 0.44
    for i, (label, vals) in enumerate(data):
        bx = px + i * slot + gap / 2; ybase = pyt + ph
        for k, v in enumerate(vals):
            segh = (v / vmax) * ph
            col = ACC if k == hi_series else grays[k % len(grays)]
            s.append(f'<rect x="{bx:.1f}" y="{ybase-segh:.1f}" width="{bw:.1f}" height="{segh:.1f}" fill="{col}"/>')
            ybase -= segh
        s.append(T(bx + bw / 2, pyt + ph + 18, label, 11, INK2, anchor="middle"))
        s.append(T(bx + bw / 2, vy(totals[i]) - 6, _fmt(totals[i], money), 10.5, INK1, 700, anchor="middle", fam=MONO))
    lx = px; ly = y + h - 20
    for k, nm in enumerate(seriesnames):
        col = ACC if k == hi_series else grays[k % len(grays)]
        s.append(f'<rect x="{lx:.1f}" y="{ly:.1f}" width="11" height="11" rx="2" fill="{col}"/>')
        s.append(T(lx + 16, ly + 9.5, nm, 10.5, INK2))
        lx += 16 + len(nm) * 13 + 20
    return "".join(s)


def slope(x, y, w, h, items, label_left="前", label_right="后", hi_index=None, money=False, title=None):
    """坡度图（两个时点的前后对比）。items=[(name,vleft,vright),...] 每项一条线连左右两点。
    线 + 端点 circle + 标签，可一个蓝高亮重点项。"""
    pad_t = 34 if title else 20; pad_b = 16
    pyt = y + pad_t; ph = h - pad_t - pad_b
    lx = x + w * 0.30; rx = x + w * 0.70
    n = len(items)
    if n == 0: return ""
    allv = [v for _, vl, vr in items for v in (vl, vr)]
    vmax = max(allv); vmin = min(allv); rng = (vmax - vmin) or 1.0
    def vy(v): return pyt + ph - ((v - vmin) / rng) * ph
    s = []
    if title: s.append(T(x, y + 16, title, 15, INK1, 700))
    s.append(T(lx, pyt - 12, label_left, 11, INK3, 600, anchor="middle"))
    s.append(T(rx, pyt - 12, label_right, 11, INK3, 600, anchor="middle"))
    s.append(L(lx, pyt, lx, pyt + ph, LINE, 0.6))
    s.append(L(rx, pyt, rx, pyt + ph, LINE, 0.6))
    for i, (name, vl, vr) in enumerate(items):
        yl = vy(vl); yr = vy(vr)
        col = ACC if i == hi_index else INK3
        sw = 2.4 if i == hi_index else 1.4
        s.append(L(lx, yl, rx, yr, col, sw))
        s.append(f'<circle cx="{lx:.1f}" cy="{yl:.1f}" r="3.5" fill="{col}"/>')
        s.append(f'<circle cx="{rx:.1f}" cy="{yr:.1f}" r="3.5" fill="{col}"/>')
        tc = INK1 if i == hi_index else INK2
        s.append(T(lx - 10, yl + 4, f"{name} {_fmt(vl, money)}", 11, tc, anchor="end"))
        s.append(T(rx + 10, yr + 4, _fmt(vr, money), 11, tc, 700, fam=MONO))
    return "".join(s)
