import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import sklearn



def getLocationsInfo(nodeID, node_data):
    row = node_data.loc[node_data[0] == nodeID]
    return [row.iloc[0][1],row.iloc[0][2]]


def draw_Graph_At_Level(level, graphsize,same_t, drawSingle=True, drawFinal=True):
    base_folder = "/home/gqxwolf/mydata/projectData/BackBone/busline_{}_{}/level{}".format(graphsize,float(same_t),level)
    print(base_folder)
    removed_single_graph_folder= base_folder+"/removed_single/"
    final_graph_folder= base_folder+"/final/"

    ####################################################################################
    fig, axs = plt.subplots(nrows=1, ncols=2,figsize=(20, 10))
    ax = axs[0]
    r_s_node_f_name = removed_single_graph_folder+"NodeInfo.txt"
    r_s_seg_f_name = removed_single_graph_folder+"SegInfo.txt"
    r_s_node_data = pd.read_csv(r_s_node_f_name, sep=" ", header=None)
    
    
    with open(r_s_seg_f_name) as f:
        r_s_content = [x.strip('\n') for x in f.readlines()]
    
    for seg in r_s_content:
        start_id = int(seg.split(" ")[0])
        end_id = int(seg.split(" ")[1])
        start_location=getLocationsInfo( start_id, r_s_node_data)
        end_location=getLocationsInfo( end_id, r_s_node_data)
        x = [start_location[0],end_location[0]]
        y = [start_location[1],end_location[1]]
        ax.plot(x,y,'-c')
    
    ax.plot(r_s_node_data[1], r_s_node_data[2],"ro", markersize="6")
    for index,node in r_s_node_data.iterrows():
        ax.annotate(int(node[0]),xy=[node[1]+2,node[2]+2])
    
    ###################################################################################
    ax = axs[1]
    f_node_f_name = final_graph_folder+"NodeInfo.txt"
    f_seg_f_name = final_graph_folder+"SegInfo.txt"
    f_node_data = pd.read_csv(f_node_f_name, sep=" ", header=None)
    
    with open(f_seg_f_name) as f:
        f_content = [x.strip('\n') for x in f.readlines()]

    for seg in f_content:
        start_id = int(seg.split(" ")[0])
        end_id = int(seg.split(" ")[1])
        start_location=getLocationsInfo( start_id, f_node_data)
        end_location=getLocationsInfo( end_id, f_node_data)
        x = [start_location[0],end_location[0]]
        y = [start_location[1],end_location[1]]
        ax.plot(x,y,'-c')

    ax.plot(f_node_data[1], f_node_data[2],"ro", markersize="6")
    for index,node in f_node_data.iterrows():
        ax.annotate(int(node[0]),xy=[node[1]+2,node[2]+2])

    ######################################################################################
    plt.show()

draw_Graph_At_Level(6,10000,2.844)
# draw_Graph_At_Level(2,100,28)
