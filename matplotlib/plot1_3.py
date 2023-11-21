import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# NR_DPU = 64 
# B 4*1M
# NR_SPLIT = 1,4
# A 4K, 8K, 16K, 32K, 64K, 128K, 256K
# latency breakdown

fontsize = 18
colors = ["lightcoral", "cornflowerblue", "lightsalmon", "teal", "aquamarine", "darkviolet"]
legends = ["pushB", "total", "run", "pull", "merge", "speedup", "grbmxm"]
labels = ['4K', '8K', '16K', '32K', '64K', '128K', '256K'] # nnzA
cpu_base_us = [4114, 6581, 13550, 22857, 37378, 56207, 111551]
upmem_data_us_1 = [
    [126292,     2257,     1227,      597,      396],
    [161294,     2943,     1453,      705,      730],
    [141932,     4886,     1938,      989,     1450],
    [143839,     7604,     2782,     1242,     2632],
    [148304,    13162,     4537,     1621,     5199],
    [142657,    23394,     7969,     2209,     9590],
    [142300,    37600,    14865,     3776,    16542],
]

upmem_data_us_4 = [
    [49232,     4873,     1355,      621,     2870],
    [59249,     8292,     1689,      825,     5661],
    [61132,    15108,     2398,     1242,    11265],
    [63841,    24619,     3757,     1761,    18788],
    [59457,    39352,     6496,     2746,    29753],
    [67608,    60355,    12044,     3842,    43900],
    [48087,   103015,    22743,     5339,    73453],
]

cpu_base_ms = [ time_us/1000 for time_us in cpu_base_us]
upmem_data_ms_1 = [[time_us/1000 for time_us in l ] for l in upmem_data_us_1]
upmem_data_ms_4 = [[time_us/1000 for time_us in l ] for l in upmem_data_us_4]

cpu_base_np = np.array(cpu_base_ms)
upmem_data_np = np.array(upmem_data_ms_1)

plt.figure(figsize=(14, 6))
# 五组数据
ax1 = plt.subplot(221)
ax2 = ax1.twinx()
x =  np.arange(len(labels))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, upmem_data_np[:,1], width, label=legends[1], color=colors[1])
ax1.bar(x - 0.5*width, upmem_data_np[:,2], width, label=legends[2], color=colors[2])
ax1.bar(x + 0.5*width, upmem_data_np[:,3], width, label=legends[3], color=colors[3])
ax1.bar(x + 1.5*width, upmem_data_np[:,4], width, label=legends[4], color=colors[4])
ax2.plot(x, cpu_base_np/upmem_data_np[:,1], label=legends[5], color=colors[5],marker='o',markerfacecolor='white')

ax1.set_xticks(x, labels=labels,fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(),fontsize=fontsize)
ax1.set_xlabel('nnzA',fontsize=fontsize)
ax1.set_ylabel('Latency/ms',fontsize=fontsize)
ax1.set_title('Latency vs. nnzA (#B split = 1)',fontsize=fontsize)
ax2.set_ylim(0,8)
ax2.set_yticklabels(ax2.get_yticklabels(),fontsize=fontsize)
# x轴刻度标签位置不进行计算
ax1.legend(bbox_to_anchor=(0.4,0.9),fontsize=fontsize)
ax2.legend(bbox_to_anchor=(0.46,1),fontsize=fontsize)


cpu_base_np = np.array(cpu_base_ms)
upmem_data_np = np.array(upmem_data_ms_4)

# 五组数据
ax1 = plt.subplot(122)
ax2 = ax1.twinx()
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.20  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
ax1.bar(x - 1.5*width, upmem_data_np[:,1], width, label=legends[1], color=colors[1])
ax1.bar(x - 0.5*width, upmem_data_np[:,2], width, label=legends[2], color=colors[2])
ax1.bar(x + 0.5*width, upmem_data_np[:,3], width, label=legends[3], color=colors[3])
ax1.bar(x + 1.5*width, upmem_data_np[:,4], width, label=legends[4], color=colors[4])
ax2.plot(x, cpu_base_np/upmem_data_np[:,1], label=legends[5], color=colors[5],marker='o',markerfacecolor='white')

ax1.set_xticks(x, labels=labels,fontsize=fontsize)
ax1.set_yticklabels(ax1.get_yticklabels(),fontsize=fontsize)
ax1.set_xlabel('nnzA',fontsize=fontsize)
ax1.set_ylabel('Latency/ms',fontsize=fontsize)
ax1.set_title('Latency vs. nnzA (#B split = 4)',fontsize=fontsize)
ax2.set_ylabel("Speedup",fontsize=fontsize)
ax2.set_ylim(0,8)
ax2.set_yticklabels(ax2.get_yticklabels(),fontsize=fontsize)


ax1.legend(bbox_to_anchor=(0.4,0.90),fontsize=fontsize)
ax2.legend(bbox_to_anchor=(0.45,1),fontsize=fontsize)


plt.subplots_adjust(wspace=0.3)

# plt.show()
plt.savefig("./plot/plot1_3.png")
