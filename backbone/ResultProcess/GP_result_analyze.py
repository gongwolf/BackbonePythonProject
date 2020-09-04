import numpy as np
log_file = "/home/gqxwolf/mydata/projectData/BackBone/output/GP_NY_5_test.log"

with open(log_file) as f:
    lines = f.readlines()
    for l in lines:
        print(l)
