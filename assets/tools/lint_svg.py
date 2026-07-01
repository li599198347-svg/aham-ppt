# -*- coding: utf-8 -*-
"""
SVG 渲染预检（防坑） —— 在批量渲染前 / 组装 PPTX 前跑一次。
用法：python lint_svg.py <svg目录>

检查三类高频坑（均来自实战复盘）：
1. tofu 高危字符：✕ ✓ ✗ ①-⑩ ↕ ☀ 等在等宽/无字形字体里会渲染成空心方块 □。
   → 对错请用 √(U+221A) / ×(U+00D7) 或画 path；序号用 圆圈+阿拉伯数字；勿把这些字符放进 MONO 文本。
2. 页脚总页数是否全册一致（避免出现 /50 与 /57 并存）。
3. 源码中文双引号 “” —— 会截断 Python 字符串导致 SyntaxError（请改用「」）。需配合传入 .py 目录用 --py。
"""
import sys, re, glob, os

RISK = ['✕', '✓', '✗', '↕', '☀', '✦', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩',
        '⑪', '⑫', '⑬', '⑭', '⑮', '㉕', '㉖', '㉗', '½', '¼', '∨']

def lint_svg_dir(d):
    svgs = sorted(glob.glob(os.path.join(d, '*.svg')))
    totals = set()
    risky = []
    for p in svgs:
        t = open(p, encoding='utf-8').read()
        hit = sorted(set(c for c in RISK if c in t))
        if hit:
            risky.append((os.path.basename(p), hit))
        for m in re.findall(r'>\s*\d+\s*/\s*(\d+)\s*<', t):  # 页脚 "x / N"
            totals.add(m)
    print(f"扫描 {len(svgs)} 个 SVG @ {d}")
    print("=== tofu 高危字符 ===")
    if risky:
        for n, h in risky:
            print(f"  [!] {n}: {' '.join(h)}")
    else:
        print("  无")
    print("=== 页脚总页数 ===", end=" ")
    print("一致：" + (totals.pop() if totals else "（未发现页脚）") if len(totals) <= 1 else f"⚠ 不一致 {totals}")

def lint_py_quotes(d):
    print("=== 源码中文双引号（会致 SyntaxError）===")
    bad = []
    for p in sorted(glob.glob(os.path.join(d, '*.py'))):
        t = open(p, encoding='utf-8').read()
        if '“' in t or '”' in t:
            bad.append(os.path.basename(p))
    print("  " + ("、".join(bad) + " ← 请改「」" if bad else "无"))

if __name__ == '__main__':
    d = sys.argv[1] if len(sys.argv) > 1 else '.'
    lint_svg_dir(d)
    if '--py' in sys.argv:
        lint_py_quotes(d)
