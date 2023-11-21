from pyecharts.charts import Bar, Line
from pyecharts import options as opts

x = ['tvse', 'path', 'tvse+path', 'tvse-m', 'tvse-m+path']

# z1 = [6.432, 3.463, 23.731, 9.188, 17.774, 5.169]
# z2 = [1.752, 0.442, 8.299, 0.777, 1.136, 0.946]
# z3 = [4.680, 3.021, 15.432, 8.411, 16.638, 4.223]
# z4 = [10.501, 5.427, 29.572, 14.380, 18.151, 4.888]
# z5 = [5.532, 2.453, 13.477, 6.044, 1.227, 0.582]
# z6 = [4.969, 2.974, 16.095, 8.336, 16.924, 4.306]

z1 = [6298, 5655, 11953, 6470, 12012]
z2 = [2191, 2922, 5113, 3400, 6161]
z3 = [17397, 19769, 37166, 23438, 47385]
z4 = [5763, 7598, 13361, 9564, 18902]
z5 = [1252, 18228, 19480, 1091, 17955]
z6 = [2183, 4791, 6974, 2635, 7522]

bar = Bar()
bar.add_xaxis(x)
bar.add_yaxis('load balance',
              z1,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('push',
              z2,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('run',
              z3,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('pull',
              z4,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('merge',
              z5,
              label_opts=opts.LabelOpts(is_show=False))
bar.add_yaxis('other',
              z6,
              label_opts=opts.LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=opts.TitleOpts('read and write scenario'),
    tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type='cross'),
    xaxis_opts=opts.AxisOpts(type_='category', axispointer_opts=opts.AxisPointerOpts(
        is_show=True, type_='shadow')),
    yaxis_opts=opts.AxisOpts(name='lattency/us')
)

# bar.set_series_opts(label_opts=opts.LabelOpts(font_size=25))
bar.render(path="bar.html")
bar.render_notebook()
