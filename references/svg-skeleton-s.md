# SVG Skeleton · S系版式骨架（结构（Structure））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ### S-01 三栏并列
```svg
<!-- 标准Chrome（见Chrome骨架） -->

<!-- 栏1：x=40 y=100 w=380 h=580 -->
<rect x="40" y="100" width="380" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[col1_title]</text>
<line x1="56" y1="136" x2="404" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="56" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col1_bullet1]</text>
<rect x="56" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col1_bullet2]</text>
<rect x="56" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col1_bullet3]</text>

<!-- 栏2：x=436 y=100 w=380 h=580（结构同栏1，替换坐标） -->
<rect x="436" y="100" width="380" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="452" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[col2_title]</text>
<line x1="452" y1="136" x2="800" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="452" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="462" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col2_bullet1]</text>
<rect x="452" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="462" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col2_bullet2]</text>
<rect x="452" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="462" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col2_bullet3]</text>

<!-- 栏3：x=832 y=100 w=408 h=580（结构同栏1，替换坐标） -->
<rect x="832" y="100" width="408" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="848" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[col3_title]</text>
<line x1="848" y1="136" x2="1224" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="848" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="858" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col3_bullet1]</text>
<rect x="848" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="858" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col3_bullet2]</text>
<rect x="848" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="858" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[col3_bullet3]</text>
```

---

## ## S-02 2×2矩阵
```svg
<!-- 标准Chrome -->

<!-- 象限1（左上）：x=40 y=100 w=590 h=282 -->
<rect x="40" y="100" width="590" height="282" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[q1_title]</text>
<line x1="56" y1="136" x2="614" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="56" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q1_bullet1]</text>
<rect x="56" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q1_bullet2]</text>

<!-- 象限2（右上）：x=646 y=100 w=594 h=282 -->
<rect x="646" y="100" width="594" height="282" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="662" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[q2_title]</text>
<line x1="662" y1="136" x2="1224" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="662" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q2_bullet1]</text>
<rect x="662" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q2_bullet2]</text>

<!-- 象限3（左下）：x=40 y=398 w=590 h=282 -->
<rect x="40" y="398" width="590" height="282" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="426" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[q3_title]</text>
<line x1="56" y1="434" x2="614" y2="434" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="56" y="448" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="458" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q3_bullet1]</text>
<rect x="56" y="472" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="482" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q3_bullet2]</text>

<!-- 象限4（右下）：x=646 y=398 w=594 h=282 -->
<rect x="646" y="398" width="594" height="282" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="662" y="426" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[q4_title]</text>
<line x1="662" y1="434" x2="1224" y2="434" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="662" y="448" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="458" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q4_bullet1]</text>
<rect x="662" y="472" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="482" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[q4_bullet2]</text>
```

---

## ## S-03 时间轴
```svg
<!-- 标准Chrome -->

<!-- 主时间轴 y=240 -->
<line x1="80" y1="240" x2="1200" y2="240" stroke="var(--brand-primary)" stroke-width="2"/>

<!-- 节点1（cx等距，3节点间距约370） -->
<circle cx="200" cy="240" r="20" fill="var(--brand-primary)"/>
<text x="200" y="246" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[m1]</text>
<text x="200" y="210" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[date1]</text>
<rect x="140" y="290" width="120" height="120" rx="3" fill="#F5F5F5" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="200" y="318" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="var(--brand-primary)">[node1_title]</text>
<text x="200" y="342" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node1_desc1]</text>
<text x="200" y="362" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node1_desc2]</text>

<!-- 节点2 cx=570 -->
<circle cx="570" cy="240" r="20" fill="var(--brand-primary)"/>
<text x="570" y="246" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[m2]</text>
<text x="570" y="210" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[date2]</text>
<rect x="510" y="290" width="120" height="120" rx="3" fill="#F5F5F5" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="570" y="318" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="var(--brand-primary)">[node2_title]</text>
<text x="570" y="342" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node2_desc1]</text>
<text x="570" y="362" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node2_desc2]</text>

<!-- 节点3 cx=940 -->
<circle cx="940" cy="240" r="20" fill="var(--brand-primary)"/>
<text x="940" y="246" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[m3]</text>
<text x="940" y="210" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[date3]</text>
<rect x="880" y="290" width="120" height="120" rx="3" fill="#F5F5F5" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="940" y="318" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="var(--brand-primary)">[node3_title]</text>
<text x="940" y="342" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node3_desc1]</text>
<text x="940" y="362" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[node3_desc2]</text>
```

---

## ## S-04 主从结构（左侧边栏+主栏+右侧边栏）
```svg
<!-- 标准Chrome -->

<!-- 左侧边栏：x=40 y=100 w=244 h=580 -->
<rect x="40" y="100" width="244" height="580" rx="4" fill="var(--brand-primary)"/>
<text x="162" y="140" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="2">[left_tag]</text>
<line x1="60" y1="156" x2="264" y2="156" stroke="#1A5FA8" stroke-width="0.5"/>
<text x="162" y="200" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#FFFFFF">[left_title]</text>
<text x="60" y="238" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#B8C8D8">[left_desc1]</text>
<text x="60" y="258" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#B8C8D8">[left_desc2]</text>
<text x="60" y="278" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#B8C8D8">[left_desc3]</text>

<!-- 主栏：x=300 y=100 w=656 h=580 -->
<rect x="300" y="100" width="656" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="316" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[main_title]</text>
<line x1="316" y1="136" x2="940" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="316" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="326" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet1]</text>
<rect x="316" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="326" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet2]</text>
<rect x="316" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="326" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet3]</text>
<rect x="316" y="222" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="326" y="232" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet4]</text>
<rect x="316" y="246" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="326" y="256" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet5]</text>

<!-- 右侧边栏：x=972 y=100 w=268 h=580 -->
<rect x="972" y="100" width="268" height="580" rx="4" fill="#F5F5F5"/>
<text x="988" y="128" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[right_tag]</text>
<line x1="988" y1="136" x2="1224" y2="136" stroke="var(--brand-primary)" stroke-width="1"/>
<text x="988" y="168" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_item1]</text>
<text x="988" y="192" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_item2]</text>
<text x="988" y="216" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_item3]</text>
```

---

## ### S-05 两栏等分
```svg
<!-- 标准Chrome -->

<!-- 左栏：x=40 y=100 w=590 h=580 -->
<rect x="40" y="100" width="590" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[left_title]</text>
<line x1="56" y1="136" x2="614" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="56" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[left_bullet1]</text>
<rect x="56" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[left_bullet2]</text>
<rect x="56" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[left_bullet3]</text>

<!-- 右栏：x=646 y=100 w=594 h=580 -->
<rect x="646" y="100" width="594" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="662" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[right_title]</text>
<line x1="662" y1="136" x2="1224" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="662" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet1]</text>
<rect x="662" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet2]</text>
<rect x="662" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="672" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[right_bullet3]</text>
```

---

## ## S-06 左因右果（6:4）
```svg
<!-- 标准Chrome -->

<!-- 主栏（因/主论点）：x=40 y=100 w=720 h=580 -->
<rect x="40" y="100" width="720" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="128" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[main_title]</text>
<line x1="56" y1="136" x2="744" y2="136" stroke="var(--brand-primary)" stroke-width="1.5"/>
<rect x="56" y="150" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="160" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet1]</text>
<rect x="56" y="174" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="184" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet2]</text>
<rect x="56" y="198" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="208" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet3]</text>
<rect x="56" y="222" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="66" y="232" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[main_bullet4]</text>

<!-- 辅栏（果/支撑）：x=776 y=100 w=464 h=580 -->
<rect x="776" y="100" width="464" height="580" rx="4" fill="#F5F5F5"/>
<rect x="776" y="100" width="4" height="580" fill="var(--brand-primary)"/>
<text x="796" y="128" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[side_tag]</text>
<line x1="796" y1="136" x2="1224" y2="136" stroke="var(--brand-primary)" stroke-width="1"/>
<text x="796" y="168" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#1A1A1A">[side_title]</text>
<text x="796" y="204" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[side_desc1]</text>
<text x="796" y="228" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[side_desc2]</text>
<text x="796" y="252" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[side_desc3]</text>
```

---

## ### S-07 阶梯递进（顶部结论+底部三支撑）
```svg
<!-- 标准Chrome -->

<!-- 顶部大结论区：x=40 y=100 w=1200 h=255 -->
<rect x="40" y="100" width="1200" height="255" rx="4" fill="var(--brand-primary)"/>
<text x="56" y="136" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="3">CORE FINDING</text>
<text x="56" y="188" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_1]</text>
<text x="56" y="228" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_2]</text>

<!-- 底部支撑1：x=40 y=371 w=380 h=309 -->
<rect x="40" y="371" width="380" height="309" rx="4" fill="#F5F5F5"/>
<rect x="40" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="60" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[support1_label]</text>
<text x="60" y="440" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[support1_title]</text>
<text x="60" y="470" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support1_desc1]</text>
<text x="60" y="494" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support1_desc2]</text>

<!-- 底部支撑2：x=436 y=371 w=380 h=309 -->
<rect x="436" y="371" width="380" height="309" rx="4" fill="#F5F5F5"/>
<rect x="436" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="456" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[support2_label]</text>
<text x="456" y="440" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[support2_title]</text>
<text x="456" y="470" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support2_desc1]</text>
<text x="456" y="494" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support2_desc2]</text>

<!-- 底部支撑3：x=832 y=371 w=408 h=309 -->
<rect x="832" y="371" width="408" height="309" rx="4" fill="#F5F5F5"/>
<rect x="832" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="852" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[support3_label]</text>
<text x="852" y="440" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[support3_title]</text>
<text x="852" y="470" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support3_desc1]</text>
<text x="852" y="494" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support3_desc2]</text>
```

---

## ## S-08 VS对照（左右对比）
```svg
<!-- 标准Chrome -->

<!-- 左侧标头 -->
<text x="320" y="160" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#888888" letter-spacing="4">[left_header]</text>
<!-- 右侧标头 -->
<text x="960" y="160" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="var(--brand-primary)" letter-spacing="4">[right_header]</text>

<!-- 中间虚线分隔 -->
<line x1="640" y1="180" x2="640" y2="650" stroke="#E2E2E2" stroke-width="0.5" stroke-dasharray="4,4"/>
<text x="628" y="410" font-family="Microsoft YaHei,sans-serif" font-size="20" fill="#CCCCCC">VS</text>

<!-- 左侧对比行（每行y递增80） -->
<rect x="60" y="200" width="520" height="60" rx="3" fill="#F5F5F5"/>
<text x="80" y="236" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[left_row1]</text>

<rect x="60" y="280" width="520" height="60" rx="3" fill="#F5F5F5"/>
<text x="80" y="316" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[left_row2]</text>

<rect x="60" y="360" width="520" height="60" rx="3" fill="#F5F5F5"/>
<text x="80" y="396" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[left_row3]</text>

<rect x="60" y="440" width="520" height="60" rx="3" fill="#F5F5F5"/>
<text x="80" y="476" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[left_row4]</text>

<!-- 右侧对比行（y坐标与左侧对齐） -->
<rect x="660" y="200" width="520" height="60" rx="3" fill="#E8F0FA"/>
<text x="680" y="236" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[right_row1]</text>

<rect x="660" y="280" width="520" height="60" rx="3" fill="#E8F0FA"/>
<text x="680" y="316" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[right_row2]</text>

<rect x="660" y="360" width="520" height="60" rx="3" fill="#E8F0FA"/>
<text x="680" y="396" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[right_row3]</text>

<rect x="660" y="440" width="520" height="60" rx="3" fill="#E8F0FA"/>
<text x="680" y="476" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[right_row4]</text>
```

---

## ## S-09 KPI看板（2×3，6个指标）
```svg
<!-- 标准Chrome -->

<!-- 行1 y=120，列x=40/440/840，每卡w=360 h=160 -->
<!-- 卡片1 -->
<rect x="40" y="120" width="360" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi1_label]</text>
<text x="56" y="210" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="var(--brand-primary)">[kpi1_value]</text>
<text x="56" y="266" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi1_desc]</text>

<!-- 卡片2 -->
<rect x="440" y="120" width="360" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="456" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi2_label]</text>
<text x="456" y="210" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="var(--brand-primary)">[kpi2_value]</text>
<text x="456" y="266" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi2_desc]</text>

<!-- 卡片3 -->
<rect x="840" y="120" width="400" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="856" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi3_label]</text>
<text x="856" y="210" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="var(--brand-primary)">[kpi3_value]</text>
<text x="856" y="266" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi3_desc]</text>

<!-- 行2 y=320 -->
<!-- 卡片4 -->
<rect x="40" y="320" width="360" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="348" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi4_label]</text>
<text x="56" y="410" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#1A7A42">[kpi4_value]</text>
<text x="56" y="466" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi4_desc]</text>

<!-- 卡片5 -->
<rect x="440" y="320" width="360" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="456" y="348" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi5_label]</text>
<text x="456" y="410" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#B01C1C">[kpi5_value]</text>
<text x="456" y="466" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi5_desc]</text>

<!-- 卡片6 -->
<rect x="840" y="320" width="400" height="160" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="856" y="348" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#888888">[kpi6_label]</text>
<text x="856" y="410" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="var(--brand-primary)">[kpi6_value]</text>
<text x="856" y="466" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[kpi6_desc]</text>
```

---

## ## S-10 HERO-2（顶部结论+底部双支撑）
```svg
<!-- 标准Chrome -->

<!-- 顶部结论区：x=40 y=100 w=1200 h=255 -->
<rect x="40" y="100" width="1200" height="255" rx="4" fill="var(--brand-primary)"/>
<text x="56" y="136" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="3">CORE FINDING</text>
<text x="56" y="188" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_1]</text>
<text x="56" y="228" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_2]</text>

<!-- 底部支撑1：x=40 y=371 w=590 h=309 -->
<rect x="40" y="371" width="590" height="309" rx="4" fill="#F5F5F5"/>
<rect x="40" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="60" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[support1_label]</text>
<text x="60" y="440" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[support1_title]</text>
<text x="60" y="472" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support1_desc1]</text>
<text x="60" y="496" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support1_desc2]</text>
<text x="60" y="520" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support1_desc3]</text>

<!-- 底部支撑2：x=646 y=371 w=594 h=309 -->
<rect x="646" y="371" width="594" height="309" rx="4" fill="#F5F5F5"/>
<rect x="646" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="666" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="2">[support2_label]</text>
<text x="666" y="440" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[support2_title]</text>
<text x="666" y="472" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support2_desc1]</text>
<text x="666" y="496" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support2_desc2]</text>
<text x="666" y="520" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[support2_desc3]</text>
```

---

## ## S-11 HERO-4（顶部结论+底部四支撑）
```svg
<!-- 标准Chrome -->

<!-- 顶部结论区：x=40 y=100 w=1200 h=255 -->
<rect x="40" y="100" width="1200" height="255" rx="4" fill="var(--brand-primary)"/>
<text x="56" y="136" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="3">CORE FINDING</text>
<text x="56" y="188" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_1]</text>
<text x="56" y="228" font-family="Songti SC,SimSun,serif" font-size="26" font-weight="bold" fill="#FFFFFF">[conclusion_line_2]</text>

<!-- 底部支撑1：x=40 y=371 w=277 h=309 -->
<rect x="40" y="371" width="277" height="309" rx="4" fill="#F5F5F5"/>
<rect x="40" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="58" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="1">[s1_label]</text>
<text x="58" y="436" font-family="Songti SC,SimSun,serif" font-size="18" font-weight="bold" fill="#1A1A1A">[s1_title]</text>
<text x="58" y="464" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s1_desc1]</text>
<text x="58" y="484" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s1_desc2]</text>

<!-- 底部支撑2：x=333 y=371 w=277 h=309 -->
<rect x="333" y="371" width="277" height="309" rx="4" fill="#F5F5F5"/>
<rect x="333" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="351" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="1">[s2_label]</text>
<text x="351" y="436" font-family="Songti SC,SimSun,serif" font-size="18" font-weight="bold" fill="#1A1A1A">[s2_title]</text>
<text x="351" y="464" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s2_desc1]</text>
<text x="351" y="484" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s2_desc2]</text>

<!-- 底部支撑3：x=626 y=371 w=277 h=309 -->
<rect x="626" y="371" width="277" height="309" rx="4" fill="#F5F5F5"/>
<rect x="626" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="644" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="1">[s3_label]</text>
<text x="644" y="436" font-family="Songti SC,SimSun,serif" font-size="18" font-weight="bold" fill="#1A1A1A">[s3_title]</text>
<text x="644" y="464" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s3_desc1]</text>
<text x="644" y="484" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s3_desc2]</text>

<!-- 底部支撑4：x=919 y=371 w=321 h=309 -->
<rect x="919" y="371" width="321" height="309" rx="4" fill="#F5F5F5"/>
<rect x="919" y="371" width="4" height="309" fill="var(--brand-primary)"/>
<text x="937" y="403" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="var(--brand-primary)" letter-spacing="1">[s4_label]</text>
<text x="937" y="436" font-family="Songti SC,SimSun,serif" font-size="18" font-weight="bold" fill="#1A1A1A">[s4_title]</text>
<text x="937" y="464" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s4_desc1]</text>
<text x="937" y="484" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[s4_desc2]</text>
```

---

## ## S-12 全版铺满
```svg
<!-- 标准Chrome -->

<!-- 全版卡片：x=40 y=100 w=1200 h=580 -->
<rect x="40" y="100" width="1200" height="580" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="56" y="132" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[card_title]</text>
<line x1="56" y1="142" x2="1224" y2="142" stroke="var(--brand-primary)" stroke-width="1.5"/>

<!-- 内容区（灵活排布，以下为5条bullet示例） -->
<rect x="56" y="162" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="68" y="172" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#333333">[bullet1]</text>
<rect x="56" y="196" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="68" y="206" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#333333">[bullet2]</text>
<rect x="56" y="230" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="68" y="240" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#333333">[bullet3]</text>
<rect x="56" y="264" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="68" y="274" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#333333">[bullet4]</text>
<rect x="56" y="298" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="68" y="308" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#333333">[bullet5]</text>
```