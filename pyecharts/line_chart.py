import pyecharts.options as opts
from pyecharts.charts import Line
x=['1-thread','2-thread','4-thread','8-thread','16-thread','32-thread','64-thread']
y1=[557,949,1366,1468,1051,955,836]
y2=[451,761,1064,918,718,558,526]

line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="scale=0.1, pipelined",y_axis=y1,symbol="arrow",is_symbol_show=True)
    .add_yaxis(series_name="scale=1, pipelined",y_axis=y2)
    # .set_global_opts(xaxis_opts=opts.AxisOpts(name='working_thread'))
    # .set_global_opts(yaxis_opts=opts.AxisOpts(name='throughput'))
    .set_global_opts(title_opts=opts.TitleOpts(title="redisgraph-throughput"))
)
line.render(path="redisgraph-benchmark-throughput.html")
line.render_notebook()