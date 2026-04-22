# SVG Skeleton · T系版式骨架（过渡（Transition））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## ## T-01 深色引言页
```svg
<!-- 深色背景 -->
<rect width="1280" height="720" fill="#0A1F3A"/>

<!-- 顶部装饰细线 -->
<rect x="80" y="80" width="40" height="2" fill="#4A6680"/>

<!-- 主引言（两行，居中偏左） -->
<text x="120" y="310" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_1]</text>
<text x="120" y="360" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_2]</text>

<!-- 副注 -->
<text x="120" y="440" font-family="Songti SC,SimSun,serif" font-size="22" fill="#B8C8D8">[sub_line]</text>

<!-- 引用来源 -->
<text x="1200" y="640" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#6B86A8">—— [source]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#4A6680">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#4A6680">[page_index]</text>
```

---

## ## T-02 白底大字宣言
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA" letter-spacing="2">[section_path]</text>

<!-- 居中大字宣言 -->
<text x="640" y="310" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_1]</text>
<text x="640" y="366" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_2]</text>

<!-- 品牌蓝短线 -->
<line x1="580" y1="410" x2="700" y2="410" stroke="#003D7A" stroke-width="2.5"/>

<!-- 副注小字 -->
<text x="640" y="456" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="16" fill="#666666">[sub_note]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">[page_index]</text>
```

---

## ### T-03 章节承接页
```svg
<!-- 极简Chrome -->
<text x="40" y="40" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA" letter-spacing="2">[section_path]</text>

<!-- 左侧：刚才讲了什么 -->
<text x="100" y="200" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#888888" letter-spacing="3">JUST COMPLETED</text>
<line x1="100" y1="220" x2="220" y2="220" stroke="#888888" stroke-width="1"/>
<text x="100" y="270" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#888888">[prev_part_title]</text>
<text x="100" y="310" font-family="Microsoft YaHei,sans-serif" font-size="14" fill="#555555">[prev_part_summary]</text>

<!-- 中间垂直分割线 -->
<line x1="520" y1="160" x2="520" y2="560" stroke="#E2E2E2" stroke-width="0.5"/>

<!-- 右侧：即将进入 -->
<text x="580" y="200" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="3">NEXT PART</text>
<line x1="580" y1="220" x2="700" y2="220" stroke="#003D7A" stroke-width="1.5"/>
<text x="580" y="320" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#003D7A">[next_part_title]</text>
<text x="580" y="380" font-family="Microsoft YaHei,sans-serif" font-size="16" fill="#555555">[next_part_intro]</text>

<!-- 底部导航 -->
<text x="640" y="650" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#AAAAAA">[part_nav]</text>

<!-- 极简页脚 -->
<text x="40" y="708" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">来源：[source]</text>
<text x="1240" y="708" text-anchor="end" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#AAAAAA">[page_index]</text>
```