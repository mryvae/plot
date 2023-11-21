from pyecharts.charts import Bar, Line
from pyecharts import options as opts

x = ['0.5K', '1K', '2K', '4K', '8K', '16K', '32K', '64K']

y1 = [61,77,115,134,202,272,433,751]
y = [257,256,286,315,465,965,2173,5218]

z1 = [64,83,220,296,576,1149,2332,4575]
z2 = [215,244,215,268,267,379,547,815]
z3 = [253,272,293,336,412,569,905,1468]
z4 = [287,309,317,323,389,373,516,732]
z5 = [32,51,91,183,381,743,1511,3093]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('load balance',
              z1,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('push',
              z2,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('run',
              z3,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('pull',
              z4,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('merge',
              z5,
              label_opts=opts.LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=opts.TitleOpts('read and write scenario'),
    tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type='cross'),
    xaxis_opts=opts.AxisOpts(name='A.nnz\nplus.nnz\nminus.nnz',type_='category', axispointer_opts=opts.AxisPointerOpts(
        is_show=True, type_='shadow')),
    yaxis_opts=opts.AxisOpts(name='lattency/us')
)

bar.extend_axis(yaxis=opts.AxisOpts(
    min_=0, max_=7,
    interval=1.4,
    # axislabel_opts=opts.LabelOpts(formatter='{value} us')
))

line = Line()
line.add_xaxis(x)
line.add_yaxis('speedup',
               y1,
               yaxis_index=1,
               label_opts=opts.LabelOpts(is_show=False)
               )


bar.overlap(line)  # 合并图
bar.render(path="fix1.html")
bar.render_notebook()
