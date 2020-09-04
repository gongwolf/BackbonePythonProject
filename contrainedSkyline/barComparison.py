import numpy
import scipy
import sklearn.preprocessing
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
import os
import json
import matplotlib as mpl
mpl.style.use('classic')
mpl.rcParams['hatch.linewidth'] = 10.0 

font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 30}
matplotlib.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)



n_groups = 3

speed_base = (0, 0, 57916745.33)
speed_improved = (0, 0, 333563.4167)


index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, speed_improved, bar_width,
                 alpha=opacity,
                 color='b',
                 label='ExactAlg-improved',
                 hatch='\\')

rects2 = plt.bar(index + bar_width, speed_base, bar_width,
                 alpha=opacity,
                 color='r',
                 label='ExactAlg-base')

plt.ylabel('frequency of skyline checking')
plt.xlabel('Cities')
# plt.title('Scores by group and gender')
plt.xticks(index + bar_width / 2, ('LA', 'SF', 'NY'))
plt.legend(loc=2,framealpha=0.5)

plt.tight_layout()
plt.savefig('read_speed_up_bar.pdf', bbox_inches='tight')
