import os
from flask import Flask, render_template, redirect, url_for, jsonify, request
from trycourier import Courier
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = 'secret_key'
app.debug = True

client = Courier(auth_token=os.getenv('COURIER_AUTH'))

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    result = a + b
    print(result)
    return jsonify(result=result)

@app.route('/')
def index():
    return render_template('main.html')

def main():
    app.run()

if __name__ == '__main__':
    main()
