import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test5.test_table values('neeraj', 11, 11.22)")
mydb.commit()
