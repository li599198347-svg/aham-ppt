# Layout Impl · 通用规范（画布/Chrome/卡片/字数表/版式选择参考）

> Phase 5 选版式时读取本文件的版式选择参考表。
> Phase 7 设计时读取本文件的Chrome模板和卡片规范。
> 坐标权威来源：grid-system.md（本文件的坐标已迁移至grid-system.md，此处仅保留模板）。

---

**品牌规范（颜色/字体/禁用规则）以 brand.md 为准，本文件只管「怎么画」。**

---

## 画布基础参数

```
viewBox：0 0 1280 720
页面背景：#FFFFFF
安全边距：左右各40px，上下各20px

Chrome 层次（每页固定）：
  顶部3pt品牌蓝线    y=0   h=3
  页眉区             y=3   h=27   （Section路径 + AHAM标识）
  页眉分割线         y=30
  Action Title区     y=36  h=58   （品牌蓝竖线 + 宋体-简Bold标题）
  AT分割线           y=94
  内容区             y=100 h=590  （各版式在此变化）
  页脚分割线         y=690
  页脚区             y=690 h=30   （来源 + 页码）
```

## 标准 Chrome 模板

```svg
<!-- 顶部品牌蓝线 -->
<rect x="0" y="0" width="1280" height="3" fill="#003D7A"/>
<!-- 页眉 -->
<text x="40" y="22" font-family="Microsoft YaHei,sans-serif"
      font-size="11" fill="#888888">[section_path]</text>
<text x="1240" y="22" text-anchor="end" font-family="Microsoft YaHei,sans-serif"
      font-size="11" font-weight="bold" fill="#003D7A">AHAM</text>
<line x1="40" y1="30" x2="1240" y2="30" stroke="#E2E2E2" stroke-width="0.5"/>
<!-- Action Title区 -->
<rect x="40" y="36" width="3" height="52" fill="#003D7A"/>
<text x="52" y="70" font-family="Songti SC,SimSun,serif"
      font-size="22" font-weight="bold" fill="#1A1A1A">[title 单行]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E2E2E2" stroke-width="0.5"/>
<!-- 页脚 -->
<line x1="40" y1="690" x2="1240" y2="690" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif"
      font-size="11" fill="#888888">来源：[source] · [date]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif"
      font-size="11" fill="#888888">[page_index] / [total_pages]</text>
```

**极简 Chrome（用于 impact / transition 类，更少装饰）**：

```svg
<!-- 不要顶部蓝线，不要 Action Title 竖线和分隔线 -->
<text x="40" y="40" font-family="Microsoft YaHei,sans-serif"
      font-size="10" fill="#AAAAAA" letter-spacing="2">[section_path]</text>
<text x="40" y="690" font-family="Microsoft YaHei,sans-serif"
      font-size="10" fill="#AAAAAA">来源：[source]</text>
<text x="1240" y="690" text-anchor="end" font-family="Microsoft YaHei,sans-serif"
      font-size="10" fill="#AAAAAA">[page_index]</text>
```

**内容区可用范围：x=40~1240，y=100~690，宽1200px，高590px**

---

---

# 版式 →  选择参考表

| narrative_purpose | 候选版式 | 首选条件 |
|---|---|---|
| **impact** | I-01 | 有震撼数字 + 强调元素为 metric |
| impact | I-02 | 核心宣言 / 引言类 |
| impact | I-03 | 对比反差 |
| impact | I-04 | 数字 + 细节支撑（3 条） |
| impact | I-05 | 紧迫性 / 时间窗 |
| **structure** | S-01 | 3 个并列要点 |
| structure | S-02 | 4 个并列要点 / 2×2 矩阵 |
| structure | S-03 | 时间/步骤序列 |
| structure | S-04 | 主从关系 |
| structure | S-05 | 2 个等权要点 |
| structure | S-06 | 因果关系 (6:4) |
| structure | S-07 | 顶部结论 + 底部 3 支撑 |
| structure | S-08 | 两方对比 |
| structure | S-09 | 6 个 KPI |
| structure | S-10 | 顶部结论 + 底部 2 支撑 |
| structure | S-11 | 顶部结论 + 底部 4 支撑 |
| structure | S-12 | 单卡铺满 |
| **explain** | E-01 | 图文结合 |
| explain | E-02 | 概念曲线 |
| explain | E-03 | 流程图 |
| explain | E-04 | 架构图 |
| **evidence** | V-01 | 多 KPI 看板 |
| evidence | V-02 | 单大图表 |
| evidence | V-03 | 时间趋势 |
| evidence | V-04 | 双图对比 |
| **transition** | T-01 | 情绪引言 / 深色底 |
| transition | T-02 | 白底宣言 |
| transition | T-03 | 章节承接 |
| **action** | A-01 | 下一步三步 |
| action | A-02 | 二选一决策 |
| action | A-03 | 责任矩阵 |

---

# 卡片内容元素规范（沿用原规格）

**卡片内边距**：16px  
**卡片标题**：y=卡片y+28，微软雅黑 Bold 14px，#003D7A  
**Bullets 起始 y**：卡片y+52，间距 24px  

```svg
<rect x="[cx+16]" y="[itemY-10]" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="[cx+26]" y="[itemY]" font-family="Microsoft YaHei,sans-serif"
      font-size="13" fill="#333333">[bullet文字]</text>
```

**大数字显示**：按 intent_visual_instruction 的字号执行，默认 48px，impact 类 80-180px。

**数据来源标注**（右下角）：
```svg
<text x="[cx+cw-16]" y="[cy+ch-10]" text-anchor="end" font-size="9" fill="#AAAAAA">
  来源：[source]，[date]</text>
```

---

# 文字换行保守字数表

| 卡片宽度 | 最多汉字/行（13px正文） |
|---------|---------------------|
| 1200px | 46字 |
| 720px | 27字 |
| 656px | 25字 |
| 594px | 22字 |
| 464px | 17字 |
| 408px | 15字 |
| 380px | 14字 |
| 277px | 10字 |
| 244px | 9字 |

---
