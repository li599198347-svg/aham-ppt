# 图表 SVG 实现模板

对应 brand.md 第7.5节的图表规范，提供各图表类型的精确SVG绘制代码。
**图表类型选择规则和颜色语义以 brand.md 7.5节为准，本文件只管「怎么画」。**

---

## 图表区坐标系统

图表通常嵌入内容页的某个卡片内，或直接占用内容区（D系版式）。

```
图表区内部坐标（相对于宿主卡片）：
  坐标轴原点偏移：左侧轴标签区 w=60，底部轴标签区 h=40
  实际绘图区：x=宿主x+60，y=宿主y+20，w=宿主w-80，h=宿主h-70
  轴线：x轴 y=绘图区底边，y轴 x=绘图区左边
  轴颜色：stroke="#888888" stroke-width="0.5"
  网格线（水平）：stroke="#E2E2E2" stroke-width="0.5" stroke-dasharray="2,2"
```

---

## 纵向柱状图模板

适用：数量对比/排名（≤12个数据点）

```svg
<!-- 以宿主卡片为 cx=卡片x，cy=卡片y，cw=卡片w，ch=卡片h 为参数 -->

<!-- Y轴（强制从0开始） -->
<line x1="[cx+60]" y1="[cy+20]" x2="[cx+60]" y2="[cy+ch-50]"
      stroke="#888888" stroke-width="0.5"/>
<!-- X轴 -->
<line x1="[cx+60]" y1="[cy+ch-50]" x2="[cx+cw-20]" y2="[cy+ch-50]"
      stroke="#888888" stroke-width="0.5"/>

<!-- 水平网格线（3~5条，等间距） -->
<line x1="[cx+60]" y1="[grid_y]" x2="[cx+cw-20]" y2="[grid_y]"
      stroke="#E2E2E2" stroke-width="0.5" stroke-dasharray="2,2"/>

<!-- Y轴刻度标签 -->
<text x="[cx+54]" y="[grid_y+4]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888">[value]</text>

<!-- 数据柱（每根柱）-->
<rect x="[bar_x]" y="[bar_y]" width="[bar_w]" height="[bar_h]"
      fill="#003D7A"/>
<!-- 柱顶数值标注 -->
<text x="[bar_x+bar_w/2]" y="[bar_y-6]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold"
      fill="#1A1A1A">[value]</text>
<!-- X轴标签 -->
<text x="[bar_x+bar_w/2]" y="[cy+ch-32]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[label]</text>

<!-- Callout（当callout_needed=true时，圈出关键柱） -->
<rect x="[target_x-4]" y="[target_y-4]"
      width="[target_w+8]" height="[target_h+8]"
      rx="2" fill="none" stroke="#003D7A" stroke-width="1.5"/>
<rect x="[callout_bx]" y="[callout_by]" width="[callout_bw]" height="24"
      rx="3" fill="#E8F0FA" stroke="#003D7A" stroke-width="1"/>
<text x="[callout_bx+callout_bw/2]" y="[callout_by+16]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold"
      fill="#003D7A">[annotation]</text>
<line x1="[callout_connect_x]" y1="[callout_by+24]"
      x2="[callout_connect_x]" y2="[target_y-4]"
      stroke="#003D7A" stroke-width="0.5" stroke-dasharray="3,2"/>
```

**柱宽计算规则：**
```
n = 数据点数量
plot_w = 绘图区宽度（cw - 80）
bar_w = plot_w / n * 0.6    （柱宽=间隔的0.6倍）
bar_gap = plot_w / n * 0.4
bar_x[i] = cx+60 + i * (plot_w/n) + bar_gap/2
```

**多系列分组柱状图：**
同一分组内各系列色按 brand.md 2.4节顺序排列，组内无间距，组间间距=单柱宽。

---

## 横向柱状图模板

适用：排名展示、长标签场景（≤8项）

```svg
<!-- X轴（从0开始） -->
<line x1="[cx+120]" y1="[cy+ch-30]" x2="[cx+cw-20]" y2="[cy+ch-30]"
      stroke="#888888" stroke-width="0.5"/>
<!-- 每条横柱 -->
<rect x="[cx+120]" y="[bar_y]" width="[bar_w]" height="[bar_h]"
      fill="#003D7A"/>
<!-- 右侧数值标注 -->
<text x="[cx+120+bar_w+6]" y="[bar_y+bar_h/2+4]"
      font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold"
      fill="#1A1A1A">[value]</text>
<!-- 左侧标签 -->
<text x="[cx+114]" y="[bar_y+bar_h/2+4]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[label]</text>
```

---

## 折线图模板

适用：趋势变化（时间序列）

```svg
<!-- 坐标轴（同纵向柱状图，但Y轴起点可不为0） -->
<!-- Y轴标注范围说明（当不从0开始时必须） -->
<text x="[cx+60]" y="[cy+16]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#888888">▲</text>
<text x="[cx+58]" y="[cy+28]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#888888">[y_max]</text>

<!-- 折线（polyline） -->
<polyline points="[x1,y1 x2,y2 x3,y3 ...]"
          fill="none" stroke="#003D7A" stroke-width="2" stroke-linejoin="round"/>
<!-- 数据节点 -->
<circle cx="[xi]" cy="[yi]" r="4" fill="#003D7A" stroke="#FFFFFF" stroke-width="1.5"/>
<!-- 节点数值（关键节点标注，非全部） -->
<text x="[xi]" y="[yi-10]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold"
      fill="#1A1A1A">[value]</text>

<!-- 目标线（如有） -->
<line x1="[cx+60]" y1="[target_y]" x2="[cx+cw-20]" y2="[target_y]"
      stroke="#1A7A42" stroke-width="1.5" stroke-dasharray="6,3"/>
<text x="[cx+cw-18]" y="[target_y-4]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#1A7A42">目标</text>

<!-- 基准线（如有） -->
<line x1="[cx+60]" y1="[baseline_y]" x2="[cx+cw-20]" y2="[baseline_y]"
      stroke="#888888" stroke-width="1" stroke-dasharray="4,3"/>
```

---

## 瀑布图模板

适用：KPI→子项贡献拆解，成本/收益分解

```svg
<!-- 基线 -->
<line x1="[cx+60]" y1="[baseline_y]" x2="[cx+cw-20]" y2="[baseline_y]"
      stroke="#888888" stroke-width="0.5"/>

<!-- 起始总量柱（深蓝） -->
<rect x="[bar0_x]" y="[bar0_y]" width="[bar_w]" height="[bar0_h]" fill="#003D7A"/>

<!-- 增量柱（正向=绿色，负向=红色，浮动） -->
<!-- 正向增量 -->
<rect x="[bar_x]" y="[float_y]" width="[bar_w]" height="[delta_h]" fill="#1A7A42"/>
<!-- 负向增量 -->
<rect x="[bar_x]" y="[float_y]" width="[bar_w]" height="[delta_h]" fill="#B01C1C"/>
<!-- 浮动连接虚线 -->
<line x1="[prev_bar_x+bar_w]" y1="[prev_top_y]" x2="[bar_x]" y2="[prev_top_y]"
      stroke="#E2E2E2" stroke-width="0.5" stroke-dasharray="2,2"/>

<!-- 结果总量柱（深蓝） -->
<rect x="[bar_last_x]" y="[bar_last_y]" width="[bar_w]" height="[bar_last_h]" fill="#003D7A"/>

<!-- 柱顶数值 -->
<text x="[bar_x+bar_w/2]" y="[bar_y-6]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold"
      fill="#1A1A1A">[±value]</text>
```

---

## 甘特图模板

适用：项目实施计划（F21版式）

```svg
<!-- 时间刻度表头 -->
<rect x="[cx+240]" y="[cy+44]" width="[月宽]" height="30" fill="#003D7A" opacity="0.1"/>
<text x="[月中心x]" y="[cy+64]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#003D7A">[月份]</text>

<!-- 任务行背景（奇偶交替） -->
<rect x="[cx+240]" y="[row_y]" width="[plot_w]" height="44"
      fill="[奇行#FFFFFF / 偶行#F5F5F5]"/>

<!-- 任务条 -->
<rect x="[task_x]" y="[row_y+10]" width="[task_w]" height="24"
      rx="3" fill="[一期#003D7A / 二期#0056A8 / 三期#3A7FC1]"/>
<text x="[task_x+task_w/2]" y="[row_y+26]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#FFFFFF">[task_name]</text>

<!-- 里程碑（菱形） -->
<polygon points="[mx],[my-10] [mx+10],[my] [mx],[my+10] [mx-10],[my]"
         fill="#1A1A1A"/>
<text x="[mx]" y="[my-14]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#1A1A1A">[milestone]</text>

<!-- 左侧任务名称 -->
<text x="[cx+230]" y="[row_y+26]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#1A1A1A">[task_name]</text>
```

---

## KPI 指标卡模板（单个组件）

适用：B05执行摘要顶部、D15数据看板，也可内嵌于其他版式

```svg
<!-- 卡片底色 -->
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]"
      rx="4" fill="#F5F5F5"/>
<!-- 顶部色条（4px，颜色=问题#B01C1C/警告#9A5200/计划#003D7A/达标#1A7A42） -->
<rect x="[cx]" y="[cy]" width="[cw]" height="4" rx="2" fill="[status_color]"/>
<!-- 指标名称 -->
<text x="[cx+16]" y="[cy+28]"
      font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[metric_name]</text>
<!-- 核心数字 -->
<text x="[cx+16]" y="[cy+ch/2+16]"
      font-family="Microsoft YaHei,sans-serif" font-size="36" font-weight="bold"
      fill="[status_color]">[value]</text>
<text x="[cx+16+数字宽+4]" y="[cy+ch/2+10]"
      font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#888888">[unit]</text>
<!-- 趋势箭头（可选） -->
<!-- 上升：▲ fill=#1A7A42；下降：▼ fill=#B01C1C -->
<text x="[cx+cw-20]" y="[cy+ch/2+16]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="18" fill="[trend_color]">[▲/▼]</text>
<!-- 描述文字 -->
<text x="[cx+16]" y="[cy+ch-16]"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888">[description]</text>
```

---

## 2×2 四象限模板

适用：E19四象限框架、F22风险评估矩阵

```svg
<!-- 背景区 -->
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]" fill="#FFFFFF"/>
<!-- 纵轴 -->
<line x1="[cx+cw/2]" y1="[cy+20]" x2="[cx+cw/2]" y2="[cy+ch-40]"
      stroke="#888888" stroke-width="1"/>
<!-- 横轴 -->
<line x1="[cx+20]" y1="[cy+ch/2]" x2="[cx+cw-20]" y2="[cy+ch/2]"
      stroke="#888888" stroke-width="1"/>
<!-- 轴端箭头 -->
<!-- 轴标签 -->
<text x="[cx+cw/2]" y="[cy+14]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[y_high_label]</text>
<text x="[cx+cw/2]" y="[cy+ch-26]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[y_low_label]</text>
<text x="[cx+cw-18]" y="[cy+ch/2+14]" text-anchor="end"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[x_high_label]</text>
<text x="[cx+22]" y="[cy+ch/2+14]"
      font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#555555">[x_low_label]</text>
<!-- 象限标题（左上角） -->
<text x="[各象限左上角x+8]" y="[各象限左上角y+20]"
      font-family="Microsoft YaHei,sans-serif" font-size="13" font-weight="bold"
      fill="#003D7A">[quadrant_title]</text>
<!-- 内容项 -->
<rect x="[item_x-4]" y="[item_y-14]" width="[item_w+8]" height="20"
      rx="3" fill="#F5F5F5"/>
<text x="[item_x]" y="[item_y]"
      font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#1A1A1A">[item_text]</text>
```

---

## Callout 标注模板（通用，可叠加在任何图表上）

```svg
<!-- 1. 圈框（圈住目标元素） -->
<rect x="[target_x-6]" y="[target_y-6]"
      width="[target_w+12]" height="[target_h+12]"
      rx="3" fill="none" stroke="#003D7A" stroke-width="1.5"/>

<!-- 2. 连接线（虚线，从气泡到圈框） -->
<line x1="[bubble_cx]" y1="[bubble_bottom_y]"
      x2="[circle_cx]" y2="[target_y-6]"
      stroke="#003D7A" stroke-width="0.5" stroke-dasharray="3,2"/>

<!-- 3. 标注气泡 -->
<rect x="[bubble_x]" y="[bubble_y]" width="[bubble_w]" height="26"
      rx="3" fill="#E8F0FA" stroke="#003D7A" stroke-width="1"/>
<text x="[bubble_x+bubble_w/2]" y="[bubble_y+17]" text-anchor="middle"
      font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold"
      fill="#003D7A">[annotation_text]</text>
```

**位置决策规则（优先级从高到低）：**
1. 图表右上角空白区（最常用）
2. 目标元素正上方
3. 目标元素右侧
4. 不得遮挡其他数据点或轴标签
