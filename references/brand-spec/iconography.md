# Iconography — Aham

## One library, one style

Across all Aham surfaces there is exactly **one icon system**:

> **Lucide** — outline (line) icons, 2 px stroke, rounded caps, single-color, on a 24×24 grid.

The Platform track may also call them `@ant-design/icons` (the Ant 5 version of essentially the same outlined set). On the Brand / Prototype / Field tracks, **Lucide is the only library**.

Why one library: mixing libraries is the #1 way that AI-generated demos start looking inconsistent. Pick Lucide. Stay there.

## CDN (recommended for prototypes)

```html
<!-- Lucide: vanilla -->
<script src="https://unpkg.com/lucide@latest"></script>
<i data-lucide="scan-line"></i>
<script>lucide.createIcons();</script>

<!-- Or as inline SVGs from https://lucide.dev/icons/ -->
```

For Ant-Design / Platform projects:
```bash
npm i @ant-design/icons
```

## Sizes

| Context | px |
|---|---|
| Inline in tables | 14 |
| Inside buttons | 16 (web) / 18 (field) |
| Body text inline | 20 |
| Nav / topbar | 22 |
| Tab bar | 24 |
| Card-head / KPI | 24–32 |
| Mobile feature/Hero | 36 (PDA) / 48 (Pad) |

## Color rules

- **Default** — inherit text color (`#333333` body / white on dark bars).
- **Active / interactive** — `#1677FF` (brand) or `#1677FF` (platform).
- **Status icons** — match the semantic color (`#2E6B3E` / `#8A5A00` / `#9C2B2B`).
- **Stroke** — exactly 2 px (Lucide default). Field UI may go 1.5 px on Pad.
- **Fill vs outline** — pick *outline only*. Filled variants are reserved for "selected/active" tab indicators.

## Status mapping (replaces emoji)

The system explicitly bans emoji in UI. Use these Lucide names instead:

| Meaning | Lucide name |
|---|---|
| Signal | `signal` |
| Wi-Fi | `wifi` |
| Battery full / low | `battery-full` / `battery-low` |
| User | `user` |
| Logout | `log-out` |
| Scan barcode | `scan-line` |
| Search | `search` |
| Refresh | `refresh-cw` |
| Delete | `trash-2` |
| Confirm / pass | `check` / `check-circle` |
| Cancel / fail | `x` / `x-circle` |
| Warning | `alert-triangle` |
| Info | `info` |
| Loading | `loader-2` (rotate) |
| Filter | `filter` |
| Settings | `settings` |
| More | `more-horizontal` |
| Back | `chevron-left` |
| Drop down | `chevron-down` |
| Print | `printer` |
| Export | `download` |
| Edit | `pencil` |
| Add | `plus` |

## Hard bans

❌ **Emoji** in any production UI (📊 🚀 ✨ 🔋 …)
❌ **Multi-color** icons
❌ **3D / skeuomorphic / Fluent-3D / Icons8-3D** style
❌ **Filled + outline mixed** in one screen
❌ Stacking icons on **colored background pills** (`bg-blue-light` rounded squares were explicitly retired)
❌ Decorative icons with no meaning — every icon must convey information
❌ Font Awesome legacy / iconfont multi-color packs
❌ Self-drawn SVGs that diverge from Lucide's geometry

## Iconography vs typography for status

For status badges you must use the **double channel**: a textual symbol (●▲✕→○) **plus a label**, color-coded. The Lucide icon is optional; the symbol+text is mandatory.

Example:
```
●  合格      ▲  预警      ✕  异常      →  进行中      ○  待检
```

## Logo as icon (favicon, app icon)

Use `assets/logo.png` (full lockup). For 24 × 24 favicons, please supply a graphic-mark-only SVG — we don't have one yet (see README caveats).

## Substitutions flagged to user

We are using **Lucide** as documented in the Aham V2.0 spec — no substitution required. The spec also mentions Tabler / Feather / IBM Carbon / Material Symbols as acceptable alternates if a particular glyph is missing from Lucide; cross-check before introducing a new library.
