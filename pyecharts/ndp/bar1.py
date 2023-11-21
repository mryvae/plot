from pyecharts.charts import Bar
# 使用 options 配置项，在 pyecharts 中，一切皆 Options
from pyecharts import options as opts

# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(width="400px",
                                 height="400px"))  # opts.InitOpts（theme标图主题=ThemeType.LIGHT）
    .add_xaxis(["FIB-Index","Bras-Index","FIB-Graph","Bras-Graph","FIB","Bras"])
    .add_yaxis("speed up", [5.07,3.65,5.72,4.63,5.22,4.27])
    .set_global_opts(yaxis_opts=opts.AxisOpts(name="speed up"))
)

bar.render(path="bar.html")
bar.render_notebook()