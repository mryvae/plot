import pyecharts.options as opts
from pyecharts.charts import Line
x=['1-thread','2-thread','4-thread','8-thread','16-thread','32-thread']
y1=[0.453,0.487,0.492,0.672,0.952,4.260]
y2=[0.453,0.447,0.440,0.433,0.473,0.396]
y3=[0.453,0.467,0.463,0.529,0.621,0.829]

line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="push-max",y_axis=y1)
    .add_yaxis(series_name="push-min",y_axis=y2,symbol="arrow",is_symbol_show=True)
    .add_yaxis(series_name="push-avg",y_axis=y3,symbol="circle",is_symbol_show=True)
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='lattency of push/ms'))
)
line.render(path="UPMEM-benchmark.html")
line.render_notebook()