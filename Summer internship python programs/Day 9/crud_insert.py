import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)

mycursor = conn.cursor()

sql = "INSERT INTO tbl_student(st_name,st_email,st_mobile)VALUES('Drashti', 'd@gmail.com', 9898989898)"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount,"row inserted.")