import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

cursor = db.cursor()

sql = "CREATE DATABASE adiva"

cursor.execute(sql)

print("Database berhasil dibuat!")
