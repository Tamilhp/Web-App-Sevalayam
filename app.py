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
        values = []
        for key, value in form_data.items():
            values.append(value)
        with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
            command = "SELECT `Name`, `Mobile no 1`,`Mobile no 2`, `Occasion`, DATE(`Date`) FROM November_modified WHERE `Occasion Date` = ? AND `Occasion Month`= ?"
            cur = con.execute(command, (values[0],values[1],))
        return render_template('display_data.html',form_data = cur)
 
 
app.run(host='localhost', port=8080)
