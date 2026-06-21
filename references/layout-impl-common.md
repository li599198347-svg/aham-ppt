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

Chrome 层次（每页固定 · 无顶部蓝条）：
  页眉区             y=0   h=32   （Section路径 + 品牌标识 + 蓝点）
  页眉分割线         y=32          stroke=#E7E7E7
  Action Title区     y=32  h=62   （无衬线 bold 标题 · 无蓝竖线）
  AT分割线           y=94
  内容区             y=100 h=590  （各版式在此变化）
  页脚分割线         y=690
  页脚区             y=690 h=30   （来源 + 页码 mono）
```

## 标准 Chrome 模板

```svg
<rect x="0" y="0" width="1280" height="720" fill="#FFFFFF"/>
<!-- 页眉（无顶部蓝条；品牌右侧蓝点为唯一蓝点缀） -->
<text x="40" y="24" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="11" letter-spacing="1" fill="#9B9B9B">[section_path]</text>
<rect x="1198" y="16" width="9" height="9" rx="2" fill="#336EE8"/>
<text x="1240" y="24" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="12" font-weight="600" fill="#262626">[brand_name]</text>
<line x1="40" y1="32" x2="1240" y2="32" stroke="#E7E7E7" stroke-width="1"/>
<!-- Action Title（整句结论 · 无衬线 bold · 无蓝竖线） -->
<text x="40" y="78" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="32" font-weight="700" fill="#262626">[title 单行]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E7E7E7" stroke-width="1"/>
<!-- 页脚 -->
<line x1="40" y1="690" x2="1240" y2="690" stroke="#E7E7E7" stroke-width="1"/>
<text x="40" y="709" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="11" fill="#9B9B9B">来源：[source] · [date]</text>
<text x="1240" y="709" text-anchor="end" font-family="'JetBrains Mono', Consolas, monospace"
      font-size="11" fill="#9B9B9B">[page_index] / [total_pages]</text>
```

**极简 Chrome（用于 impact / transition 类，更少装饰）**：

```svg
<!-- 不要顶部蓝线，不要 Action Title 竖线和分隔线 -->
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="10" fill="#9B9B9B" letter-spacing="2">[section_path]</text>
<text x="40" y="690" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="10" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="690" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="10" fill="#9B9B9B">[page_index]</text>
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

# 卡片内容元素规范（Aham UI v6.1）

**卡片**：无边框无阴影。成块用 `rx=12 fill=#F3F3F3` 面板（少用），否则只留白 + `#E7E7E7` 细横线分隔。
**卡片内边距**：16px
**卡片标题**：y=卡片y+30，无衬线 600 15px，**#262626（墨色，非蓝）**
**Bullets 起始 y**：卡片y+58，间距 26px（• 点 + 文字，非蓝竖条）

```svg
<circle cx="[cx+19]" cy="[itemY-4]" r="3" fill="#9B9B9B"/>
<text x="[cx+32]" y="[itemY]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
      font-size="14" fill="#262626">[bullet文字]</text>
```

**大数字显示**：数字用 mono `'JetBrains Mono', Consolas, monospace`，墨色 #262626（唯一关键数可用 #336EE8）；默认 48px，impact 类 80-160px。

**数据来源标注**（右下角）：
```svg
<text x="[cx+cw-16]" y="[cy+ch-10]" text-anchor="end" font-size="9" fill="#9B9B9B">
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
