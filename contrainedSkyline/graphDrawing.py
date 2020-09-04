import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn

node_f_name = "/home/gqxwolf/mydata/projectData/testGraph50_4/data/NodeInfo.txt"
seg_f_name = "/home/gqxwolf/mydata/projectData/testGraph50_4/data/SegInfo.txt"
hotel_f_name = "/home/gqxwolf/shared_git/bConstrainSkyline/data/staticNode.txt"

node_data = pd.read_csv(node_f_name, sep=" ", header=None)
rect_hw=30
rect_q=100

hotel_data = pd.read_csv(hotel_f_name,sep=",", header=None)

plt.plot(node_data[1], node_data[2],"ro", markersize="6")
plt.plot(hotel_data[1], hotel_data[2],"bs")

for index,node in hotel_data.iterrows():
    #print node[1],",",node[2] 
    #plt.axhline(y=node[2],color="b",ls="dashed",lw=0.3)
    #plt.axvline(x=node[1],color="b",ls="dashed",lw=0.3)
    #circle = plt.Circle((node[1],node[2]),30, color='r',fill=False)
    #if node[0] in [4,24,11,10,16,3,18]:
    #    rectangle = plt.Rectangle((node[1]-rect_hw/2,node[2]-rect_hw/2),rect_hw,rect_hw,fill=False,ls="dashed",color="g")
    #else:
    #    rectangle = plt.Rectangle((node[1]-rect_hw/2,node[2]-rect_hw/2),rect_hw,rect_hw,fill=False,ls="dashed")
    #rectangle = plt.Rectangle((node[1]-rect_hw/2,node[2]-rect_hw/2),rect_hw,rect_hw,fill=False,ls="dashed")
    plt.annotate(int(node[0]),xy=[node[1]-8,node[2]+2])
    #plt.gca().add_patch(rectangle)

for index,node in node_data.iterrows():
    #rectangle = plt.Rectangle((node[1]-rect_hw/2,node[2]-rect_hw/2),rect_hw,rect_hw,fill=False,ls="dashed")
    if node[0] in [7,24,4,11,32,15,0,6,21,26,8,30]:
        plt.annotate(int(node[0]),xy=[node[1]+2,node[2]+2],color="r")
    #elif node[0] in [0,2,3,9,10,14,16,17,18,19,23,24,31,33,36,37,40,45,46,48,49]:
    #    plt.annotate(int(node[0]),xy=[node[1]+2,node[2]+2],color="y")
    #elif node[0] in [21,7,6,39,15,30]:
    #    plt.annotate(int(node[0]),xy=[node[1]+2,node[2]+2],color="c")
    else:
        plt.annotate(int(node[0]),xy=[node[1]+2,node[2]+2])
    #plt.gca().add_patch(rectangle)


query_p = [123.22092,139.60222]
plt.plot(query_p[0],query_p[1],"rs")
plt.axhline(y=query_p[1],color="r")
plt.axvline(x=query_p[0],color="r")

circle = plt.Circle(query_p, 100, color='r',fill=False)
rectangle = plt.Rectangle((query_p[0]-rect_q/2,query_p[1]-rect_q/2),rect_q,rect_q,fill=False,color="r")
plt.gca().add_patch(rectangle)
plt.gca().add_patch(circle)

plt.annotate("q",xy=[query_p[0]+2,query_p[1]+2])


with open(seg_f_name) as f:
    content = [x.strip('\n') for x in f.readlines()]

for n in np.arange(0,380,40):
    plt.axhline(y=n,color="b", ls ="dashed",lw=0.4)
    plt.axvline(x=n,color="b", ls ="dashed",lw=0.4)

def drawPath(x):
    x = x.split("-")
    end_x=0
    end_y=0

    for i in xrange(0,len(x)-2,2):
        start=int(x[i][1:-1])
        end=int(x[i+2][1:-1])
        #print start,"  ",end
        #print node_data.iloc[start]
        x1 = node_data.iloc[start][1]
        x2 = node_data.iloc[end][1]
        end_x=x2
        y1 = node_data.iloc[start][2]
        y2 = node_data.iloc[end][2]
        end_y=y2
        #plt.plot([x1,x2],[y1,y2],'r-',lw=0.4)
        plt.arrow(x1,y1,x2-x1,y2-y1,head_width=3, head_length=2, color="k",ls="dotted")
    plt.plot(end_x,end_y,"ks",markersize="2") 


# path = []
# path.append("(29)-[128]-(10)-[168]-(30)-[184]-(26)-[112]-(0)-[121]-(23)")
# path.append("(24)-[127]-(33)-[26]-(20)-[93]-(36)")

# for p in path:
#     #print type(p)
#     drawPath(p)

#aaaa = plt.axes()

    
#print node_data
#print "================"
#print node_data.iloc[0]
#for c in content:
#    startNode = int(c.split(" ")[0])
#    endNode = int(c.split(" ")[1])
#    x1=node_data.iloc[startNode][1]
#    x2=node_data.iloc[endNode][1]
#    y1=node_data.iloc[startNode][2]
#    y2=node_data.iloc[endNode][2]
#    plt.plot([x1,x2],[y1,y2],'r-',lw=0.4)
plt.axis('scaled')
plt.show()
