import pymysql
from  workingrepo import *
 
#con = pymysql.connect('localhost', 'admin', 'AbrecJcz123', 'oapisip')
'''
con=pymysql.connect(host='localhost',
        user='admin',
        password='AbrecJcz123',
        db='oapisip',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

with con: 
 
    cur = con.cursor() 

    cur.execute("SELECT * FROM stud")
 
    rows = cur.fetchall()
 
    for row in rows:
        #print("{0} {1} {2}".format(row[0], row[1], row[2]))
        print(row["studID"], row["studFam"])

'''
msql()
