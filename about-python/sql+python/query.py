import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("select * from test5.test_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()
