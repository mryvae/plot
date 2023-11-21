import pyecharts.options as opts
from pyecharts.charts import Line
x = ['1', '2', '4', '8', '16']
y1 = [84, 116, 127, 142, 178]
y2 = [65, 90, 95, 103, 144]
y = [436, 494, 568, 734, 1220]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)
    y2[i] = round(y[i]/y2[i], 2)

line = (
    Line(init_opts=opts.InitOpts(width="600px",
                                 height="400px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="upmem-worst", y_axis=y1)
    .add_yaxis(series_name="upmem-ideal", y_axis=y2)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='#thread'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)

line.render(path="UPMEM-EFS-scenario-speedup-benchmark.html")
line.render_notebook()
