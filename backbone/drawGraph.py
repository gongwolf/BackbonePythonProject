import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import os
import gc
import numpy as np
from rand_cmap import rand_cmap
import random as rd
from matplotlib import cm

matplotlib.use("TkAgg")


def readNodeList(node_list_file_name):
    nodelist = []
    with open(node_list_file_name) as f:
        lines = f.readlines()
        nodelist = [int(line) for line in lines]
    return nodelist


def readNodeListWithCoefficient(node_list_file_name):
    node_info = {}
    coefficient_list = []
    with open(node_list_file_name) as f:
        lines = f.readlines()
        for line in lines:
            (node_id, coefficient) = line.split()
            node_info[int(node_id)] = float(coefficient)
            coefficient_list.append(float(coefficient))
    return node_info, list(dict.fromkeys(coefficient_list))


def readPathList(path_file_name):
    path_list = []
    with open(path_file_name) as f:
        lines = f.readlines()
        for line in lines:
            path_list.append([int(node) for node in line.strip().split()])
    return path_list


# edge_list23 = np.loadtxt("backbone/data/edge23")
# edge_list24 = np.loadtxt("backbone/data/edge24")
# edge_list25 = np.loadtxt("backbone/data/edge25")
# edge_list33 = np.loadtxt("backbone/data/edge33")
# edge_list34 = np.loadtxt("backbone/data/edge34")
# edge_list35 = np.loadtxt("backbone/data/edge35")


# node_list_file = "backbone/data/node_list"
# nodeList = readNodeList(node_list_file)

# path_file = "backbone/data/path1"
# path_list = readPathList(path_file)

# node_list_file = "backbone/data/node_list_3227_8222_n"
# nodeList1 = readNodeList(node_list_file)

# node_list_file = "backbone/data/node_list1"
# nodeList1 = readNodeList(node_list_file)

# node_list_file = "backbone/data/node_list2"
# nodeList2 = readNodeList(node_list_file)

# node_list_file = "backbone/data/node_list3"
# nodeList3 = readNodeList(node_list_file)

# source_highway_nodes_file = "backbone/data/node_list_3227_8222_flat_source_node"
# src_highways = readNodeList(source_highway_nodes_file)

# dest_highway_nodes_file = "backbone/data/node_list_3227_8222_flat_dest_node"
# dest_highways = readNodeList(dest_highway_nodes_file)

# node_level_1 = "backbone/data/node_list_3227_out_level1"
# nodeList_level1 = readNodeList(node_level_1)

# node_level_2 = "backbone/data/node_list_3227_out_level2"
# nodeList_level2 = readNodeList(node_level_2)

# node_level_3 = "backbone/data/node_list_3227_out_level3"
# nodeList_level3 = readNodeList(node_level_3)


# node_level_1_dest = "backbone/data/node_list_8222_out_level1"
# nodeList_level1_dest = readNodeList(node_level_1_dest)

# node_level_2_dest = "backbone/data/node_list_8222_out_level2"
# nodeList_level2_dest = readNodeList(node_level_2_dest)

# node_level_3_dest = "backbone/data/node_list_8222_out_level3"
# nodeList_level3_dest = readNodeList(node_level_3_dest)


def getLocationsInfo(nodeID, node_data):
    row = node_data.loc[node_data[0] == nodeID]
    return [row.iloc[0][1], row.iloc[0][2]]


def drawSpecialNode(
    id, ax, node_data, marker="o", markersize="1.5", showtext=False, color="b"
):
    dest_id = id
    dest_node = node_data.loc[node_data[0] == dest_id]
    plt.plot(dest_node[1], dest_node[2], marker,
             markersize=markersize, color=color)
    if showtext:
        ax.annotate(dest_id, xy=(dest_node[1], dest_node[2]))


def drawSpecialEdgs(edge_list, ax, marker="-b", lw=1):
    new_list = edge_list
    if edge_list.ndim == 1:
        new_list = new_list.reshape(-1, 4)
    for e in new_list:
        # print("{}  {}  {}  {}".format(e[0], e[1], e[2], e[3]))
        plt.plot([e[0], e[2]], [e[1], e[3]], marker, linewidth=lw)


def drawSpecialPath(path_list, ax, node_data, marker="-r", lw=2):
    for i in range(len(path_list)):
        print("Drawing path {} ............................".format(i))
        for j in range(len(path_list[i]) - 1):
            start_id = path_list[i][j]
            end_id = path_list[i][j + 1]
            start_node = node_data.loc[node_data[0] == start_id]
            end_node = node_data.loc[node_data[0] == end_id]
            # print(start_node)
            # print(end_node)
            if not start_node.empty and not end_node.empty:
                # print("{}  {} : {} {} {} {} ".format(start_id, end_id, start_node.iloc[0][1], end_node.iloc[0][1], start_node.iloc[0][2], end_node.iloc[0][2]))
                plt.plot(
                    [start_node.iloc[0][1], end_node.iloc[0][1]],
                    [start_node.iloc[0][2], end_node.iloc[0][2]],
                    marker,
                    linewidth=lw,
                )


def draw_raw_Graph(graph_folder, save_path):
    node_list_file = "backbone/data/node_list1"
    node_info, coeff_list = readNodeListWithCoefficient(node_list_file)
    # add 1 for the node not in the list, and add 1 for the border node which color is black
    n_value = len(coeff_list) + 1

    print(coeff_list)
    magma_cmap = cm.get_cmap("magma", n_value)
    # print(magma_cmap.colors)
    # newcolors = magma_cmap(np.linspace(0, 1, len(coeff_list)+1))
    # pink = np.array([248/256, 24/256, 148/256, 1])
    # newcolors[len(coeff_list):, :] = pink
    # newcmp = ListedColormap(newcolors)
    # print(coeff_list)

    # Clear the current axes.
    plt.cla()
    # Clear the current figure.
    plt.clf()
    # Closes all the figure windows.
    plt.close("all")

    fig, ax = plt.subplots(figsize=(20, 15), dpi=334)
    print(graph_folder)
    ###########################################################################
    node_f_name = graph_folder + "NodeInfo.txt"
    seg_f_name = graph_folder + "SegInfo.txt"
    # node_f_name = "/home/gqxwolf/mydata/Backbone_Py_Project/process_challenge9/output/sub_level0_ny_NodeInfo.txt"
    # seg_f_name = "/home/gqxwolf/mydata/Backbone_Py_Project/process_challenge9/output/sub_level0_ny_SegInfo.txt"
    node_data = pd.read_csv(node_f_name, sep=" ", header=None)

    # read the edges informations
    with open(seg_f_name) as f:
        content = [x.strip("\n") for x in f.readlines()]

    print("There are {} edges in the graph. ".format(len(content)))
    print(len(node_data[0]))

    c = []
    for nid in node_data[0]:
        # if nid in nodeList2:
        #     c.append(0)
        if nid in node_info:
            c.append(node_info[nid])
        else:
            c.append(n_value)
    print(len(c))
    print("============================================")

    index = 0
    for seg in content:
        start_id = int(seg.split(" ")[0])
        end_id = int(seg.split(" ")[1])
        start_location = getLocationsInfo(start_id, node_data)
        end_location = getLocationsInfo(end_id, node_data)
        x = [start_location[0], end_location[0]]
        y = [start_location[1], end_location[1]]
        plt.plot(x, y, "-c", lw=0.5)
        index += 1
        if index % 1000 == 0:
            print(index, "-------------")

    # new_cmap = rand_cmap(n_value, type='bright', first_color_black=True,
    #                      last_color_black=False, verbose=False)

    # magma_cmap, or new_cmap
    plt.scatter(node_data[1], node_data[2], marker="o", c=c, cmap=magma_cmap, alpha=1)
    # plt.scatter(node_data[1], node_data[2], marker="o", s=0.4, alpha=0.75)

    print("Finish the reading of the data")

    sptree = np.loadtxt("backbone/data/DijEdges")
    drawSpecialEdgs(sptree, ax, marker="-r", lw=0.5)

    # print(23)
    # drawSpecialEdgs(edge_list23, ax, marker="-r", lw=2)
    # print(24)
    # drawSpecialEdgs(edge_list24, ax, marker="-k", lw=2)
    # print(25)
    # drawSpecialEdgs(edge_list25, ax, marker="-b", lw=2)
    # print(33)
    # drawSpecialEdgs(edge_list33, ax, marker="-g", lw=3)
    # print(34)
    # drawSpecialEdgs(edge_list34, ax, marker="-y", lw=3)
    # print(35)
    # drawSpecialEdgs(edge_list35, ax, marker="-m", lw=4)

    ###
    # drawSpecialNode(3227, ax, node_data, marker="go", markersize=4, showtext=True)
    # drawSpecialNode(8376, ax, node_data, marker="go", markersize=4, showtext=True)
    # drawSpecialNode(8247, ax, node_data, marker="go", markersize=4, showtext=True)

    # drawSpecialPath(path_list, ax, node_data)

    # ####
    # new_cmap = rand_cmap(100, type='bright', first_color_black=True,
    #                      last_color_black=False, verbose=False)

    # for dest_id in nodeList3:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(2))
    
    # for dest_id in nodeList2:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(0))

    # color_idx = rd.randint(1, 99)
    # for dest_id in nodeList2:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(0))

    # color_idx = rd.randint(1,99)
    # for dest_id in nodeList3:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(color_idx))

    # for dest_id in nodeList_level1_dest:
    #     drawSpecialNode(dest_id, ax, node_data)

    # color_idx = rd.randint(1,99)
    # for dest_id in nodeList_level2_dest:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(color_idx))

    # color_idx = rd.randint(1,99)
    # for dest_id in nodeList_level3_dest:
    #     drawSpecialNode(dest_id, ax, node_data, color=new_cmap(color_idx))

    # for dest_id in nodeList2:
    #     drawSpecialNode(dest_id, ax, node_data, marker="go")

    # for dest_id in nodeList3:
    #     drawSpecialNode(dest_id, ax, node_data, marker="yo")

    # drawSpecialNode(8458, ax, node_data, marker="wo")
    # plt.show()
    plt.savefig(save_path)
    gc.collect()


# fig_directory = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY_10K/figs/"
# fig_directory = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY/figs/"

# if not os.path.exists(fig_directory):
#     os.makedirs(fig_directory)

# for i in range(7,-1,-1):
#     level="level{}".format(i)
#     path = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY_10K/" + level + "/"
#     save_path=fig_directory + level + "_111-1.png"
#     draw_raw_Graph(path, save_path)


# level = "level{}".format(0)
# # path = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY/non-single/" + level + "/"
# path = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY_10K/" + level + "/"
# save_path = fig_directory + level + "_103-1.png"
# draw_raw_Graph(path, save_path)

# level = "level{}".format(0)
# path = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY/" + level + "/"
# save_path=fig_directory + level + "_flat_3227_8222_paths.png"
# draw_raw_Graph(path, save_path)


# path = "/home/gqxwolf/mydata/projectData/BackBone/busline_sub_graph_NY/non-single/" + level + "/"
# save_path = fig_directory + level + "_non_single_sub_ny.png"
# draw_raw_Graph(path, save_path)

# node_list_file = "backbone/data/node_list"
# node_info,coeff_list  = readNodeListWithCoefficient(node_list_file)
# magma = cm.get_cmap("magma",len(coeff_list))
# print(coeff_list)

'''USE CASES ON C9_NY_10K'''
path = "/home/gqxwolf/mydata/projectData/BackBone/C9_NY_10K/level0"
save_path = path + "_raw_graph.png"
draw_raw_Graph(path, save_path)
