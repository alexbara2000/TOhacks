import os
from flask import Flask, render_template, redirect, json
from trycourier import Courier
from dotenv import load_dotenv
import data

load_dotenv()

app = Flask(__name__)
app.secret_key = 'secret_key'
app.debug = True

client = Courier(auth_token=os.getenv('COURIER_AUTH'))

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/province/<province>', methods=['GET', 'POST'])
def province(province):
    print(data.df.head())
    chart_data = data.df.to_json()
    print(chart_data)

    # chart_data=[]
    # chart_data.append(["date","new_confirmed","new_deceased"])
    # with open(province+'test.csv', mode='r') as csv_file:
    #     reader = csv.reader(csv_file)
    #     print(reader)
    #     for row in reader:
    #         new_row=[row[0],int(row[1]),int(row[2])]
    #         chart_data.append(new_row)

    # data = pd.read_csv(province+'.csv')
    # data['date'] = pd.to_datetime(data['date'])
    # data['date'] = data['date'].map(dt.datetime.toordinal)
    # x = data['date']
    # y = data['new_confirmed']
    # z = data['cumulative_confirmed']
    # a = data['new_deceased']
    # b = data['cumulative_deceased']
    # print(y)
    # chart_data = [x,y,z]
    # print(chart_data)
    # print(chart_data)
    prediction = data.predictNextDay("Quebec")
    # print(prediction)

    # chart_data = [["Year", "Sales", "province"],
    #     ["2004", 1000, 400],
    #     ["2005", 1170, 460],
    #     ["2006", 660, 1120],
    #     ["2007", 1030, 540],]
    return render_template('province.html', province=province, chart_data=chart_data)

def main():
    app.run()

if __name__ == '__main__':
    main()
