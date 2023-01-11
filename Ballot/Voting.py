import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import json


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
        if (name ==  'emails'):
            mycursor.execute("CREATE TABLE emails (email VARCHAR(255), u_id VARCHAR(255), voted VARCHAR(255))")
        elif (name  == 'votes'):
            mycursor.execute("CREATE TABLE votes (category VARCHAR(255), person VARCHAR(255), u_id VARCHAR(255))")

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

def insert_student(mydb, email):
    mycursor = mydb.cursor(buffered=True)
    if(not check_for_item(mydb, 'emails', 'email', email)):
        u_id = uuid.uuid4()
        while (check_for_item(mydb, 'emails', 'u_id', u_id)):
            u_id = uuid.uuid4()

        sql = "INSERT INTO emails (email, u_id, voted) VALUES (%s, %s, %s)"
        val = ("{}".format(email), "{}".format(u_id), "False")
        mycursor.execute(sql, val)
        mydb.commit()
        return str(u_id)
    else:
        return "ERROR"

def insert_vote(mydb, u_id, category, person):
    mycursor = mydb.cursor(buffered=True)
    if(get_by_u_id(mydb, 'emails', u_id, 'voted') == 'False'):
        sql = "INSERT INTO votes (category, person, u_id) VALUES (%s, %s, %s)"
        val = ("{}".format(category), "{}".format(person), "{}".format(u_id))
        mycursor.execute(sql, val)
        mydb.commit()
        return True
    else:
        return False

def check_args(actual, expected):
    if (actual == expected):
        return True
    else:
        return False

def set_by_u_id(mydb, table, u_id, type, val):
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE {} SET {} = '{}' WHERE u_id = '{}'".format(table, type, val, u_id))
    mydb.commit()

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
    data = str(sys.argv[1])
    print(data)
    data = data.replace('[ ', '["')
    data = data.replace(' ]', '"]')
    data = data.replace('u_id : ', '"u_id" :"')
    data = data.replace(' }', '"}')
    data = data.replace(' , ', '","')

    for x in range(0, 9):
        data = data.replace('vote_{}'.format(x), '"vote_{}"'.format(x))

    res = json.loads(data)
    u_id = res["u_id"]
    mydb = connect_database('ctrl_a')
    create_table(mydb, 'votes')
    
    for group in list(res):
        if (group != "u_id"):
            for item in res[group]:
                result = insert_vote(mydb, u_id, group, item)
                if (result == False):
                    print("ERROR, already voted")
                    exit()
    set_by_u_id(mydb, 'emails', u_id, 'voted', 'True')
    print("Vote Submitted Succesfully")


if __name__ == "__main__":
    main()