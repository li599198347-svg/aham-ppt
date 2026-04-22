# Layout Impl · I系版式实现（震撼（Impact））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-i.md。

---

# I 系 · 震撼类（Impact）

**共同特征**：
- 使用极简 Chrome
- 单页聚焦一个强调元素（数字 / 短句 / 反差）
- 信息密度 20-40%
- 留白 ≥ 50%
- 字号超大（60pt+）

## I-01 单数字超大屏 

**适用**：核心结论用单一数字概括；战略拐点宣言

```svg
<!-- 极简 Chrome -->
<text x="40" y="40" font-size="10" fill="#AAAAAA" letter-spacing="2">[section_path]</text>

<!-- 左侧大数字（居中偏左，留白60%） -->
<text x="140" y="316" font-family="Songti SC,SimSun,serif"
      font-size="180" font-weight="bold" fill="#003D7A">[big_number]</text>

<!-- 细线 -->
<line x1="140" y1="360" x2="380" y2="360" stroke="#1A1A1A" stroke-width="1.2"/>

<!-- 断言 -->
<text x="140" y="410" font-family="Songti SC,SimSun,serif"
      font-size="30" font-weight="bold" fill="#1A1A1A">[assertion]</text>

<!-- 支撑数据 -->
<text x="140" y="470" font-family="Microsoft YaHei,sans-serif"
      font-size="14" fill="#666666">[support_1]</text>
<text x="140" y="494" font-family="Microsoft YaHei,sans-serif"
      font-size="14" fill="#666666">[support_2]</text>

<!-- 警示强调 -->
<text x="140" y="580" font-family="Microsoft YaHei,sans-serif"
      font-size="13" fill="#B01C1C" letter-spacing="1">[warning]</text>

<!-- 极简页脚 -->
```

**信息密度**：25%  
**要求字段**：`big_number`, `assertion`, `support_1`, `support_2`, `warning`

## I-02 一句话宣言 

**适用**：核心战略口号；情绪宣言页

```svg
<!-- 深色底（或白底） -->
<rect width="1280" height="720" fill="#0A1F3A"/>

<!-- 极简标识 -->
<text x="80" y="80" font-size="11" fill="#6B86A8" letter-spacing="3">INTERLUDE · [page_no]</text>

<!-- 主引言（居中偏左，大字） -->
<text x="120" y="300" font-family="Songti SC,SimSun,serif"
      font-size="42" font-weight="bold" fill="#FFFFFF">[declaration_line_1]</text>
<text x="120" y="360" font-family="Songti SC,SimSun,serif"
      font-size="42" font-weight="bold" fill="#FFFFFF">[declaration_line_2]</text>

<!-- 副注释（小字，浅色） -->
<text x="120" y="450" font-family="Songti SC,SimSun,serif"
      font-size="28" fill="#B8C8D8">[sub_line_1]</text>
<text x="120" y="490" font-family="Songti SC,SimSun,serif"
      font-size="28" fill="#B8C8D8">[sub_line_2]</text>

<!-- 右下角引用源 -->
<text x="1200" y="620" text-anchor="end" font-size="13" fill="#6B86A8">—— [source]</text>
```

**信息密度**：15%  
**要求字段**：`declaration_line_1/2`, `sub_line_1/2`, `source`

## I-03 反差双栏 

**适用**：现状 vs 目标；之前 vs 之后；失败路径 vs 成功路径

```svg
<!-- 左侧：警示 / 现状 -->
<text x="100" y="200" font-size="11" fill="#B01C1C" letter-spacing="2">[left_label]</text>
<text x="100" y="286" font-family="Songti SC,SimSun,serif"
      font-size="80" font-weight="bold" fill="#B01C1C">[left_big]</text>
<text x="100" y="340" font-size="16" fill="#333">[left_desc]</text>

<!-- 中间分隔 -->
<line x1="640" y1="180" x2="640" y2="560" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="620" y="380" font-size="24" fill="#888888">→</text>

<!-- 右侧：目标 / 未来 -->
<text x="720" y="200" font-size="11" fill="#1A7A42" letter-spacing="2">[right_label]</text>
<text x="720" y="286" font-family="Songti SC,SimSun,serif"
      font-size="80" font-weight="bold" fill="#1A7A42">[right_big]</text>
<text x="720" y="340" font-size="16" fill="#333">[right_desc]</text>
```

**信息密度**：35%

## I-04 数据冲击（大数字+细节支撑）

**适用**：一个震撼数字 + 三条支撑原因

```svg
<!-- 左侧大数字 -->
<text x="140" y="316" font-size="170" font-weight="bold" fill="#003D7A">[big_number]</text>

<line x1="140" y1="340" x2="420" y2="340" stroke="#1A1A1A" stroke-width="1.5"/>

<!-- 断言 -->
<text x="140" y="376" font-size="30" font-weight="bold" fill="#1A1A1A">[assertion]</text>

<!-- 右侧三大支撑 -->
<line x1="800" y1="160" x2="800" y2="590" stroke="#E2E2E2" stroke-width="1"/>
<text x="860" y="180" font-size="13" fill="#B01C1C" letter-spacing="2">[right_header]</text>
<line x1="860" y1="206" x2="980" y2="206" stroke="#B01C1C" stroke-width="1.8"/>

<!-- 三行支撑 -->
<!-- 每行 y = 250 + i*110 -->
<text x="860" y="250" font-size="14" font-weight="bold" fill="#1A1A1A">① [reason_1_label]</text>
<text x="860" y="282" font-size="13" fill="#333333">[reason_1_desc]</text>
<!-- 行间分隔线 -->
<line x1="860" y1="320" x2="1180" y2="320" stroke="#E2E2E2" stroke-width="0.5"/>

<!-- ...类似的 ② ③ -->
```

**信息密度**：40%

## I-05 时间窗警告 

**适用**：紧迫性表达；窗口期论证；"再不做就来不及"类

```svg
<!-- 顶部横向时间轴 -->
<line x1="100" y1="200" x2="1180" y2="200" stroke="#CCCCCC" stroke-width="1.5"/>

<!-- 过去、现在、未来三节点 -->
<circle cx="200" cy="200" r="8" fill="#888"/>
<text x="200" y="240" text-anchor="middle" font-size="12" fill="#888">过去</text>

<circle cx="640" cy="200" r="20" fill="#B01C1C"/>
<text x="640" y="207" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFF">当前</text>
<text x="640" y="252" text-anchor="middle" font-size="13" font-weight="bold" fill="#B01C1C">★ [now_label]</text>

<circle cx="1080" cy="200" r="8" fill="#CCC" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
<text x="1080" y="240" text-anchor="middle" font-size="12" fill="#888">未来</text>

<!-- 下方警示 -->
<text x="640" y="380" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="34" font-weight="bold" fill="#1A1A1A">[warning_title]</text>
<text x="640" y="420" text-anchor="middle" font-size="15" fill="#555">[warning_desc]</text>

<!-- 大号倒计时 -->
<text x="640" y="520" text-anchor="middle" font-size="60" font-weight="bold" fill="#B01C1C">
  [window_period]</text>
<text x="640" y="560" text-anchor="middle" font-size="14" fill="#888">[window_label]</text>
```

**信息密度**：35%

---
