# -*- coding: utf-8 -*-
"""关系图 / UI 原型组件库（自包含，通用）。供 B·现代专业档使用。
颜色一律传入；缺省取 Aham 角色色，使用时改成你的 tokens 角色色即可。
不写死任何品牌名/客户名——示例文字用占位符 BRAND。"""
import math as _m
SANS="Inter, 'PingFang SC', 'Microsoft YaHei', sans-serif"
MONO="'JetBrains Mono', Consolas, monospace"
ACC="#336EE8"; INK1="#262626"; INK2="#6E6E6E"; INK3="#9B9B9B"; INK4="#C4C4C4"; LINE="#E7E7E7"; PANEL="#F3F3F3"
BRAND="BRAND"  # 出片前替换为实际品牌占位

def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def T(x,y,s,size=14,fill=INK1,w=None,fam=SANS,anchor="start",ls=None):
    a=f' font-weight="{w}"' if w else ''; l=f' letter-spacing="{ls}"' if ls else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}" font-size="{size}" fill="{fill}"{a}{l}>{esc(s)}</text>'
def P(x,y,w,h,fill=PANEL,blue=False,r=12,stroke=None,sw=1):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{st}/>'
    if blue: s+=f'<rect x="{x}" y="{y}" width="3" height="{h}" rx="1.5" fill="{ACC}"/>'
    return s
def L(x1,y1,x2,y2,c=LINE,sw=1,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"{d}/>'

# ---- 箭头：直线 / 曲线 ----
def arrow(x1,y1,x2,y2,c=INK3,sw=1.5,dash=None):
    ang=_m.atan2(y2-y1,x2-x1); hl=8
    ax,ay=x2-hl*_m.cos(ang),y2-hl*_m.sin(ang)
    p1=(x2-hl*_m.cos(ang-0.42),y2-hl*_m.sin(ang-0.42))
    p2=(x2-hl*_m.cos(ang+0.42),y2-hl*_m.sin(ang+0.42))
    return L(x1,y1,ax,ay,c,sw,dash)+f'<polygon points="{x2},{y2} {p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="{c}"/>'
def carrow(x1,y1,x2,y2,c=INK3,sw=1.6,bend=0.18,dash=None):
    mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=x2-x1,y2-y1
    cx,cy=mx-dy*bend,my+dx*bend
    ang=_m.atan2(y2-cy,x2-cx); hl=9
    p1=(x2-hl*_m.cos(ang-0.4),y2-hl*_m.sin(ang-0.4))
    p2=(x2-hl*_m.cos(ang+0.4),y2-hl*_m.sin(ang+0.4))
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="M{x1} {y1} Q {cx} {cy} {x2} {y2}" fill="none" stroke="{c}" stroke-width="{sw}"{d}/>'
            f'<polygon points="{x2},{y2} {p1[0]},{p1[1]} {p2[0]},{p2[1]}" fill="{c}"/>')

# ---- chip / hexagon / KPI ----
def chip(x,y,w,h,label,sub=None,blue=False,dashed=False):
    st=f' stroke="{ACC if blue else INK4}" stroke-width="1.2"'
    da=' stroke-dasharray="4 3"' if dashed else ''
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#FFFFFF"{st}{da}/>'
    if blue and not dashed: s+=f'<rect x="{x}" y="{y}" width="3" height="{h}" rx="1.5" fill="{ACC}"/>'
    s+=T(x+w/2,y+(h/2+5 if not sub else h/2-2),label,13.5,INK1,600,anchor="middle")
    if sub: s+=T(x+w/2,y+h/2+16,sub,10.5,INK3,anchor="middle")
    return s
def hexagon(cx,cy,r,fill="#FFFFFF",stroke=INK3,sw=1.4):
    pts=" ".join(f"{cx+r*_m.cos(_m.radians(a))},{cy+r*_m.sin(_m.radians(a))}" for a in range(0,360,60))
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def kpi(x,y,w,h,value,label,unit="",accent=False):
    c=ACC if accent else INK1
    s=P(x,y,w,h,"#FFFFFF",blue=accent,r=10,stroke=LINE,sw=1)
    s+=T(x+18,y+h*0.5,value,30,c,700,fam=MONO)
    if unit: s+=T(x+18+len(str(value))*18,y+h*0.5,unit,13,INK3)
    s+=T(x+18,y+h*0.5+24,label,12,INK2)
    return s

# ---- 状态点（双通道：色点 + 文字，色盲友好）----
def status(x,y,label,kind="ok"):
    c={"ok":"#5A7A60","warn":"#8A7333","bad":"#9E3D31","idle":INK3}.get(kind,INK3)
    return f'<circle cx="{x}" cy="{y-4}" r="4" fill="{c}"/>'+T(x+12,y,label,12.5,INK1)

# ---- 设备屏 / 手机 / 按钮（UI 原型）----
def device_screen(x,y,w,h,brand=BRAND,app="APP",clock="00:00"):
    """返回 (壳 svg, 内容区 ix,iy,iw,ih)。顶栏：品牌占位 brand + 应用名 app + 时间 clock。
    app/clock 均为中性占位，调用时按实际业务系统名/时间传入，勿写死行业。"""
    bez=6
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#FFFFFF" stroke="{INK3}" stroke-width="2"/>'
    ix,iy,iw,ih=x+bez,y+bez+18,w-2*bez,h-2*bez-18
    s+=f'<rect x="{x+bez}" y="{y+bez}" width="{w-2*bez}" height="18" rx="3" fill="{PANEL}"/>'
    s+=f'<circle cx="{x+bez+10}" cy="{y+bez+9}" r="3" fill="{ACC}"/>'
    s+=T(x+bez+20,y+bez+13,f"{brand} {app}",9,INK2,600)
    s+=T(x+w-bez-8,y+bez+13,clock,9,INK3,fam=MONO,anchor="end")
    s+=f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="4" fill="#FFFFFF"/>'
    return s,(ix,iy,iw,ih)
def phone_screen(x,y,w,h):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#FFFFFF" stroke="{INK3}" stroke-width="2"/>'
    s+=f'<rect x="{x+w/2-18}" y="{y+7}" width="36" height="5" rx="2.5" fill="{INK4}"/>'
    ix,iy,iw,ih=x+8,y+22,w-16,h-30
    s+=f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="6" fill="{PANEL}"/>'
    return s,(ix,iy,iw,ih)
def big_btn(x,y,w,h,label,sub=None,primary=False):
    fill=ACC if primary else "#FFFFFF"; stroke="none" if primary else INK4
    tc="#FFFFFF" if primary else INK1
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
    s+=T(x+w/2,y+(h/2+6 if not sub else h/2-2),label,15,tc,700,anchor="middle")
    if sub: s+=T(x+w/2,y+h/2+16,sub,10,("#FFFFFF" if primary else INK3),anchor="middle")
    return s

# ---- 真实照片占位框（禁 AI 生成 / 网图）----
def placeholder(x,y,w,h,label="现场实拍 · 待替换"):
    s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{PANEL}" stroke="{INK4}" stroke-width="1.2" stroke-dasharray="6 4"/>'
    s+=f'<path d="M{x+w/2-16} {y+h/2-2} l10 -12 l9 11 l7 -7 l12 17 Z" fill="#FFFFFF" stroke="{INK3}" stroke-width="1.3"/>'
    s+=f'<circle cx="{x+w/2-12}" cy="{y+h/2-12}" r="4" fill="none" stroke="{INK3}" stroke-width="1.3"/>'
    s+=T(x+w/2,y+h-16,label,11,INK3,anchor="middle")
    return s

# ---- 分层架构蓝图（ISA-95 风，通用 N 层）----
def blueprint(x,y,w,layers,row_h=56,gap=14,hi_index=None):
    """layers: [(name, level_label), ...] 自上而下。hi_index 高亮某层。"""
    s=""
    for i,(nm,lv) in enumerate(layers):
        ry=y+i*(row_h+gap); hl=(i==hi_index)
        s+=f'<rect x="{x}" y="{ry}" width="{w}" height="{row_h}" rx="10" fill="#FFFFFF" stroke="{ACC if hl else LINE}" stroke-width="{1.6 if hl else 1.2}"/>'
        if hl: s+=f'<rect x="{x}" y="{ry}" width="4" height="{row_h}" rx="2" fill="{ACC}"/>'
        s+=T(x+24,ry+row_h/2+6,nm,16,INK1,700)
        s+=T(x+w-18,ry+row_h/2+5,lv,12,INK3,fam=MONO,anchor="end")
    return s

# ---- 泳道流程（横向，多泳道 + 节点）----
def swimlane(x,y,w,lanes,lane_h=88,gap=10):
    """lanes: [(lane_name, [node1,node2,...]), ...] 仅画车道与节点框，连线请用 carrow 自接。"""
    s=""; label_w=120
    for i,(ln,nodes) in enumerate(lanes):
        ly=y+i*(lane_h+gap)
        s+=f'<rect x="{x}" y="{ly}" width="{w}" height="{lane_h}" rx="8" fill="{PANEL if i%2 else "#FFFFFF"}" stroke="{LINE}" stroke-width="1"/>'
        s+=f'<rect x="{x}" y="{ly}" width="{label_w}" height="{lane_h}" rx="8" fill="#FFFFFF" stroke="{LINE}" stroke-width="1"/>'
        s+=T(x+label_w/2,ly+lane_h/2+5,ln,13,INK1,600,anchor="middle")
        n=len(nodes);
        if n:
            slot=(w-label_w-40)/n; nw=min(slot-18,150)
            for j,nd in enumerate(nodes):
                nx=x+label_w+20+j*slot
                s+=f'<rect x="{nx}" y="{ly+lane_h/2-19}" width="{nw}" height="38" rx="8" fill="#FFFFFF" stroke="{INK4}" stroke-width="1.2"/>'
                s+=T(nx+nw/2,ly+lane_h/2+5,nd,12.5,INK1,anchor="middle")
    return s
