import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv("test1.csv")
data = data[['TV', 'radio', 'newspaper', 'sales']]
#0 for row and 1 for column
#X = np.array(data['TV'])
X = np.array(data.drop('sales', 1))
y = np.array(data['sales'])
#print(X)
#print(y)
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.2)

#dung reshape khi chi lay 1 thuoc tinh vi khi lay 1 thuoc tinh thi chi co mang 1 chieu ma fit yeu cau X phai la mang 2 chieu
#X_train = X_train.reshape(-1, 1)q
#X_test = X_test.reshape(-1, 1)
#print(X_test)
#print(y_test)
'''max = 0
for _ in range(10000):
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()
    linear.fit(X_train, y_train)
    acc = linear.score(X_test, y_test)
    if max < acc:
        max = acc
        with open("HouseModel.pickle", "wb") as f:
            pickle.dump(linear, f)'''

pickle_in = open("HouseModel.pickle", "rb")
linear = pickle.load(pickle_in)
acc = linear.score(X_test, y_test)

print(acc)
print('coef: \n', linear.coef_)
print('intercept: \n', linear.intercept_)

draw = linear.predict(X_test)
#draw
plt.scatter(data['TV'], data['sales'])
plt.plot(X_test, linear.predict(X_test), color='black')
plt.show()
