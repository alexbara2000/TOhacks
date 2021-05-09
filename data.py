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

def predictNextDay(csv):
    data = pd.read_csv(csv+'.csv')
    print(data)
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
    tomorrow_y=lr_y.predict(np.array([[x[0]+1]]))
    lr_z = LinearRegression()
    lr_z.fit(np.array(x).reshape(-1,1), np.array(z).reshape(-1,1))
    tomorrow_z=lr_z.predict(np.array([[x[0]+1]]))
    lr_a = LinearRegression()
    lr_a.fit(np.array(x).reshape(-1,1), np.array(a).reshape(-1,1))
    tomorrow_a=lr_a.predict(np.array([[x[0]+1]]))
    lr_b = LinearRegression()
    lr_b.fit(np.array(x).reshape(-1,1), np.array(b).reshape(-1,1))
    tomorrow_b=lr_b.predict(np.array([[x[0]+1]]))
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

print(predictNextDay("Quebec"))
print(predictNext5Day("Quebec"))




#query_string = """SELECT date, location_key , place_id, new_confirmed, new_deceased, cumulative_confirmed, cumulative_deceased, latitude, longitude FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
#WHERE country_code LIKE '%CA%' AND latitude IS NOT null AND new_confirmed IS NOT null
#ORDER BY date DESC
#LIMIT 100000
#"""

def queryString_filtered(Province_code):
    return """SELECT date, location_key , place_id, new_confirmed, new_deceased, cumulative_confirmed, cumulative_deceased, latitude, longitude FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE location_key LIKE '%CA""" + Province_code +"""%' AND latitude IS NOT null AND new_confirmed IS NOT null
    ORDER BY date DESC
    LIMIT 100000"""


#table = database.query(query_string)

#  for row in table.result():  # Wait for the job to complete.
#     print("{}: {}, {}, {}, {}, {}, {}".format(row["date"], row["new_confirmed"], row["new_deceased"], row["cumulative_confirmed"], row["cumulative_deceased"], row["latitude"], row["longitude"]))



def ClassifyData(table):
    byProvince  = table.result().to_dataframe()
    return byProvince

q = queryString_filtered("_QC")
print(q)
table = database.query(q)
p = ClassifyData(table)
print(p)

