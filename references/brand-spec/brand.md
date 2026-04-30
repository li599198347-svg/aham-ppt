# Aham Design System

> **🔒 v1.0 — 已锁定基线** · 2026-04-20
> 所有规范、tokens、组件卡片及 3 套 UI Kit 均已通过评审。后续变更走 v1.1 分支，不直接改动 v1.0。
>
> **未交付的外部素材（不阻塞锁定，后续回填）**：
> - [ ] 完整字体包 — 思源黑体 Regular/Medium/Bold、思源宋体 Regular/SemiBold、Roboto Mono Regular/Medium（本地 woff2）
> - [ ] Logo 变体 7 个 — 反白 / 单色黑 / 单色白 / 纯图标 / 方版 / 竖版 / SVG 源文件
> - [ ] 平台现有产品截图 `shot1–shot5.png`（用于像素对齐重建）
> - [ ] [示例业务实景照片] 5–8 张（用于官网 hero、产品页、业务场景等）

**Brand**: Aham（示例品牌 · Demo Brand）
**Locale**: 主要场景为 zh-CN（简体中文），品牌名使用拉丁字母。
**Applicability**: 本规范适用于严肃 B2B 场景，追求严谨、克制、工程化、可靠、懂行的视觉与文字表达风格。
**Brand attributes**: 严谨 (Rigor) · 克制 (Restraint) · 工程化 (Engineered) · 可靠 (Dependable) · 懂行 (Domain-aware)

> 📘 **使用者说明**：Aham 是一个虚构的示例品牌，用于承载这套规范的完整演示。
> 你可以将本规范作为模板，替换品牌名、主色、字体栈等关键 token，适配你自己的品牌。
> 具体替换点见项目根目录的 `README.md`。

## Products / surfaces represented

Aham's design system is **multi-channel** with several parallel sub-specs that share brand basics but diverge per surface. Three "tracks" of UI exist:

| Track | Primary color | Border-radius | Where used |
|---|---|---|---|
| **Brand V2.0** — corporate identity, deliverables | `#1677FF` | `0/2/4 px` (sharp) | Word/Excel/PPT, contracts, business cards, website |
| **Prototype (品牌版) V1.0** — standalone Demo prototypes | `#1677FF` | `0/2/4 px` (sharp) | AI-generated demos / prototypes for prospects |
| **Aham Platform V1.0** — Ant-Design-5 based platform | `#1677FF` | `6/4/8 px` | Customer projects built ON the Aham platform |
| **Field Design V1.0** — on-site mobile/PDA & industrial Pad | `#1677FF` | `2/4/6 px` | PDA scanners, ruggedized tablets for on-site operators |

> ✅ 品牌蓝统一为 `#1677FF`（`--blue-500`），所有轨道（Brand / Prototype / Platform / Field）共用同一主色，无需区分。

## Sources (originals on disk)

All design rules below are extracted from these uploaded source documents:

- `uploads/Aham DesignV2.0.md` — master brand & design spec (1477 lines)
- `uploads/原型设计规范 V1.0.md` — Brand-version prototype spec
- `uploads/原型设计规范 - Aham 平台版 V1.0.md` — Platform (Ant 5) prototype spec
- `uploads/Aham-Field-Design-System-V1.0.md` — Field / on-site device spec
- `uploads/logo.png` — primary logo (provided)

---

## CONTENT FUNDAMENTALS

**Voice**: A senior consultant with 15 years' experience speaking — professional, direct, restrained-emotional, uses numbers instead of adjectives. **Tone shifts by channel** but never warm-fuzzy or playful.

| Channel | Tone |
|---|---|
| Proposal body | Rigorous, third-person — "调研显示核心计划模块从未正式启用。" |
| Executive summary | Decisive, recommendation-led — "我们建议分三期实施新系统。" |
| Client email | Polite, short, action-oriented — "已将修订版发您，请于周五前反馈。" |
| Contract / quote | Legal, no decoration — "本报价有效期 30 日。" |
| Software UI copy | Short, imperative, no exclamation marks — "保存"、"确认删除该工单？" |
| Error messages | Cause + remedy — "网络中断，请检查连接后重试。" |

**Person**: 第三人称为主 (third-person dominant); first-person plural "我们" only in executive summaries / recommendations. Never "我"/"I".

**Casing**: Brand name always written `Aham` (not AHAM, not aham). Chinese name is `Aham` or full `Aham（示例品牌）`. UI labels ≤ 4 Chinese characters; button text ≤ 6 characters.

**Mixed-script spacing rules** (strict):
- Half-width space between Chinese and Latin: `使用 A 系统` ✓ — never `使用A系统`
- Half-width space between Chinese and digits: `上线 45 天` ✓
- **No** space between digits and unit: `30%`、`5kg`、`¥1,200`
- Acronyms: full term on first mention, then abbreviated.

**Banned vocabulary** (never appears in deliverables):
> 赋能 · 颠覆 · 生态 · 闭环 · 最佳实践 · 全链路 · 一站式 · 数字孪生 · 智慧 XX · AI+ · 元宇宙 · 无缝 · 极致 · 唯一 · 行业第一 · 显著 · 大幅 · 明显 · 考虑 · 可能 · 或许 · 加强 · 完善 · 优化 · 积极推进

Replace with **specific, quantified statements**: not "显著提升" but "提升 37%"; not "全面赋能" but "覆盖计划、执行、追溯的 8 个模块".

**Emoji**: ❌ Never. Status uses Lucide icons + symbol+text combos (`● 合格` / `▲ 预警` / `✕ 异常`).

**Number formatting**: Currency `¥1,200,000`; percentages 1-decimal `37.5%`; ranges `15%–20%`; dates `YYYY-MM-DD`; times `HH:mm` or `YYYY-MM-DD HH:mm:ss`. **All numbers shown in monospace** (`Roboto Mono` / `JetBrains Mono`). Every figure must cite source + time.

**Recommendation pattern** — every recommendation contains all four:
> 【具体行动】+【量化目标】+【责任方】+【时间节点】

**Vibe**: Quiet authority. White paper, not landing page. The reader should feel they are reading a McKinsey-grade deliverable for a serious B2B audience.

---

## VISUAL FOUNDATIONS

**Design philosophy** (four pillars):
1. **粗体排版** (Bold typography) — hierarchy via weight, not color.
2. **可见网格** (Visible grid) — table lines, columns, and rows are deliberately seen.
3. **克制色板** (Restrained palette) — exactly one accent color; everything else is neutral.
4. **高信息密度** (High information density) — tables over prose, numbers over adjectives.

**Single-accent rule**: Across the entire system, **one accent color only** — `#1677FF` (Brand) or `#1677FF` (Platform). All other color is grayscale + semantic-status only.

### Color
- **Brand blue**: `#1677FF` (V2.0, prototype, field). 9-step scale `blue-50` → `blue-900`.
- **Platform blue**: `#1677FF` (Ant 5 / Aham platform). Never substituted with brand blue.
- **Neutrals (ink scale)**: `#FFFFFF` → `#FAFAFA` → `#F5F5F5` → `#E2E2E2` → `#CCCCCC` → `#BBBBBB` → `#888888` → `#555555` → `#333333` → `#1A1A1A` → `#0A0E14`. **Never pure black `#000000`**.
- **Semantic** (always paired with symbol): success `#2E6B3E`, warning `#8A5A00`, danger `#9C2B2B`. Light backgrounds `#EDF3EE / #F7EFE0 / #F5E6E6`.
- **Accent dots** (cyan `#20C0C0`, violet `#A050FF`): only on brand promo materials (website hero), max 5% area, **never in deliverables or UI**.

### Typography
- **Sans (titles, UI, table headers)**: Source Han Sans SC → Noto Sans SC → PingFang SC → Microsoft YaHei → sans-serif.
- **Serif (body paragraphs in docs only)**: Source Han Serif SC → Songti SC → SimSun → serif. *Field & UI tracks: no serif at all.*
- **Mono (all numbers, IDs, codes, money, time)**: Roboto Mono / JetBrains Mono / SF Mono / Courier New. Mandatory for every number on screen.
- **Weights**: Regular / Medium / Bold. **Light is forbidden**; Heavy only on covers.
- Hierarchy is by *weight*, not color; titles ≤ 22pt in docs, 32–40pt only on covers.

### Spacing
8 pt baseline grid: `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 px`. Field track contracts to `4 / 8 / 12 / 16 / 24` only.

### Borders & dividers
1 px solid `#E2E2E2` is the universal divider. **No `box-shadow` for separation** — use a 1 px hairline. Tables: keep horizontal lines; **all vertical lines forbidden**.

### Corner radius (intentional fragmentation)
- Brand / prototype / field: `0 / 2 / 4 / 6 px` (sharp; never > 6).
- Platform (Ant 5): `2 / 4 / 6 / 8 px` (Ant defaults).
- **Never** `> 8 px`. No 50%-rounded avatars — use `4 px` square-rounded.

### Shadows (almost never)
"Use a 1 px line before reaching for a shadow." Allowed only:
- BottomSheet/Toast: `0 2px 8px rgba(0,0,0,.08)`
- Dialog: `0 4px 16px rgba(0,0,0,.12)`
- Mobile elevation: `0 2px 8px rgba(0,0,0,.04)`
- ❌ No card hover shadows, button shadows, glow halos.

### Backgrounds
Always white `#FFFFFF` or near-white `#FAFAFA`. **No** gradients, no tinted backgrounds, no warm grays (`#F4F1EF` is explicitly banned), no glassmorphism, no decorative patterns. Big-screen dashboard is the only deep-blue exception (`#02081C`, no gradients/particles).

### Animation
**Minimal**. Default transition `0.15s ease`. Hover = `filter: brightness(1.05)`; pressed = `filter: brightness(0.95)`. **No** number-roll-ups, card float, pulse, skeleton shimmer, bouncy scale, hero parallax. Loading is a single spinning Lucide `loader-2` — no percentages.

### Hover & press states
- Hover: lighter background (`#F5F5F5`) or brand blue text. **Never** opacity changes.
- Press: darker brand color (`#0958D9` for `#1677FF`). No scale-down.
- Disabled: bg `#F5F5F5`, text `#BBBBBB`, no border.
- Focus: 2 px brand-blue outline + 2 px lighter halo (Ant style only on Platform).

### Cards
White background, **1 px solid `#E2E2E2` border, 4 px radius, no shadow.** Padding `12 px` (field) / `16 px` (web). Page background `#FAFAFA` so cards "lift" via contrast, not via shadow.

### Imagery
Real, domain-authentic scenes relevant to your industry (equipment, operators, work environments) — **never** stock-photo handshakes, never AI-rendered generic imagery. Cool, low-saturation, professional tone. Apply 10% overlay of `#041D48` so all photos read as one family. When real images are unavailable, use **labeled placeholders** (`[待替换·示例业务实景]`), never invent.

### Illustrations
Isometric line + single-fill in brand-blue scale only. No cartoons, no Q-versions, no 3D renders.

### Transparency & blur
Used **only** for modal masks (`rgba(0,0,0,.5)`) and Toast backgrounds (`rgba(26,26,26,.92)`). No glass/blur effects in cards, headers, or backgrounds.

### Layout rules
- Web admin: top bar `56 px` (white, 3 px brand-blue top accent line) + side nav `220 px` (white, no color) + content `#FAFAFA`.
- Field PDA: status `24 px` + topbar `56 px` (brand-blue) + bottom CTA `48 px`.
- Field Pad: AppBar `56 px` (brand-blue), no Hero on inner pages, operation area ≥ 87%.
- **Hero banners forbidden** on inner pages across all surfaces; allowed only on landing/home & login.

### Iconography vibe
Lucide line icons, 1.5–2 px stroke, single color, never multi-color, never 3D/skeuomorphic, never emoji. See `ICONOGRAPHY.md`.

---

## File index

| File | Purpose |
|---|---|
| `README.md` | This file — context, content, visual foundations. |
| `colors_and_type.css` | All design-token CSS variables for both Brand & Platform tracks. |
| `ICONOGRAPHY.md` | Icon-system rules, libraries, examples. |
| `SKILL.md` | Cross-compatible skill manifest for Claude Code. |
| `assets/` | Logo, photos, illustrations, raw brand assets. |
| `fonts/` | Webfont loaders + reference for Sans/Serif/Mono families. |
| `preview/` | HTML cards rendered in the Design System tab. |
| `ui_kits/brand/` | Brand-V2.0 prototype UI kit (`#1677FF`, sharp corners). |
| `ui_kits/platform/` | Aham Platform UI kit (Ant 5 + `#1677FF`). |
| `ui_kits/field-pda/` | Field PDA mobile kit. |
| `SKILL.md` | Agent-Skills-compatible manifest (cross-Claude-Code). |
| `CONFLICTS_AND_UNIFIED_RULES.md` | Reconciliation of the 4 source specs into 4 tracks (A/B/C/D). |

## Caveats / asks for the user
- **Fonts**: Source Han Sans/Serif and Roboto Mono / JetBrains Mono are loaded from Google Fonts (Noto Sans SC / Noto Serif SC / Roboto Mono / JetBrains Mono). If you need bundled `.ttf`/`.woff2` for offline / PDF embedding, please upload the originals.
- **Platform screenshots** (`assets/shot1.png` … `shot5.png` referenced in the platform spec) were *not* provided. The Aham-Platform UI kit is reconstructed from the spec text only — please attach the screenshots if you want pixel-level fidelity.
- **Logo variants** (icon-only, reverse, mono) were not provided. Only `assets/logo.png` (primary horizontal) is available; we recommend producing the full 7-variant pack listed in V2.0 § 4.2.
