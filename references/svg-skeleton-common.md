# SVG Skeleton · 通用骨架代码库（Aham UI v6.1）

> 本文件包含所有版式共用的骨架：Chrome框架、卡片骨架、状态、箭头。
> Phase 7 每页设计时必须加载本文件。
> **视觉取值唯一来源：brand.md / tokens.css。底永远纯白，蓝只点缀。**

---

## 设计语言速记（每页都遵守）

- **底永远 `#FFFFFF`**，无顶部蓝条、无色块墙、无渐变、无图片满铺。
- **三层灰**：内容/底 `#FFFFFF` · 面板 `#F3F3F3`(极少) · 线/选中 `#E7E7E7`。
- **墨四级**：`#262626` 主 / `#6E6E6E` 次 / `#9B9B9B` 三(占位/页脚) / `#C4C4C4` 四(最弱线)。
- **蓝 `#336EE8` 只点缀**：品牌点 / 主操作 / 选中下划线 / 推荐标 / **单个**高亮数据点 / 封面·关键页短装饰条。蓝若第一眼注意到就超标。
- **无衬线**：`Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif`；数字 mono `'JetBrains Mono', Consolas, monospace`。层级靠字号+字重。
- **卡片无边框无阴影**；分块优先留白 + `#E7E7E7` 细横线；成块才用 `#F3F3F3` 面板。
- **状态 = 6px 点 + 文字**；表格只横线、数字右对齐 mono。

---

## Chrome骨架（标准内容页，先复制此段）

```svg
<svg width="1280" height="720" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="1280" height="720" fill="#FFFFFF"/>

<!-- ① 页眉：Section 路径（左） + 品牌（右，唯一蓝点） -->
<text x="40" y="24" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" letter-spacing="1" fill="#9B9B9B">[section_path]</text>
<rect x="1198" y="16" width="9" height="9" rx="2" fill="#336EE8"/>
<text x="1240" y="24" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="12" font-weight="600" fill="#262626">[brand_name]</text>
<line x1="40" y1="32" x2="1240" y2="32" stroke="#E7E7E7" stroke-width="1"/>

<!-- ② Action Title（整句结论 · 无衬线 bold · 无蓝竖线） -->
<text x="40" y="78" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="32" font-weight="700" fill="#262626">[title]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E7E7E7" stroke-width="1"/>

<!-- ③ 内容区（在此处插入版式内容） -->
<!-- CONTENT_AREA: x=40 y=100 w=1200 h=590 -->

<!-- ④ 页脚 -->
<line x1="40" y1="690" x2="1240" y2="690" stroke="#E7E7E7" stroke-width="1"/>
<text x="40" y="709" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#9B9B9B">来源：[source] · [date]</text>
<text x="1240" y="709" text-anchor="end" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#9B9B9B">[page_index] / [total_pages]</text>

<!-- ⑤ 可选·关键页品牌点缀：左下蓝短条（全页仅此一处蓝面） -->
<!-- <rect x="40" y="672" width="84" height="2" fill="#336EE8"/> -->
</svg>
```

**双行标题时，替换②为：**
```svg
<text x="40" y="60" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="22" font-weight="700" fill="#262626">[title_line_1]</text>
<text x="40" y="86" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="22" font-weight="700" fill="#262626">[title_line_2]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E7E7E7" stroke-width="1"/>
```

**极简Chrome（impact / transition 类）：**
```svg
<svg width="1280" height="720" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<rect x="0" y="0" width="1280" height="720" fill="#FFFFFF"/>
<text x="40" y="40" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#9B9B9B" letter-spacing="2">[section_path]</text>
<!-- CONTENT_AREA -->
<text x="40" y="700" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="11" fill="#9B9B9B">来源：[source]</text>
<text x="1240" y="700" text-anchor="end" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" fill="#9B9B9B">[page_index]</text>
</svg>
```

---

## 卡片骨架（在内容区内使用 · 优先留白，成块才用面板）

### 默认：无卡片，靠留白 + 细横线分块
```svg
<!-- 区块标题 -->
<text x="[x]" y="[y]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="20" font-weight="600" fill="#262626">[block_title]</text>
<!-- 区块下细横线（分隔，不画框） -->
<line x1="[x]" y1="[y+14]" x2="[x2]" y2="[y+14]" stroke="#E7E7E7" stroke-width="1"/>
```

### 面板卡（需要明显成块时，无边框无阴影）
```svg
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]" rx="12" fill="#F3F3F3"/>
<!-- 卡片标题（墨色，非蓝） -->
<text x="[cx+16]" y="[cy+30]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="15" font-weight="600" fill="#262626">[card_title]</text>
<!-- Bullet（• 点 + 文字，起始 y=cy+58，间距 26） -->
<circle cx="[cx+19]" cy="[itemY-4]" r="3" fill="#9B9B9B"/>
<text x="[cx+32]" y="[itemY]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="14" fill="#262626">[bullet_1]</text>
```

### 强调 / Callout（用面板 + 左侧蓝细条点缀，**不铺蓝底**）
```svg
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]" rx="12" fill="#F3F3F3"/>
<rect x="[cx]" y="[cy]" width="3" height="[ch]" rx="1.5" fill="#336EE8"/>
<text x="[cx+18]" y="[cy+30]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="15" font-weight="600" fill="#262626">[callout_title]</text>
```

### 数据来源标注（有 data_points 时必须，右下角）
```svg
<text x="[cx+cw-16]" y="[cy+ch-12]" text-anchor="end" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="9" fill="#9B9B9B">来源：[source]，[date]</text>
```

---

## 状态：6px 点 + 文字（绝不 pill / 徽章 / 色块 / 红黄绿灯）

```svg
<circle cx="[x]" cy="[y-4]" r="3.5" fill="[状态色]"/>
<text x="[x+13]" y="[y]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="13" fill="#6E6E6E">[达标/预警/风险/进行中]</text>
```
状态色：达标 `#5A7A60` · 预警 `#8A7333` · 风险 `#9E3D31` · 中性/进行中 `#9B9B9B`。
**颜色+文字双通道**：颜色之外，文字本身必须能区分（达标/预警/风险），去色后仍可辨。

---

## 数字 / KPI（mono · 墨色，关键时才一个蓝）

```svg
<!-- 标签 -->
<text x="[x]" y="[y]" font-family="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif" font-size="15" fill="#9B9B9B">[label]</text>
<!-- 数值（等宽，墨色；唯一关键数可用 #336EE8） -->
<text x="[x]" y="[y+50]" font-family="'JetBrains Mono', Consolas, monospace" font-size="50" font-weight="700" fill="#262626">[value]</text>
<text x="[x+数字宽]" y="[y+50]" font-family="Inter, sans-serif" font-size="22" fill="#9B9B9B">[unit]</text>
```

---

## 箭头（替代 marker，用 polygon · 中性灰）

```svg
<line x1="[x1]" y1="[y]" x2="[x2-12]" y2="[y]" stroke="#9B9B9B" stroke-width="2"/>
<polygon points="[x2-12],[y-6] [x2],[y] [x2-12],[y+6]" fill="#9B9B9B"/>
```
