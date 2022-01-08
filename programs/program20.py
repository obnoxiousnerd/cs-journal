# Program to test connectivity to a MySQL server.

from mysql import connector

cnx = connector.connect(user="root", password="12345678")
if cnx:
    print("Connection established.")
else:
    print("Connection failed.")
cnx.close()
