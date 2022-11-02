import pandas as pd 
import sqlite3
from flask import Flask, render_template, request

from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        for key, value in form_data.items():
            with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
                command = "SELECT * FROM November WHERE `Occasion Date` = ?"
                cur = con.execute(command, (value,))
        return render_template('data.html',form_data = cur)
 
 
app.run(host='localhost', port=8080)

"""def hello():
    date = input("Enter the date: ")
    with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
        command = "SELECT * FROM November WHERE `Occasion Date` = ?"
        cur = con.execute(command, (date,))
        for row in cur:
            print(row)

app.run('localhost', port='8080')"""