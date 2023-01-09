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

def database_exists(mydb, id):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW DATABASES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(id)):
            return True
    return False


def create_database(mydb, id):
    if (not database_exists(mydb, id)):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("CREATE DATABASE {}".format(id))

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

def check_for_item(mydb, dbname, type, item):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM {} WHERE {} ='{}'".format(dbname, type, item)
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
    if(not check_for_item(mydb, 'emails', 'email', email)):
        u_id = uuid.uuid4()
        while (check_for_item(mydb, 'emails', 'u_id', u_id)):
            u_id = uuid.uuid4()

        sql = "INSERT INTO emails (email, u_id) VALUES (%s, %s)"
        val = ("{}".format(email), "{}".format(u_id))
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "SUCCESS, record inserted.")
    else:
        print("ERROR, EMAIL duplication detected")


def main():
    if (len(sys.argv) == 1):
        print("ERROR, No command given")
        raise

    command = str(sys.argv[1])

    if (command == 'help'):
        print("""
        $ create_database [db_id]
        $ create_table [db_id] [table_name]
        $ reset_table [db_id] [table_name]
        $ insert_email [db_id] [email (single string)]
        $ help
        """)
    else:
        if (len(sys.argv) <= 2):
            print("ERROR, not enough parameters provided")
            raise
        
        if (command == 'create_database'):
            create_database(mydb, sys.argv[2])
        elif (command == 'create_table'):
            mydb = connect_database(sys.argv[2])
            create_table(mydb, sys.argv[3])
        elif (command == 'reset_table'):
            mydb = connect_database(sys.argv[2])
            reset_table(mydb, sys.argv[3])
        elif (command == 'insert_email'):
            mydb = connect_database(sys.argv[2])
            insert_email(mydb, sys.argv[3])
        else:
            print("No command found")


if __name__ == "__main__":
    main()