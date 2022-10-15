import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="python",\
                             database="school")
mycursor=mydb.cursor()
mycursor.execute("Alter table student add(marks int(3))")
