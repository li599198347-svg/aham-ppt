# Aham PPT · 代码资产目录

本目录包含 SVG → 原生 PPTX 的工具链。**只有一个入口**，其他都是底层实现。

---

## 入口：`svg_to_pptx_wrapper.py` ★

唯一对外使用的模块。调用方式：

```python
from svg_to_pptx_wrapper import svg_to_native_pptx
from pathlib import Path

svg_files = sorted(Path('svg_final').glob('*.svg'))
svg_to_native_pptx(svg_files, Path('output.pptx'))
```

**重要**：只使用这个 wrapper，**不要**直接调用 `svg_to_pptx/` 内部模块。

---

## 工具链主体：`svg_to_pptx/`

**用途**：把 SVG 文件批量转成原生可编辑的 PPTX 文件。

**特性**：
- 每个 SVG 元素 → 独立的 PPT 原生形状（不是图片嵌入）
- 所有文字都是可编辑 textbox，在 PowerPoint 里双击就能改
- 矩形、圆、线条都是 PPT 原生 shape
- 多边形（如梯形）通过 custGeom 实现，仍可编辑

**来源**：基于 `github.com/hugohe3/ppt-master`（MIT License）。
详见 `svg_to_pptx/LICENSE_NOTE.md`。

---

## 文件清单

```
assets/
├── README.md                    # 本文件
├── svg_to_pptx_wrapper.py       # ★ 对外入口
└── svg_to_pptx/                 # 工具链主体
    ├── __init__.py
    ├── drawingml_context.py
    ├── drawingml_converter.py
    ├── drawingml_elements.py
    ├── drawingml_paths.py
    ├── drawingml_styles.py
    ├── drawingml_utils.py
    ├── pptx_builder.py
    ├── pptx_cli.py
    ├── pptx_dimensions.py
    ├── pptx_discovery.py
    ├── pptx_media.py
    ├── pptx_notes.py
    ├── pptx_slide_xml.py
    └── LICENSE_NOTE.md
```

---

## 设计原则

- **不手写 python-pptx 代码拼形状**：baseline 偏移、letter-spacing、textbox 宽度估算有无数坑
- **不用 EMF 嵌入后声称"可编辑"**：那只是图片
- **PPTX 生成后不直接改 PPTX**：会与 SVG 真源漂移
- **出现故障时，回去改 SVG 源，重新运行工具链**
