import mysql.connector
import pandas as pd
import uuid

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
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(id)):
            return True
    return False


def create_database(mydb, id):
    if (not databse_exists(mydb, id)):
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE {}".format(id))
        return mycursor
    return mydb.cursor()


def table_exists(mydb, name):
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(name)):
            return True
    return False


def create_table(mydb, name):
    mycursor = mydb.cursor()
    if (not table_exists(mydb, name)):
        mycursor.execute("CREATE TABLE {} (email VARCHAR(255), u_id VARCHAR(255))".format(name))


def check_for_item(mydb, type, item):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM emails WHERE {} ='{}'".format(type, item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if len(myresult) > 0:
        return True
    return False


def reset_table(mydb, table):
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS {}".format(table))
    create_table(mydb, table)
    print("SUCCESS, {} resetted".format(table))


def insert_email(mydb, email):
    mycursor = mydb.cursor()
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


def main():
    mydb = connect_database('')
    create_database(mydb, 'ctrl_a')
    mydb = connect_database('test')
    reset_table(mydb, 'emails')
    insert_email(mydb, 'hi@uwaterloo.ca')



if __name__ == "__main__":
    main()