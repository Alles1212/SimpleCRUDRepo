#!C:\Program Files\Python310\python.exe
# -*- coding: utf-8 -*-
#指定stdio輸出編碼為utf-8，以避免亂碼
import cgi
import sys
#處理stdio輸出編碼，以避免亂碼
sys.stdout.reconfigure(encoding='utf-8')

#連線DB, 取得coonection 與 cursor物件
from dbConfig import conn, cur

#送出http header
print("Content-Type: text/html; charset=utf-8\n")

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from Form Posts
jobName=form.getvalue('name')
jobUrgent=form.getvalue('urgent')
jobContent=form.getvalue('content')

sql = "insert into todo (jobName, jobUrgent, jobContent) values (%s, %s, %s)"; 
#SQL中的 %s 代表未來要用變數綁定進去的地方
cur.execute(sql,(jobName, jobUrgent,jobContent))
conn.commit() #connmit the transaction
conn.close()

print("OK, <a href='a2.list.py'>Back</a>")
