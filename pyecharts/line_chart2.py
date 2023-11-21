import pyecharts.options as opts
from pyecharts.charts import Line
x=['1M','2M','4M','8M','16M']
y1=[535,674,735,1095,1190]
y2=[640,1435,1442,3192,3512]

line=(
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="UPMEM",y_axis=y1,symbol="arrow",is_symbol_show=True)
    .add_yaxis(series_name="GraphBLAS",y_axis=y2)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='B.nnz'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='time/ms'))
    .set_global_opts(title_opts=opts.TitleOpts(title="UPMEM vs GraphBLAS"))
)
line.render(path="UPMEM-benchmark.html")
line.render_notebook()