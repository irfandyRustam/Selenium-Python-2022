# insert, update, delete
import mysql.connector

insert_query = "INSERT INTO student values(104, 'Kim');"
update_query = "UPDATE student SET sname='Mary' WHERE sid=104;"
delete_query = "DELETE FROM student WHERE sid=104;"

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb") # establish connection to db
    curs = con.cursor() # create cursor
    curs.execute(delete_query)  # execute query through cursor
    con.commit()    # commit transaction
    con.close()
except:
    print("Connection failed")

print("Finished ..")