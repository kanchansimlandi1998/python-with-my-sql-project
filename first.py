




import mysql.connector
connection_data = mysql.connector.connect(host="localhost",username="root",port= 3307,password="1234")
cursor_data=connection_data.cursor()

try:
    cursor_data.execute("SHOW DATABASES")

except:
    connection_data.rollback()

for x in cursor_data:
  print(x)

connection_data.close()