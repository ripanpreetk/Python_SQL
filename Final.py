# This script, Opens "canada" database then tells what all tables available in that base and show the content of each table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", #added hostname, I have my database in my PC so I localhost is the hostname
  user="root", #added Username of my database
  password="ripan", #Enter your database password
  database="canada") #Enter the database name which you want to read

mycursor = mydb.cursor()
mycursor.execute("SHOW tables")   #command to show tables

alist=[] #I have created a empty list

for table_names in mycursor: #putting all table tables in "table_names" variable
    for item in table_names: #added another loop as I want all table names in list format [list is arry in java]
        alist.append(item)  #added all the table names in one list/array
print(f"Tables avaialble in database:{alist}\n")

for table_name in alist: # added a loop to expand each table contents
    query=f"select * from {table_name}" #written a query

    mycursor.execute(query)  #executing the above mentioned query

    print(f"TABLE NAME: {table_name}")  #printing table name above each table

    print(mycursor.column_names) #printing column names of a table

    myresult=mycursor.fetchall() #this command fetch all the rows and columns of table
    for x in myresult: #this loop will print them in next lines
        print(x)

    print(f"\nNo of rows in {table_name} : {mycursor.rowcount}")  # printing the number of rows
    print(f"No of columns in {table_name} : {len(mycursor.column_names)}")  # printing the number of columns

    print("\n-----------------------------\n")


