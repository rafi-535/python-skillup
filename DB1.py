import mysql.connector
# Create the connection object

myconn=mysql.connector.connect(host="localhost",user="root",password="tiger")

my_cur= myconn.cursor() # Creating cursor object

try:

    d = my_cur.execute("show databases")
    print(d)
except:
    myconn.rollback()

myconn.close()#Closing connection