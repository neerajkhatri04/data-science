import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE table if not exists test5.test_table(col1 VARCHAR(10), col2 int, col3 float)")

mydb.close()