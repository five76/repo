import pymysql
from  workingrepo import *
import mysql.connector
from pprint import pprint

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
#msql()
def conndb(sql='',val=[],):
    con=mysql.connector.connect(host='localhost',
        user='admin',
        password='AbrecJcz123',
        database='oapisip')
        #charset='utf8')
        #ursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()

    cur.execute("SELECT studID,taskID FROM marks")

    myresult = cur.fetchall()
    pprint(myresult)
    #for x in myresult:
    #    print(x)
    #with con:

     #   cur = con.cursor()
        #sql = "INSERT INTO marks (studID,taskID,mark,date,attempt) VALUES (%s,%s,%s,%s,%s)"
        #val=  ('isip20_01','task_03_01',0,'2021-11-09',0)
      #  cur.executemany(sql,val)

       # con.commit()


conndb()
