# SVG Skeleton · 通用骨架代码库

> 本文件包含所有版式共用的骨架：Chrome框架、卡片骨架、箭头写法。
> Phase 7 每页设计时必须加载本文件。

---

## Chrome骨架（所有内容页必须先复制此段）

```svg
<svg width="1280" height="720" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">

<!-- ① 顶部品牌色线 -->
<rect x="0" y="0" width="1280" height="3" fill="var(--brand-primary)"/>

<!-- ② 页眉 -->
<text x="40" y="22" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888">[section_path]</text>
<text x="1240" y="22" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="var(--brand-primary)">[brand_name]</text>
<line x1="40" y1="30" x2="1240" y2="30" stroke="#E2E2E2" stroke-width="0.5"/>

<!-- ③ Action Title（单行） -->
<rect x="40" y="36" width="3" height="52" fill="var(--brand-primary)"/>
<text x="52" y="70" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[title]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E2E2E2" stroke-width="0.5"/>

<!-- ④ 内容区（在此处插入版式内容） -->
<!-- CONTENT_AREA: x=40 y=100 w=1200 h=590 -->

<!-- ⑤ 页脚 -->
<line x1="40" y1="690" x2="1240" y2="690" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888">来源：[source] · [date]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888">[page_index] / [total_pages]</text>

</svg>
```

**双行标题时，替换③为：**
```svg
<rect x="40" y="36" width="3" height="52" fill="var(--brand-primary)"/>
<text x="52" y="56" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#1A1A1A">[title_line_1]</text>
<text x="52" y="82" font-family="Songti SC,SimSun,serif" font-size="20" font-weight="bold" fill="#1A1A1A">[title_line_2]</text>
<line x1="40" y1="94" x2="1240" y2="94" stroke="#E2E2E2" stroke-width="0.5"/>
```

**极简Chrome（impact/transition类用）：**
```svg
<svg width="1280" height="720" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">
<text x="40" y="40" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA" letter-spacing="2">[section_path]</text>
<!-- CONTENT_AREA -->
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">[page_index]</text>
</svg>
```

---

## 卡片骨架（在内容区内使用）

### 标准白色卡片
```svg
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]" rx="4" fill="#FFFFFF" stroke="#E2E2E2" stroke-width="0.5"/>
<!-- 卡片标题 -->
<text x="[cx+16]" y="[cy+28]" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="var(--brand-primary)">[card_title]</text>
<!-- Bullet 1 -->
<rect x="[cx+16]" y="[cy+42]" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="[cx+26]" y="[cy+52]" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[bullet_1]</text>
<!-- Bullet 2（y += 24） -->
<rect x="[cx+16]" y="[cy+66]" width="3" height="14" rx="1" fill="var(--brand-primary)"/>
<text x="[cx+26]" y="[cy+76]" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[bullet_2]</text>
```

### 深蓝强调卡
```svg
<rect x="[cx]" y="[cy]" width="[cw]" height="[ch]" rx="4" fill="var(--brand-primary)"/>
<text x="[cx+16]" y="[cy+28]" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">[card_title]</text>
<rect x="[cx+16]" y="[cy+42]" width="3" height="14" rx="1" fill="#FFFFFF"/>
<text x="[cx+26]" y="[cy+52]" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#FFFFFF">[bullet_1]</text>
```

### 箭头（替代marker，用polygon）
```svg
<!-- 水平箭头：从(x1,y)到(x2,y) -->
<line x1="[x1]" y1="[y]" x2="[x2-12]" y2="[y]" stroke="var(--brand-primary)" stroke-width="2"/>
<polygon points="[x2-12],[y-6] [x2],[y] [x2-12],[y+6]" fill="var(--brand-primary)"/>
```