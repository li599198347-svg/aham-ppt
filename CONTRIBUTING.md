# 贡献指南

欢迎修改、重组、二次开发本技能（开放分发，MIT）。

## 改动约定
- **视觉/规范以 `references/brand-spec/` 为权威**：色值、字体、版式只从 `brand.md` / `tokens.css` 查表，不在其它文件写死色值。取值同步自设计源 [aham-ui](https://github.com/li599198347-svg/aham-ui)。
- **方法论与视觉分离**：八阶段流程、Action Title、探测场景等是方法论；颜色/字体/卡片是视觉。改一类不应顺手改另一类。
- 改示例后跑 `python3 examples/build_examples.py` 重新生成 8 页 SVG + `preview/deck.html`；如需验证 PPTX，用 `assets/svg_to_pptx_wrapper.py` 转换并确认 0 跳过。
- 提交走分支 + PR，提交信息沿用仓库既有风格（`feat:` / `fix:` / `docs:` / `chore:`）。

## 发版流程（SemVer + Keep a Changelog）
1. 定版本号：破坏性=MAJOR、向后兼容新功能=MINOR、修复=PATCH。
2. 把 `CHANGELOG.md` 的 `[Unreleased]` 内容移入 `## [X.Y.Z] - YYYY-MM-DD`，按 新增/变更/修复/移除 分组，补底部版本链接。
3. 提交推送后建 Release（自动打 tag）：
   ```sh
   gh release create vX.Y.Z --title "vX.Y.Z — 一句话主题" --notes-file <notes.md> --latest
   ```
4. 确认 README 的 Release 徽章动态显示新版本；**社交封面绝不印版本号**（版本由徽章动态显示）。
