import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="python",\
                             database="school")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE student(Rollno int(3) primary key,\
name varchar(15),age integer,city char(8))")
