from pyecharts.charts import Bar
# 使用 options 配置项，在 pyecharts 中，一切皆 Options
from pyecharts import options as opts

# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # opts.InitOpts（theme标图主题=ThemeType.LIGHT）
    .add_xaxis(["index", "matrix","other"])
    .add_yaxis("RedisGraph", [28.643,206.700,71.461])
    .add_yaxis("RedisGraph-upmem", [32.385,35.241,58.673])
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 16)))
    .set_global_opts(yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 16), name="lattency/ms"))
    .set_global_opts(title_opts=opts.TitleOpts(title="benchmark"))
    .set_series_opts(label_opts=opts.LabelOpts(font_size=16))
)
bar.set_series_opts(label_opts=opts.LabelOpts(font_size=25))
bar.render(path="MyKV-Redis-GET.html")
bar.render_notebook()