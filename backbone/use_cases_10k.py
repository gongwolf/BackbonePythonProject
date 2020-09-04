import sys

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import gc
import glob
import re
import matplotlib.image as mpimg
import numpy as np


def getLocationsInfo(nodeID, node_data):
    row = node_data.loc[node_data[0] == nodeID]
    return [row.iloc[0][1], row.iloc[0][2]]


def read_Path_Node_List(result_folder, method_name, src, dest):
    path_list = []
    path_file = glob.glob("{}/{}_{}_{}*.log".format(result_folder, method_name, src, dest))[0]
    # print(path_file)
    with open(path_file) as f:
        lines = f.readlines()
        for line in lines:
            # print(line.strip())
            if method_name == "backbone" and "-->" not in line:
                node_str_list = line.split("[")[2].replace("]", "").replace(" ", "")
                path_list.append([int(node) for node in node_str_list.split(",")])
            else:
                r = re.findall("\(.*", line.strip())
                if method_name == 'bbs':
                    str_path = r[0]
                elif method_name == 'backbone':
                    str_path = r[0].replace("--[null]-->", ",")
                node_str_list = re.sub("--\[\d{1,5}\]-->", ",", str_path.replace("(", "").replace(")", ""))
                path_list.append([int(node) for node in node_str_list.split(",")])

    # print(len(path_list), " paths")
    return path_list


def drawSpecialPath(path_list, ax, node_data, marker="-b", lw=0.5):
    for i in range(len(path_list)):
        # print("Drawing path {} ............................".format(i))
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


def draw_bbs_path(graph_folder, save_path, result_path, src, dest):
    fig, ax = plt.subplots(figsize=(20, 15), dpi=334)
    # print(graph_folder)

    node_f_name = graph_folder + "NodeInfo.txt"
    seg_f_name = graph_folder + "SegInfo.txt"

    node_data = pd.read_csv(node_f_name, sep=" ", header=None)

    with open(seg_f_name) as f:
        content = [x.strip("\n") for x in f.readlines()]

    src_node = node_data.loc[node_data[0] == src]
    dest_node = node_data.loc[node_data[0] == dest]
    plt.scatter(src_node[1], src_node[2], marker="*", color="r", alpha=0.99)
    plt.scatter(dest_node[1], dest_node[2], marker="*", color="r", alpha=0.99)

    # index = 0
    for seg in content:
        start_id = int(seg.split(" ")[0])
        end_id = int(seg.split(" ")[1])
        start_location = getLocationsInfo(start_id, node_data)
        end_location = getLocationsInfo(end_id, node_data)
        x = [start_location[0], end_location[0]]
        y = [start_location[1], end_location[1]]
        plt.plot(x, y, "-c", lw=0.5)
        # index += 1
        # if index % 1000 == 0:
        #     print(index, "-------------")

    bbs_paths = read_Path_Node_List(result_path, 'bbs', src, dest)
    drawSpecialPath(bbs_paths, ax, node_data)

    # plt.scatter(node_data[1], node_data[2], marker="o", alpha=0.99)
    plt.savefig(save_path)
    gc.collect()


def draw_backbone_path(graph_folder, save_path, result_path, src, dest):
    fig, ax = plt.subplots(figsize=(20, 15), dpi=334)
    # print(graph_folder)

    node_f_name = graph_folder + "NodeInfo.txt"
    seg_f_name = graph_folder + "SegInfo.txt"

    node_data = pd.read_csv(node_f_name, sep=" ", header=None)

    with open(seg_f_name) as f:
        content = [x.strip("\n") for x in f.readlines()]

    src_node = node_data.loc[node_data[0] == src]
    dest_node = node_data.loc[node_data[0] == dest]
    plt.scatter(src_node[1], src_node[2], marker="*", color="r", alpha=0.99)
    plt.scatter(dest_node[1], dest_node[2], marker="*", color="r", alpha=0.99)

    index = 0
    for seg in content:
        start_id = int(seg.split(" ")[0])
        end_id = int(seg.split(" ")[1])
        start_location = getLocationsInfo(start_id, node_data)
        end_location = getLocationsInfo(end_id, node_data)
        x = [start_location[0], end_location[0]]
        y = [start_location[1], end_location[1]]
        plt.plot(x, y, "-c", lw=0.5)
        # index += 1
        # if index % 1000 == 0:
        #     print(index, "-------------")

    bbs_paths = read_Path_Node_List(result_path, 'backbone', src, dest)
    drawSpecialPath(bbs_paths, ax, node_data)

    # plt.scatter(node_data[1], node_data[2], marker="o", alpha=0.99)
    plt.savefig(save_path)
    gc.collect()


def draw_raw_Graph(graph_folder, bbs_save_path, backbone_save_path, result_path, src, dest):
    draw_bbs_path(graph_folder, bbs_save_path, result_path, src, dest)
    draw_backbone_path(graph_folder, backbone_save_path, result_path, src, dest)

    img1 = mpimg.imread(bbs_save_path)
    img2 = mpimg.imread(backbone_save_path)

    plt.figure(1)
    plt.subplot(121)
    plt.imshow(img1)

    plt.subplot(122)
    plt.imshow(img2)
    plt.title('"C9_NY_10K_graph_{}_{}.png".format(src, dest)')
    plt.savefig(graph_folder + "C9_NY_10K_graph_{}_{}.png".format(src, dest))
    plt.cla()
    plt.clf()


# '''USE CASES ON C9_NY_10K'''
query_list = np.genfromtxt('query.list', delimiter='	')
# print(query_list)
for query in query_list:
    src = int(query[0])
    dest = int(query[1])
    print("drawing the figures from {} to {}".format(src, dest))
    path = "/home/gqxwolf/mydata/projectData/BackBone/C9_NY_10K/level0/"
    bbs_save_path = path + "bbs_C9_NY_10K_graph_{}_{}.png".format(src, dest)
    backbone_save_path = path + "backbone_C9_NY_10K_graph_{}_{}.png".format(src, dest)
    result_path = "/home/gqxwolf/mydata/projectData/BackBone/result/C9_NY_10K/results/"
    draw_raw_Graph(path, bbs_save_path, backbone_save_path, result_path, src, dest)
