import mysql.connector
database=mysql.connector.connect(
host='localhost',
user='root',
password='s1m0n2oo2',

)


cursorobject= database.cursor()
cursorobject.execute('CREATE DATABASE elder ')

print("all done")

