#!C:\Program Files\Python310\python.exe
# -*- coding: utf-8 -*-
#指定stdio輸出編碼為utf-8，以避免亂碼
import sys 
#處理stdio輸出編碼，以避免亂碼
sys.stdout.reconfigure(encoding='utf-8')

#連線DB, 取得coonection 與 cursor物件
from dbConfig import conn, cur

#送出http header
print("Content-Type: text/html; charset=utf-8\n")

print("""<html><head>
<meta charset="utf-8">
<title>查詢結果</title></head>
<body>
<p>Todo list</p>
<a href="0.輸入表單.html">新增待辦事項</a>
<hr />
<table width="200" border="1">
  <tr>
    <td>id</td>
    <td>Job</td>
    <td>Urgent</td>
    <td>Job Content</td>
    <td>-</td>
  </tr>

""")

# Get data from Form Posts
sql = "select id,jobName, jobUrgent, jobContent from todo;";
cur.execute(sql) 
records = cur.fetchall()       
#用迴圈逐筆取出
for (id, jobName, jobUrgent, jobContent) in records:
	print("<tr><td>", id,"</td><td>", jobName, "</td><td>", jobUrgent, "</td><td>", jobContent, "</td>")
	print("<td></td></tr>")
print("</table>")
print("</body></html>")

cur.close()     #關閉 Cursor 物件
conn.close()

