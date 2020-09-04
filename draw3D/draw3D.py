#%%
from mpl_toolkits.mplot3d import Axes3D
from numpy import genfromtxt

import numpy as np
import matplotlib.pyplot as plt

#%%
fig = plt.figure(figsize=[60,40])
ax = fig.add_subplot(111, projection='3d')
#%%
my_data = genfromtxt('draw3D/bbs_data', delimiter=' ')
my_query_data = genfromtxt('draw3D/query_data', delimiter=',')
print(my_data)
print(my_query_data)
# %%
ax = plt.axes(projection="3d")
ax.scatter(my_query_data[:,0],my_query_data[:,1],my_query_data[:,2], marker="^")
ax.scatter(my_data[:,0],my_data[:,1],my_data[:,2], marker="o")
ax.set_title("D3 Scatter Plot", size=18)

plt.show()