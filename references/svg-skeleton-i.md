# SVG Skeleton · I系版式骨架（震撼（Impact））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ### I-01 单数字超大屏
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B" letter-spacing="2">[section_path]</text>

<!-- 大数字 -->
<text x="140" y="380" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="180" font-weight="bold" fill="#262626">[big_number]</text>

<!-- 细分隔线 -->
<line x1="140" y1="410" x2="420" y2="410" stroke="#262626" stroke-width="1.2"/>

<!-- 断言（无衬线 Bold） -->
<text x="140" y="456" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="30" font-weight="bold" fill="#262626">[assertion]</text>

<!-- 支撑说明 -->
<text x="140" y="506" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" fill="#6E6E6E">[support_1]</text>
<text x="140" y="530" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" fill="#6E6E6E">[support_2]</text>

<!-- 警示（可选，红色） -->
<text x="140" y="610" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9E3D31" letter-spacing="1">[warning]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">[page_index]</text>
```

---

## ### I-02 一句话宣言（深色底）
```svg
<!-- 深色背景 -->
<rect width="1280" height="720" fill="#1C1C1C"/>
<text x="80" y="80" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#A8A8A8" letter-spacing="3">INTERLUDE · [page_no]</text>

<!-- 主引言（两行） -->
<text x="120" y="300" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="42" font-weight="bold" fill="#FFFFFF">[declaration_line_1]</text>
<text x="120" y="360" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="42" font-weight="bold" fill="#FFFFFF">[declaration_line_2]</text>

<!-- 副注 -->
<text x="120" y="450" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="28" fill="#A8A8A8">[sub_line_1]</text>
<text x="120" y="490" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="28" fill="#A8A8A8">[sub_line_2]</text>

<!-- 引用来源 -->
<text x="1200" y="640" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#A8A8A8">—— [source]</text>
```

---

## ### I-03 反差双栏（现状vs目标）
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B" letter-spacing="2">[section_path]</text>

<!-- 左：警示/现状 -->
<text x="100" y="200" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#9E3D31" letter-spacing="2">[left_label]</text>
<text x="100" y="310" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="80" font-weight="bold" fill="#9E3D31">[left_big]</text>
<text x="100" y="370" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="16" fill="#262626">[left_desc]</text>

<!-- 中间分隔 -->
<line x1="640" y1="160" x2="640" y2="580" stroke="#E7E7E7" stroke-width="0.5"/>
<text x="628" y="388" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="24" fill="#9B9B9B">→</text>

<!-- 右：目标/未来 -->
<text x="720" y="200" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#5A7A60" letter-spacing="2">[right_label]</text>
<text x="720" y="310" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="80" font-weight="bold" fill="#5A7A60">[right_big]</text>
<text x="720" y="370" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="16" fill="#262626">[right_desc]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">[page_index]</text>
```

---

## ## I-04 数据冲击（大数字+细节支撑）
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B" letter-spacing="2">[section_path]</text>

<!-- 左侧大数字 -->
<text x="140" y="380" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="170" font-weight="bold" fill="#262626">[big_number]</text>
<line x1="140" y1="400" x2="440" y2="400" stroke="#262626" stroke-width="1.5"/>
<text x="140" y="440" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="28" font-weight="bold" fill="#262626">[assertion]</text>

<!-- 右侧竖分隔线 -->
<line x1="800" y1="140" x2="800" y2="610" stroke="#E7E7E7" stroke-width="1"/>

<!-- 右侧三条支撑（每条间距110） -->
<text x="860" y="170" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#9E3D31" letter-spacing="2">[right_header]</text>
<line x1="860" y1="192" x2="1000" y2="192" stroke="#9E3D31" stroke-width="1.8"/>

<text x="860" y="234" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" font-weight="bold" fill="#262626">[reason1_label]</text>
<text x="860" y="258" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#262626">[reason1_desc]</text>
<line x1="860" y1="290" x2="1200" y2="290" stroke="#E7E7E7" stroke-width="0.5"/>

<text x="860" y="332" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" font-weight="bold" fill="#262626">[reason2_label]</text>
<text x="860" y="356" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#262626">[reason2_desc]</text>
<line x1="860" y1="388" x2="1200" y2="388" stroke="#E7E7E7" stroke-width="0.5"/>

<text x="860" y="430" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" font-weight="bold" fill="#262626">[reason3_label]</text>
<text x="860" y="454" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#262626">[reason3_desc]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">[page_index]</text>
```

---

## ## I-05 时间窗警告
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B" letter-spacing="2">[section_path]</text>

<!-- 顶部横向时间轴 y=200 -->
<line x1="100" y1="200" x2="1180" y2="200" stroke="#C4C4C4" stroke-width="1.5"/>

<!-- 过去节点 -->
<circle cx="200" cy="200" r="8" fill="#9B9B9B"/>
<text x="200" y="234" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[past_label]</text>

<!-- 当前节点（红色强调） -->
<circle cx="640" cy="200" r="20" fill="#9E3D31"/>
<text x="640" y="207" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[now_label]</text>
<text x="640" y="250" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" font-weight="bold" fill="#9E3D31">[now_tag]</text>

<!-- 未来节点（虚线圆） -->
<circle cx="1080" cy="200" r="8" fill="#C4C4C4" stroke="#9B9B9B" stroke-width="1" stroke-dasharray="3,3"/>
<text x="1080" y="234" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" fill="#9B9B9B">[future_label]</text>

<!-- 警示标题 -->
<text x="640" y="360" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="34" font-weight="bold" fill="#262626">[warning_title]</text>
<text x="640" y="404" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="15" fill="#6E6E6E">[warning_desc]</text>

<!-- 大号窗口期 -->
<text x="640" y="510" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="60" font-weight="bold" fill="#9E3D31">[window_period]</text>
<text x="640" y="558" text-anchor="middle" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" fill="#9B9B9B">[window_label]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="10" fill="#9B9B9B">[page_index]</text>
```