import numpy
import scipy
import sklearn.preprocessing
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
import os
import json

font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 30}
matplotlib.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

with open('speedup.txt') as infile:
    trend = numpy.loadtxt(infile)
    # print trend

# with open('speedup_1.txt') as infile:
#     trend_1 = numpy.loadtxt(infile)
    # print trend


# y_max = max(trend[:,1])
#plt.ylim([0, 2])

#plt.plot(trend[:,0], trend[:,1], 'b^-', label='Varying graph size', ms=15, lw=5)
#plt.plot(trend_1[:,0], trend_1[:,1], 'ro-', label='Varying # of object', ms=15, lw=5)
#serial = 2449436.627
# plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-baseline', ms=18, lw=5)
# plt.plot(trend[:,0], trend[:,1], 'ro-', label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,1], c='r',marker=".",ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,1], 'b.', ls="--",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], 'b.', ls="solid",label='Approx-range-indexed', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], 'gx-', label='Approx-minPath', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,5], c='k', marker="s",ls="solid",label='Approx-mix', ms=10, lw=4)
# plt.plot(trend[:,0], trend[:,3], c='k', marker="s",ls="--",label='Approx-mix-index', ms=10, lw=4)
# plt.plot(trend[:,0], trend[:,0], 'ro-', ms=10, lw=4, label='Ideal parallel algorithm')
# plt.plot(trend[:,0], serial/trend[:,1], 'b^-', ms=10, lw=4, label='Perfect')
# plt.xlabel('|D|/N ', **axis_font)
# plt.xlabel('average degree of the graph ', **axis_font)

#baseline vs improved, skyline candidates
# plt.plot(trend[:,0], trend[:,1], 'b^-', label='ExactAlg-baseline', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], 'ro-', label='ExactAlg-improved', ms=18, lw=4)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# # plt.ylabel('Running Time (Sec.)', **axis_font)
# plt.xlabel('# of objects (in thousands)', **axis_font)
# # plt.xlabel('average degree of the graph ', **axis_font)
# # plt.xlabel('# of graph nodes (in 100K)', **axis_font)
# plt.legend(loc=2,framealpha=0.3)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# plt.savefig('speedup_c_exp1.pdf', bbox_inches='tight')




# speedup-approx
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='s', ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], c='k', marker="d",ls="solid",label='Approx-mix', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='k', marker="d", fillstyle='none',markeredgewidth="4",ls="--",label='Approx-mix-indexed', ms=18, lw=4)
# # plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.ylabel('Running Time (Sec.)', **axis_font)
# # plt.xlabel(r'$\tau$ (kilometers)', **axis_font)
# plt.xlabel('# of graph nodes (in millions)', **axis_font)
# # plt.xlabel('# of objects (in thousands)', **axis_font)
# plt.legend(loc=2,framealpha=0.3)
# # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# plt.savefig('speedup_c_exp1.pdf', bbox_inches='tight')


# speedup varying tau
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='s', ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], c='k', marker="d",ls="solid",label='Approx-mix', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='k', marker="d", fillstyle='none',markeredgewidth="4",ls="--",label='Approx-mix-indexed', ms=18, lw=4)
# plt.ylabel('Running Time (Sec.)', **axis_font)
# plt.xlabel(r'$\tau$ (kilometers)', **axis_font)
# plt.legend(loc=2,framealpha=0.3)
# plt.savefig('speedup.pdf', bbox_inches='tight')



# speedup wit improved exact
plt.plot(trend[:,0], trend[:,1], c='r', marker ='o', ls="-",label='ExactAlg-improved', ms=18, lw=4)
plt.plot(trend[:,0], trend[:,2], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
plt.plot(trend[:,0], trend[:,3],  c='k', marker="d", fillstyle='none',markeredgewidth="4",ls="--",label='Approx-mix-indexed', ms=18, lw=4)
plt.ylabel('Running Time (Sec.)', **axis_font)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.xlabel('# of objects (in thousands)', **axis_font)
plt.xlabel('# of graph nodes (in millions)', **axis_font)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.legend(loc=2)
plt.savefig('speedup.pdf', bbox_inches='tight')


#frequency
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='s', ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=18, lw=4)
# # plt.xlabel('# of objects (in thousands)', **axis_font)
# plt.xlabel('# of graph nodes (in millions)', **axis_font)
# # plt.xlabel(r'$\tau$ (kilometers)', **axis_font)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.legend(loc=5)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# plt.savefig('speedup_c_exp1.pdf', bbox_inches='tight')


#frequency with improved exact
# plt.plot(trend[:,0], trend[:,1], c='r', marker ='o', ls="-",label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=18, lw=4)
# plt.xlabel('# of objects (in thousands) ', **axis_font)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.legend(loc=2)
# plt.savefig('speedup.pdf', bbox_inches='tight')

# goodness
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='s', ls="solid",label='Approx-range', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls="solid",label='Approx-mix', ms=18, lw=4)
# plt.ylabel('Goodness', **axis_font)
# # plt.xlabel('# of objects (in thousands) ', **axis_font)
# # plt.xlabel(r'$\tau$ (kilometers)', **axis_font)
# plt.xlabel('# of graph nodes (in millions)', **axis_font)
# plt.legend(loc=1)
# plt.ylim(0.4,0.9)
# plt.savefig('goodness_c_exp5.pdf', bbox_inches='tight')


# goodness top 10_100
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='s', ls="-.",label='Approx-range_top10', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls=":",label='Approx-range_top100', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], c='k', marker="d",ls=":",label='Approx-mix_top100', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='k', marker="d",fillstyle='none',markeredgewidth="4",ls="-.",label='Approx-mix_top10', ms=18, lw=4)
# plt.ylabel('Goodness', **axis_font)
# # plt.xlabel('# of objects (in thousands) ', **axis_font)
# plt.legend(loc=5,framealpha=0.3,fontsize=22)
# plt.xlabel(r'$\tau$ (kilometers)', **axis_font)
# plt.ylim(0.4,0.9)
# plt.savefig('goodness_top_10_100.pdf', bbox_inches='tight')


#goodness top 100
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='*', ls=":",label='Approx-range_top100', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="d",ls=":",label='Approx-mix_top100', ms=15, lw=4)
# plt.ylabel('Goodness', **axis_font)
# plt.xlabel('# of graph node (in thousands) ', **axis_font)
# plt.legend(loc=4)
# plt.savefig('goodness_top_100.pdf', bbox_inches='tight')


# plt.xlabel('# of graph nodes (in thousands) ', **axis_font)
# plt.ylabel('Visited Ratio', **axis_font)


# plt.savefig('speedup.pdf', bbox_inches='tight')
# plt.show()

# plt.plot(trend[:,0], trend[:,1], c='g', marker ='p', ls="solid",label='Query Time', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], c='k', marker="8",ls="solid",label='# of Skyline candidates', ms=15, lw=4)
# plt.ylabel('Ratio', **axis_font)
# plt.xlabel('# of graph nodes (in thousands)')
# plt.legend(loc=1)
# plt.savefig('goodness_top_100.pdf', bbox_inches='tight')



#index building
# plt.plot(trend[:,0], trend[:,1], c='g', marker ='p', ls="solid",label='Index Size', ms=18, lw=4)
# plt.ylabel('Size in Disk (M)', **axis_font)
# # plt.ylabel('Construction Time (Sec.)', **axis_font)
# plt.xlabel('Index size vs. N (|D|=1,000, N in 100K)')
# plt.legend(loc=2)
# # plt.savefig('index_c_time.pdf', bbox_inches='tight')
# plt.savefig('index_size.pdf', bbox_inches='tight')

##############################
# Astar Comparison
##############################

#Running time
# plt.plot(trend[:,0], trend[:,1], c='C1', marker ='x', fillstyle='none',markeredgewidth="4",ls="-.",label='Approx-A*-landmark', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], 'b^-', label='ExactAlg-baseline', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], 'ro-', label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
# plt.ylabel('Running Time (Sec.)', **axis_font)
# plt.legend(loc=2,framealpha=0.3)

#comparison 4 methods
# plt.plot(trend[:,0], trend[:,1], c='C1', marker ='x', fillstyle='none',markeredgewidth="4",ls="-.",label='Approx-A*-landmark', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,2], 'b^-', label='ExactAlg-baseline', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,3], 'ro-', label='ExactAlg-improved', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.legend(loc=2,framealpha=0.3)
# output="astar_frequency_comparison_4_methods.pdf"

#comparison of A* with appro-range-index
# plt.plot(trend[:,0], trend[:,1], c='C1', marker ='x', fillstyle='none',markeredgewidth="4",ls="-.",label='Approx-A*-landmark', ms=18, lw=4)
# plt.plot(trend[:,0], trend[:,4], c='g', marker ='s', fillstyle='none',markeredgewidth="4",ls="--",label='Approx-range-indexed', ms=18, lw=4)
# plt.ylabel('# of Skyline Candidates', **axis_font)
# plt.legend(loc=2,framealpha=0.3)
# output="astar_frequency_comparison_2_methods.pdf"

#X-axis and output#
# plt.xlabel('# of graph nodes (in thousands)', **axis_font)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
# # plt.savefig('astar_frequency_comparison_speed_up.pdf', bbox_inches='tight')
# plt.savefig(output, bbox_inches='tight')


