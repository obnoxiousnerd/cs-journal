# MySQL show databases and show tables command.

from mysql import connector
cnx = connector.connect(user="root", password="12345678")
if cnx:
    cursor = cnx.cursor()
    cursor.execute("show databases")
    data = cursor.fetchall()
    print(data)
    cursor.execute("use world")
    cursor.execute("show tables")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    cnx.close()
else:
    print("Connection failed.")