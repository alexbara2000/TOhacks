import os
import data
from flask import Flask, render_template, redirect, json
from trycourier import Courier
from dotenv import load_dotenv
from forms import ContactForm
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

@app.route('/mail')
def mail():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        'mail.html',
        form=form
    )

@app.route('/province/<province>', methods=['GET', 'POST'])
def province(province):
    df = data.classify(province)
    new_df = df.drop(columns=['location_key', 'cumulative_confirmed', 'cumulative_deceased'])
    new_df['date'] = new_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    chart_data = [new_df.columns.to_numpy().tolist(), *new_df.values.tolist()]

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
    prediction = []
    for i in range(6):
        prediction.append(data.predict(df, i + 1))
    print(prediction)

    return render_template('province.html', province=province, chart_data=chart_data, prediction=prediction)

def main():
    app.run()

if __name__ == '__main__':
    main()
