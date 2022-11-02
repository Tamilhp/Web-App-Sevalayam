import pandas as pd 
import sqlite3

with sqlite3.connect(r"E:\Tamil Selvan\Sqlite sevalayam\sponsors.db") as con:
    command = "SELECT * FROM November WHERE `Occasion Date` = '2013-11-01 00:00:00'"
    cur = con.execute(command)
    for row in cur:
        print(row)