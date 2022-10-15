import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="python",\
                             database="school")
mycursor=mydb.cursor()
mycursor.execute("DELETE FROM student where Rollno=1")
mycursor.execute("DELETE FROM student where Rollno=2")
mycursor.execute("DELETE FROM student where Rollno=3")
mycursor.execute("DELETE FROM student where Rollno=4")
mycursor.execute("DELETE FROM student where Rollno=5")
mycursor.execute("DELETE FROM student where Rollno=6")
mydb.commit()
