import numpy
import matplotlib.pyplot as plt
import matplotlib
import os

font = {'family': 'Arial',
        'weight': 'normal',
        'size': 30}
matplotlib.rc('font', **font)
axis_font = {'fontname': 'Arial', 'size': '35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

folder_name = os.path.dirname(__file__)

with open('{}/data_p.txt'.format(folder_name)) as infile:
    trend = numpy.loadtxt(infile)

line1 = ax.plot(trend[:, 0], trend[:, 1], c='r', marker='o',
                ls="-", label='construction time', ms=18, lw=4)
ax.set_ylabel('Construction time (Sec.)', **axis_font)
ax.set_xlabel('percentage', **axis_font)
ax.set_xticks(trend[:, 0])
# ax.tick_params(axis="x", which='major', labelsize=25)
# ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
ax.set_ylim(3000, 4000)

# plt.show()
plt.savefig('index_construction_varing_p_22K.pdf', bbox_inches='tight')
