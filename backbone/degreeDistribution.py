import numpy as np
import matplotlib.pyplot as plt

degree_number = [3135, 3272, 9881, 3632, 66, 44]
degree_name = [i for i in range(1, len(degree_number)+1)]

fig, ax = plt.subplots(figsize=(20, 15))
plt.bar(degree_name, degree_number, width=0.99, align="center")
plt.show()
