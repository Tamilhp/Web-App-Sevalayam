import pandas as pd
import sqlite3

con = sqlite3.connect('sponsors.db')
wb = pd.read_excel(
    r'C:\Users\Sakthi\Desktop\New folder\Project\November.xlsx', sheet_name=None)

with sqlite3.connect(r'C:\Users\Sakthi\Desktop\New folder\Project\sponsors.db') as con:
    for key in wb:
        wb[key].to_sql(key, con, index=False)
    con.commit()
