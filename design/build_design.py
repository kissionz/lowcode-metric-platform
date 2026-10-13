from pathlib import Path
from html import escape
root=Path(__file__).resolve().parent
P='oklch(0.49 0.19 258)'; INK='oklch(0.23 0.008 258)'; MUT='oklch(0.46 0.008 258)'; LINE='oklch(0.9 0.004 258)'; BG='oklch(0.98 0 0)'; TINT='oklch(0.96 0.015 258)'; WHITE='white'; GREEN='oklch(0.43 0.1 160)'; BLUE='oklch(0.52 0.12 245)'
def rect(x,y,w,h,fill=WHITE,stroke=LINE,r=8,dash=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def text(x,y,t,size=14,c=INK,weight=400):
 return f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" font-weight="{weight}">{escape(str(t))}</text>'
def button(x,y,w,t,primary=False):
 return rect(x,y,w,36,P if primary else WHITE,P if primary else LINE,6)+text(x+12,y+24,t,14,WHITE if primary else INK,500)
def pill(x,y,t,c=GREEN):
 w=len(t)*12+20
 return rect(x,y,w,24,BG,LINE,4)+text(x+10,y+17,t,12,c)
def line(x1,y1,x2,y2,c=LINE,dash=''):
 return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="1" '+(f'stroke-dasharray="{dash}"' if dash else '')+'/>'
def svg(body,slug,title,desc,h=800,w=1440):
 return f'<svg viewBox="0 0 {w} {h}" role="img" aria-labelledby="{slug}-title {slug}-desc"><title id="{slug}-title">{title}</title><desc id="{slug}-desc">{desc}</desc>{body}</svg>'
def shell(title,edit=False,empty=False):
 s=rect(0,0,1440,800,BG,LINE,0)+rect(0,0,1440,64,WHITE,LINE,0)
 s+=rect(20,18,28,28,P,P,6)+text(26,38,'✦',18,WHITE)+text(60,39,'北极星',20,INK,650)
 s+=text(180,38,'增长工作空间',14,MUT)+text(1284,38,'运营团队',14,MUT)+rect(1380,18,28,28,TINT,LINE,14)+text(1386,38,'林',12,P)
 if edit:
  s+=text(24,99,'‹ 我的看板',14,MUT)+text(148,99,title,18,INK,600)+pill(352,82,'草稿',MUT)+text(440,99,'✓ 已保存 · 刚刚',12,GREEN)
  s+=button(816,78,184,'✦ AI 一键生成')+button(1016,78,64,'撤销')+button(1088,78,64,'重做')+button(1160,78,88,'预览看板')+button(1260,78,152,'发布看板',True)
  s+=rect(0,124,264,676,WHITE,LINE,0)+rect(1108,124,332,676,WHITE,LINE,0)
 else:
  s+=rect(0,64,200,736,WHITE,LINE,0)
  for yy,t,sel in [(108,'▦  我的看板',True),(160,'◈  指标中心',False),(212,'▤  看板模板',False)]:
   if sel:s+=rect(16,yy-24,168,40,TINT,TINT,6)
   s+=text(32,yy,t,14,P if sel else MUT,600 if sel else 400)
  s+=text(24,744,'帮助与反馈',12,MUT)
 return s
def library():
 s=text(20,158,'添加组件',16,INK,600)+text(188,158,'收起 ‹',12,MUT)
 s+=rect(16,180,232,36,BG,LINE,6)+text(28,204,'⌕ 搜索指标名称或标签',12,MUT)
 s+=text(20,244,'全部指标',12,P,600)+text(100,244,'我的收藏',12,MUT)+line(16,256,248,256)
 s+=text(20,286,'增长指标  12',12,MUT)
 vals=[('日活跃用户数','去重计数 · 每日更新'),('新增用户数','计数 · 每日更新'),('注册转化率','比例 · 每日更新'),('次日留存率','比例 · 每日更新'),('获客成本','金额 · 每日更新')]
 for i,(t,d) in enumerate(vals):
  y=304+i*64
  s+=rect(16,y,232,52,TINT if i==0 else WHITE,P if i==0 else LINE,6)
  s+=text(28,y+24,'⠿',16,MUT)+text(48,y+24,t,14,INK,500)+text(48,y+44,d,12,MUT)+text(224,y+24,'+',16,P)
 s+=text(20,640,'内容组件',12,MUT)
 for i,t in enumerate(['图片','文本','网页']):s+=button(16+i*80,656,72,t)
 s+=line(16,716,248,716)+text(20,744,'拖拽到画布，或点击 + 添加',12,MUT)+text(20,768,'指标口径由分析师统一维护',12,MUT)
 return s
def trend(x,y,w,h):
 s=''
 for i in range(4):
  yy=y+i*h/3;s+=line(x,yy,x+w,yy)+text(x-40,yy+4,['14万','11万','8万','5万'][i],12,MUT)
 pts=[.72,.62,.70,.43,.54,.37,.48,.26,.32,.14,.23,.10]
 coords=[(x+i*w/11,y+p*h) for i,p in enumerate(pts)]
 path='M'+' L'.join(f'{a:.1f} {b:.1f}' for a,b in coords)
 s+=f'<path d="{path} L{x+w} {y+h} L{x} {y+h} Z" fill="{TINT}"/>'
 s+=f'<path d="{path}" fill="none" stroke="{P}" stroke-width="3" stroke-linejoin="round"/>'
 for i,t in enumerate(['09/13','09/20','09/27','10/04','10/12']):s+=text(x+i*w/4-8,y+h+24,t,12,MUT)
 return s
def card(x,y,w,h,title,selected=False):
 s=rect(x,y,w,h,WHITE,P if selected else LINE,8)+text(x+20,y+32,title,14,INK,600)+text(x+w-28,y+32,'⋯',18,MUT)
 if selected:
  for xx,yy in [(x-4,y-4),(x+w-4,y-4),(x-4,y+h-4),(x+w-4,y+h-4)]:s+=rect(xx,yy,8,8,WHITE,P,0)
 return s
def kpi(x,y,w,title,val,sub):
 return card(x,y,w,136,title)+text(x+20,y+78,val,30,INK,600)+text(x+20,y+110,sub,12,GREEN)
def bar(x,y,w):
 s=''
 for i,(t,n,l) in enumerate([('自然搜索','7,420',.9),('内容推荐','5,240',.64),('付费广告','3,950',.48),('直接访问','2,310',.28)]):
  yy=y+i*44;s+=text(x,yy+16,t,12,MUT)+rect(x+72,yy+4,(w-152)*l,16,P if i==0 else BLUE,P if i==0 else BLUE,2)+text(x+w-64,yy+16,n,12,INK)
 return s
# List
s=shell('我的看板')+text(232,124,'我的看板',28,INK,650)+text(232,156,'把日常关注的指标，组织成团队的决策视图。',14,MUT)+button(1088,96,164,'✦ AI 一键生成')+button(1264,96,144,'+ 新建看板',True)
s+=rect(232,192,300,36,WHITE,LINE,6)+text(244,216,'⌕ 搜索看板',14,MUT)+text(564,216,'全部  8',14,P,600)+text(668,216,'我创建的',14,MUT)+text(784,216,'共享给我',14,MUT)
s+=rect(232,252,1176,468,WHITE,LINE,8)+rect(232,252,1176,44,BG,LINE,0)
for x,t in [(252,'看板名称'),(808,'状态'),(936,'创建人'),(1064,'最近更新'),(1312,'操作')]:s+=text(x,280,t,12,MUT,500)
rows=[('增长经营总览','日活、新增、转化与渠道效果','已发布','林晓','今天 10:32'),('新用户转化分析','从访问到注册的转化链路','草稿','林晓','今天 09:15'),('渠道投放周报','获客成本、渠道规模和趋势','已发布','陈安','10/11 18:40'),('产品留存观察','新老用户留存与活跃分布','已发布','陈安','10/10 16:20')]
for i,(a,b,c,d,e) in enumerate(rows):
 y=316+i*92;s+=rect(252,y,40,40,TINT,TINT,6)+text(264,y+27,'▦',20,P)+text(312,y+17,a,16,INK,600)+text(312,y+42,b,12,MUT)+pill(808,y+8,c,GREEN if c=='已发布' else MUT)+text(936,y+28,d)+text(1064,y+28,e,14,MUT)+text(1312,y+28,'打开  ⋯',14,P)
 if i<3:s+=line(252,y+72,1388,y+72)
s+=text(232,756,'新建看板：填写名称 → 选择空白画布或模板 → 进入编辑器',12,MUT)
list_svg=svg(s,'boards','看板列表设计稿','集中管理草稿与已发布看板，从新建入口开始搭建。')
# empty
s=shell('增长经营总览',True)+library()+text(292,158,'看板画布',14,INK,600)+text(920,158,'12 列网格  ·  100%',12,MUT)
s+=rect(292,184,788,556,WHITE,LINE,8,'6 6')+rect(600,324,160,104,TINT,LINE,8)+text(640,389,'⠿  指标',20,P,500)
s+=text(500,472,'拖入第一个指标，开始搭建',24,INK,600)+text(464,508,'从左侧选择指标；我们会生成适合它的默认图表。',14,MUT)+button(572,544,132,'添加指标')+button(720,544,132,'选择模板')
s+=text(1132,158,'看板设置',16,INK,600)
for yy,l,v in [(204,'看板名称','增长经营总览'),(292,'默认时间范围','最近 30 天'),(380,'画布布局','12 列 · 自动吸附'),(468,'组件间距','16 px')]:s+=text(1132,yy,l,12,MUT)+rect(1132,yy+16,284,36,WHITE,LINE,6)+text(1144,yy+40,v)
s+=text(1132,592,'添加组件后',14,INK,600)+text(1132,620,'点击组件，即可在这里调整',12,MUT)+text(1132,640,'图表类型、维度与展示计算。',12,MUT)
empty_svg=svg(s,'empty','空画布设计稿','左侧提供指标，画布解释拖拽与点击添加两种方式，右侧先展示看板设置。')
# editor
s=shell('增长经营总览',True)+library()+text(288,157,'编辑布局',14,INK,600)+text(940,157,'12 列 · 自动吸附',12,MUT)
s+=rect(288,180,796,44,WHITE,LINE,6)+text(304,208,'全局筛选',12,MUT)+pill(380,190,'最近 30 天',INK)+pill(504,190,'渠道：全部',INK)+text(652,208,'+ 添加筛选',12,P)
s+=kpi(288,244,252,'日活跃用户数（最新日）','128,460','↑ 12.8%  较上一周期')+kpi(560,244,252,'新增用户数（期间）','18,920','↑ 8.4%  较上一周期')+kpi(832,244,252,'注册转化率','6.42%','↑ 0.36 个百分点')
s+=card(288,400,796,332,'日活跃用户趋势',True)+text(308,456,'按日 · 去重用户数 · 跟随全局筛选',12,MUT)+trend(340,492,704,176)
s+=text(292,772,'拖动组件标题移动位置  ·  拖动边角调整大小  ·  支持撤销',12,MUT)
s+=text(1132,158,'组件配置',16,INK,600)+text(1132,188,'日活跃用户趋势',14,MUT)+text(1132,228,'数据',14,P,600)+text(1212,228,'样式',14,MUT)+text(1292,228,'交互',14,MUT)+line(1132,244,1416,244)
s+=text(1132,276,'指标',12,MUT)+rect(1132,288,284,40,BG,LINE,6)+text(1144,314,'日活跃用户数   查看口径 ↗',14,INK)
s+=text(1132,364,'展现形式',12,MUT)
for i,(t,sel) in enumerate([('指标卡',False),('折线',True),('柱状',False),('饼图',False),('表格',False)]):s+=rect(1132+i*58,380,52,48,TINT if sel else WHITE,P if sel else LINE,6)+text(1140+i*58,410,t,12,P if sel else MUT)
for yy,l,v in [(460,'展示维度','日期 · 按日'),(548,'展示计算','指标默认值 · 去重计数'),(636,'时间范围','跟随看板全局时间')]:s+=text(1132,yy,l,12,MUT)+rect(1132,yy+12,284,36,WHITE,LINE,6)+text(1144,yy+36,v,14,INK)+text(1392,yy+36,'⌄',12,MUT)
s+=text(1132,712,'跨日去重需重新查询原始用户集合。',12,MUT)+text(1132,732,'此指标不支持直接累加每日人数。',12,MUT)+button(1132,752,284,'应用到组件',True)
editor_svg=svg(s,'editor','看板编辑器设计稿','三栏编辑器展示指标中心、可调整布局的画布，以及选中折线图的数据配置。')
# view
s=shell('增长经营总览')+text(232,120,'增长经营总览',28,INK,650)+pill(468,100,'已发布')+text(232,152,'覆盖活跃规模、新用户增长与渠道转化。',14,MUT)+button(1136,96,96,'刷新数据')+button(1244,96,72,'分享')+button(1328,96,80,'编辑',True)
s+=rect(232,180,1176,48,WHITE,LINE,6)+text(248,210,'筛选',12,MUT)+pill(300,192,'最近 30 天',INK)+pill(436,192,'渠道：全部',INK)+text(1020,210,'数据更新于 2026/10/12 09:00',12,MUT)
s+=kpi(232,248,376,'日活跃用户数（最新日）','128,460','↑ 12.8%  较上一周期')+kpi(632,248,376,'新增用户数（期间）','18,920','↑ 8.4%  较上一周期')+kpi(1032,248,376,'注册转化率','6.42%','↑ 0.36 个百分点')
s+=card(232,408,736,320,'日活跃用户趋势')+text(252,460,'● 日活跃用户数',12,P)+trend(280,488,636,176)+card(992,408,416,320,'新增用户渠道分布')+text(1012,460,'按渠道汇总 · 最近 30 天',12,MUT)+bar(1012,488,372)
s+=text(232,772,'查看模式：点击图表可查看数据明细与指标口径；当前筛选仅影响本次查看。',12,MUT)
view_svg=svg(s,'viewer','已发布看板查看页设计稿','隐藏编辑面板，让团队使用全局筛选并阅读趋势与渠道对比，展示数据更新时间。')
# Creation entry and AI conversation designs
base=list_svg.split('</desc>',1)[1].rsplit('</svg>',1)[0]
s=base+f'<rect width="1440" height="800" fill="{INK}" opacity="0.16"/>'
s+=rect(400,176,640,440,WHITE,LINE,12)+text(432,220,'新建看板',24,INK,600)+text(1000,220,'×',20,MUT)
s+=text(432,264,'看板名称',12,MUT)+rect(432,280,576,40,WHITE,LINE,6)+text(448,306,'增长经营总览')
s+=rect(432,344,276,160,WHITE,LINE,8)+text(452,376,'▦ 手工搭建',18,INK,600)+text(452,408,'从空白画布或模板开始',14,MUT)+text(452,436,'选择指标、配置图表、调整布局',12,MUT)+button(452,456,236,'创建空白看板')
s+=rect(732,344,276,160,TINT,P,8)+text(752,376,'✦ AI 一键生成',18,INK,600)+text(752,408,'选好指标，描述分析目标',14,MUT)+text(752,436,'AI 自动组织图表、筛选与布局',12,MUT)+button(752,456,236,'打开 AI 对话',True)
s+=text(432,556,'两种方式生成的看板，都支持完整手工编辑。',14,MUT)+text(432,584,'需要现成结构？  从模板创建 →',12,P)
create_svg=svg(s,'create','新建看板的两种入口','新建看板弹窗提供手工搭建与 AI 一键生成，两者进入同一个看板编辑器。')
base=shell('增长经营总览',True)+library()+text(288,158,'看板画布',14,INK,600)+rect(288,184,648,556,WHITE,LINE,8,'6 6')+rect(544,324,136,104,TINT,LINE,8)+text(572,388,'⠿ 指标',20,P,500)+text(384,472,'拖入指标，或用 AI 生成',24,INK,600)+text(368,508,'右侧选好指标与分析方式，即可构建看板。',14,MUT)+button(460,544,132,'添加指标')+button(612,544,132,'选择模板')
s=base+rect(960,124,480,676,WHITE,LINE,0)
s+=text(984,158,'✦ AI 看板助手',18,INK,600)+text(1328,158,'收起 ›',14,MUT)+line(960,180,1440,180)
s+=text(984,208,'帮你把业务问题组织成一张看板。',14,MUT)
s+=rect(984,228,432,84,BG,LINE,8)+text(1000,252,'选择你关注的指标',14,INK,600)
for x,w,t in [(1000,120,'✓ 日活用户'),(1132,120,'✓ 新增用户'),(1264,132,'✓ 注册转化率')]:s+=rect(x,268,w,28,TINT,LINE,4)+text(x+8,288,t,12,P)
s+=text(984,340,'已选 3 项  ·  添加指标 +  ·  查看指标口径',12,P)
s+=rect(1032,360,384,60,TINT,TINT,8)+text(1048,384,'我想看最近 30 天的增长表现，',14,INK)+text(1048,404,'并比较不同渠道的新用户贡献。',14,INK)
s+=text(984,452,'建议从这三个角度查看，你也可以调整：',14,INK,500)
for y,t,sub in [(472,'✓ 规模总览与环比','3 张指标卡 · 与上一周期比较'),(528,'✓ 日活变化趋势','按日期查看日活变化，跟随全局时间'),(584,'✓ 渠道贡献对比','新增用户按渠道分组，降序排列')]:
 s+=rect(984,y,432,48,WHITE,LINE,6)+text(1000,y+20,t,14,P,500)+text(1000,y+38,sub,12,MUT)
s+=text(984,658,'将生成 5 个组件 · 最近 30 天 · 12 列布局',12,MUT)+line(960,676,1440,676)
s+=rect(984,692,432,44,WHITE,LINE,6)+text(1000,720,'补充分析目标或调整生成方案…',14,MUT)
s+=text(984,772,'可收起对话，继续操作画布',12,MUT)+button(1272,748,144,'生成看板',True)
ai_svg=svg(s,'ai','AI 一键生成的右侧对话抽屉','用户在可收起的右侧抽屉选择指标、描述目标并选择分析方式，AI 按方案生成普通看板组件。')
base=editor_svg.split('</desc>',1)[1].rsplit('</svg>',1)[0]
s=base+rect(284,392,804,348,BG,BG,0)+card(288,400,472,332,'日活跃用户趋势',True)+text(308,456,'按日 · 跟随全局筛选',12,MUT)+trend(340,492,388,176)+card(780,400,304,332,'新增用户渠道分布')+text(800,456,'按渠道 · 降序',12,MUT)+bar(800,492,264)+rect(724,140,188,32,TINT,LINE,6)+text(736,162,'✦ AI 对话 · 展开',12,P,500)
s+=rect(480,744,580,36,WHITE,LINE,6)+text(496,768,'✓ 已生成看板 · 5 个组件均可继续编辑',14,GREEN)
ready_svg=svg(s,'ai-ready','AI 生成后继续手工编辑','AI 收起为可展开入口，生成的看板使用普通组件配置面板，可移动、缩放和修改。')

# Mixed content component board
s=shell('增长经营总览',True)+library()+text(288,158,'编辑布局',14,INK,600)+text(940,158,'12 列 · 自动吸附',12,MUT)
s+=rect(288,180,796,44,WHITE,LINE,6)+text(304,208,'全局筛选',12,MUT)+pill(380,190,'最近 30 天',INK)+pill(504,190,'渠道：全部',INK)
s+=card(288,244,796,112,'文本 · 本周增长观察')+text(308,306,'新增用户增长 8.4%，自然搜索贡献最多。',18,INK,600)+text(308,334,'关注注册链路转化，持续跟踪渠道获客效率。',14,MUT)
s+=card(288,376,388,348,'图片 · 本月增长活动',True)
s+=rect(308,432,348,240,BG,LINE,6)+rect(340,472,284,144,TINT,LINE,8)+text(364,514,'秋季增长计划',24,P,600)+text(364,546,'品牌活动素材预览',14,MUT)+button(364,568,144,'查看活动内容')+text(308,704,'活动素材.png · 等比适应 · 可替换',12,MUT)
s+=card(696,376,388,348,'网页 · 活动进度')+rect(716,432,348,40,BG,LINE,6)+text(732,458,'活动进度页面 · 内嵌预览',12,MUT)+rect(716,472,348,200,WHITE,LINE,0)+text(736,504,'活动执行概览',18,INK,600)
for i,(t,status) in enumerate([('落地页上线','已完成'),('渠道素材发布','已完成'),('转化效果复盘','进行中')]):s+=line(736,532+i*40,1044,532+i*40)+text(736,558+i*40,t,14,INK)+text(980,558+i*40,status,12,GREEN)
s+=text(716,704,'打不开内嵌内容？  在新标签页打开 ↗',12,P)
s+=text(1132,158,'图片配置',16,INK,600)+text(1132,188,'本月增长活动',14,MUT)+line(1132,208,1416,208)
for yy,l,v in [(244,'图片来源','上传图片   /   图片链接'),(332,'当前图片','活动素材.png    替换图片'),(420,'显示方式','等比适应 ⌄'),(508,'替代文本','秋季增长活动的宣传素材'),(596,'点击行为','打开活动详情链接')]:s+=text(1132,yy,l,12,MUT)+rect(1132,yy+16,284,40,WHITE,LINE,6)+text(1144,yy+42,v,14,INK)
s+=text(1132,696,'图片、文本和网页沿用同一布局规则。',12,MUT)+text(1132,718,'可移动、缩放、复制、删除和撤销。',12,MUT)+button(1132,752,284,'应用到组件',True)
content_svg=svg(s,'content','图片、文本与网页混合看板','看板中添加文本说明、活动图片和网页内嵌组件，选中图片后在右侧配置来源、显示方式与替代文本。')

# diagram two standalone inline, 4px grid
arrow='<defs><marker id="{slug}-arrow" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="'+MUT+'"/></marker></defs>'
def flow(slug,labels,subs):
 s=arrow.replace('{slug}',slug)
 for i in range(4):s+=f'<path d="M{224+i*240} 100 H{256+i*240}" stroke="{MUT}" fill="none" marker-end="url(#{slug}-arrow)"/>'
 for i,(a,b) in enumerate(zip(labels,subs)):
  x=16+i*240;s+=rect(x,60,208,80,TINT if i==2 else WHITE,P if i==2 else LINE,8)+text(x+16,92,a,16,INK,600)+text(x+16,120,b,12,MUT)
 s+=line(16,180,1184,180)+text(16,208,'实线箭头：用户推进主流程    ·    高亮节点：主要操作区域',12,MUT)
 return svg(s,slug,'主交互流程' if slug=='journey' else ('AI 构建看板流程' if slug=='ai-flow' else '拖入指标后的反馈'), '说明用户的顺序操作，以及每个步骤产生的反馈。',240,1200)
flow1=flow('journey',['新建看板','选择指标','搭建与配置','预览检查','发布与分享'],['名称、空白或模板','搜索、收藏、查看口径','拖拽、维度、展示计算','查看布局与筛选结果','选择成员与访问范围'])
ai_flow=flow('ai-flow',['打开 AI 抽屉','选指标与目标','选择分析方式','AI 构建看板','继续手工编辑'],['可随时收起、恢复对话','只选已授权的真实指标','趋势、对比、构成、环比','统一组件、筛选与布局','拖拽、缩放、配置、发布'])
flow2=flow('drop',['开始拖拽','悬停画布','松手生成','调整配置','应用配置'],['指标卡片跟随指针','显示落点、尺寸占位','推荐图表、加载示例','先预览新配置结果','替换图表、记录撤销'])
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:oklch(0.98 0 0);color:oklch(0.23 0.008 258);font:16px/1.65 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}header{padding:48px max(28px,calc((100vw - 1440px)/2));background:white;border-bottom:1px solid oklch(0.9 0.004 258)}header .meta{color:oklch(0.46 0.008 258);font-size:14px}h1{font-size:36px;line-height:1.3;margin:14px 0}h2{font-size:24px;margin:0 0 8px}h3{font-size:18px;margin:20px 0 8px}p{margin:8px 0;max-width:76ch}nav{display:flex;gap:24px;flex-wrap:wrap;margin-top:24px}a{color:oklch(0.49 0.19 258);text-decoration:none}a:hover{text-decoration:underline}main{max-width:1496px;padding:36px 28px 64px;margin:auto}section{scroll-margin-top:24px;margin-bottom:56px}.intro{display:grid;grid-template-columns:1.3fr 1fr;gap:48px}.notes{color:oklch(0.46 0.008 258);font-size:14px;margin-bottom:20px}figure{margin:24px 0 12px;background:white;border:1px solid oklch(0.9 0.004 258);border-radius:8px;overflow:hidden}svg{display:block;width:100%;height:auto;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}figcaption{padding:16px 24px;border-top:1px solid oklch(0.9 0.004 258);color:oklch(0.46 0.008 258);font-size:14px}.annotation{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;padding:8px 0}.annotation b{display:block}.annotation p{font-size:14px;color:oklch(0.46 0.008 258)}table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px;background:white}th,td{text-align:left;border-bottom:1px solid oklch(0.9 0.004 258);padding:16px;vertical-align:top}th{background:oklch(0.96 0 0)}.status{display:inline-block;background:oklch(0.96 0.015 258);color:oklch(0.49 0.19 258);padding:4px 10px;border-radius:4px;font-size:13px}footer{border-top:1px solid oklch(0.9 0.004 258);padding-top:24px;color:oklch(0.46 0.008 258);font-size:14px}@media(max-width:800px){.intro,.annotation{grid-template-columns:1fr;gap:16px}header{padding:28px}h1{font-size:28px}figure{overflow-x:auto}figure svg{min-width:1000px}table{min-width:720px}.table-wrap{overflow:auto}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{header{padding:16px}nav{display:none}main{padding:16px}section{break-inside:avoid}figure svg{min-width:0}figure{break-inside:avoid}}'''
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%277%27 fill=%27%232563eb%27/%3E%3C/svg%3E"><meta name="viewport" content="width=device-width,initial-scale=1"><title>北极星 · 拖拽指标看板设计提案</title><style>{css}</style></head><body><header><div class="meta">北极星 / 产品与交互设计 / 2026.10.12</div><h1>从一个指标，到一张业务看板。</h1><p>业务运营快速搭建，分析师维护可信指标。让“选数据、看结果、调布局”留在同一个工作空间。</p><nav><a href="#plan">产品规划</a><a href="#boards">看板管理</a><a href="#create">创建看板</a><a href="#ai">AI 生成</a><a href="#empty">空画布</a><a href="#editor">编辑器</a><a href="#components">内容组件</a><a href="#viewer">查看看板</a><a href="#flows">交互示意</a><a href="#rules">配置与状态</a><a href="#scope">阶段范围</a></nav></header><main>
<section id="plan"><div class="intro"><div><h2>先定产品骨架</h2><p>创建入口提供手工搭建与 AI 一键生成。手工路径：新建看板 → 添加指标 → 生成推荐图表 → 配置展示 → 调整布局 → 预览 → 发布。首个指标使用推荐默认配置，减少首次搭建的表单负担。</p><h3>两个角色，一套可信口径</h3><p>运营拥有看板创建和组件配置权限；分析师维护指标定义、可用维度、默认聚合与更新时间。指标中心里的口径变化应展示版本提示，并在发布前检查受影响组件。</p></div><div><h3>本稿的设计定位</h3><p>运营在办公室的桌面电脑上，边查看业务结果边组织周会看板。因此采用浅色工作台、稳定三栏布局、中性灰层次与蓝色关键操作。</p><p>当前交付为静态设计稿与交互规格。图中按钮、筛选和拖拽反馈用于说明设计；数据均为示例。桌面编辑优先，移动端先支持查看。</p><span class="status">待审阅 · 设计方案 v3</span></div></div></section>
<section id="boards"><h2>看板管理：找到最近使用的工作视图</h2><p class="notes">列表优先呈现名称、状态和更新时间；新建入口始终可见。支持复制看板、收藏、归档与按名称搜索。</p><figure>{list_svg}<figcaption>新建看板弹窗提供手工搭建、AI 一键生成与模板入口；列表页也可直接打开 AI 对话。</figcaption></figure></section>
<section id="create"><h2>新建看板：选择适合任务的创建方式</h2><p class="notes">一个创建入口，手工搭建与 AI 生成共用名称、权限和保存规则。</p><figure>{create_svg}<figcaption>点击 AI 一键生成后创建看板草稿，并在编辑器右侧打开对话抽屉；关闭创建弹窗前不创建草稿。</figcaption></figure></section>
<section id="ai"><h2>AI 一键生成：从指标与业务问题开始</h2><p class="notes">右侧 480px 非模态抽屉，画布仍可操作。打开时临时替代组件配置区；收起后恢复普通配置面板，对话保留。</p><figure>{ai_svg}<figcaption>指标用结构化选择器添加，业务目标可自由输入。AI 给出可选择的分析方式及组件方案，点击“生成看板”后自动构建。</figcaption></figure><div class="annotation"><div><b>按问题组织分析</b><p>规模总览、时间趋势、渠道对比、占比构成、同比环比。仅推荐指标支持的维度与计算；用户可勾选、移除或继续对话。</p></div><div><b>随时收起与恢复</b><p>保留会话、已选指标、未发送输入和后台生成任务。收起入口显示生成中或完成状态；展开回到原位置。</p></div><div><b>统一看板能力</b><p>AI 输出同一套指标引用、组件配置、筛选与网格布局。数据查询、编辑、撤销、保存、发布和权限校验使用相同规则。</p></div></div><figure>{ready_svg}<figcaption>生成完成后抽屉可收起，普通组件自动呈现在画布上。点击任意组件即可手工修改，也可展开对话继续优化。</figcaption></figure><h3>生成与迭代规则</h3><div class="table-wrap"><table><thead><tr><th>阶段</th><th>交互</th><th>结果</th></tr></thead><tbody><tr><td>指标选择</td><td>搜索、多选、查看口径；支持对话推荐后显式选择</td><td>指标标识与权限来自指标中心；无法解析时列出候选，待用户选择</td></tr><tr><td>分析方案</td><td>选择分析方式、时间、维度与比较周期；查看预计组件</td><td>默认方案可直接生成；缺少必要条件时针对性追问</td></tr><tr><td>构建看板</td><td>展示准备方案、校验配置、构建组件的进度，支持取消和收起</td><td>校验完成后作为一次变更写入草稿；失败保留对话与原画布，支持重试</td></tr><tr><td>已有看板调整</td><td>对话生成变更预览，明确新增、修改与删除范围，再应用</td><td>应用为一次可撤销操作；手工编辑期间的版本变化须重新预览后应用</td></tr><tr><td>继续编辑与发布</td><td>使用普通组件配置、布局和发布入口</td><td>AI 与手工看板采用相同文档结构和权限，生成完成后保存草稿</td></tr></tbody></table></div></section>
<section id="empty"><h2>空画布：先完成第一次添加</h2><p class="notes">指标中心留在编辑器左侧，支持拖拽与点击 + 两种入口；模板用于提供初始布局与配置。</p><figure>{empty_svg}<figcaption>新增组件默认遵循指标推荐形式；指标加载后直接展示结果，再由用户按需修改。</figcaption></figure><div class="annotation"><div><b>指标卡片</b><p>显示名称、类型与新鲜度。点击名称查看业务解释、口径、可用维度、负责人。</p></div><div><b>首屏引导</b><p>画布给出明确下一步；点击添加也能完成操作，避免把拖拽作为唯一入口。</p></div><div><b>默认设置</b><p>名称、全局时间和布局在未选中组件时显示。指标默认配置随新增动作一起带入。</p></div></div></section>
<section id="editor"><h2>编辑器：搭建与配置在同一处完成</h2><p class="notes">左侧添加指标与内容，中间验证结果，右侧配置选中组件。指标卡回答“多少”，趋势回答“变化”，分组图表回答“来自哪里”。</p><figure>{editor_svg}<figcaption>选中组件显示边框与缩放柄；标题区域负责拖动。右侧编辑先预览，再点击“应用到组件”，避免半完成配置影响画布。</figcaption></figure><div class="annotation"><div><b>数据配置</b><p>展现形式、维度、展示计算、时间范围、组件筛选、排序与 Top N；仅显示指标支持的选项。</p></div><div><b>样式配置</b><p>标题、单位、小数位、颜色、图例、坐标轴、目标线。按图表类型逐项出现。</p></div><div><b>交互配置</b><p>第一版支持查看明细和口径。后续加入图表联动与维度下钻，并显式展示筛选范围。</p></div></div></section>
<section id="components"><h2>添加组件：数据与内容共同组织业务信息</h2><p class="notes">左侧统一“添加组件”：指标组件提供五种展现形式；内容组件提供图片、文本和网页。点击或拖入创建占位，选中后在右侧完成配置。</p><figure>{content_svg}<figcaption>文本用于说明结论与口径，图片用于活动素材或业务截图，网页用于嵌入已有工作页面。全部组件使用同一网格、撤销、保存和发布流程。</figcaption></figure><h3>指标的五种展现形式</h3><div class="table-wrap"><table><thead><tr><th>展现形式</th><th>用途</th><th>核心配置</th></tr></thead><tbody><tr><td>指标卡</td><td>总量、最新值、比例与目标达成</td><td>单位、小数位、比较周期、目标值、趋势提示</td></tr><tr><td>折线</td><td>按时间查看变化</td><td>时间维度、粒度、系列、图例、坐标轴</td></tr><tr><td>柱状</td><td>分类或时间对比</td><td>分组、方向、排序、堆叠、Top N</td></tr><tr><td>饼图</td><td>同一整体的构成比例</td><td>分类维度、占比标签、图例、其他项；支持环形样式。须可加、非负且整体大于零</td></tr><tr><td>表格</td><td>多维度明细与精确数值</td><td>列选择、排序、分页、单位、汇总行；汇总遵循指标口径</td></tr></tbody></table></div><h3>内容组件配置</h3><div class="table-wrap"><table><thead><tr><th>组件</th><th>添加与编辑</th><th>展示和异常状态</th></tr></thead><tbody><tr><td>图片</td><td>上传或粘贴图片链接；替换、替代文本、点击链接、等比适应/填充裁剪</td><td>加载占位、上传进度、失效图片提示；组件尺寸变化时保持图片比例</td></tr><tr><td>文本</td><td>就地编辑；标题、段落、列表、粗体、链接、对齐、字号与颜色</td><td>支持长文滚动与高度调整；内容作为看板文档保存，编辑时显示文本工具栏</td></tr><tr><td>网页</td><td>输入 HTTPS 地址；配置标题、刷新和内嵌滚动，提供在新标签页打开入口</td><td>预览前检查链接；目标站点禁止嵌入或要求登录时明确提示，并提供打开原网页入口</td></tr></tbody></table></div><div class="annotation"><div><b>统一添加</b><p>点击内容组件即创建占位并打开配置，也可拖到指定位置。尚未完成配置显示“待配置”，发布检查会指出缺失项。</p></div><div><b>统一操作</b><p>全部组件支持移动、缩放、复制、删除与撤销；全局指标筛选只作用于兼容的数据组件，内容组件保留自身配置。</p></div><div><b>AI 与手工一致</b><p>AI 可生成文本标题与分析说明，并使用用户提供的图片和网页。内容资产、图表配置和网格位置存入同一看板文档。</p></div></div></section>
<section id="viewer"><h2>查看页：把空间还给业务结果</h2><p class="notes">查看与编辑分开。全局筛选、更新时间、口径说明始终可达；分享沿用成员访问权限。</p><figure>{view_svg}<figcaption>查看筛选是当前会话状态，不改变作者保存的默认配置。重新编辑时创建草稿，线上已发布版本持续可访问。</figcaption></figure></section>
<section id="flows"><h2>交互示意：主流程与即时反馈</h2><p class="notes">三张顺序流程图分别说明手工搭建、AI 生成，以及拖拽动作中的视觉反馈。错误与回退规则见下表。</p><figure>{flow1}</figure><figure>{ai_flow}</figure><figure>{flow2}</figure><div class="annotation"><div><b>落点与碰撞</b><p>12 列网格显示占位，周围组件自动让位。落在已有组件上时继续视为新组件；替换指标通过组件菜单显式操作。</p></div><div><b>安全修改</b><p>移动、缩放、删除和应用配置都进入撤销栈。组件右侧配置存在未应用更改时，切换组件须提示应用或放弃。</p></div><div><b>发布检查</b><p>检查指标权限、维度兼容性和配置完整性。预览使用查看页布局；发布时选定访问范围并生成版本。</p></div></div></section>
<section id="rules"><h2>配置规则：把复杂计算收在可信指标后面</h2><div class="table-wrap"><table><thead><tr><th>配置项</th><th>建议行为</th><th>例子与边界</th></tr></thead><tbody>
<tr><td>指标定义</td><td>分析师维护，运营可查看口径与版本</td><td>注册转化率 = 注册用户数 / 访问用户数；组件保留指标标识与口径版本</td></tr>
<tr><td>展现形式</td><td>按类型推荐，按兼容性限制</td><td>时间维度推荐折线；类别推荐条形；无分组推荐指标卡；占比图仅在可加且非负时提供</td></tr>
<tr><td>展示维度</td><td>只列出已授权且指标支持的维度</td><td>日期可选日/周/月；渠道维度支持排序与 Top N，其余并入“其他”并注明</td></tr>
<tr><td>展示计算</td><td>默认口径、累计、同比、环比；按能力开放</td><td>跨渠道转化率重新聚合分子分母；去重人数跨天重新去重；库存取期末值。累计只用于可累计指标</td></tr>
<tr><td>比较周期</td><td>说明基准周期和完整性</td><td>较上一周期、去年同期；区分百分比变化与百分点差值，分母为零显示“无法比较”</td></tr>
<tr><td>筛选关系</td><td>全局筛选与组件局部筛选取交集</td><td>组件可覆盖时间范围，并显示“独立时间”标记；不支持某筛选时标记“不适用”，不静默忽略</td></tr>
<tr><td>保存与发布</td><td>自动保存草稿，显式发布版本</td><td>新组件完整生成或应用配置后保存；保存失败提示重试；发布失败保留草稿和原线上版本</td></tr>
<tr><td>布局与尺寸</td><td>网格吸附、按图表限制最小尺寸</td><td>指标卡最小 2 列；图表最小 4 列。提供宽高输入与移动操作作为键盘替代；窄屏按阅读顺序堆叠</td></tr>
</tbody></table></div><h3>状态必须让人知道下一步</h3><div class="table-wrap"><table><thead><tr><th>状态</th><th>画布反馈</th><th>操作</th></tr></thead><tbody><tr><td>数据加载中</td><td>组件骨架；已有结果重新加载时保留旧图并标记“更新中”</td><td>支持取消查询；保留布局</td></tr><tr><td>无数据</td><td>提示当前时间和筛选下无结果，区分 0 与缺失</td><td>调整筛选或查看口径</td></tr><tr><td>配置不兼容</td><td>指出字段与原因，例如“此指标不支持渠道维度”</td><td>返回配置；应用按钮禁用并说明原因</td></tr><tr><td>查询失败或超时</td><td>组件内错误信息与更新时间，不影响其他组件</td><td>重试、查看错误详情</td></tr><tr><td>权限不足</td><td>遮挡数据，提示向负责人申请访问</td><td>查看申请入口；分享不扩大底层数据权限</td></tr><tr><td>未保存或网络中断</td><td>明确“保存失败”，保留本次修改并提示离开风险</td><td>重试保存；恢复网络后继续</td></tr></tbody></table></div></section>
<section id="scope"><h2>按两阶段落地</h2><div class="table-wrap"><table><thead><tr><th>阶段</th><th>覆盖内容</th><th>验收重点</th></tr></thead><tbody><tr><td>确认后：高保真原型</td><td>新建看板；AI 对话抽屉、指标多选、分析方式选择、模拟生成及普通组件编辑；指标搜索、点击与拖拽；图片、文本、网页添加与配置；指标卡、折线、柱状、饼图、表格；推荐图表；类型/维度/展示计算切换；移动与缩放；撤销/重做；本地草稿；预览和模拟发布</td><td>用示例数据走通完整路径，验证操作反馈、配置约束、布局与状态；AI 原型使用示例生成流程，模拟生成与发布明确标记</td></tr><tr><td>后续：业务接入</td><td>真实 AI 方案生成服务、指标查询服务、口径版本、真实权限、服务端保存、版本发布、数据刷新；再加入协同编辑、下钻、联动、导出与告警</td><td>查询正确性、性能、权限与数据新鲜度；发布版本可追溯</td></tr></tbody></table></div><h3>这一轮重点确认</h3><p>① 添加组件入口是否清晰；② 五种指标展现形式的配置范围；③ 图片、文本和网页的编辑方式；④ AI 生成与手工编辑的衔接。</p></section><footer>设计提案 v3 · 全部界面为静态稿，数据与人员为示例 · 建议桌面审阅；窄屏可横向查看画布。</footer></main></body></html>'''
(root/'design-review.html').write_text(html)
print(root/'design-review.html')
