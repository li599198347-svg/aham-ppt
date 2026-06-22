# -*- coding: utf-8 -*-
"""双档主题模板：A 克制档 / B 现代专业档（默认）。
两档共用内容与组件，只切换封面/目录/章节模板与页眉皮肤。
全部参数化、无品牌/客户硬编码——调用时传入实际文字。
1280x720 画布。依赖同目录 components.py / icons.py。"""
from components import (T,P,L,esc,SANS,MONO,ACC,INK1,INK2,INK3,INK4,LINE,PANEL)
from icons import ICON, icon_circle, num_badge, num_ring

def _svg(body,bg="#FFFFFF"):
    return (f'<svg width="1280" height="720" viewBox="0 0 1280 720" '
            f'xmlns="http://www.w3.org/2000/svg"><rect width="1280" height="720" fill="{bg}"/>{body}</svg>')

# ============================================================
#  封面
# ============================================================
def cover(theme,brand,title,subtitle,chapters,meta_left="",meta_right=""):
    """theme='A'|'B'. chapters=[(num,zh,sub,icon),...]"""
    if theme=="A":
        b=[f'<rect x="40" y="60" width="12" height="12" rx="2" fill="{ACC}"/>',
           T(62,76,brand,19,INK1,700),
           T(40,312,title,46,INK1,700)]
        if subtitle: b.append(T(40,374,subtitle,19,INK2))
        b.append(f'<rect x="42" y="398" width="116" height="4" fill="{ACC}"/>')
        # 右侧竖排目录
        b.append(L(856,276,856,496))
        b.append(T(892,296,"目录　CONTENTS",13,INK3,ls=2))
        for i,(n,zh,sub,ic) in enumerate(chapters[:6]):
            y=344+i*42
            b.append(T(892,y,n,16,INK3,fam=MONO)); b.append(T(936,y,zh,17,INK1))
        b.append(L(40,648,1240,648))
        b.append(T(40,682,meta_left,13,INK3)); b.append(T(1240,682,meta_right,13,INK3,anchor="end"))
        return _svg("".join(b))
    # B · Hero
    b=[f'<rect x="40" y="60" width="12" height="12" rx="2" fill="{ACC}"/>',
       T(62,76,brand,19,INK1,700),
       T(80,168,"MANUFACTURING OPERATIONS",13,INK3,ls=5),
       T(80,332,title,58,INK1,700)]
    if subtitle: b.append(T(80,404,subtitle,20,INK2))
    b.append(f'<rect x="84" y="430" width="150" height="5" rx="2" fill="{ACC}"/>')
    # 右侧浅色信息块 + 章节缩略（motif，不堆色）
    b.append(P(812,96,428,528,PANEL,r=22))
    b.append(T(852,150,"本册导览",15,INK1,700)); b.append(T(852,172,"IN THIS DECK",10,INK3,ls=2))
    for i,(n,zh,sub,ic) in enumerate(chapters[:5]):
        y=214+i*78
        b.append(icon_circle(ic,874,y,18,INK2,"#FFFFFF",isize=22))
        b.append(T(906,y-4,n+"  "+zh,16,INK1,600));
        if sub: b.append(T(906,y+18,sub,12,INK2))
    b.append(L(80,648,1240,648))
    b.append(T(80,682,meta_left,13,INK3)); b.append(T(1240,682,meta_right,13,INK3,anchor="end"))
    return _svg("".join(b))

# ============================================================
#  目录
# ============================================================
def toc(theme,chapters):
    """chapters=[(num,zh,sub,icon),...]"""
    if theme=="A":
        b=[T(40,200,"目录",40,INK1,700),T(40,250,"CONTENTS",15,INK3,ls=3)]
        for i,(n,zh,sub,ic) in enumerate(chapters):
            y=180+i*120
            b.append(T(620,y,n,30,INK3,fam=MONO,w=700))
            b.append(T(690,y,zh,24,INK1,600)); b.append(T(690,y+30,sub,14,INK2))
            if i<len(chapters)-1: b.append(L(620,y+58,1240,y+58))
        return _svg("".join(b))
    # B · 图标圆 + 描述 + 右侧缩略
    b=[T(40,140,"目录",40,INK1,700),T(40,190,"CONTENTS",15,INK3,ls=3),L(40,210,1240,210)]
    for i,(n,zh,sub,ic) in enumerate(chapters):
        y=270+i*96
        b.append(icon_circle(ic,80,y,24,ACC,PANEL,isize=28))
        b.append(T(124,y-8,n,14,INK3,fam=MONO,w=700)); b.append(T(124,y+16,zh,22,INK1,700))
        b.append(T(470,y+6,sub,15,INK2))
        if i<len(chapters)-1: b.append(L(40,y+48,1240,y+48))
    return _svg("".join(b))

# ============================================================
#  章节过渡页
# ============================================================
def section(theme,num,zh,summary,total="04",items=None):
    """items(B 用)=[(icon,text),...] 右侧「本章内容」。"""
    if theme=="A":
        b=[T(40,40,"",11,INK3),
           T(40,300,num,120,INK4,700,fam=MONO),
           f'<rect x="44" y="330" width="90" height="4" fill="{ACC}"/>',
           T(40,400,zh,40,INK1,700),
           T(40,452,summary,17,INK2),
           T(1240,700,f"{num} / {total}",11,INK3,fam=MONO,anchor="end")]
        return _svg("".join(b))
    # B · 大水印编号 + 右侧本章内容
    b=[f'<rect x="0" y="0" width="470" height="720" fill="{PANEL}"/>',
       T(60,300,num,200,"#FFFFFF",700,fam=MONO),
       f'<rect x="60" y="470" width="120" height="6" rx="3" fill="{ACC}"/>',
       T(60,540,zh,38,INK1,700),
       T(60,592,summary,15,INK2),
       T(60,640,f"PART {num} / {total}",13,INK3,ls=3,fam=MONO)]
    # 水印描边编号（叠在浅块上，避免纯填充太重）
    b.insert(1,T(60,300,num,200,PANEL,700,fam=MONO))
    rx=560
    b.append(T(rx,150,"本章内容",16,INK1,700)); b.append(T(rx,172,"IN THIS SECTION",10,INK3,ls=2))
    for i,(ic,t) in enumerate(items or []):
        y=230+i*84
        b.append(icon_circle(ic,rx+22,y,19,INK2,PANEL,isize=23))
        b.append(T(rx+52,y-4,t,16,INK1,600))
        if i<len(items)-1: b.append(L(rx,y+40,1240,y+40,LINE,1))
    return _svg("".join(b))

# ============================================================
#  内容页页眉（chrome）
# ============================================================
def chrome(theme,section_label,title,source,page,total,body,brand="",tsize=26,icon=None):
    head=[T(40,24,section_label,11,INK3,ls=1)]
    if brand:
        head.append(f'<rect x="1188" y="16" width="9" height="9" rx="2" fill="{ACC}"/>')
        head.append(T(1240,24,brand,12,INK1,600,anchor="end"))
    head.append(L(40,32,1240,32))
    tx=40
    if theme=="B" and icon:
        head.append(icon_circle(icon,58,66,16,ACC,PANEL,isize=20)); tx=86
    head.append(T(tx,74,title,tsize,INK1,700))
    head.append(L(40,90,1240,90))
    foot=[L(40,690,1240,690),
          T(40,709,"来源："+source,11,INK3),
          T(1240,709,f"{page} / {total}",11,INK3,fam=MONO,anchor="end")]
    return _svg("".join(head)+body+"".join(foot))
