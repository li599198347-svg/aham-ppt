# Layout Impl · E系版式实现（说明（Explain））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-e.md。

---

# E 系 · 说明类（Explain）

**共同特征**：
- 用图示（流程图、架构图、概念图）承担主要信息
- 文字为辅（说明图的内涵）
- 信息密度 50-75%

## E-01 左图右文（55:45）

**适用**：左侧一张示意图，右侧文字说明

```
图：x=40  y=140 w=660 h=480
文：x=740 y=140 w=500 h=480
```

图区可以是：
- 概念示意图（曲线图 / 漏斗 / 金字塔）
- 行业示意图（工厂 / 工位 / 流程）
- 真实图表（matplotlib 生成）

右侧文字：
- 顶部一行章节标签
- 中部大字判断句（宋体 Bold 24pt）
- 底部 2-3 条支撑要点

**信息密度**：55%

## E-02 概念曲线图 

**适用**：HERO-3 成长模型、S 型曲线、拐点分析

```svg
<!-- 坐标系 -->
<line x1="140" y1="540" x2="140" y2="220" stroke="#1A1A1A" stroke-width="2"/>
<line x1="140" y1="540" x2="800" y2="540" stroke="#1A1A1A" stroke-width="2"/>
<text x="60" y="216" text-anchor="end" font-size="12" fill="#555">[Y轴标签]</text>
<text x="810" y="546" font-size="12" fill="#555">[X轴标签]</text>

<!-- 三段曲线 -->
<!-- Stage 1 爬升 -->
<path d="M 160 520 Q 220 500, 280 440 T 360 370" 
      stroke="#1A7A42" stroke-width="4.5" fill="none"/>
<!-- Stage 2 平台 -->
<path d="M 360 370 Q 440 340, 500 335 T 580 360" 
      stroke="#9A5200" stroke-width="4.5" fill="none"/>
<!-- 成功路径虚线 -->
<path d="M 580 360 Q 650 320, 720 270" 
      stroke="var(--brand-primary)" stroke-width="4.5" fill="none" stroke-dasharray="6,4"/>

<!-- 关键节点 -->
<circle cx="580" cy="360" r="11" fill="#B01C1C"/>
<line x1="580" y1="350" x2="580" y2="270" stroke="#B01C1C" stroke-width="1.2" stroke-dasharray="3,3"/>
<text x="560" y="244" font-size="12" font-weight="bold" fill="#B01C1C">★ 当前位置</text>

<!-- 阶段标签 -->
<text x="240" y="570" font-size="14" font-weight="bold" fill="#1A7A42">[阶段1]</text>
<text x="440" y="570" font-size="14" font-weight="bold" fill="#9A5200">[阶段2]</text>
<text x="640" y="570" font-size="14" font-weight="bold" fill="var(--brand-primary)">[阶段3]</text>

<!-- 右侧判断文字 -->
<text x="900" y="300" font-family="Songti SC,SimSun,serif"
      font-size="26" font-weight="bold" fill="#1A1A1A">[conclusion_line_1]</text>
<text x="900" y="340" font-family="Songti SC,SimSun,serif"
      font-size="26" font-weight="bold" fill="#1A1A1A">[conclusion_line_2]</text>
```

**信息密度**：60%

## E-03 流程示意图 

**适用**：业务流程、工艺链、操作步骤

```svg
<!-- 多阶段流程框 + 箭头 -->
<!-- 阶段1 -->
<rect x="80" y="280" width="180" height="80" fill="#F5F5F5" stroke="var(--brand-primary)" stroke-width="1.5"/>
<text x="170" y="308" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--brand-primary)">STAGE 1</text>
<text x="170" y="332" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A1A1A">[阶段1]</text>
<text x="170" y="350" text-anchor="middle" font-size="10" fill="#555">[说明]</text>

<!-- 箭头到阶段2 -->
<line x1="260" y1="320" x2="330" y2="320" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="330,320 322,316 322,324" fill="var(--brand-primary)"/>

<!-- 阶段2... -->
```

**信息密度**：60%

## E-04 架构层次图 

**适用**：系统架构、组织结构、分层模型

```svg
<!-- 顶层 -->
<rect x="240" y="140" width="800" height="110" fill="var(--brand-primary)"/>
<text x="640" y="180" text-anchor="middle" font-size="12" fill="#FFF" letter-spacing="3">[TOP_LAYER_TAG]</text>
<text x="640" y="212" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="22" font-weight="bold" fill="#FFF">[顶层]</text>

<!-- 箭头 -->
<line x1="640" y1="250" x2="640" y2="310" stroke="var(--brand-primary)" stroke-width="2"/>

<!-- 中层 -->
<rect x="240" y="310" width="800" height="110" fill="#B01C1C"/>
<!-- 类似顶层 -->

<!-- 底层 -->
<rect x="240" y="480" width="800" height="110" fill="#3A7FC1"/>

<!-- 双向箭头 + 侧边说明卡 -->
<rect x="60" y="330" width="160" height="60" fill="#FFF" stroke="var(--brand-primary)"/>
<text x="140" y="356" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--brand-primary)">[下发说明]</text>
```

**信息密度**：65%

---
