import pandas as pd 
import sqlite3
from flask import Flask, render_template, request

from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/enterdata')
def enterdata():
    return render_template("enterdata.html")
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form
        values = []
        for key, value in form_data.items():
            values.append(value)
        with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
            command = "SELECT `Name`, `Mobile no 1`,`Mobile no 2`, `Occasion`, DATE(`Occasion Date`) FROM November WHERE strftime('%d',`Occasion Date`) = ? AND strftime('%m',`Occasion Date`)= ?"
            cur = con.execute(command, (values[0],values[1],))
        return render_template('display_data.html',form_data = cur)
 
@app.route('/savedata', methods = ['POST','GET'])
def savedata():
    if request.method == 'GET':
        return f"The URL /savedata is accessed directly. Try going to '/' to submit form"
    if request.method == 'POST':
        form_data = request.form
        values = []
        for key, value in form_data.items():
            values.append(value)
        with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
            command = "INSERT INTO `November` (`Name`, `Mobile no 1`, `Mobile no 2`,`Occasion`,`Occasion Date`,`Address`) VALUES(?,?,?,?,?,?)"
            con.execute(command, (values[0], values[1], values[2], values[3], values[4], values[5]))
            con.commit()
        return render_template('newdata.html')
app.run(host='localhost', port=8080)
