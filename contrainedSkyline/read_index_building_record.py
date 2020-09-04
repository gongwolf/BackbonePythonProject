import subprocess
import os

fname = "/home/gqxwolf/shared_git/bConstrainSkyline/target/output/complementary/index_building_records.txt"

def getFolderSize(path):
    """disk usage in human readable format (e.g. '2,1GB')"""
    return subprocess.check_output(['du','-sh', path]).split()[0].decode('utf-8')

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

graphsize=degree=t_range=hotelnum=0
index_c_time = long(0)
size = 0

for line in content:
    if line.startswith("/"):
        size = getFolderSize(line)
        index_file_name = line.split("/")[-1]
        graphsize = index_file_name.split("_")[1]
        degree = index_file_name.split("_")[2]
        t_range = index_file_name.split("_")[3]
        hotelnum = index_file_name.split("_")[4]
    if line.startswith("index"):
        index_c_time = float(line.split(" ")[-1])/1000
        print("%s-%s-%s-%s    %.2f  %s" %(graphsize,degree,t_range,hotelnum,index_c_time,size))

