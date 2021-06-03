import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", #added hostname, I have my database in my PC so I localhost is the hostname
  user="root", #added Username of my database
  password="ripan", #Enter your database password
  )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase") #command to create database if doesn't exist
mycursor.execute("SHOW DATABASES") #this command will show all the databases available at the address mentioned above

for x in mycursor: #this command will print all databases names
  print(x)
