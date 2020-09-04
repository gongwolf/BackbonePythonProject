from __future__ import division

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_file = "/home/gqxwolf/mydata/pythonProject/hotels_distance.dat"
font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 30}
plt.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

with open(data_file) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print content

dist_list=[i+1 for i in range(len(content))]
print dist_list
# sum=int(content[10].split(" ")[1])
# print "total ",sum
num_count=np.zeros(len(dist_list)+1)
print num_count

sum=0 
for line in content:
    sum+= int(line.split(" ")[1])

print sum
#print content[-1]

Expectation = 0;

for line in  content:
    d_num = int(line.split(" ")[0])
    counter = int(line.split(" ")[-1])
    num_count[d_num]=counter/sum
    Expectation = Expectation+d_num*num_count[d_num]


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

    index = np.arange(len(dist_list)+1)
    plt.bar(index,num_count,width=1.0,align="center",linewidth="1",edgecolor="k")
    ax = plt.gca()
    #plt.text(0.05, 20, r'Expected Value = 4.212033487',fontsize=20)
    plt.xlim(-0.5,len(dist_list)+0.5)
    plt.ylabel("Probability")
    plt.xlabel("Number of Bus Stops within 300 meters")

    textstr = 'Expected Value = {0:.2f} ' 

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # place a text box in upper left in axes coords
    ax.text(0.30, 0.95, textstr.format(Expectation), transform=ax.transAxes, fontsize=30, verticalalignment='top', bbox=props)

    # plt.show()
    plt.savefig('distribute_300.pdf', bbox_inches='tight')



plot_bar()

