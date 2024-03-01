import mysql.connector
conn = mysql.connector.connect(host = "localhost",database = "jm_data",user = "root",password = "root")

cursor = conn.cursor()

print(conn.is_connected())
mysql = "select * from branch"
cursor.execute(mysql)
rows = cursor.fetchall()
print(rows)