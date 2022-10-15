import mysql.connector
mydb=mysql.connector.connect(host="localhost",\
                             user="root",\
                             passwd="python",\
                             database="school")
mycursor=mydb.cursor()
mycursor.execute("INSERT INTO student VALUES(7,'adarsh',17,'Mumbai',398)")
mycursor.execute("INSERT INTO student VALUES(8,'ishu',16,'chail',390)")
mycursor.execute("INSERT INTO student VALUES(9,'anurag',15,'shimla',388)")
mycursor.execute("INSERT INTO student VALUES(10,'amit',19,'goa',300)")
mycursor.execute("INSERT INTO student VALUES(11,'yash',20,'pune',410)")
mycursor.execute("INSERT INTO student VALUES(12,'kapil',18,'delhi',345)")
mydb.commit()
