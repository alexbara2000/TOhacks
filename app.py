import os
from flask import Flask, render_template, redirect
from trycourier import Courier
from dotenv import load_dotenv

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
    return render_template('province.html')

def main():
    app.run()

if __name__ == '__main__':
    main()
