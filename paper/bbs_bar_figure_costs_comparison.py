import matplotlib
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Arial', 'weight': 'normal', 'size': 30}
matplotlib.rc('font', **font)
axis_font = {'fontname': 'Arial', 'size': '35'}

graph = "C9_NY_5K"

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

labels = ['200', '400', '600']
''' grouped values '''

'''5K'''
G1_v1_method_value = [1.33, 1.378, 1.367]
G1_v2_method_value = [1.526, 1.662, 1.651]
G1_v3_method_value = [1.417, 1.476, 1.456]

G2_v1_method_value = [1.106, 1.105, 1.111]
G2_v2_method_value = [1.423, 1.444, 1.516]
G2_v3_method_value = [1.893, 2, 2.053]

G3_v1_method_value = [1.106, 1.142, 1.154]
G3_v2_method_value = [1.573, 1.709, 1.769]
G3_v3_method_value = [1.478, 1.446, 1.496]


# '''10K'''
# G1_v1_method_value = [1.422, 1.528, 1.508]
# G1_v2_method_value = [1.937, 2.269, 2.184]
# G1_v3_method_value = [1.432, 1.539, 1.518]
#
# G2_v1_method_value = [1.552, 1.697, 1.695]
# G2_v2_method_value = [2.06, 2.483, 2.428]
# G2_v3_method_value = [1.655, 1.841, 1.838]
#
# G3_v1_method_value = [1.196, 1.258, 1.267]
# G3_v2_method_value = [1.51, 1.76, 1.751]
# G3_v3_method_value = [1.676, 1.973, 1.992]


'''15K'''
# G1_v1_method_value = [1.283, 1.318, 1.317]
# G1_v2_method_value = [1.853, 2.042, 2.008]
# G1_v3_method_value = [1.323, 1.351, 1.518]
#
# G2_v1_method_value = [1.037, 1.041, 1.044]
# G2_v2_method_value = [2.524, 3.037, 3.01]
# G2_v3_method_value = [1.493, 1.704, 1.698]
#
# G3_v1_method_value = [1.091, 1.045, 1.053]
# G3_v2_method_value = [1.394, 1.598, 1.598]
# G3_v3_method_value = [1.906, 1.924, 1.936]


'''
===============================================================
'''

x = np.arange(len(labels))  # the label locations
width = 0.1  # the width of the bars

# draw groups
g1_x = [x[0]+i*width-4.5*width for i in range(3)]
g2_x = [x[1]+i*width-4.5*width for i in range(3)]
g3_x = [x[2]+i*width-4.5*width for i in range(3)]

g1_x_position = g1_x+g2_x+g3_x
g2_x_position = [i+3*width for i in g1_x_position]
g3_x_position = [i+6*width for i in g1_x_position]
v1_values = G1_v1_method_value+G2_v1_method_value+G3_v1_method_value
v2_values = G1_v2_method_value+G2_v2_method_value+G3_v2_method_value
v3_values = G1_v3_method_value+G2_v3_method_value+G3_v3_method_value

rects_g1_v1 = ax.bar(g1_x_position, v1_values, width,
                     label='none', align='edge', alpha=.99, linewidth=1, edgecolor="black")
rects_g1_v2 = ax.bar(g2_x_position, v2_values, width,
                     label='each', align='edge', alpha=.99, linewidth=1, edgecolor="black", hatch="\\")
rects_g1_v3 = ax.bar(g3_x_position, v3_values, width, label='normal',
                     align='edge', alpha=.99, linewidth=1, edgecolor="black", hatch="/")


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('cluster size')
ax.set_ylabel('averagecosts  ratio ')
ax.set_title('Comparison on {}'.format(graph))
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(fontsize="x-small", loc=0, handletextpad=0.1, labelspacing=.1)

fig.tight_layout()

plt.xlim(0-6*width, len(x)-width)
plt.ylim(1)

# plt.show()
plt.savefig("""distance_{}.pdf""".format(graph))
