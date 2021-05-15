import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

dataframe = pd.read_csv('test1.csv')
#c1
x = dataframe[:]['TV']
x = x.values
#c2
y = dataframe.values[:, 4]

regr = linear_model.LinearRegression()
regr.fit(x.reshape(-1, 1), y)
plt.scatter(x, y, color = 'red')

plt.plot(x, regr.predict(x.reshape(-1, 1)), color = 'blue')
print("nhap gia tri du doan: ")
i = int(input())
a = np.array([i]).reshape(-1, 1)
print(regr.predict(a))
plt.show()
