import matplotlib
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Arial', 'weight': 'normal', 'size': 30}
matplotlib.rc('font', **font)
axis_font = {'fontname': 'Arial', 'size': '35'}

graph = "C9_NY_10K"

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

labels = ['200', '400', '600']
bbs_value = [47771.427, 47771.427, 52072.087]
v1_method_value = [570.023, 467.677, 1051.75]
v2_method_value = [439.58, 435.99, 999.803]
v3_method_value = [464.39, 432.573, 955.22]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

rectsBBS = ax.bar(x-2*width, [round(i, 1) for i in bbs_value],
                  width, label='BBS', align='edge', alpha=.99)
rectsV1 = ax.bar(x-width, [round(i, 1) for i in v1_method_value], width,
                 label='none', align='edge', hatch="\\", alpha=.99)
rectsV2 = ax.bar(x, [round(i, 1) for i in v2_method_value], width,
                 label='each', align='edge', hatch="/", alpha=.99)
rectsV3 = ax.bar(x+width, [round(i, 1) for i in v3_method_value], width,
                 label='normal', align='edge', hatch="-", alpha=.99)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('cluster size')
ax.set_ylabel('# of skyline paths')
ax.set_title(
    'Comparison on {}'.format(graph))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(fontsize="x-small", loc=0, handletextpad=0.1, labelspacing=.1)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', size=10, weight='bold')


autolabel(rectsBBS)
autolabel(rectsV1)
autolabel(rectsV2)
autolabel(rectsV3)

fig.tight_layout()

plt.xlim(0-2.5*width, len(x)-width)

# plt.show()
plt.savefig("""query_time_C9_NY_10K.pdf""")
