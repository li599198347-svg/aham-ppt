# SVG Skeleton · G系版式骨架（结构分解（G））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ### G-01 树状分解图
```svg
<!-- 标准Chrome -->

<!-- 顶层节点：居中，x=490 y=120 w=300 h=60 -->
<rect x="490" y="120" width="300" height="60" rx="4" fill="#003D7A"/>
<text x="640" y="156" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="18" font-weight="bold" fill="#FFFFFF">[root_title]</text>

<!-- 竖线：从顶层底部到分支行 -->
<line x1="640" y1="180" x2="640" y2="240" stroke="#003D7A" stroke-width="1.5"/>
<!-- 横线：连接三个分支 -->
<line x1="200" y1="240" x2="1080" y2="240" stroke="#003D7A" stroke-width="1.5"/>

<!-- 分支1竖线+节点：x=140 y=240 w=220 h=60 -->
<line x1="200" y1="240" x2="200" y2="270" stroke="#003D7A" stroke-width="1.5"/>
<rect x="90" y="270" width="220" height="60" rx="4" fill="#E8F0FA" stroke="#003D7A" stroke-width="1"/>
<text x="200" y="306" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#003D7A">[branch1_title]</text>

<!-- 分支1子节点1：x=90 y=370 w=100 h=48 -->
<line x1="140" y1="330" x2="140" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="90" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="140" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf1_1]</text>

<!-- 分支1子节点2：x=200 y=370 w=100 h=48 -->
<line x1="250" y1="330" x2="250" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="200" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="250" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf1_2]</text>

<!-- 分支2竖线+节点：居中 x=530 y=270 w=220 h=60 -->
<line x1="640" y1="240" x2="640" y2="270" stroke="#003D7A" stroke-width="1.5"/>
<rect x="530" y="270" width="220" height="60" rx="4" fill="#E8F0FA" stroke="#003D7A" stroke-width="1"/>
<text x="640" y="306" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#003D7A">[branch2_title]</text>

<!-- 分支2子节点1 -->
<line x1="580" y1="330" x2="580" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="530" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="580" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf2_1]</text>

<!-- 分支2子节点2 -->
<line x1="690" y1="330" x2="690" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="640" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="690" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf2_2]</text>

<!-- 分支3竖线+节点：x=970 y=270 w=220 h=60 -->
<line x1="1080" y1="240" x2="1080" y2="270" stroke="#003D7A" stroke-width="1.5"/>
<rect x="970" y="270" width="220" height="60" rx="4" fill="#E8F0FA" stroke="#003D7A" stroke-width="1"/>
<text x="1080" y="306" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#003D7A">[branch3_title]</text>

<!-- 分支3子节点1 -->
<line x1="1020" y1="330" x2="1020" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="970" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="1020" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf3_1]</text>

<!-- 分支3子节点2 -->
<line x1="1130" y1="330" x2="1130" y2="370" stroke="#AAAAAA" stroke-width="1"/>
<rect x="1080" y="370" width="100" height="48" rx="3" fill="#F5F5F5" stroke="#CCCCCC" stroke-width="0.5"/>
<text x="1130" y="399" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#333333">[leaf3_2]</text>

<!-- 底部说明文字区 y=460 -->
<text x="200" y="470" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[branch1_desc]</text>
<text x="640" y="470" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[branch2_desc]</text>
<text x="1080" y="470" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[branch3_desc]</text>
```

**占位符说明：**
- `[root_title]`：顶层核心概念（≤10字）
- `[branch1/2/3_title]`：三个分支标题（≤8字）
- `[leaf1_1]` 等：叶节点（≤6字）
- `[branch1/2/3_desc]`：分支补充说明（≤15字，可选）

---

## ### G-02 三支柱并立
```svg
<!-- 标准Chrome -->

<!-- 支柱1：x=40 y=130 w=370 h=520，左侧竖线强调 -->
<rect x="40" y="130" width="370" height="520" rx="4" fill="#F5F5F5"/>
<rect x="40" y="130" width="5" height="520" fill="#003D7A"/>

<!-- 支柱1顶部标签+大字 -->
<text x="225" y="170" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="2">[pillar1_tag]</text>
<text x="225" y="230" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#1A1A1A">[pillar1_title]</text>
<line x1="65" y1="250" x2="390" y2="250" stroke="#CCCCCC" stroke-width="0.5"/>

<!-- 支柱1要点（每条y递增32） -->
<rect x="65" y="268" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="76" y="279" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar1_point1]</text>
<rect x="65" y="300" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="76" y="311" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar1_point2]</text>
<rect x="65" y="332" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="76" y="343" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar1_point3]</text>
<rect x="65" y="364" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="76" y="375" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar1_point4]</text>

<!-- 支柱1底部结论 -->
<rect x="55" y="570" width="340" height="60" rx="3" fill="#003D7A"/>
<text x="225" y="606" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[pillar1_conclusion]</text>

<!-- 支柱2：x=455 y=130 w=370 h=520 -->
<rect x="455" y="130" width="370" height="520" rx="4" fill="#F5F5F5"/>
<rect x="455" y="130" width="5" height="520" fill="#003D7A"/>
<text x="640" y="170" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="2">[pillar2_tag]</text>
<text x="640" y="230" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#1A1A1A">[pillar2_title]</text>
<line x1="480" y1="250" x2="805" y2="250" stroke="#CCCCCC" stroke-width="0.5"/>
<rect x="480" y="268" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="491" y="279" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar2_point1]</text>
<rect x="480" y="300" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="491" y="311" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar2_point2]</text>
<rect x="480" y="332" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="491" y="343" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar2_point3]</text>
<rect x="480" y="364" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="491" y="375" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar2_point4]</text>
<rect x="470" y="570" width="340" height="60" rx="3" fill="#003D7A"/>
<text x="640" y="606" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[pillar2_conclusion]</text>

<!-- 支柱3：x=870 y=130 w=370 h=520 -->
<rect x="870" y="130" width="370" height="520" rx="4" fill="#F5F5F5"/>
<rect x="870" y="130" width="5" height="520" fill="#003D7A"/>
<text x="1055" y="170" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="2">[pillar3_tag]</text>
<text x="1055" y="230" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#1A1A1A">[pillar3_title]</text>
<line x1="895" y1="250" x2="1220" y2="250" stroke="#CCCCCC" stroke-width="0.5"/>
<rect x="895" y="268" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="906" y="279" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar3_point1]</text>
<rect x="895" y="300" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="906" y="311" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar3_point2]</text>
<rect x="895" y="332" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="906" y="343" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar3_point3]</text>
<rect x="895" y="364" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="906" y="375" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[pillar3_point4]</text>
<rect x="885" y="570" width="340" height="60" rx="3" fill="#003D7A"/>
<text x="1055" y="606" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF">[pillar3_conclusion]</text>
```

**占位符说明：**
- `[pillar1/2/3_tag]`：支柱标签（如"战略层" "执行层"，≤6字，大写字母或中文）
- `[pillar1/2/3_title]`：支柱标题（≤6字）
- `[pillar1/2/3_point1~4]`：每条要点（≤18字）
- `[pillar1/2/3_conclusion]`：底部结论（≤20字）

---

## ### G-03 层级金字塔
```svg
<!-- 标准Chrome -->

<!-- 金字塔层1（顶层·最重要）：梯形 用polygon -->
<!-- 顶层梯形：上宽400，下宽560，居中于x=640，y=120，高=110 -->
<polygon points="440,120 840,120 870,230 410,230" fill="#003D7A"/>
<text x="640" y="165" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#8AAED0" letter-spacing="2">[layer1_tag]</text>
<text x="640" y="200" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#FFFFFF">[layer1_title]</text>

<!-- 层2：上宽560，下宽720，y=236，高=110 -->
<polygon points="410,236 870,236 910,346 370,346" fill="#1A5FA8"/>
<text x="640" y="281" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#A0C4E8" letter-spacing="2">[layer2_tag]</text>
<text x="640" y="316" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#FFFFFF">[layer2_title]</text>

<!-- 层3：上宽720，下宽880，y=352，高=110 -->
<polygon points="370,352 910,352 950,462 330,462" fill="#3A7FC1"/>
<text x="640" y="397" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#C0DDF0" letter-spacing="2">[layer3_tag]</text>
<text x="640" y="432" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#FFFFFF">[layer3_title]</text>

<!-- 层4（底层·最基础）：上宽880，下宽1040，y=468，高=110 -->
<polygon points="330,468 950,468 990,578 290,578" fill="#6BA3D6"/>
<text x="640" y="513" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#E0EEF8" letter-spacing="2">[layer4_tag]</text>
<text x="640" y="548" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#FFFFFF">[layer4_title]</text>

<!-- 右侧注释（每层对齐） -->
<line x1="875" y1="175" x2="960" y2="175" stroke="#CCCCCC" stroke-width="0.5" stroke-dasharray="3,3"/>
<text x="970" y="180" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[layer1_desc]</text>

<line x1="915" y1="291" x2="960" y2="291" stroke="#CCCCCC" stroke-width="0.5" stroke-dasharray="3,3"/>
<text x="970" y="296" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[layer2_desc]</text>

<line x1="955" y1="407" x2="960" y2="407" stroke="#CCCCCC" stroke-width="0.5" stroke-dasharray="3,3"/>
<text x="970" y="412" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[layer3_desc]</text>

<line x1="990" y1="523" x2="1000" y2="523" stroke="#CCCCCC" stroke-width="0.5" stroke-dasharray="3,3"/>
<text x="1010" y="528" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[layer4_desc]</text>
```

**占位符说明：**
- `[layer1/2/3/4_tag]`：层级标签（如"战略" "管理" "执行" "操作"，≤4字）
- `[layer1/2/3/4_title]`：层级名称（≤8字）
- `[layer1/2/3/4_desc]`：右侧说明（≤20字，可选留空）
- **注意**：顶层(layer1)颜色最深，向下逐渐变浅，已预设好，不修改颜色