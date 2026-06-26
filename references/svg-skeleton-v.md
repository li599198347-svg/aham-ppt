# SVG Skeleton · V系版式骨架（证据（Evidence））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

> **⭐ v3 · 图表区一律用 charts 组件填充**：下方各 V 版式中标着「[此处替换为…图表代码]」的图表区，不再手画 —— 改为 `from charts import bar, hbar, line, waterfall, funnel, gantt, bullet, stacked, slope`，用该版式注释里给出的图表区 x/y/w/h 调用对应组件（例：V-02 单图区 x=40 y=100 w=1200 h=540 → `bar(40,100,1200,540,data,...)`；V-03 折线区 x=40 y=100 w=800 h=540 → `line(40,100,800,540,values,xlabels,...)`）。组件已内置 brand §7.5 合规与 PPTX 兼容。**V-01 的 KPI 卡：数值一律墨色 `#262626`（绝不用红绿染数字，见 chart-impl.md KPI 模板），涨跌状态靠左侧细条 + 趋势文字双通道（达标 `#5A7A60` / 风险 `#9E3D31` / 中性 `#9B9B9B`）；蓝 `#336EE8` 仅留给单个高亮指标。**

---

## ## V-01 KPI看板（证据类）
```svg
<!-- V-01与S-09结构相同，颜色语义更严格 -->
<!-- 标准Chrome -->

<!-- 说明：数值一律墨色 #262626；涨跌靠左侧细条 + 趋势文字（达标 #5A7A60 / 风险 #9E3D31 / 中性 #9B9B9B），不染数字红绿 -->
<!-- 参照 S-09 骨架，左侧细条作状态标，数值保持墨色 -->
<!-- 卡片1（达标） -->
<rect x="40" y="120" width="360" height="160" rx="4" fill="#F3F3F3"/>
<rect x="40" y="120" width="4" height="160" fill="#5A7A60"/>
<text x="56" y="152" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi1_label]</text>
<text x="56" y="214" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi1_value]</text>
<text x="56" y="268" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi1_trend]</text>

<!-- 卡片2（风险） -->
<rect x="440" y="120" width="360" height="160" rx="4" fill="#F3F3F3"/>
<rect x="440" y="120" width="4" height="160" fill="#9E3D31"/>
<text x="456" y="152" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi2_label]</text>
<text x="456" y="214" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi2_value]</text>
<text x="456" y="268" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi2_trend]</text>

<!-- 卡片3（中性） -->
<rect x="840" y="120" width="400" height="160" rx="4" fill="#F3F3F3"/>
<rect x="840" y="120" width="4" height="160" fill="#9B9B9B"/>
<text x="856" y="152" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi3_label]</text>
<text x="856" y="214" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi3_value]</text>
<text x="856" y="268" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi3_trend]</text>

<!-- 行2 y=320，同上规律，替换kpi4/5/6内容 -->
<rect x="40" y="320" width="360" height="160" rx="4" fill="#F3F3F3"/>
<rect x="40" y="320" width="4" height="160" fill="#9B9B9B"/>
<text x="56" y="352" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi4_label]</text>
<text x="56" y="414" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi4_value]</text>
<text x="56" y="468" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi4_trend]</text>

<rect x="440" y="320" width="360" height="160" rx="4" fill="#F3F3F3"/>
<rect x="440" y="320" width="4" height="160" fill="#5A7A60"/>
<text x="456" y="352" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi5_label]</text>
<text x="456" y="414" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi5_value]</text>
<text x="456" y="468" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi5_trend]</text>

<rect x="840" y="320" width="400" height="160" rx="4" fill="#F3F3F3"/>
<rect x="840" y="320" width="4" height="160" fill="#9E3D31"/>
<text x="856" y="352" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[kpi6_label]</text>
<text x="856" y="414" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="44" font-weight="bold" fill="#262626">[kpi6_value]</text>
<text x="856" y="468" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#6E6E6E">[kpi6_trend]</text>
```

---

## ## V-02 单大图表
```svg
<!-- 标准Chrome -->

<!-- 图表区：x=40 y=100 w=1200 h=540（AI在此调用 charts.py 组件，如 bar(40,100,1200,540,data,...)） -->
<rect x="40" y="100" width="1200" height="540" rx="4" fill="#F3F3F3"/>
<text x="640" y="378" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9B9B9B">[此处替换为 charts.py 组件调用]</text>

<!-- 数据来源标注 -->
<text x="56" y="656" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[data_source] · [data_date]</text>
```

---

## ## V-03 趋势折线图（图表左+洞察右）
```svg
<!-- 标准Chrome -->

<!-- 图表区：x=40 y=100 w=800 h=540 -->
<rect x="40" y="100" width="800" height="540" rx="4" fill="#F3F3F3"/>
<text x="440" y="378" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9B9B9B">[此处替换为 charts.py 的 line(40,100,800,540,...) 调用]</text>

<!-- 右侧洞察区：x=860 y=100 w=380 h=540 -->
<text x="860" y="140" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#262626" letter-spacing="2">KEY INSIGHT</text>
<line x1="860" y1="152" x2="1000" y2="152" stroke="#9B9B9B" stroke-width="1.5"/>
<text x="860" y="192" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="22" font-weight="bold" fill="#262626">[insight_title]</text>
<text x="860" y="230" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#6E6E6E">[insight_desc1]</text>
<text x="860" y="254" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#6E6E6E">[insight_desc2]</text>
<text x="860" y="278" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#6E6E6E">[insight_desc3]</text>

<!-- 关键数字强调 -->
<text x="860" y="360" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="48" font-weight="bold" fill="#262626">[key_number]</text>
<text x="860" y="400" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9B9B9B">[key_number_label]</text>

<!-- 数据来源 -->
<text x="860" y="626" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[data_source]</text>
```

---

## ## V-04 双图对比
```svg
<!-- 标准Chrome -->

<!-- 左图区：x=40 y=100 w=590 h=540 -->
<rect x="40" y="100" width="590" height="540" rx="4" fill="#F3F3F3"/>
<text x="56" y="128" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" font-weight="bold" fill="#262626">[left_chart_title]</text>
<text x="335" y="388" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9B9B9B">[此处替换为左侧 charts.py 组件调用]</text>

<!-- 右图区：x=646 y=100 w=594 h=540 -->
<rect x="646" y="100" width="594" height="540" rx="4" fill="#F3F3F3"/>
<text x="662" y="128" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" font-weight="bold" fill="#262626">[right_chart_title]</text>
<text x="943" y="388" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9B9B9B">[此处替换为右侧 charts.py 组件调用]</text>
```