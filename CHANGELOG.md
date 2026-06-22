# Changelog 更新日志

本项目所有重要变更记录于此。

格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本遵循 [语义化版本 SemVer](https://semver.org/lang/zh-CN/)。

## [Unreleased]

## [2.1.0] - 2026-06-22 — 双档主题 + 工具链修复

### 新增
- **双档主题系统**：A 克制档 / B 现代专业档（默认 B）。共用内容与组件，仅切换封面/目录/章节模板与页眉皮肤；两档均坚持单一主色 + 中性灰，不引入多色体系。见 `references/theme-tiers.md`。
- **启动选档步骤**（SKILL.md Step 1.5）：规范加载后、解析材料前询问一次，回车默认 B。
- **图标与组件库**（`assets/components/`）：`icons.py`（~40 线性图标 + icon_circle/num_badge/num_ring）、`components.py`（泳道/蓝图/箭头/KPI/状态/设备屏/手机/占位框）、`themes.py`（A/B 封面/目录/章节/页眉模板）。
- 设计规则：**强调色语义** QC 项（禁无语义单点强调色）、真实照片**占位框**（禁 AI 图/网图）、**样张先行**。
- 内容方法论：一手材料优先、措辞分寸、show-don't-tell、脱敏固定步骤、流程先确认形态。见 `references/enhancements.md`。

### 修复
- **转换器文本宽度估算偏窄导致折行**（`assets/svg_to_pptx/drawingml_utils.py` 的 `estimate_text_width`）：窄字符 0.3→0.5、基准 0.55→0.62、mMwWOQ→0.82、CJK→1.02、整体 ×1.08。修复编号"01"、长英文串被 LibreOffice 拆行的问题。

### 变更
- 规范微调：放开"内容区线性单色图标"为 B 档允许项（原仅限导航/发送栏）。
- 建议产物写"版本目录"、页码用 ORDER 列表统一重排（见 enhancements.md）。

## [2.0.1] - 2026-06-21

### 新增
- 示例新增 3 种版式：**流程闭环**（E-03）、**VS 对照**（S-08）、**深色过渡**（T-01），示例增至 11 页。
- README 加「示例预览」图墙——11 页真实渲染截图（2× 高清），存 `assets/shots/`。
- `examples/render_shots.py`：用 Playwright/Chromium 把示例 SVG 渲染成 PNG（Inter/JetBrains 网络字体 + 系统 CJK）。

### 变更
- Action Title 字号统一为 24pt（32px）；品牌蓝点位置微调（与品牌字留清晰间距）。

## [2.0.0] - 2026-06-21

设计语言换血：从旧规范（McKinsey 风 · `#1677FF` 重蓝 · 衬线标题 · 描边大卡）
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

[Unreleased]: https://github.com/li599198347-svg/aham-ppt/compare/v2.0.1...HEAD
[2.0.1]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.0.1
[2.0.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v2.0.0
[1.1.0]: https://github.com/li599198347-svg/aham-ppt/releases/tag/v1.1.0
