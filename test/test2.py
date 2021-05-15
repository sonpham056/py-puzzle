import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

dataframe = pd.read_csv('test1.csv')
x = dataframe.values[:, 3]
y = dataframe.values[:, 4]

def h(x):
    return a1 * x + a2

def mse(x, y, a1, a2):
    sum = 0
    n = len(x)
    for i in range(n):
        sum += (h(x[i]) - y[i]) ** 2
    return sum/n

#print(mse(x, y, 1, 2))

def derivative_a2(x, y):
    sum = 0
    n = len(x)
    for i in range(n):
        sum += h(x[i]) - y[i]
    return 1 / n * sum

def derivative_a1(x, y):
    sum = 0
    n = len(x)
    for i in range(n):
        sum += (h(x[i]) - y[i]) * x[i]
    return 1 / n * sum



learning_rate = 0.001
a1 = 2
a2 = 2
mse_his = []
for i in range(100): # lặp cho tới khi lỗi < 0.1
    tmp1 = a1 - learning_rate * derivative_a1(x, y)
    print(derivative_a1(x, y))
    tmp2 = a2 - learning_rate * derivative_a2(x, y)
    print(derivative_a2(x, y))
    a1 = tmp1
    a2 = tmp2
    mse_his.append(mse(x, y, a1, a2))

print(a1, a2)
print(mse_his)
print('Nhap du doan: ')
n = int(input())
print(h(n))
x_test = np.arange(0,len(x))
y_test = h(x_test)
plt.scatter(x, y, color = 'red')
plt.plot(mse_his, color = 'blue')
plt.plot(x_test,y_test)
plt.show()
