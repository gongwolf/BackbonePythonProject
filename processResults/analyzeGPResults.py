import re
import sys


def read_logs(lf):
    with open(lf) as f:
        lines = f.readlines()

    skyline_sum = 0

    for l in lines:
        if "summation" in l:
            c_l = l.replace("\n", "")
            r = re.findall("summation of skyline:\\d+", c_l)
            str_n = r[0].replace("summation of skyline:", "")
            skyline_sum += int(str_n)

    size_in_bytes = skyline_sum*32
    print(size_in_bytes)
    print(size_in_bytes/(10**6))
    print(lines[-2].replace("\n", ""))
    print(lines[-1].replace("\n", ""))


log_file = ["/home/gqxwolf/mydata/projectData/BackBone/output/GP_NY_5_test.log",
            "/home/gqxwolf/mydata/projectData/BackBone/output/GP_NY_10_test.log",
            "/home/gqxwolf/mydata/projectData/BackBone/output/GP_NY_15_test.log"]

for lf in log_file:
    read_logs(lf)
    print("----------------------------------")
