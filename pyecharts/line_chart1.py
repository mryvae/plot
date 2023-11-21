import pyecharts.options as opts
from pyecharts.charts import Line
x=['1-thread','2-thread','4-thread','8-thread','16-thread','32-thread','64-thread']
y1=[677,979,1236,1244,1129,964,846]
y2=[434,725,1030,897,721,547,526]

line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="scale=0.1, no pipeline",y_axis=y1,symbol="arrow",is_symbol_show=True)
    .add_yaxis(series_name="scale=1, no pipeline",y_axis=y2)
    # .set_global_opts(xaxis_opts=opts.AxisOpts(name='working_thread'))
    # .set_global_opts(yaxis_opts=opts.AxisOpts(name='throughput'))
    .set_global_opts(title_opts=opts.TitleOpts(title="redisgraph-throughput"))
)
line.render(path="redisgraph-benchmark-throughput-no-pipeline.html")
line.render_notebook()