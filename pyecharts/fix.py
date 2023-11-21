from pyecharts.charts import Bar, Line
from pyecharts import options as opts

x = ['0.5K', '1K', '2K', '4K', '8K', '16K', '32K', '64K']

y1 = [57, 74, 97, 114, 164, 230, 297, 409]
y = [57, 57, 68, 82, 162, 438, 974, 2227]

z1 = [23, 35, 56, 101, 191, 368, 733, 1474]
z2 = [200, 190, 206, 233, 251, 228, 287, 385]
z3 = [167, 168, 176, 175, 206, 227, 284, 383]
z4 = [260, 265, 302, 368, 360, 360, 489, 687]
z5 = [27, 48, 90, 173, 354, 691, 1442, 2885]
z6 = [677, 706, 830, 1050, 1362, 1874, 3235, 5814]

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
    title_opts=opts.TitleOpts('read scenario'),
    tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type='cross'),
    xaxis_opts=opts.AxisOpts(name='A.nnz',type_='category', axispointer_opts=opts.AxisPointerOpts(
        is_show=True, type_='shadow')),
    yaxis_opts=opts.AxisOpts(name='lattency/us')
)

bar.extend_axis(yaxis=opts.AxisOpts(
    min_=0, max_=6,
    interval=1,
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
