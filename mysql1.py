import mysql.connector as c
mydb = c.connect(host = 'localhost', user = 'root', password = 'varshaluthra')
if mydb.is_connected():
    print("Succesfully connected")
else:
     print("Not Connected")
    

