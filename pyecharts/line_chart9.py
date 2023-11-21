import pyecharts.options as opts
from pyecharts.charts import Line


x = ['FIB-Index', 'EFS-Index', 'FIB-Graph', 'EFS-Graph', 'FIB',  'FES',]
y1 = [21156, 50613, 6282, 94560, 27438, 145173]
y = [107374, 185043, 35950, 438422, 143324, 619545]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

line = (
    Line(init_opts=opts.InitOpts(width="800px",
                                 height="400px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="puncture experiment", y_axis=y1)
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)

line.render(path="UPMEM-FIB-EFS-scenario-speedup-benchmark.html")
line.render_notebook()
