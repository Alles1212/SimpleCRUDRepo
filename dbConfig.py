#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb

try:
	conn = mysql.connector.connect(
		user="root",
		password="",
		host="localhost",
		port=3306,
		database="test"
	)

except mysql.connector.Error as e: # mariadb.Error as e:
	print(e)
	print("Error connecting to DB")
	exit(1)
cur=conn.cursor()


