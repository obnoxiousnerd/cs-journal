# MySQL insert command.

from mysql import connector

cnx = connector.connect(user="root", password="12345678", database="test")
if cnx:
    cursor = cnx.cursor()
    cursor.execute("insert into xiics values (1, 'David')")
    cursor.execute("insert into xiics values (2, 'Victor')")
    cursor.execute("insert into xiics values (3, 'Eric')")
    cursor.execute("insert into xiics values (4, 'Phil')")
    cursor.execute("commit")
    cursor.execute("select * from xiics")
    data = cursor.fetchall()
    print(data)
    cursor.close()
    cnx.close()
else:
    print("Connection failed")
