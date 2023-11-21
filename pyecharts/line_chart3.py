import pyecharts.options as opts
from pyecharts.charts import Line
x=['0.5K','1K','2K','4K','8K','16K','32K','64K']
y1=[57,74,97,114,164,230,297,409]
y = [57,57,68,82,162,438,974,2227]

# y1 = []
# y2 = []

for i in range(len(y)):
    y1[i] = round(y[i]/y1[i], 2)

line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="merge",y_axis=y1)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='A.nnz'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
    .set_global_opts(title_opts=opts.TitleOpts(title="read and write scenario"))
)
line.render(path="UPMEM-latency-benchmark.html")
line.render_notebook()