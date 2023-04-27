from flask import Flask, render_template,request,redirect
from string import Template
import mysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/buscar')
def about():
    return render_template('buscar.html')

if __name__ == '__main__':
    app.run(debug=True)
