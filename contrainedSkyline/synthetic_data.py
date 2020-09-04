import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

nodenum = str(4000)
node_f_name = "/home/gqxwolf/mydata/projectData/busline_"+nodenum+"/data/NodeInfo.txt"
seg_f_name = "/home/gqxwolf/mydata/projectData/busline_"+nodenum+"/data/SegInfo.txt"

node_f_name = "/home/gqxwolf/mydata/projectData/testGraph"+nodenum+"_4/data/NodeInfo.txt"
seg_f_name = "/home/gqxwolf/mydata/projectData/testGraph"+nodenum+"_4/data/SegInfo.txt"


fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

node_data = pd.read_csv(node_f_name, sep=" ", header=None)
seg_data = pd.read_csv(seg_f_name, sep=" ", header=None)


plt.plot(node_data[1], node_data[2],"ro", markersize="5")

#for seg in seg_data:
for index,row in seg_data.iterrows():
    print row[0],row[1]
    x=[node_data.loc[row[0]][1],node_data.loc[row[0]][2]]
    y=[node_data.loc[row[1]][1],node_data.loc[row[1]][2]]
    plt.arrow(x[0],x[1],y[0]-x[0],y[1]-x[1],fc="k", ec="k",head_width=1, head_length=1 )
    # print y

plt.savefig('synthetic_old_'+nodenum+'.pdf', bbox_inches='tight')

plt.show()