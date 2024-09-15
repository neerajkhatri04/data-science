import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
)

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

type(mycursor)

for x in mycursor:
    print(x)