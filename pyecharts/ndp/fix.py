from pyecharts.charts import Bar, Line
from pyecharts import options as opts

x = ["FIB-Index","Bras-Index","FIB-Graph","Bras-Graph","FIB","Bras"]

y1 = [21156,50613,6282,94560,27438,145173]
y = [107374,185043,35950,438422,143324,619545]

z1 = [21156,50613,6282,94560,27438,145173]
z2 = [107374,185043,35950,438422,143324,619545]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

bar = Bar(init_opts=opts.InitOpts(width="600px",
                                 height="400px"))
bar.add_xaxis(x)
bar.add_yaxis('UPMEM',
              z1,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('CPU',
              z2,
              label_opts=opts.LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=opts.TitleOpts('read scenario'),
    tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type='cross'),
    yaxis_opts=opts.AxisOpts(name='lattency/us')
)

bar.extend_axis(yaxis=opts.AxisOpts(
    min_=0, max_=6,
    interval=1,
    # axislabel_opts=opts.LabelOpts(formatter='{value} us')
))

line = Line(init_opts=opts.InitOpts(width="800px",
                                 height="400px"))
line.add_xaxis(x)
line.add_yaxis('speedup',
               y1,
               yaxis_index=1,
               label_opts=opts.LabelOpts(is_show=False)
               )


bar.overlap(line)  # 合并图
bar.render(path="fix1.html")
bar.render_notebook()