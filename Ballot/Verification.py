import mysql.connector
import uuid
import sys


def connect_database(database):
    if (database == ""):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
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

def check_for_item(mydb, tablename, type, item):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM {} WHERE {} ='{}'".format(tablename, type, item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if len(myresult) != 0:
        return True
    return False


def main():
    u_id = str(sys.argv[1])

    try:
        mydb = connect_database('ctrl_a')
        if (check_for_item(mydb, 'emails', 'u_id', u_id)):
            print("True")
        else:
            print("False")
    except:
        print("ERROR")

if __name__ == "__main__":
    main()