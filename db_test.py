import os
import pymysql

conn = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    connect_timeout=5
)

print("MySQL connection OK")
cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT*FROM products;")
result = cursor.fetchall()
print(result)
cursor.close()  
conn.close()