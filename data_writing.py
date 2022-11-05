import pandas as pd
import sqlite3

con = sqlite3.connect('sponsors.db')
wb = pd.read_excel(r'E:\Tamil Selvan\Sqlite sevalayam\November.xlsx', sheet_name=None)

with sqlite3.connect(r'E:\Tamil Selvan\Sqlite sevalayam\sponsors.db') as con:
    for key in wb:
            wb[key].to_sql(key, con, index=False)
    con.commit()
