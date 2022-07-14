import mysql.connector
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="root", database="mydb") # establish connection to db
    curs = con.cursor() # create cursor
    curs.execute("SELECT * FROM caldata")  # execute query through cursor

    for row in curs:
        print(row[0], row[1])

    con.close() # close connection
except:
    print("Connection failed")

print("Finished ..")