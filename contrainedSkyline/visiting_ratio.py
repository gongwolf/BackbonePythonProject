import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


font = {'family' : 'Arial',
        'weight' : 'normal',
        'size'   : 30}
plt.rc('font', **font)
axis_font = {'fontname':'Arial', 'size':'35'}

fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)


with open('visiting_ratio_200.dat') as infile:
    trend = np.loadtxt(infile)

print trend

data_x=trend[:,0]
data_y=trend[:,1]


print data_x.reshape(-1,1)
print data_y.reshape(-1,1)
regr = linear_model.LinearRegression()
regr.fit(data_x.reshape(-1,1) , data_y.reshape(-1,1) )
predict_y = regr.predict(data_x.reshape(-1,1))
print predict_y

plt.scatter(data_x, data_y,  color='blue',marker='^', s=400)
plt.plot(data_x, predict_y, color='blue', linewidth=8)

plt.xlabel('|D|/N',**axis_font)
plt.ylabel('Visiting Ratio',**axis_font)

plt.savefig('linear_visiting_ratio.pdf', bbox_inches='tight')
