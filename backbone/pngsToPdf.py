from PIL import Image
import os
import re

path = "/home/gqxwolf/mydata/projectData/BackBone/C9_NY_10K/level0/"

img_file_list = []
for f in os.listdir(path):
    if re.match(r'C9_NY_10K_graph.*\.png', f):
        img_file_list.append(f)

image = Image.open("{}{}".format(path, img_file_list[0]))
im = image.convert('RGB')
# im.save("{}C9_NY_10K_list_all.pdf".format(path))
print("{}{}".format(path, img_file_list[0]))

imagelist = []
for i in range(1, len(img_file_list)):
    image_append = Image.open("{}{}".format(path, img_file_list[i]))
    im_append = image_append.convert('RGB')
    imagelist.append(im_append)
    print("{}{}".format(path, img_file_list[i]))
im.save("{}C9_NY_10K_list_all.pdf".format(path), save_all=True, append_images=imagelist)
