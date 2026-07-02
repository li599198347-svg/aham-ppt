# SVG Skeleton D · 咨询密集异形层（v2.5）

> **身份**：不是第 8 个版式系，而是与 `charts.py` 同级的**可调用层**——异形形体 + 标注层，
> 可叠加在 I/S/E/V/G 任意版式之上，或按本文件 §2 的 X-90 段版式独立成页。
> **坐标真源** `grid-system.md`；**视觉真源** `brand.md`（灰阶为主 + ACC 蓝单点缀）；
> **代码真源** `assets/components/consulting.py`（参数化函数，照 charts.py 模式，不逐坐标手画）。
> Phase-7 命中 X-90 段版式、或任意页需要标注层时，加载本文件并调用 consulting.py。

---

## §0 为什么要这一层：降「AI 方形大卡片味」三原则

AI 生成 deck 的公认短板是结构纪律、行动标题与视觉层级（Slideworks 五工具实测评述，2026）。
形体语言是补"视觉层级"的直接抓手。三原则（均有出处）：

1. **图表即主角，裸摊白底**——密集页不许给图表再套卡片/外框容器；标题陈述结论、图表即证明
   （BCG "smart simplicity"，Deckary《BCG Presentation Style》）。公共 pptx 规范同向：
   "标题下强调线 / 边缘色条是 AI 生成幻灯片的标志"。本技能 skeleton-common 的
   "卡片无边框无阴影" 在 D 层收紧为：**图表区禁任何外框**。
2. **异形替代等宽矩形阵**——chevron 时间轴、瀑布为"桥/差值"类默认、Mekko/100% 堆叠替代饼图、
   2×2 / 散点 / 甘特为 MBB 常备图谱（Deckary《McKinsey Slides》图谱清单；PopAi 版式清单
   "Project Timeline (Chevron Style)"、"'So What?' Box"）。等宽矩形阵只在内容本身同构时使用。
3. **标注层 + 跨区连接**——椭圆圈注关键数、引线把图表元素牵到编号动作/旁注、So-What 锚点条、
   大号淡水印；高密度靠严格栅格对齐维持可读（Deckary："grid-aligned layouts… calm and easy
   to read even when a slide is information-dense"）。

---

## §1 API 速查（assets/components/consulting.py）

| 函数 | 用途 |
|---|---|
| `chevron_flow(x,y,w,h,stages,hi)` | 雪佛龙阶段链；stages=[(名,数,副)]；hi 段白底描边+ACC 数字 |
| `flow_bands(x,y,w,h,sources,target,hi)` | 锥形流向带（sankey-lite），带宽∝数值；hi 源 ACC |
| `dumbbell_rows(x,y,w,rows,row_h,hi)` | 哑铃行 a→b 对比，每行独立比例尺，增幅标箭上 |
| `dot_matrix(x,y,cols,rows,gap,r,col_labels)` | 点阵机制图；mode∈solid/ring/dim |
| `driver_node(...kind=root/branch/leaf)` + `driver_elbow(x1,y1,x2,y2)` | 驱动树节点与肘线 |
| `chain_steps(x,y,vals,step,r,deltas,cap)` | 链式递减（存活/收敛叙事），末端胶囊 |
| `mark_ellipse(cx,cy,rx,ry)` | 手绘感椭圆圈注（禁 rotate） |
| `leader(x1,y1,x2,y2)` | 引线箭头（line+polygon） |
| `watermark(x,y,text,size)` | 大号淡水印，**最先绘制** |
| `sowhat(x,y,w,h,label,text,dark)` | So-What 锚点条（灰面板或深墨） |
| `tick_label(cx,y_top,text,level)` / `check(x,y)` | 细段错层小标注 / 线画对勾（替 ✓） |

---

## §2 X-90 段版式（挂接既有系，编号 90+ 避撞）

> **X-90 是元素级版式，不是整页版式**：单页由「1 个主视觉 + ≥1 个辅助层 + 标注层 + So-What」组合而成，
> 组合配方如下；单元素占满内容区即判过简（见 §3 密度纪律）。

| ID | 名称 | 主视觉 | 必配辅助层（≥1） |
|---|---|---|---|
| E-90 | 雪佛龙阶段链 | chevron_flow | 100% 构成条（tick_label 处理细段）／chain_steps 存活链／时间锚点行 |
| V-90 | 流向带 | flow_bands | 增量排序小条列／机制注解面板（PANEL） |
| V-91 | 哑铃对比 | dumbbell_rows（3–5 行） | 「差额从哪来」拆解小条＋leader／结构小块（driver_node） |
| V-92 | 点阵机制 | dot_matrix | 汇聚块（driver_node root）＋leader／「去向」100% 堆叠条／图例行 |
| G-90 | 驱动树 | driver_node/elbow 三级 | 叶级公式块／n−1 迷你示例树／双行自洽校验条（check()） |
| I-90 | 链式递减 | chain_steps | 出局分布堆叠条／机制注解面板／watermark 大数字 |

> G 系原有手画树骨架继续有效；G-90 是其参数化替代，二选一。

## §3 密度与标注纪律（可叠加任意版式）

**密度纪律（v2.5.1，防「一页一组件」式过简）：**
- 单个 X-90 元素**禁止**独占内容区；每页 = 1 主视觉 + ≥1 辅助层 + 标注层 + So-What。
- 相关元素允许同页并用（如 点阵＋堆叠条、哑铃＋拆解条、链＋分布条）；数据图表可与 charts.py 同页混排。
- 内容区（40/100/1200/590）留白靠栅格分配，不靠"整块空着"。

**标注层配额：**
- 每页 ≤1 处椭圆圈注、≤2 条引线；水印 op ≤ 0.04 且最先绘制；So-What 全页至多 1 条。
- **chrome 红线**：页眉/页脚/左缘留白归 skeleton-common 与 themes.py，D 层元素不得进入 x<40 或页眉页脚区。
- **蓝的记账**：hi 参数与 ACC 文字合并计入 brand"单点缀"——全页至多一个蓝语义。

## §4 PPTX 兼容补遗（2026-07 实测，FIFA26 版式实战）

1. `<text>`/`<ellipse>` 上 **translate+rotate 组合变换实测转换后漂移**（即使规范允许元素级
   rotate）——D 层不做竖排；斜椭圆观感靠 rx/ry 比例。chrome（含左缘）归 skeleton-common，D 层禁触。
2. 箭头永远 line+polygon（`marker` 在 path/polyline 上静默丢失）。
3. `✓/✗` 在 `lint_svg.py` tofu 高危名单——用 `check()` 线画对勾。
4. 细段标注文字**自带空格**并 `tick_label(level)` 错层（曾出 "1/44" 粘连事故）。
5. mono 文本内全角 `＋ ＝` 实测可正常转换（Pango 逐字回退）。

---

## §5 冒烟基线

`examples/consulting/demo_d.svg`：一页跑全 11 个 API（v2.5.1 已移除侧标）；`svg_to_native_pptx` 转换 SUCCESS，
`<p:pic>`=0、`<p:sp>`=327，lint 无 tofu。世界杯 10 页真源同目录，可作版式参考。
