import mysql.connector
import pandas as pd
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

def databse_exists(mydb, id):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW DATABASES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(id)):
            return True
    return False


def create_database(mydb, id):
    if (not databse_exists(mydb, id)):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("CREATE DATABASE {}".format(id))
        return mycursor
    return mydb.cursor()


def table_exists(mydb, name):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW TABLES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(name)):
            return True
    return False


def create_table(mydb, name):
    mycursor = mydb.cursor(buffered=True)
    if (not table_exists(mydb, name)):
        mycursor.execute("CREATE TABLE {} (email VARCHAR(255), u_id VARCHAR(255))".format(name))


def check_for_item(mydb, type, item):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM emails WHERE {} ='{}'".format(type, item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if len(myresult) != 0:
        return True
    return False


def reset_table(mydb, table):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("DROP TABLE IF EXISTS {}".format(table))
    create_table(mydb, table)
    print("SUCCESS, {} resetted".format(table))


def insert_email(mydb, email):
    mycursor = mydb.cursor(buffered=True)
    if(not check_for_item(mydb, 'email', email)):
        u_id = uuid.uuid4()
        while (check_for_item(mydb, 'u_id', u_id)):
            u_id = uuid.uuid4()

        sql = "INSERT INTO emails (email, u_id) VALUES (%s, %s)"
        val = ("{}".format(email), "{}".format(u_id))
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "SUCCESS, record inserted.")
    else:
        print("ERROR, EMAIL duplication detected")


#Commands:
#
#connect_database
#create_database
#select_table
#reset_table
#insert_email

def main():
    command = str(sys.argv[1])
    input = []
    counter = 0

    if (len(sys.argv) == 0):
        print("ERROR, No command given")
        raise

    for item in sys.argv:
        if counter == 0:
            command = str(item)
        else:
            input.insert(item)

    if (command == ''):
        
    elif (command == ''):
        




if __name__ == "__main__":
    main()