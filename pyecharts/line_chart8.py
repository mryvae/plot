import pyecharts.options as opts
from pyecharts.charts import Line

x = ['add', 'sub', 'mxm', 'sub+add+mxm']
y1 = [1987, 2115, 3545, 6656]
y = [8560, 8498, 30764, 46115]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

line = (
    Line(init_opts=opts.InitOpts(width="647px",
                                 height="400px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="FIB operators", y_axis=y1)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='operator'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)

line.render(path="UPMEM-FIB-scenario-speedup-benchmark.html")
line.render_notebook()
