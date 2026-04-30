# Aham PPT 技能

一套对标麦肯锡/德勤标准的 AI PPT 制作技能，含完整八阶段流程 + 原生 PPTX 输出工具链。

> 📘 **Aham 是虚构的示例品牌。** 你可以直接使用本技能生成"Aham 风格"的 PPT，
> 也可以（推荐）将它替换为你自己的品牌。替换指引见本文档下方。
>
> 关于本技能的来源与脱敏说明，见 `ORIGIN.md`。

---

## 快速开始

### 1. 安装技能

将整个 `aham-ppt/` 目录放到你的 Claude 技能路径下。

**Claude Code 或 Claude 桌面版的标准路径**：
```
~/.claude/skills/user/aham-ppt/
```

**Claude.ai Web 的标准路径**：
```
/mnt/skills/user/aham-ppt/
```

### 2. 触发技能

在 Claude 对话中，说出以下任一触发词即可：

- 帮我做 PPT
- 做演示文稿
- 做一个汇报
- 根据这份资料做 PPT
- 做客户方案 PPT
- 制作幻灯片

技能会自动按八阶段流程推进，从规范加载到质检交付全程覆盖。

### 3. 准备素材

执行前请准备好：
- 需要转化为 PPT 的原始素材（文字、数据、图表、PDF 均可）
- 明确的受众（给客户老板 / 给内部管理层 / 给投资人？）
- 预期篇幅（10 页 / 30 页 / 50 页？）
- 交付时间（影响流程中每一步的深度）

---

## 换成你自己的品牌（4 步）

### Step 1：替换品牌元信息

编辑 `references/brand-spec/brand.md` 开头的 Brand 块：

```markdown
**Brand**: 你的品牌名
**Locale**: 你的主要语言环境
**Applicability**: 你的品牌调性描述
**Brand attributes**: 你的品牌属性关键词
```

### Step 2：替换主色和色阶

编辑 `references/brand-spec/tokens.css`：

```css
--blue-500: #你的主色;   /* 主品牌色 */
--blue-50:  #极浅色;
--blue-100: #很浅色;
/* ... blue-900 */
```

**推荐工具**：用 [Ant Design 色板生成器](https://ant.design/docs/spec/colors)
输入你的主色，会自动生成 9 档梯度。

### Step 3：替换字体栈（可选）

如果你的品牌用了不同字体，编辑 `tokens.css` 的字体变量：

```css
--ff-sans:  "你的标题字体", "Noto Sans SC", ...;
--ff-serif: "你的正文字体", ...;
--ff-mono:  "你的数字字体", ...;
```

### Step 4：搜索替换剩余的 "Aham" 字样

```bash
cd aham-ppt/
grep -rn "Aham\|aham" .
```

把出现的品牌名替换为你自己的品牌名即可。

---

## 目录结构

```
aham-ppt/
├── SKILL.md                      # 技能入口（YAML 头触发配置）
├── ORIGIN.md                     # 本技能的脱敏说明
├── README.md                     # 本文件
├── LESSONS.md                    # 24 个场景化经验索引（供人阅读）
│
├── assets/                       # 工具链代码
│   ├── README.md
│   ├── svg_to_pptx_wrapper.py    # 对外入口
│   └── svg_to_pptx/              # SVG → 原生 PPTX 工具链主体
│
└── references/                   # 方法论与规范
    ├── brand-spec/               # ★ 品牌视觉规范（替换这里的内容适配你的品牌）
    │   ├── brand.md              # 主规范（色彩/字体/禁用）
    │   ├── track-rules.md        # 四轨道分流规则
    │   ├── tokens.css            # CSS 变量（色值/字体栈）
    │   └── iconography.md        # 图标规范
    │
    ├── designer-rules.md         # 设计师执行规则
    ├── chart-impl.md             # 图表实现
    ├── coach-engine.md           # 教练引擎（能力自适应）
    ├── grid-system.md            # 网格系统
    ├── quality-audit-protocol.md # 质检协议
    ├── pptx-native-rules.md      # 原生 PPTX 输出规则
    │
    ├── phase-01.md ~ phase-08.md # 八阶段流程详细指引
    ├── layout-library.md         # 版式库总览
    ├── layout-impl-*.md          # 各版式类型的实现（7 个文件）
    └── svg-skeleton-*.md         # 各版式的 SVG 骨架模板（7 个文件）
```

---

## 八阶段流程

本技能的核心是这条八阶段流水线：

| # | 阶段 | 产物 |
|---|---|---|
| 1 | 规范加载 | 确认轨道 A，加载色值、字体、禁用清单 |
| 2 | 材料解析 | 从原始素材中提取关键信息、证据、数字 |
| 3 | 论点提炼 | 按麦肯锡金字塔结构提炼核心论点 |
| 4 | 叙事骨架 | 搭建 Ghost Deck（每页一句话的结论骨架） |
| 5 | 大纲版式 | 规划 Part 结构、每页版式类型 |
| 6 | 样稿确认 | 选 3-5 页做样稿，与用户对齐视觉方向 |
| 7 | 逐页设计 | 生成所有页的 SVG + 调用工具链转为 PPTX |
| 8 | 质检交付 | 按 QC 清单逐项扫描、修正、最终交付 |

详细指引见 `references/phase-01.md` ~ `phase-08.md`。

---

## 设计哲学（四个支柱）

本规范的四条核心原则：

1. **粗体排版** — 用字重建立层级，不用颜色
2. **可见网格** — 表格线、栏格、行是有意可见的
3. **克制色板** — 只有一个强调色，其余皆中性灰 + 语义色
4. **高信息密度** — 表格优于文字，数字优于形容词

**绝对禁用**：渐变 · 3D · 投影 · 纯黑 #000 · 第二装饰彩色 · 饼图 · 表格竖线 · emoji · 圆角 > 8px。

---

## 相关资源

- `ORIGIN.md` — 本技能的来源与脱敏说明
- `LESSONS.md` — 24 个场景化经验，供人工翻阅
- `references/brand-spec/brand.md` — 品牌规范完整文档
- `references/designer-rules.md` — 设计师执行细则

---

## 反馈与贡献

本技能为开放分发版本，欢迎修改、重组、二次开发。
如果你在使用中发现方法论缺陷或工具链 bug，欢迎通过任何渠道反馈。
