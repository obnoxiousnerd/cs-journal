# MySQL update command.

from mysql import connector

cnx = connector.connect(user="root", password="12345678", database="test")
if cnx:
    cursor = cnx.cursor()
    cursor.execute("update xiics set name='Dean' where name='David'")
    cursor.execute("select * from xiics")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    cnx.close()
else:
    print("Connection failed")