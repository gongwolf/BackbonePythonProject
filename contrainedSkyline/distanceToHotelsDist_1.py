from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_file = "/home/gqxwolf/mydata/pythonProject/hotels_distance.dat"


with open(data_file) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print content

dist_list=[i+1 for i in range(8)]
print dist_list
sum=int(content[7].split(" ")[1])
print "total ",sum
num_count=np.zeros(len(dist_list))
print num_count

#print content[-1]

Expectation = 0;

i = 0
index = np.zeros(len(dist_list))
for line in  content:
    d_num = line.split(" ")[0]
    counter = float(line.split(" ")[-1])
    print d_num," ",counter
    num_count[i]=counter/sum
    index[i]=i
    i+=1
print index

idx = range(8)
#print len(num_count)
#print len(dist_list)

def plot_bar():
    font = {'family' : 'Arial',
            'weight' : 'normal',
            'size'   : 30}
    plt.rc('font', **font)
    axis_font = {'fontname':'Arial', 'size':'30'}

    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(10)

    plt.bar(index,num_count,width=1,align="center",linewidth="1",edgecolor="k")
    ax.set_xticks(index)
    ax.set_xticklabels(['0.3', '0.5','1','2','3','4','5', '6'])
    plt.xlim(-0.5,7.5)

    #plt.text(0.05, 20, r'Expected Value = 4.212033487',fontsize=20)
    
    plt.ylabel("Percentage",**font)
    plt.xlabel("Distance in (Km)",**font)

    # textstr = 'Expected Value = {0:.2f} ' 

    # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    # ax.text(0.40, 0.95, textstr.format(Expectation), transform=ax.transAxes, fontsize=25, verticalalignment='top', bbox=props)

    # plt.show()
    plt.savefig('percentage_distribution_based_on_pathsEndNodeTo.pdf', bbox_inches='tight')



plot_bar()

