import pyecharts.options as opts
from pyecharts.charts import Line
x = ['2K', '4K', '8K', '16K', '32K', '64K']
y1 = [[5128, 5960, 8285, 12368, 20013, 35197], [9266, 10602, 14603, 20598, 33613, 58840], [13226, 16508, 22888, 32966, 53626, 94037],
      [14066, 15215, 17247, 21541, 26640, 43437], [28207, 31964, 37153, 46794, 61572, 109746]]
y2 = [[4849, 9425, 18859, 38826, 78708, 158778], [8377, 16313, 32834, 67448, 136915, 277041], [14394, 25738, 51693, 106274, 215623, 435819],
      [7475, 12583, 23335, 45383, 89477, 178074], [17745, 32877, 63676, 127509, 256655, 513346]]

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
    .add_yaxis(series_name="tvse", y_axis=y[0])
    .add_yaxis(series_name="path", y_axis=y[1], symbol="arrow", is_symbol_show=True)
    .add_yaxis(series_name="tvse+path", y_axis=y[2], symbol="circle", is_symbol_show=True)
    .add_yaxis(series_name="tvse-m", y_axis=y[3], symbol="square", is_symbol_show=True)
    .add_yaxis(series_name="tvse-m+path", y_axis=y[4], symbol="triangle", is_symbol_show=True)
    .set_global_opts(xaxis_opts=opts.AxisOpts(name='batch\n size'))
    .set_global_opts(yaxis_opts=opts.AxisOpts(name='speedup'))
)
line.render(path="UPMEM-benchmark.html")
line.render_notebook()
