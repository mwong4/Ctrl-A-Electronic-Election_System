import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os

# Connects to database, connecting to localhost by default
def connect_database(database):
    if (database == ""): #Default
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            port="3306"
        )
    else:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            port="3306",
            database="{}".format(database)
        )
    return mydb

# Check if an item of type and of value item
def check_for_item(mydb, tablename, type, item):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM {} WHERE {} ='{}'".format(tablename, type, item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if len(myresult) != 0:
        return True
    return False

# Setter for any database value, using u_id to query
def set_by_u_id(mydb, table, u_id, type, val):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE {} SET {} = '{}' WHERE u_id = '{}'".format(table, type, val, u_id))
    mydb.commit()

# getter for any database value, using u_id to query
def get_by_u_id(mydb, table, u_id, type):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {} WHERE u_id='{}'".format(table, u_id))
    myresult = mycursor.fetchall()
    
    for x in myresult:
        if (type == 'email'):
            return x[0]
        elif (type == 'u_id'):
            return x[1]
        elif (type == 'voted'):
            return x[2]


def main():
    load_dotenv()
    u_id = str(sys.argv[1]) # Get u_id from input

    try:
        mydb = connect_database('ctrl_a') # Below: Make sure user registered and has not voted yet
        if (check_for_item(mydb, 'emails', 'u_id', u_id) and get_by_u_id(mydb, 'emails', u_id, 'voted') == "False"):
            print("True")
        else:
            print("False")
    except:
        print("ERROR")

if __name__ == "__main__":
    main()