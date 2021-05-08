from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt
import pandas as pd
import numpy as np

# data = pd.read_csv('covidData.csv')
# print(data)
# data['date'] = pd.to_datetime(data['date'])
# data['date'] = data['date'].map(dt.datetime.toordinal)
# x = data['date']
# y = data['new_confirmed']
# z = data['cumulative_confirmed']
# print(x)
# print(y)
# print(z)

# # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

# lr = LinearRegression()
# lr.fit(np.array(x).reshape(-1,1), np.array(y).reshape(-1,1))
# tomoorrow=lr.predict(np.array([[737917]]))
# print(tomoorrow)


# model = DecisionTreeClassifier()

def predictNextDay(csv):
    data = pd.read_csv(csv+'.csv')
    data['date'] = pd.to_datetime(data['date'])
    data['date'] = data['date'].map(dt.datetime.toordinal)
    x = data['date']
    y = data['new_confirmed']
    z = data['cumulative_confirmed']
    a = data['new_deceased']
    b = data['cumulative_deceased']
    lr_y = LinearRegression()
    lr_y.fit(np.array(x).reshape(-1,1), np.array(y).reshape(-1,1))
    tomorrow_y=lr_y.predict(np.array([[737917]]))
    lr_z = LinearRegression()
    lr_z.fit(np.array(x).reshape(-1,1), np.array(z).reshape(-1,1))
    tomorrow_z=lr_z.predict(np.array([[737917]]))
    lr_a = LinearRegression()
    lr_a.fit(np.array(x).reshape(-1,1), np.array(a).reshape(-1,1))
    tomorrow_a=lr_a.predict(np.array([[737917]]))
    lr_b = LinearRegression()
    lr_b.fit(np.array(x).reshape(-1,1), np.array(b).reshape(-1,1))
    tomorrow_b=lr_b.predict(np.array([[737917]]))
    return [tomorrow_y[0][0], tomorrow_z[0][0], tomorrow_a[0][0], tomorrow_b[0][0]]

print(predictNextDay("Quebec"))