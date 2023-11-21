import pyecharts.options as opts
from pyecharts.charts import Line
x = ['2K', '4K', '8K', '16K', '32K', '64K']
y1 = [[660, 653, 729, 814, 1068, 1681], [574, 615, 690, 795, 1004, 1544], [777, 795, 1034, 1217, 1949, 3197],
      [784, 979, 1379, 2025, 3511, 6640]]
y2 = [[322, 564, 1056, 2106, 4180, 8364], [326, 556, 1046, 2085, 4138, 8263], [713, 1225, 2264, 4319, 8459, 16804],
      [1350, 2415, 4575, 9050, 17806, 35872]]

y = []

for list1, list2 in zip(y1, y2):
    tmp = []
    for elem1, elem2 in zip(list1, list2):
        tmp.append(round(elem2/elem1, 2))
    y.append(tmp)

# print(y)

line = (
    Line(init_opts=opts.InitOpts(width="647px",
                                 height="400px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(series_name="add", y_axis=y[0])
    .add_yaxis(series_name="sub", y_axis=y[1], symbol="arrow", is_symbol_show=True)
    .add_yaxis(series_name="mxm", y_axis=y[2], symbol="circle", is_symbol_show=True)
    .add_yaxis(series_name="sub_add_mxm", y_axis=y[3], symbol="square", is_symbol_show=True)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='batch\n size'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)
line.render(path="UPMEM-benchmark.html")
line.render_notebook()
