import os
from flask import Flask, render_template, redirect
from trycourier import Courier
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = 'secret_key'
app.debug = False

client = Courier(auth_token=os.getenv('COURIER_AUTH'))

@app.route('/')
def index():
    return render_template('main.html')

def main():
    app.run()

if __name__ == '__main__':
    main()
