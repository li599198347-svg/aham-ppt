# SVG Skeleton · A系版式骨架（动作（Action））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ### A-01 下一步三步决策
```svg
<!-- 标准Chrome -->

<!-- STEP 1：x=40 y=160 w=380 h=400 -->
<rect x="40" y="160" width="380" height="400" rx="4" fill="#F5F5F5"/>
<rect x="40" y="160" width="4" height="400" fill="#003D7A"/>
<text x="60" y="192" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="3">STEP 01 · [step1_time]</text>
<text x="60" y="236" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[step1_action]</text>
<text x="60" y="268" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step1_detail1]</text>
<text x="60" y="292" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step1_detail2]</text>
<text x="60" y="316" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step1_detail3]</text>

<!-- STEP 2：x=450 y=160 w=380 h=400 -->
<rect x="450" y="160" width="380" height="400" rx="4" fill="#F5F5F5"/>
<rect x="450" y="160" width="4" height="400" fill="#003D7A"/>
<text x="470" y="192" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="3">STEP 02 · [step2_time]</text>
<text x="470" y="236" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[step2_action]</text>
<text x="470" y="268" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step2_detail1]</text>
<text x="470" y="292" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step2_detail2]</text>
<text x="470" y="316" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[step2_detail3]</text>

<!-- STEP 3：x=860 y=160 w=380 h=400 -->
<rect x="860" y="160" width="380" height="400" rx="4" fill="#003D7A"/>
<rect x="860" y="160" width="4" height="400" fill="#8AAED0"/>
<text x="880" y="192" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="3">STEP 03 · [step3_time]</text>
<text x="880" y="236" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#FFFFFF">[step3_action]</text>
<text x="880" y="268" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#FFFFFF">[step3_detail1]</text>
<text x="880" y="292" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#FFFFFF">[step3_detail2]</text>
<text x="880" y="316" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#FFFFFF">[step3_detail3]</text>
```

---

## ## A-02 是/否选择矩阵
```svg
<!-- 标准Chrome -->

<!-- 选项A（推荐）：x=40 y=140 w=1200 h=220 -->
<rect x="40" y="140" width="1200" height="220" rx="4" fill="#E8F0FA"/>
<rect x="40" y="140" width="5" height="220" fill="#003D7A"/>
<text x="62" y="174" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="3">OPTION A · 推荐</text>
<text x="62" y="222" font-family="Songti SC,SimSun,serif" font-size="28" font-weight="bold" fill="#1A1A1A">[option_a_title]</text>
<text x="62" y="260" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[option_a_desc1]</text>
<text x="62" y="284" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[option_a_desc2]</text>
<!-- 右侧标注 -->
<text x="1180" y="222" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#1A7A42">[option_a_pros]</text>
<text x="1180" y="252" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#B01C1C">[option_a_cons]</text>

<!-- 中间分隔 -->
<text x="640" y="392" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#AAAAAA">或者</text>
<line x1="100" y1="392" x2="500" y2="392" stroke="#E2E2E2" stroke-width="0.5"/>
<line x1="780" y1="392" x2="1180" y2="392" stroke="#E2E2E2" stroke-width="0.5"/>

<!-- 选项B（备选）：x=40 y=410 w=1200 h=220 -->
<rect x="40" y="410" width="1200" height="220" rx="4" fill="#F5F5F5"/>
<rect x="40" y="410" width="5" height="220" fill="#888888"/>
<text x="62" y="444" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888" letter-spacing="3">OPTION B · 备选</text>
<text x="62" y="492" font-family="Songti SC,SimSun,serif" font-size="28" font-weight="bold" fill="#555555">[option_b_title]</text>
<text x="62" y="530" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#888888">[option_b_desc1]</text>
<text x="62" y="554" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#888888">[option_b_desc2]</text>
<text x="1180" y="492" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#1A7A42">[option_b_pros]</text>
<text x="1180" y="522" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#B01C1C">[option_b_cons]</text>
```

---

## ### A-03 责任矩阵
```svg
<!-- 标准Chrome -->

<!-- 表头行：y=120 h=44 -->
<rect x="40" y="120" width="1200" height="44" rx="0" fill="#1A1A1A"/>
<text x="60" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">行动事项</text>
<text x="680" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">责任方</text>
<text x="980" y="148" font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold" fill="#FFFFFF">截止时间</text>

<!-- 数据行1：y=164 h=60，奇数行填色 -->
<rect x="40" y="164" width="1200" height="60" fill="#FAFAFA"/>
<line x1="40" y1="224" x2="1240" y2="224" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="60" y="192" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[action_1]</text>
<text x="60" y="212" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[action_1_detail]</text>
<text x="680" y="198" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[owner_1]</text>
<text x="980" y="198" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_1]</text>

<!-- 数据行2：y=224 h=60，偶数行白色 -->
<rect x="40" y="224" width="1200" height="60" fill="#FFFFFF"/>
<line x1="40" y1="284" x2="1240" y2="284" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="60" y="252" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[action_2]</text>
<text x="60" y="272" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[action_2_detail]</text>
<text x="680" y="258" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[owner_2]</text>
<text x="980" y="258" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_2]</text>

<!-- 数据行3：y=284 h=60，奇数行 -->
<rect x="40" y="284" width="1200" height="60" fill="#FAFAFA"/>
<line x1="40" y1="344" x2="1240" y2="344" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="60" y="312" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[action_3]</text>
<text x="60" y="332" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[action_3_detail]</text>
<text x="680" y="318" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[owner_3]</text>
<text x="980" y="318" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_3]</text>

<!-- 数据行4：y=344 h=60 -->
<rect x="40" y="344" width="1200" height="60" fill="#FFFFFF"/>
<line x1="40" y1="404" x2="1240" y2="404" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="60" y="372" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[action_4]</text>
<text x="60" y="392" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[action_4_detail]</text>
<text x="680" y="378" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[owner_4]</text>
<text x="980" y="378" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_4]</text>
```