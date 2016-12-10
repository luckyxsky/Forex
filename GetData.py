__author__ = 'Administrator'

import sqlite3

cx=sqlite3.connect("./data/ForexUniverseData.db")
cu=cx.cursor()

cu.execute("select * from GBPUSDH1")
#cu.fetchall()

for item in cu.fetchall():
    for element in item:
        print element,
        print


