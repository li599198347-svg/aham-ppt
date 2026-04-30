# Layout Impl · A系版式实现（动作（Action））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-a.md。

---

# A 系 · 动作类（Action）

**共同特征**：
- 推动决策和行动
- 清晰的行动条目或选择结构
- 信息密度 50-70%

## A-01 下一步三步决策 

```svg
<!-- 顶部标题 -->
<text x="40" y="140" font-family="Songti SC,SimSun,serif"
      font-size="24" font-weight="bold" fill="#1A1A1A">[title]</text>

<!-- 三步行动卡 -->
<!-- STEP 1 -->
<rect x="40" y="200" width="400" height="360" fill="#F5F5F5"/>
<rect x="40" y="200" width="4" height="360" fill="var(--brand-primary)"/>
<text x="60" y="232" font-size="11" fill="var(--brand-primary)" letter-spacing="3">STEP 01 · 本周</text>
<text x="60" y="272" font-family="Songti SC,SimSun,serif"
      font-size="22" font-weight="bold" fill="#1A1A1A">[step_1_action]</text>
<text x="60" y="300" font-size="13" fill="#555">[step_1_detail]</text>

<!-- STEP 2, STEP 3 类似 -->
```

**信息密度**：60%

## A-02 是/否选择矩阵 

**适用**：决策二选一、门控条件判断

```svg
<!-- 上半：选择 A -->
<rect x="40" y="140" width="1200" height="240" fill="#E8F0FA"/>
<rect x="40" y="140" width="4" height="240" fill="var(--brand-primary)"/>
<text x="60" y="172" font-size="11" fill="var(--brand-primary)" letter-spacing="3">OPTION A · 推荐</text>
<text x="60" y="220" font-family="Songti SC,SimSun,serif"
      font-size="28" font-weight="bold" fill="#1A1A1A">[option_a]</text>
<text x="60" y="262" font-size="14" fill="#555">[pros_and_cons_a]</text>

<!-- 下半：选择 B -->
<rect x="40" y="420" width="1200" height="240" fill="#F5F5F5"/>
<rect x="40" y="420" width="4" height="240" fill="#888"/>
<text x="60" y="452" font-size="11" fill="#888" letter-spacing="3">OPTION B · 备选</text>
<!-- 类似 A -->
```

**信息密度**：55%

## A-03 责任矩阵 

**适用**：行动 + 责任方 + 截止时间 表格

```svg
<!-- 表头 -->
<rect x="40" y="140" width="1200" height="44" fill="#1A1A1A"/>
<text x="60" y="168" font-size="12" font-weight="bold" fill="#FFF">行动</text>
<text x="660" y="168" font-size="12" font-weight="bold" fill="#FFF">责任方</text>
<text x="960" y="168" font-size="12" font-weight="bold" fill="#FFF">截止时间</text>

<!-- N 行（每行 y 递增 60） -->
<rect x="40" y="184" width="1200" height="60" fill="#FAFAFA"/>
<text x="60" y="212" font-size="14" font-weight="bold" fill="#1A1A1A">[action_1]</text>
<text x="60" y="230" font-size="11" fill="#555">[action_1_detail]</text>
<text x="660" y="218" font-size="13" fill="#333">[owner_1]</text>
<text x="960" y="218" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_1]</text>
```

**信息密度**：65%

---
