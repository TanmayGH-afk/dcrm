import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Root@123",
)

cusorObject = dataBase.cursor()

cusorObject.execute("CREATE DATABASE Databasecrm")

print("All Done!")