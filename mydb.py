import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'soupablo'
)


cursorObject = dataBase.cursor()  

cursorObject.execute('CREATE DATABASE elderCEO')


print('perfectoooo')