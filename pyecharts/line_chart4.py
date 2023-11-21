import pyecharts.options as opts
from pyecharts.charts import Line
x = ['2K', '4K', '8K', '16K', '32K', '64K', '128K']
y1 = [[138, 187, 282, 472, 861, 1565, 2935], [109, 146, 228, 329, 520, 932, 1727], [97, 110, 152, 212, 328, 539, 983],
      [89, 96, 118, 154, 225, 358, 598], [87, 97, 104, 128, 168, 246, 411]]
y2 = [[47, 82, 172, 477, 1069, 2430, 5267], [58, 67, 143, 375, 906, 1905, 4093], [64, 63, 124, 306, 688, 1656, 3525],
      [62, 91, 210, 465, 1067, 2170, 4485], [58, 122, 284, 603, 1245, 2615, 5348]]

y=[]

for list1,list2 in zip(y1,y2):
    tmp =[]
    for elem1,elem2 in zip(list1,list2):
        tmp.append(round(elem2/elem1, 2))
    y.append(tmp)

# print(y)

line = (
    Line()
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="hit ratio 1", y_axis=y[0])
    .add_yaxis(series_name="hit ratio 1/2", y_axis=y[1], symbol="arrow", is_symbol_show=True)
    .add_yaxis(series_name="hit ratio 1/4", y_axis=y[2], symbol="circle", is_symbol_show=True)
    .add_yaxis(series_name="hit ratio 1/8", y_axis=y[3], symbol="square", is_symbol_show=True)
    .add_yaxis(series_name="hit ratio 1/16", y_axis=y[4], symbol="triangle", is_symbol_show=True)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='A.nnz'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup ratio'))
)
line.render(path="UPMEM-benchmark.html")
line.render_notebook()
