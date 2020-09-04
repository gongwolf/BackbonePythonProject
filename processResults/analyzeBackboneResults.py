import numpy as np

import re

log_file = "/home/gqxwolf/shared_git/backboneProject/output/Backbone_LFF_SF_300-[2020-08-12~10-13-55].log"

rt_list = []

reg_str = "running time of finding results at highest level:"
with open(log_file) as f:
    for l in f.readlines():
        if reg_str in l:
            cl = l.replace("\n", "")
            r = re.findall(reg_str + " \\d+", cl)
            rt_list.append(int(r[0].replace(reg_str, "")))

rt = np.asarray(rt_list)
print(rt.sum(0))
print(rt.shape)
print(round(rt.sum(0) / rt.shape[0], 3))
