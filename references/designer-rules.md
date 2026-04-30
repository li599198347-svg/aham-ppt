# Designer Rules · SVG设计规范

Phase 7 每页SVG设计的执行规范。
**品牌规范以 brand.md 为权威来源，本文件只管「怎么画」。**
**颜色唯一来源：brand.md §2。禁止自定义色值，包括在本文件中写死色值。**
**语义色必须颜色+符号双通道（brand.md §2.3）。**

## CSS 变量映射（SVG 生成时必须在 `<defs><style>` 块中声明）

```svg
<defs><style>
  :root {
    --brand-primary:   [从 BRAND_RULES 取主色，如 #1677FF];
    --brand-near-black: #1A1A1A;
    --brand-gray:       #888888;
    --brand-light-bg:   #F5F5F5;
    --brand-border:     #E2E2E2;
    --semantic-success: #2E6B3E;
    --semantic-warning: #8A5A00;
    --semantic-danger:  #9C2B2B;
  }
</style></defs>
```

> `var(--brand-primary)` 在骨架代码中统一使用；具体色值从 Phase 1 加载的 BRAND_RULES 填入。

---

---

## 执行前确认

Phase 7 每页设计开始时确认以下输入已就绪：
- Phase 5 布局规划卡（含版式ID和区域坐标）
- Phase 6 视觉基调确认单
- BRAND_RULES（来自 brand.md §2）

输出格式默认为 SVG（由工具链转PPTX）。

---

## 执行流程

```
Step 1  读 Phase 5 布局规划卡 → 确认版式ID和区域坐标
Step 2  读 svg-skeleton-[系].md → 复制对应版式骨架
Step 3  读 layout-impl-[系].md → 确认版式实现细节
Step 4  若有图表 → 读 chart-impl.md 对应模板
Step 5  替换骨架中所有 [占位符] 为实际内容，不改坐标
Step 6  执行输出前自检（含PPTX兼容性5条负面约束）
```

---

## 路径A：结构性页面

读取 `svg-skeleton-common.md` 中的 Chrome 骨架，按页面类型选对应模板：
- cover → I-01 单数字超大屏
- exec_summary → S-09 KPI看板
- toc → S-12 全版铺满
- section → T-03 章节承接页
- end → A-01 下一步三步决策

替换所有 `[占位符]` 为实际内容。

**交叉检查：替换完成后，SVG 中不能有任何 `[` 或 `]` 字符（占位符未替换完）。**

---

## 路径B：内容页

### B-0：确认页面基调

在绘制任何卡片之前，读取 Phase 5 布局规划卡确认：
1. `叙事目的`（决定整体视觉基调，对应 narrative_purpose）
2. `信息密度`（对应 deck_mode 的 bullets 上限）
3. `内容要点`（这就是要画的内容）

**根据 narrative_purpose 的视觉基调指引**：

| narrative_purpose | 视觉基调 | 关键指令 |
|---|---|---|
| **impact** | 震撼 | 单数字/单句字号 ≥80pt，留白 ≥ 50%，极简 Chrome |
| **structure** | 结构 | 标准 Chrome，多区块布局，信息密度中高 |
| **explain** | 说明 | 图示优先，图示占画面 ≥ 40% |
| **evidence** | 证据 | 图表优先，数据来源标注必备 |
| **transition** | 过渡 | 极简，留白 ≥ 60%，可深色底 |
| **action** | 动作 | 清晰结构化，行动条目带编号 |

### B-1：Chrome 结构

**根据 narrative_purpose 选择 Chrome 类型**：

| narrative_purpose | Chrome 类型 |
|---|---|
| impact (I-02 I-05) | 极简 Chrome |
| transition | 极简 Chrome 或深色底 |
| 其他 | 标准 Chrome |

从 `references/layout-impl.md` 读取对应 Chrome 模板，填入：
- `[section_path]`、`[title]`、`[source]`、`[date]`、`[page_index]`、`[total_pages]`
- Draft标签：`is_draft=true` 时渲染

**字体关键规则**（brand.md 7.2节）：
- Action Title：`font-family="Songti SC,SimSun,serif"` Bold
- 内容小标题：`font-family="Microsoft YaHei,sans-serif"` Bold，fill=var(--brand-primary)
- 正文说明：`font-family="Microsoft YaHei,sans-serif"` Regular，fill=#555555
- 数字/KPI：`font-family="Microsoft YaHei,sans-serif"` Bold，fill=状态色（impact 类用 Songti SC）

### B-2：按 layout_code 读取坐标

根据 `layout_code` 在 `layout-impl-[系].md` 中查找对应坐标系统（参考该文件）。

### B-3：卡片样式

**白色卡片（默认）**：
```svg
<rect rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
```

**强调卡（深蓝底）**：
```svg
<rect rx="4" fill="var(--brand-primary)"/>
<!-- 内部所有文字改为 fill="white" -->
```

**浅蓝底卡（Callout/信息型）**：
```svg
<rect rx="4" fill="#E8F0FA" stroke="var(--brand-primary)" stroke-width="0.5"/>
```

### B-4：卡片内容元素

**卡片内边距**：16px

**卡片标题**：y=卡片y+28，微软雅黑 Bold 14px，var(--brand-primary)

**Bullets**（起始y=卡片y+52，间距24px）：
```svg
<rect x="[cx+16]" y="[itemY-10]" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="[cx+26]" y="[itemY]" font-family="Microsoft YaHei,sans-serif"
      font-size="13" fill="#333333">[bullet文字]</text>
```

**impact 类大数字**（按 narrative_purpose=impact 指令）：
```svg
<text x="[卡片中心x]" y="[卡片中心y]" text-anchor="middle"
      font-family="Songti SC,SimSun,serif" font-size="[140-180]"
      font-weight="bold" fill="var(--brand-primary)">[big_number]</text>
```

**数据来源标注**（有 data_points 时必须）：
```svg
<text x="[cx+cw-16]" y="[cy+ch-10]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="9" fill="#AAAAAA">
  来源：[source]，[date]</text>
```

### B-5：文字换行（见 layout-impl.md 字数表）

### B-6：信息密度约束

按 Phase 5 布局规划卡中的信息密度字段执行：
- presenting 模式：≤3条 bullet
- hybrid 模式（默认）：≤5条 bullet
- reading 模式：≤7条 bullet
- impact 类页面：必须有 ≥60pt 大数字
- explain 类页面：必须有图示（占画面 ≥40%）

---

## 品牌规范执行纪律

## 场景 15 · 颜色使用必须从品牌规范读取,不得自定义 ★★

**Trigger Point**:设计任何涉及颜色选择的页面时。

**核心原则(最高优先级)**:
> **颜色规范的单一源头是 `references/brand-spec/brand.md`。**
> **顾问/AI 不得在任何文档中自定义颜色值**,包括但不限于 PPT 设计说明、Skill 文档、方案附录。

### AI 最常见的三种失守方式

1. **多色相分类滥用**:为了区分模块擅自引入绿/红/蓝等多种色相
2. **擅自定义色值**:在 Skill 里写"深蓝 var(--brand-primary)"这种具体色值,形成第二套"事实标准",与 brand.md 分裂
3. **擅自收紧/放宽规范**:比如"不用绿色""最多 3 种色相"——这些限制如果 brand.md 没有,就是 AI 的臆造

### 正确做法

- 所有颜色使用决策 → **读取 brand.md §2 配色体系**,按规范执行
- 需要说明某个颜色含义时 → **引用规范条款**(如"按 brand.md §2.3 语义色表,✕ 异常用语义警示色")
- 规范里没有的场景 → **停下来问用户**,不自己补充

### 必问问题(每次要引入颜色时)

1. brand.md **第几节第几条**明确允许这个颜色的使用?
2. 我是在**执行规范**,还是在**补充规范**?(补充就是越权)
3. 如果我觉得规范没覆盖到,是**规范有漏洞**,还是**我没读仔细**?
4. 如果规范真有漏洞,正确做法是**告知用户并请求规范更新**,而不是自己临时定义

### Aham 规范结构概览(查表索引)

顾问执行时直接查 brand.md 对应章节,不在本文件复述具体色值:

- **§2.1** 主品牌色(含近黑、品牌深蓝等 5 种)
- **§2.2** 中性色序列(7 档明度)
- **§2.3** 语义色(必须符号+颜色双通道,5 种状态)★ 关键硬要求
- **§2.4** 图表系列色顺序

### §2.3 的硬要求

brand.md §2.3 明确规定:
> **"禁止单独依赖颜色传达状态——必须同时使用符号作为第二通道"**

这意味着:如果要在某个工序上标"缺口",不能只用红色高亮,**必须同时用 ✕ 或 ▲ 符号**。
这条规则容易被忽略,所有语义色场景都要双通道。

### 多色相滥用的本质

不是"AI 爱花哨",而是 **AI 没有把"品牌规范"作为权威参照**,每次设计都在重新发明配色。一旦建立了"从 brand.md 读取"的纪律,多色相滥用问题会**自动消失**,因为规范本身就限定了色彩谱系。

### Usage(三步走)

1. 设计前读 brand.md §2 配色体系
2. 列出本页所有需要颜色的元素,逐一映射到规范中的色值
3. 如果某个元素在规范里找不到对应位置,**停下来问用户**,不自行决策

### Cost of Skipping

- 规范与设计分裂,每次都在"重新发明"
- 规范升级(如 V1.4)后,所有旧 PPT 和旧 Skill 描述都失效
- AI 成为"规范的第二作者",权威性被稀释
- 客户看到不同 PPT 色值不一致,品牌一致性崩塌

### 钜普项目的两次翻车(作为教训)

**翻车 1 · P9 第一版多色相滥用**
- 错误:上游绿 / 中游红 / 下游蓝三色相分类
- 用户纠正:不应用色相分类,应该用明度变化

**翻车 2 · AI 在 Skill 里擅自定义色值**
- 错误:在 SKILL_UPGRADE_NOTES 里写具体色值,形成第二套规范
- 用户纠正:"你不应该在这里定义,都应该从 brand.md 读取"

---

## 架构级修正:brand.md 作为唯一真源

### 背景

钜普项目在 Phase 4.5 样稿阶段连续暴露了两层问题:
1. **单页级**:P9 用多色相分类(绿/红/蓝分段)
2. **技能级**:AI 在 SKILL 文档里擅自定义色值,试图"补充规范"

用户明确指出:
> "**整个设计规范是比技能更严谨的存在**。可能因为技能的要求,就在更改设计规范。设计规范是下一个环节的事情。"

这个表述把问题的**责任层次**说清楚了——**技能是规范的执行者,不是共同作者。**

### 四项强制纪律

#### 纪律 1 · 前置读取

在 SKILL 执行时(Phase 0.5 品牌规范读取阶段),必须强制读取:
- `references/brand-spec/brand.md §2 配色体系`
- `references/brand-spec/brand.md §3 字体体系`
- `references/brand-spec/brand.md §7 PPT 规范`

读取后把**完整色值白名单**加载到上下文,后续所有设计决策**只能从白名单查表**。

#### 纪律 2 · designer 阶段的硬性规则

在 `designer-rules.md` 里有顶级原则:
> **任何涉及颜色的决策,必须先在 brand.md §2 中找到对应条款。**
> **规范里没有的色值,不得使用。**
> **如遇规范未覆盖的场景,停下来问用户,禁止自行补充色值。**

#### 纪律 3 · QC 阶段的强制审计

在输出前必须有**色值合规审计**:

```python
## 审计结果示例(供参考)

钜普项目 Phase 4.5 的一次合规审计:

```
违规触发点: 7 张样稿中有 3 张违规,共 10 处色值违规
修正方案: A · 严格合规替换(映射到 brand.md §2 标准色)
修正后: 7 张全部通过审计,单一源头原则建立
```

违规色值映射记录供未来参考:

| 违规色值 | 映射到 | 规范位置 |
|---|---|---|
| 擅创的深蓝底 | 近黑 | §2.1 |
| 擅创的中灰 | 注释灰 | §2.2 |
| 擅创的冷灰 | H2 底线色 | §2.2 |

(具体色值按 brand.md 查表,不在本文件写死)

---

## 自查清单

每次设计时,Claude 要问自己:

- [ ] 我用的每个颜色,都能在 brand.md 里找到对应条款吗?
- [ ] 有没有因为"好看"就临时定义色值?
- [ ] 语义色场景有没有用**颜色+符号**双通道?
- [ ] 字体选择,是按 §3 查表,还是凭记忆?
- [ ] 如果用户问"为什么用这个色",我能指出规范条款吗?

---

---

## PPTX 兼容性硬性约束（SVG转PPTX实测雷区）

以下规则来自实测问题总结。违反任意一条，转换后的PPTX会出现内容丢失、空白页或排版错位。

### 约束1：特殊字符必须转义（最高优先级）

SVG文字内容中，以下字符必须使用XML转义：

| 原字符 | 转义写法 | 常见场景 |
|--------|---------|---------|
| `&` | `&amp;` | R&D、AT&T、P&L |
| `<` | `&lt;` | 比较符、尖括号 |
| `>` | `&gt;` | 比较符 |
| `"` | `&quot;` | 属性值内的引号 |

工具链会自动修复裸露的 `&`，但其他字符仍需手动处理。
写SVG时养成习惯：**文字内容有特殊符号，先转义再填入**。

### 约束2：箭头必须用 `<polygon>` 画，禁止用 `<marker>`

`<marker>` 定义的箭头在 `<path>` 和 `<polyline>` 上的 `marker-end` 属性转换后会丢失。

```svg
<!-- ❌ 禁止：marker箭头，转换后消失 -->
<defs>
  <marker id="arrow" ...><path d="M0,0 L10,5 L0,10"/></marker>
</defs>
<path d="M100,100 L300,100" marker-end="url(#arrow)"/>

<!-- ✅ 正确：polygon多边形直接画箭头 -->
<line x1="100" y1="100" x2="290" y2="100" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="285,94 300,100 285,106" fill="var(--brand-primary)"/>
```

注：`<line>` 元素上的 `marker-end` 有部分支持，但仍推荐用 `<polygon>` 确保100%可靠。

### 约束3：禁止 `<g>` 上的 `rotate` 和负数 `scale`

`<g transform="rotate(...)">` 只旋转容器边框，不旋转子元素坐标，转换后子元素位置偏移。
`<g transform="scale(-1, 1)">` 等负数缩放在DrawingML中无对应实现，会被忽略。

```svg
<!-- ❌ 禁止：group级别rotate，子元素坐标会偏移 -->
<g transform="rotate(45, 640, 360)">
  <rect x="500" y="300" width="200" height="100"/>
</g>

<!-- ✅ 正确：计算旋转后的绝对坐标，直接写入元素 -->
<rect x="..." y="..." width="200" height="100" transform="rotate(45, 600, 350)"/>
```

`translate` 是安全的，可以在 `<g>` 上使用。

### 约束4：多行文字换行方式（两种方式均可靠）

SVG `<text>` 不支持自动换行。有两种可靠的换行方式，工具链均支持：

**方式一：`<tspan dy="1.4em">` 换行（推荐，语义清晰）**
工具链会自动将每个 `<tspan dy>` 拆成独立的 TextBox，坐标正确。
```svg
<text x="100" y="100" font-size="16">
  <tspan x="100" dy="0">第一行文字内容</tspan>
  <tspan x="100" dy="1.4em">第二行文字内容</tspan>
  <tspan x="100" dy="1.4em">第三行文字内容</tspan>
</text>
```

**方式二：独立 `<text>` 标签，各自指定 y 坐标（可靠，适合复杂布局）**
```svg
<text x="100" y="100" font-size="16">第一行文字内容</text>
<text x="100" y="124" font-size="16">第二行文字内容</text>
<text x="100" y="148" font-size="16">第三行文字内容</text>
```

**禁止：** 在文字内容里用 `\n` 换行（被折叠为空格，换行消失）。

### 约束5：单行文字长度不得超过容器宽度

工具链生成的TextBox宽度是按文字内容估算的，不会自动裁剪。文字超出容器在PPTX里仍然超出。

**各字号单行最大字数参考（中文，容器宽度1200px）：**

| 字号 | 单行最大中文字数 | 单行最大英文字符数 |
|------|---------------|-----------------|
| 14px | 约 62 字 | 约 150 字符 |
| 16px | 约 55 字 | 约 130 字符 |
| 18px | 约 48 字 | 约 115 字符 |
| 22px（Action Title） | 约 38 字 | 约 90 字符 |
| 28px | 约 30 字 | 约 72 字符 |

超出时必须拆成多个 `<tspan>`，不得依赖容器自动截断。

### 约束6：`Songti SC` 字体在Windows会映射为 `SimSun`

工具链已内置映射，但 `SimSun` 与 `Songti SC` 字形宽度有差异，大字号下间距会偏移。

追求跨平台一致性时，Action Title 字体写法建议：
```svg
font-family="SimSun, Songti SC, serif"
```
Windows 优先读 `SimSun`，macOS 优先读 `Songti SC`，视觉差异最小化。

---

## 输出前自检

**结构性页面**：
- [ ] 所有 `[xxx]` 占位符已替换

**内容页**：
- [ ] viewBox = `0 0 1280 720`
- [ ] Chrome 类型与 narrative_purpose 匹配
- [ ] Action Title 字体是 `Songti SC,SimSun,serif`
- [ ] Action Title Y坐标：单行y=70，双行第一行y=56（若非极简 Chrome）
- [ ] 坐标严格按布局规划卡，无自行调整
- [ ] 所有卡片间距 ≥16px
- [ ] impact类页面有大数字 ≥60pt
- [ ] explain类页面有图示
- [ ] 强调卡内所有文字为 white
- [ ] 文字按保守字数换行（见上方字数参考表）
- [ ] 无禁用元素（饼图/3D/纯黑#000000/渐变/阴影）
- [ ] 有 data_points 的卡片已在右下角标注来源
- [ ] Callout 已渲染（callout_needed=true时）
- [ ] **[PPTX兼容] 文字内容中 & < > " 已转义**
- [ ] **[PPTX兼容] 无 `<marker>` 箭头，箭头已改用 `<polygon>`**
- [ ] **[PPTX兼容] 无 `<g transform="rotate(...)">` 或负数scale**
- [ ] **[PPTX兼容] 多行文字已用 `<tspan dy="...">` 或独立 `<text y="...">` 换行，无 `\n`**

---

## 输出

写入：`./workspace/slides/slide_[page_index补零两位].svg`

汇报：**"第[N]页：[page_type]·[narrative_purpose] — [title前15字] → slide_[NN].svg"**

---
