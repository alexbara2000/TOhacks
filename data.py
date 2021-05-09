from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import datetime as dt
import pandas as pd
import numpy as np
import database
import json as json

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

province_map = dict(alberta='_AB', british_columbia='_BC', manitoba='_MB', new_brunswick='_NB', newfoundland_and_labrador='_NL', northwest_territories='_NT', nova_scotia='_NS', nunavut='_NU', ontario='_ON', prince_edward_island='_PE', quebec='_QC', saskatchewan='_SK', yukon='_YT')

def predictNextDay(csv, days):
    data = pd.read_csv(csv+'.csv')
    data['date'] = pd.to_datetime(data['date'])
    data['date'] = data['date'].map(dt.datetime.toordinal)
    # print (data)
    x = data['date']
    # print(x)
    y = data['new_confirmed']
    z = data['cumulative_confirmed']
    a = data['new_deceased']
    b = data['cumulative_deceased']
    lr_y = LinearRegression()
    lr_y.fit(np.array(x).reshape(-1,1), np.array(y).reshape(-1,1))
    tomorrow_y=lr_y.predict(np.array([[x[0]+days]]))
    lr_z = LinearRegression()
    lr_z.fit(np.array(x).reshape(-1,1), np.array(z).reshape(-1,1))
    tomorrow_z=lr_z.predict(np.array([[x[0]+days]]))
    lr_a = LinearRegression()
    lr_a.fit(np.array(x).reshape(-1,1), np.array(a).reshape(-1,1))
    tomorrow_a=lr_a.predict(np.array([[x[0]+days]]))
    lr_b = LinearRegression()
    lr_b.fit(np.array(x).reshape(-1,1), np.array(b).reshape(-1,1))
    tomorrow_b=lr_b.predict(np.array([[x[0]+days]]))
    return [tomorrow_y[0][0], tomorrow_z[0][0], tomorrow_a[0][0], tomorrow_b[0][0]]


def predictNext5Day(csv):
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
    tomorrow_y=lr_y.predict(np.array([[x[0]+5]]))
    lr_z = LinearRegression()
    lr_z.fit(np.array(x).reshape(-1,1), np.array(z).reshape(-1,1))
    tomorrow_z=lr_z.predict(np.array([[x[0]+5]]))
    lr_a = LinearRegression()
    lr_a.fit(np.array(x).reshape(-1,1), np.array(a).reshape(-1,1))
    tomorrow_a=lr_a.predict(np.array([[x[0]+5]]))
    lr_b = LinearRegression()
    lr_b.fit(np.array(x).reshape(-1,1), np.array(b).reshape(-1,1))
    tomorrow_b=lr_b.predict(np.array([[x[0]+5]]))
    return [tomorrow_y[0][0], tomorrow_z[0][0], tomorrow_a[0][0], tomorrow_b[0][0]]

# print(predictNextDay("Quebec"))
# print(predictNext5Day("Quebec"))


def query_string(province_code):
    return """SELECT date, location_key, new_confirmed, new_deceased, cumulative_confirmed, cumulative_deceased FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key LIKE '%CA""" + province_code +"""%' AND latitude IS NOT null AND new_confirmed IS NOT null
    ORDER BY date ASC
    LIMIT 100000"""


def classify(province):
    province_code = province_map.get(province, '')
    print(province_code)
    table = database.query(query_string(province_code))
    return table.result().to_dataframe()
