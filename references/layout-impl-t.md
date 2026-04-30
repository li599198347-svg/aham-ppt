# Layout Impl · T系版式实现（过渡（Transition））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-t.md。

---

# T 系 · 过渡类（Transition）

**共同特征**：
- 极少信息，多留白
- 情绪承接 / 章节过渡 / 引言
- 信息密度 10-25%
- 用极简 Chrome 或深色底

## T-01 深色引言页 

**适用**：章节间过渡、情绪承接、关键观点引言

```svg
<rect width="1280" height="720" fill="#0A1F3A"/>

<!-- 顶部装饰：仅一条细线 -->
<rect x="80" y="80" width="40" height="2" fill="#4A6680"/>

<!-- 主引言（居中偏左） -->
<text x="120" y="320" font-family="Songti SC,SimSun,serif"
      font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_1]</text>
<text x="120" y="370" font-family="Songti SC,SimSun,serif"
      font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_2]</text>

<!-- 副注 -->
<text x="120" y="450" font-family="Songti SC,SimSun,serif"
      font-size="24" fill="#B8C8D8">[sub_line]</text>

<!-- 右下角引用源 -->
<text x="1200" y="640" text-anchor="end" font-size="13" fill="#6B86A8">—— [source]</text>
```

**信息密度**：15%

## T-02 白底大字宣言 

**适用**：战略宣言、核心观点、一句话承诺

```svg
<!-- 极简 Chrome（只有页眉和页脚） -->

<!-- 居中大字宣言 -->
<text x="640" y="340" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_1]</text>
<text x="640" y="394" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_2]</text>

<!-- 品牌蓝短线点缀 -->
<line x1="580" y1="440" x2="700" y2="440" stroke="var(--brand-primary)" stroke-width="2.5"/>

<!-- 副注（小字） -->
<text x="640" y="490" text-anchor="middle" font-size="16" fill="#666">[sub_note]</text>
```

**信息密度**：15%

## T-03 章节承接页 

**适用**：Part 之间的过渡，明确"刚才讲了什么，接下来讲什么"

```svg
<!-- 左侧：刚才讲了什么 -->
<text x="100" y="180" font-size="11" fill="#888" letter-spacing="3">JUST COMPLETED</text>
<line x1="100" y1="206" x2="200" y2="206" stroke="#888" stroke-width="1"/>
<text x="100" y="260" font-family="Songti SC,SimSun,serif"
      font-size="22" font-weight="bold" fill="#888">[Part 1 · 回顾]</text>
<text x="100" y="300" font-size="14" fill="#555">[summary_of_previous]</text>

<!-- 中间：大号章节切换 -->
<text x="640" y="420" text-anchor="middle" font-size="14" fill="var(--brand-primary)" letter-spacing="4">
  NEXT PART</text>
<text x="640" y="470" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="40" font-weight="bold" fill="var(--brand-primary)">[Part 2 标题]</text>
<line x1="540" y1="510" x2="740" y2="510" stroke="var(--brand-primary)" stroke-width="2"/>
<text x="640" y="550" text-anchor="middle" font-size="16" fill="#555">[Part 2 引言]</text>

<!-- 底部小字：Part 编号导航 -->
<text x="640" y="640" text-anchor="middle" font-size="11" fill="#AAA">
  Part 1 ─── [Part 2 (当前)] ─── Part 3 ─── Part 4 ...</text>
```

**信息密度**：25%

---
