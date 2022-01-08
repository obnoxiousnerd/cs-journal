# MySQL create table command.
from mysql import connector

cnx = connector.connect(user="root", password="12345678", database="test")
if cnx:
    cursor = cnx.cursor()
    cursor.execute("drop table if exists xiics")
    cursor.execute("create table xiics (roll_no int, name varchar(20))")
    cursor.execute("desc xiics")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    cnx.close()
else:
    print("Connection failed")
