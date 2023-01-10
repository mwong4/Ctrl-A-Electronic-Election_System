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
        mycursor.execute("CREATE TABLE {} (email VARCHAR(255), u_id VARCHAR(255), voted VARCHAR(255))".format(name))

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

def check_args(actual, expected):
    if (actual == expected):
        return True
    else:
        print("ERROR, not enough parameters provided")
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
    if (len(sys.argv) == 1):
        print("ERROR, No command given")
        exit()

    command = str(sys.argv[1])
    mydb = connect_database('ctrl_a')
    print(get_by_u_id(mydb, 'emails', '9a516c58-1cc6-4b44-8621-db38def392a5', 'voted'))

    if (command == 'help'):
        print("""
        $ create_database [db_id]
        $ create_table [db_id] [table_name]
        $ reset_table [db_id] [table_name]
        $ insert_email [db_id] [email (single string)]
        $ set [db_id] [table_name] [u_id] [type] [val]
        $ get [db_id] [table_name] [u_id] [type]
        $ help
        """)
    else:
        if (command == 'create_database'):
            if not check_args(len(sys.argv), 3): 
                exit()
            create_database(mydb, sys.argv[2])
        elif (command == 'create_table'):
            if not check_args(len(sys.argv), 4): 
                exit()
            mydb = connect_database(sys.argv[2])
            create_table(mydb, sys.argv[3])
        elif (command == 'reset_table'):
            if not check_args(len(sys.argv), 4): 
                exit()
            mydb = connect_database(sys.argv[2])
            reset_table(mydb, sys.argv[3])
        elif (command == 'insert_email'):
            if not check_args(len(sys.argv), 4): 
                exit()
            mydb = connect_database(sys.argv[2])
            id = insert_student(mydb, sys.argv[3])
        elif (command == 'set'):
            if not check_args(len(sys.argv), 7): 
                exit()
            mydb = connect_database(sys.argv[2])
            set_by_u_id(mydb, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
        elif (command == 'get'):
            if not check_args(len(sys.argv), 6): 
                exit()
            mydb = connect_database(sys.argv[2])
            print(get_by_u_id(mydb, sys.argv[3], sys.argv[4], sys.argv[5]))
        else:
            print("No command found")


if __name__ == "__main__":
    main()