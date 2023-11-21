import pyecharts.options as opts
from pyecharts.charts import Line

x = ['tvse', 'path', 'tvse+path', 'tvse-m', 'tvse-m+path']
y1 = [35084, 58336, 94047, 46598, 109937]
y = [179160, 327650, 507536, 194840, 583065]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

line = (
    Line(init_opts=opts.InitOpts(width="800px",
                                 height="400px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="EFS operators", y_axis=y1)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='operator'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)

line.render(path="UPMEM-EFS-scenario-speedup-benchmark.html")
line.render_notebook()
