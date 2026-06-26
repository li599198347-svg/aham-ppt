# Changelog 更新日志

本项目所有重要变更记录于此。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本遵循 [语义化版本 SemVer](https://semver.org/lang/zh-CN/)。

## [Unreleased]

## [2.4.0] - 2026-06-26 — 更稳的流程（防跳步）+ 更准的版式（去重 · 单一决策表 · 硬门禁）

> 治两大体验问题：Claude **跳步骤** 与 **版式选不对**。不改对外触发与产出视觉，核心八阶段方法论不变。

### 新增
- **选版式单一权威表**：`layout-library §版式选择速查` 设为唯一决策表 + 标注「首选核心集」（治选项过载）；`phase-05` 删内联映射、改为引用。
- **数据强制图表化 = 硬门禁（规划/设计/质检三环）**：Phase 5 布局规划卡每页必勾「版式自检」（≥3 条数据→必用 charts / 非数据页先判结构图 / 主角↔版式匹配）；Phase 7 设计前门禁加同款拦截；Phase 8 新增 `L4.5 版式合规`（数据被文字化 = ERROR）。
- Phase 7 出片前必声明"已加载 svg-skeleton + grid-system、坐标照抄不自算"。

### 变更
- **README 重排**：改为"为什么做 / 定位 / 八步法 / 样式与示例 / 使用方法 / 更新记录 / 关于"线性结构；删技术目录树与冗余预览（图墙收为 6 张），篇幅减半。
- **入口铁律（治"跳步骤"）**：`SKILL.md` Step 2 从"列阶段名"改为 **"逐阶段加载 + 卡点等待 + 不可跳步 + 进度可见"** 的强制循环；8 个 phase 顶部"可插拔模块"→"必经一步（不可跳过/合并）"。经对抗验证补漏：进度行 `【N/8】` 下沉到每个 phase 文件顶部；明确 **Phase 1 ≠ Step 1**（受众卡/完成卡不被"已加载文件"吞掉）；phase-05 补顶部 `强制等待锚点`。

### 修复
- 出片/质检阶段不再用红绿染 KPI / 大数字（S-09、I-05 改墨色，状态靠点+文字双通道）。
- 修孤儿 **T-02**：补"白底大字宣言/金句"选择路径（原先零路径指向）。
- **HERO 家族统一命名**（S-07 阶梯递进→HERO-3，选择速查三行收一）。
- `designer-rules` 路径A 的封面/目录/章节改走 `themes.py`，删除与之打架的旧 cover→I-01 映射；SPC 系不再谎称"骨架在 common.md 末尾"。

### 移除
- 删重复版式：**I-02**（→T-01）、**I-03**（→S-08）、**V-01**（→S-09）；删 **Ch 伪系**（数据图表归 V 系 + `charts.py`）。
- 版式库：声明 37→**34 ID**，骨架实存 **31 个**（i3 s12 e4 v3 t3 a3 g3）。

## [2.3.0] - 2026-06-26 — 仓库清理：去悬空引用 / 退役影子层 / 删死代码 / 规范单一源

> 工程与规范层清理，**不改变技能的对外行为与产出视觉**；核心八阶段引擎保持不变。

### 修复
- 修正 **9 处**指向不存在文件 `aham-ui-office.md` 的悬空引用 → 改指 `brand.md §7` + `tokens.css §10`（取值唯一事实源）。
- 出片/质检阶段不再教用衬线"宋体-简"与"顶部蓝条 / Action Title 蓝竖线"（违 brand 北极星，照做会被 Phase 8 判 ERROR）：`phase-06/07/08` 统一无衬线 + 无蓝竖线。
- Action Title 字号统一 **32px**（双行 22px）；删除 `designer-rules` 与 `grid-system §八` 冲突的字数表（字数表唯一源 = `grid-system §八`）。
- 图表配色去红绿：瀑布正负改灰阶 + 符号、甘特去蓝灰多色混用；KPI 数值不再染红绿（V-01 骨架数值改墨色，状态靠点 + 文字）。
- 修正 `designer-rules` 自相矛盾（"禁写死色值"却内置色表）、伪造的 brand §2.3 引文、过时的 brand 结构索引；T-01 深色页去游离钢蓝 `#4A6680`。
- 全仓脱敏真实项目名；修补 `layout-impl.md` / `svg-skeleton.md` 单数断链与 SPC/G 系→文件映射例外。

### 变更
- **规范单一事实源化**：PPTX 兼容雷区唯一源 = `designer-rules`；字数表 = `grid-system §八`；节奏阈值 = `layout-library §节奏约束`；版式坐标 = `grid-system`；其余文件改为引用而非各写一份。
- **视觉档接线**：`phase-05/07` 显式按 `theme` 调用 `themes.py`（A/B→cover/toc/section/chrome；C→cover_dark/section_dark/quote_dark），兑现选档对产物的影响。
- **C 高表现力档正式登记**：`brand.md §2.1` 登记 `#1C1C1C` 为唯一非纯白底例外（限封面/章节/金句），`tokens.css §10` + `quality-audit` 收录 C 档深色 ramp。
- `iconography` 回写 v2.1"内容区线性图标"为 B/C 档例外；Phase 1 完成卡记录 deck_mode/output_format/theme；Phase 3→4 反对意见链路补专家模式回退（取受众卡"主要顾虑"）。

### 移除
- 退役整套影子版式层 `references/layout-impl-*.md`（7 个，与 `svg-skeleton-*` 重复且坐标漂移；坐标真源是 `grid-system`）。
- 删除 `references/enhancements.md`（v2.1 增量已并入 `designer-rules` / `phase-02` / 组件代码）。
- 工具链死代码：`pptx_cli.py` / `pptx_discovery.py`（无人调用的第二入口）、切换动画死分支（缺失模块 `pptx_animations`）、失效的 `config` / `project_utils` import、死函数 `get_element_opacity` / `num_badge` / `num_ring`。
- 一次性发版脚本移出 `examples/` → `tools/`（`article_figures.py` / `social_banners.py`），去掉硬编码 `~/Desktop` 输出路径。
- 旧 demo `examples/Aham-PPT-Demo.pptx`、散落的 `.DS_Store`。

## [2.2.0] - 2026-06-26 — C 高表现力档 + 数据图表组件 + 去对标

### 新增
- **C · 高表现力档**：A/B 基础上新增深色重音页（`#1C1C1C`）+ 超大 mono 数字 + 图表占版面，面向路演/竞标/重点客户；深色模板 `cover_dark / section_dark / quote_dark`（`themes.py`）。视觉档由 A/B 两档扩为 **A/B/C 三档**。
- **数据图表组件库** `assets/components/charts.py`：9 类（柱/横柱/折线/瀑布/漏斗/甘特/子弹/堆叠/坡度），一行调用、brand §7.5 合规、转换实测可编辑。
- **防平淡规则链**：数据强制图表化 + 图形化占比下限 + 防平淡审计（`phase-04/05`、`chart-impl`、`quality-audit-protocol`、`designer-rules`）。

### 变更
- 文案去除“对标麦肯锡/德勤”“咨询级”等对标式描述，统一为“克制”定位；八阶段“麦肯锡金字塔”→“金字塔原理”。
- 重做 banner（`social-preview` · “三档风格 · 八阶段流程 · 原生 PPTX”）；README 加「🆕 三档视觉风格」节 + C 档封面 + A/B/C 对比；Pages 同步。

## [2.1.0] - 2026-06-22 — 双档主题 + 工具链修复

### 新增
- **双档主题系统**：A 克制档 / B 现代专业档（默认 B）。共用内容与组件，仅切换封面/目录/章节模板与页眉皮肤；两档均坚持单一主色 + 中性灰，不引入多色体系。见 `references/theme-tiers.md`。
- **启动选档步骤**（SKILL.md Step 1.5）：规范加载后、解析材料前询问一次，回车默认 B。
- **图标与组件库**（`assets/components/`）：`icons.py`（~40 线性图标 + icon_circle/num_badge/num_ring）、`components.py`（泳道/蓝图/箭头/KPI/状态/设备屏/手机/占位框）、`themes.py`（A/B 封面/目录/章节/页眉模板）。
- 设计规则：**强调色语义** QC 项（禁无语义单点强调色）、真实照片**占位框**（禁 AI 图/网图）、**样张先行**。
- 内容方法论：一手材料优先、措辞分寸、show-don't-tell、脱敏固定步骤、流程先确认形态。

### 修复
- **转换器文本宽度估算偏窄导致折行**（`assets/svg_to_pptx/drawingml_utils.py` 的 `estimate_text_width`）：窄字符 0.3→0.5、基准 0.55→0.62、mMwWOQ→0.82、CJK→1.02、整体 ×1.08。修复编号"01"、长英文串被 LibreOffice 拆行的问题。

### 变更
- 规范微调：放开"内容区线性单色图标"为 B 档允许项（原仅限导航/发送栏）。
- 建议产物写"版本目录"、页码用 ORDER 列表统一重排。

## [2.0.1] - 2026-06-21

### 新增
- 示例新增 3 种版式：**流程闭环**（E-03）、**VS 对照**（S-08）、**深色过渡**（T-01），示例增至 11 页。
- README 加「示例预览」图墙——11 页真实渲染截图（2× 高清），存 `assets/shots/`。
- `examples/render_shots.py`：用 Playwright/Chromium 把示例 SVG 渲染成 PNG（Inter/JetBrains 网络字体 + 系统 CJK）。

### 变更
- Action Title 字号统一为 24pt（32px）；品牌蓝点位置微调（与品牌字留清晰间距）。

## [2.0.0] - 2026-06-21

设计语言换血：从旧规范（`#1677FF` 重蓝 · 衬线标题 · 描边大卡）
全量迁移到 **Aham UI v6.1**（Claude desktop 气质 · 冷色的纸 · 蓝是点缀）。
生成的 PPT 视觉彻底改变；八阶段方法论、触发词、调用方式保持不变。

### 变更
- 主色 `#1677FF` → `#336EE8`，且蓝降为**点缀**——无顶部蓝条、绝不铺底（「蓝若第一眼注意到就超标」）。
- 中性体系改为三层灰 `#FFFFFF` / `#F3F3F3` / `#E7E7E7` + 墨四级 `#262626` / `#6E6E6E` / `#9B9B9B` / `#C4C4C4`（禁纯黑 `#000`）。
- 字体改为**单一无衬线** Inter / 微软雅黑（禁衬线），数字一律等宽 mono JetBrains Mono / Consolas。
- 卡片**无边框无阴影**；分块靠留白 + 细横线；选中 / 强调 = 扁平灰，非蓝。
- 状态 = **6px 点 + 文字**；表格只横线、数字右对齐 mono；图表灰阶 + **一个**蓝高亮。
- Action Title 改为无衬线 bold（24pt / 32px），去掉左侧蓝竖线与衬线。
- `track-rules` 重构为四介质轨（网页 / 应用 / Office / 邮件），明确**本技能 = Office 轨 · PPT 子模型**。

### 新增
- `examples/`：8 页密集示例（封面 / KPI 看板 / 方案选型 / 趋势 / 路线图 / 大数字 / 三层架构 / 2×2 矩阵）。
- `examples/build_examples.py`：示例生成器，一键产出 8 页 SVG + 浏览器预览 `preview/deck.html`。
- 示例转 PPTX 工具链回归：8/8 通过、0 跳过、原生可编辑。

### 移除
- 旧视觉件：深蓝强调卡、浅蓝 Callout、描边白卡、顶部 3pt 蓝条、衬线标题、状态色块 / 红黄绿灯、图表多色。
- 全仓库旧视觉 token（`#1677FF` / `#1A1A1A` / `#E2E2E2` / 思源宋体 / Roboto Mono / `var(--brand-primary)`）清零。

## [1.1.0] - 2026-04-30

### 修复
- 修复版式命名冲突、品牌色硬编码等 8 项问题。

[Unreleased]: https://github.com/li599198347-svg/aham-ppt/compare/v2.4.0...HEAD
[2.4.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.4.0
[2.3.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.3.0
[2.2.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.2.0
[2.1.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.1.0
[2.0.1]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.0.1
[2.0.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.0.0
[1.1.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v1.1.0
