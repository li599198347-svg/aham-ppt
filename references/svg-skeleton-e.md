# SVG Skeleton · E系版式骨架（说明（Explain））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ## E-01 左图右文（55:45）
```svg
<!-- 标准Chrome -->

<!-- 图形区：x=40 y=140 w=660 h=480（此处留占位框，AI填入实际图形SVG） -->
<rect x="40" y="140" width="660" height="480" rx="4" fill="#F5F5F5" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="370" y="388" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#AAAAAA">[此处替换为实际图形SVG代码]</text>

<!-- 右侧文字区：x=740 y=140 w=500 h=480 -->
<text x="740" y="172" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[right_tag]</text>
<line x1="740" y1="182" x2="880" y2="182" stroke="var(--brand-primary)" stroke-width="1.5"/>
<text x="740" y="224" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[right_title_line1]</text>
<text x="740" y="258" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[right_title_line2]</text>
<line x1="740" y1="276" x2="1224" y2="276" stroke="#E2E2E2" stroke-width="0.5"/>
<rect x="740" y="296" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="752" y="306" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet1]</text>
<rect x="740" y="320" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="752" y="330" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet2]</text>
<rect x="740" y="344" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="752" y="354" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet3]</text>
<rect x="740" y="368" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="752" y="378" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet4]</text>
```

---

## ## E-02 概念曲线图
```svg
<!-- 标准Chrome -->

<!-- 坐标系 -->
<line x1="140" y1="560" x2="140" y2="180" stroke="#1A1A1A" stroke-width="2"/>
<line x1="140" y1="560" x2="820" y2="560" stroke="#1A1A1A" stroke-width="2"/>
<text x="60" y="178" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[y_label]</text>
<text x="830" y="566" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[x_label]</text>

<!-- 三段曲线 -->
<path d="M 160 540 Q 220 520, 280 460 T 380 390" stroke="#1A7A42" stroke-width="4.5" fill="none"/>
<path d="M 380 390 Q 450 360, 510 352 T 580 370" stroke="#9A5200" stroke-width="4.5" fill="none"/>
<path d="M 580 370 Q 650 330, 720 280" stroke="var(--brand-primary)" stroke-width="4.5" fill="none" stroke-dasharray="6,4"/>

<!-- 当前位置标记 -->
<circle cx="580" cy="370" r="11" fill="#B01C1C"/>
<line x1="580" y1="360" x2="580" y2="272" stroke="#B01C1C" stroke-width="1.2" stroke-dasharray="3,3"/>
<text x="558" y="252" font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold" fill="#B01C1C">[current_label]</text>

<!-- 三阶段标签 -->
<text x="270" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A7A42">[stage1_label]</text>
<text x="460" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#9A5200">[stage2_label]</text>
<text x="650" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[stage3_label]</text>

<!-- 右侧结论文字 -->
<text x="900" y="290" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[conclusion_line1]</text>
<text x="900" y="326" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[conclusion_line2]</text>
<line x1="900" y1="344" x2="1224" y2="344" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="900" y="372" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[right_desc1]</text>
<text x="900" y="396" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[right_desc2]</text>
```

---

## ### E-03 流程示意图（箭头用polygon，不用marker）
```svg
<!-- 标准Chrome -->

<!-- 阶段1：x=80 y=260 w=200 h=100 -->
<rect x="80" y="260" width="200" height="100" rx="4" fill="#F5F5F5" stroke="var(--brand-primary)" stroke-width="1.5"/>
<text x="180" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="var(--brand-primary)" letter-spacing="2">STAGE 01</text>
<text x="180" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[stage1_name]</text>

<!-- 箭头（polygon替代marker）：从阶段1到阶段2 -->
<line x1="280" y1="310" x2="330" y2="310" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="330,304 342,310 330,316" fill="var(--brand-primary)"/>

<!-- 阶段2：x=342 y=260 w=200 h=100 -->
<rect x="342" y="260" width="200" height="100" rx="4" fill="#F5F5F5" stroke="var(--brand-primary)" stroke-width="1.5"/>
<text x="442" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="var(--brand-primary)" letter-spacing="2">STAGE 02</text>
<text x="442" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[stage2_name]</text>

<!-- 箭头 -->
<line x1="542" y1="310" x2="592" y2="310" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="592,304 604,310 592,316" fill="var(--brand-primary)"/>

<!-- 阶段3：x=604 y=260 w=200 h=100 -->
<rect x="604" y="260" width="200" height="100" rx="4" fill="#F5F5F5" stroke="var(--brand-primary)" stroke-width="1.5"/>
<text x="704" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="var(--brand-primary)" letter-spacing="2">STAGE 03</text>
<text x="704" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[stage3_name]</text>

<!-- 箭头 -->
<line x1="804" y1="310" x2="854" y2="310" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="854,304 866,310 854,316" fill="var(--brand-primary)"/>

<!-- 阶段4：x=866 y=260 w=200 h=100 -->
<rect x="866" y="260" width="200" height="100" rx="4" fill="var(--brand-primary)"/>
<text x="966" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="#8AAED0" letter-spacing="2">STAGE 04</text>
<text x="966" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">[stage4_name]</text>
```

---

## ### E-04 架构层次图
```svg
<!-- 标准Chrome -->

<!-- 顶层：x=240 y=140 w=800 h=110 -->
<rect x="240" y="140" width="800" height="110" rx="4" fill="var(--brand-primary)"/>
<text x="640" y="178" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="3">[top_layer_tag]</text>
<text x="640" y="212" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#FFFFFF">[top_layer_name]</text>

<!-- 向下箭头 -->
<line x1="640" y1="250" x2="640" y2="295" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="634,295 640,307 646,295" fill="var(--brand-primary)"/>

<!-- 中层：x=240 y=307 w=800 h=110 -->
<rect x="240" y="307" width="800" height="110" rx="4" fill="#B01C1C"/>
<text x="640" y="345" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#F0A0A0" letter-spacing="3">[mid_layer_tag]</text>
<text x="640" y="379" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#FFFFFF">[mid_layer_name]</text>

<!-- 向下箭头 -->
<line x1="640" y1="417" x2="640" y2="462" stroke="#B01C1C" stroke-width="2"/>
<polygon points="634,462 640,474 646,462" fill="#B01C1C"/>

<!-- 底层：x=240 y=474 w=800 h=110 -->
<rect x="240" y="474" width="800" height="110" rx="4" fill="#3A7FC1"/>
<text x="640" y="512" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#A0C4E8" letter-spacing="3">[bot_layer_tag]</text>
<text x="640" y="546" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#FFFFFF">[bot_layer_name]</text>
```