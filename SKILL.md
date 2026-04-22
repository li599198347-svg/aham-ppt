---
name: aham-ppt
description: >
  全流程AI制作PPT演示文稿技能，对标麦肯锡/德勤顶级咨询公司标准（轨道 A · Brand）。
  当用户说"帮我做PPT""做演示文稿""做一个汇报""根据这份资料做PPT"
  "做客户方案PPT""制作幻灯片"时立即触发。即使只有一句话需求也触发。
  八阶段模块化流程：规范加载→材料解析→论点提炼→叙事骨架→大纲版式→样稿确认→逐页设计→质检交付。
  内置能力自适应教练机制，无论用户专业水平高低，均引导至及格以上输出。
  注意：本技能用于 PowerPoint / pptx 输出；SVG/HTML 版本见 ppt-svg 技能。
---

# Aham PPT 技能 — 轨道 A · Brand

---

## Step 1 · 加载规范（优先级顺序）

**优先级 1（主路径）：**
```
view references/brand-spec/brand.md
view references/brand-spec/track-rules.md
```
重点提取轨道 A（Brand）中 PPT 相关内容：Action Title 规则、版式、色值、字体。

**优先级 2（PPT 专项规范）：**
```
view references/designer-rules.md
view references/phase-01.md  ← 规范加载阶段
（按执行阶段依次读取对应 phase-XX.md）
```

**优先级 3（降级兜底）：**
使用本文件末尾「降级基线」。

加载 pptx 文档生成技能：
```
view /mnt/skills/public/pptx/SKILL.md
```

---

## Step 2 · 八阶段执行

按 references/phase-01.md ~ phase-08.md 中的详细指引执行，此处仅列阶段名称：

1. 规范加载（本 Step 1）
2. 材料解析与关键信息提取
3. 核心论点提炼（麦肯锡金字塔结构）
4. 叙事骨架搭建（Ghost Deck）
5. 大纲与版式规划
6. 样稿确认（与用户对齐）
7. 逐页设计输出
8. 质检交付（QC 清单）

---

## 降级基线（无法读取外部规范时）

> ⚠️ 未找到外部规范，使用内嵌基线（PPT 轨道 A）。

**轨道 A · PPT 核心规则：**
- 主色：`#1677FF`
- Action Title：每页必须是完整结论句（非主题词），白底深色文字 + 左侧 3pt `#1677FF` 竖线
- 字体：Source Han Sans SC（标题/UI）+ Source Han Serif SC（正文段落，仅文档使用）
- 标题层级：用字重区分，≤ 22pt（封面 32–40pt）
- 禁用：纯黑 #000 / 渐变 / 3D / 投影 / 第二装饰彩色 / emoji / 饼图 / 独立图例
- 禁用词：赋能·颠覆·生态·闭环·最佳实践·全链路·一站式·显著·大幅
- 数字格式：货币 ¥1,200,000；百分比 37.5%；日期 YYYY-MM-DD；数字用等宽字体
- 每页一个核心结论，表格优于文字堆砌
