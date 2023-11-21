import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# NR_DPU = 64
# B 4*1M
# NR_SPLIT = 1,4
# A 4K, 8K, 16K, 32K, 64K, 128K, 256K
# latency breakdown

fontsize = 10
titlefontsize = 12
colors = ["lightcoral", "cornflowerblue",
          "lightsalmon", "teal", "aquamarine", "darkviolet"]
legends = ["PIM-greedy", "PIM-hash", "RedisGraph"]
labels = ['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8',
          '#9', '#10', '#11', '#12', '#13', '#14', '#15']  # nnzA
cpu_base_us = [4114, 6581, 13550, 22857, 37378, 56207, 111551]
jump_1 = [
    [7017, 6885, 54065],
    [6672, 6249, 64986],
    [6529, 6485, 64216],
    [3304, 3255, 39580],
    [2282, 2752, 10754],
    [3525, 3222, 31195],
    [3917, 4251, 38013],
    [2182, 2279, 7805],
    [2054, 2559, 21986],
    [4937, 4476, 44315],
    [3528, 3143, 25894],
    [6378, 4528, 41505],
    [4010, 4046, 30474],
    [3886, 3692, 30972],
    [4637, 3991, 31128],
]

jump_2 = [
    [9801, 11241, 86228],
    [9338, 11264, 99633],
    [9128, 10721, 92465],
    [5828, 5972, 45046],
    [13782, 84143, 19331],
    [6691, 7116, 42646],
    [9479, 10880, 56329],
    [2898, 11511, 8608],
    [4928, 13493, 24458],
    [8705, 9642, 63041],
    [5469, 6803, 31875],
    [26200, 33646, 64716],
    [7258, 7868, 50175],
    [6975, 7470, 46452],
    [8240, 8165, 48853],
]

jump_3 = [
    [13458, 15691, 118619],
    [13050, 15021, 132495],
    [13539, 14603, 129143],
    [14399, 14235, 64718],
    [58790, 227116, 114048],
    [23094, 25685, 73171],
    [17287, 20169, 85923],
    [15091, 58370, 43055],
    [19019, 45179, 52927],
    [17842, 21346, 90022],
    [9572, 15695, 40626],
    [61139, 73558, 99677],
    [14191, 15111, 71127],
    [13354, 14193, 66357],
    [14712, 16007, 69582],
]

jumps = []

jump_1 = [[time_us/1000 for time_us in l] for l in jump_1]
jump_2 = [[time_us/1000 for time_us in l] for l in jump_2]
jump_3 = [[time_us/1000 for time_us in l] for l in jump_3]

fig = plt.figure(figsize=(16, 6))
# 子图 1
rpq_data_np = np.array(jump_1)
jumps.append(sum(rpq_data_np))
ax1 = plt.subplot(2, 4, (1, 2))
ax2 = ax1.twinx()
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, rpq_data_np[:, 0],
        width, label=legends[0], color=colors[0])
ax1.bar(x - 0.5*width, rpq_data_np[:, 1],
        width, label=legends[1], color=colors[1])
ax1.bar(x + 0.5*width, rpq_data_np[:, 2],
        width, label=legends[2], color=colors[2])

ax2.plot(x, rpq_data_np[:, 2]/rpq_data_np[:, 0], label="speedup of PIM-rpq over RedisGraph",
         color=colors[3], marker='o', markerfacecolor='white')

ax2.plot(x, rpq_data_np[:, 1]/rpq_data_np[:, 0], label="speedup of PIM-rpq over PIM-hash",
         color=colors[4], marker='*', markerfacecolor='white')

ax1.set_xticks(x, labels=labels, fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=fontsize)
ax1.set_xlabel('Trace ID', fontsize=fontsize)
ax1.set_ylabel('Latency/ms', fontsize=fontsize)
ax1.set_title('(a) k = 1', fontsize=titlefontsize)
ax2.set_ylim(0, 15)
ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=fontsize)
# x轴刻度标签位置不进行计算
# ax1.legend(bbox_to_anchor=(0.4, 0.9), fontsize=fontsize)
# ax2.legend(bbox_to_anchor=(0.46, 1), fontsize=fontsize)

# 子图 2
rpq_data_np = np.array(jump_2)
jumps.append(sum(rpq_data_np))
ax1 = plt.subplot(2, 4, (3, 4))
ax2 = ax1.twinx()
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, rpq_data_np[:, 0],
        width, label=legends[0], color=colors[0])
ax1.bar(x - 0.5*width, rpq_data_np[:, 1],
        width, label=legends[1], color=colors[1])
ax1.bar(x + 0.5*width, rpq_data_np[:, 2],
        width, label=legends[2], color=colors[2])

ax2.plot(x, rpq_data_np[:, 2]/rpq_data_np[:, 0], label="speedup of PIM-rpq over RedisGraph",
         color=colors[3], marker='o', markerfacecolor='white')

ax2.plot(x, rpq_data_np[:, 1]/rpq_data_np[:, 0], label="speedup of PIM-rpq over PIM-hash",
         color=colors[4], marker='*', markerfacecolor='white')

ax1.set_xticks(x, labels=labels, fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=fontsize)
ax1.set_xlabel('Trace ID', fontsize=fontsize)
ax1.set_ylabel('Latency/ms', fontsize=fontsize)
ax1.set_title('(b) k = 2', fontsize=titlefontsize)
ax2.set_ylim(0, 15)
ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=fontsize)
# x轴刻度标签位置不进行计算
# ax1.legend(bbox_to_anchor=(0.4, 0.9), fontsize=fontsize)
# ax2.legend(bbox_to_anchor=(0.46, 1), fontsize=fontsize)

# 子图 3
rpq_data_np = np.array(jump_3)
jumps.append(sum(rpq_data_np))
ax1 = plt.subplot(2, 4, (5, 6))
ax2 = ax1.twinx()
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, rpq_data_np[:, 0],
        width, label=legends[0], color=colors[0])
ax1.bar(x - 0.5*width, rpq_data_np[:, 1],
        width, label=legends[1], color=colors[1])
ax1.bar(x + 0.5*width, rpq_data_np[:, 2],
        width, label=legends[2], color=colors[2])

ax2.plot(x, rpq_data_np[:, 2]/rpq_data_np[:, 0], label="speedup of PIM-rpq over RedisGraph",
         color=colors[3], marker='o', markerfacecolor='white')

ax2.plot(x, rpq_data_np[:, 1]/rpq_data_np[:, 0], label="speedup of PIM-rpq over PIM-hash",
         color=colors[4], marker='*', markerfacecolor='white')

ax1.set_xticks(x, labels=labels, fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=fontsize)
ax1.set_xlabel('Trace ID', fontsize=fontsize)
ax1.set_ylabel('Latency/ms', fontsize=fontsize)
ax1.set_title('(c) k = 3', fontsize=titlefontsize)
ax2.set_ylim(0, 15)
ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=fontsize)
# x轴刻度标签位置不进行计算
# ax1.legend(bbox_to_anchor=(0.4, 0.9), fontsize=fontsize)
# ax2.legend(bbox_to_anchor=(0.46, 1), fontsize=fontsize)

fig.tight_layout()

ax1 = plt.subplot(2, 4, 7)
ax2 = ax1.twinx()
labels_normal = ['k=1', 'k=2', 'k=3']

jumps = [[time_us/15 for time_us in l] for l in jumps]
rpq_data_np = np.array(jumps)
x = np.arange(len(labels_normal))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, rpq_data_np[:, 0],
        width, label=legends[0], color=colors[0])
ax1.bar(x - 0.5*width, rpq_data_np[:, 1],
        width, label=legends[1], color=colors[1])
ax1.bar(x + 0.5*width, rpq_data_np[:, 2],
        width, label=legends[2], color=colors[2])

ax2.plot(x, rpq_data_np[:, 2]/rpq_data_np[:, 0], label="speedup of PIM-rpq over RedisGraph",
         color=colors[3], marker='o', markerfacecolor='white')

ax2.plot(x, rpq_data_np[:, 1]/rpq_data_np[:, 0], label="speedup of PIM-rpq over PIM-hash",
         color=colors[4], marker='*', markerfacecolor='white')

ax1.set_xticks(x, labels=labels_normal, fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=fontsize)
ax1.set_ylabel('Latency/ms', fontsize=fontsize)
ax1.set_title('(d) normalized', fontsize=titlefontsize)
ax2.set_ylim(0, 10)
ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=fontsize)
# x轴刻度标签位置不进行计算
ax1.legend(bbox_to_anchor=(1.3, 0.8), loc='upper left')
ax2.legend(bbox_to_anchor=(1.3, 0.3), loc='upper left')
# ax1.legend(fontsize=fontsize)
# ax2.legend(fontsize=fontsize)

plt.subplots_adjust(wspace=0.5)

# plt.show()
plt.savefig("./plot/rpq_short.png")
