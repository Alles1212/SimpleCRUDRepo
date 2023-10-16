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

print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>無標題文件</title>
</head>
<body>
<p>my todo task</p>
<hr />""")

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from Form Posts
jobID=int(form.getvalue('id'))
if jobID <=0:
	print("error!! empty ID")
	exit(0)

sql = "select jobName, jobUrgent, jobContent from todo where id=%s;"
cur.execute(sql,(jobID,))
jobName, jobUrgent, jobContent = cur.fetchone()

print(f"""
<form method="post" action="a3.update.py">
<input type='hidden' name='jobID' value={jobID}" />
工作名稱: <input name="name" type="text"  value="{jobName}" /> <br>

緊急程度: <select name="urgent">
<option selected value="{jobUrgent}">{jobUrgent}</option>
<option value="普通">普通</option>
<option value="急">急</option>
<option value="急死了">急死了</option>
</select> <br>

工作說明: <textarea name='content'>{jobContent}</textarea><br>

<input type="submit" name="Submit" value="送出" />
</form>
</body>
</html>

""")
