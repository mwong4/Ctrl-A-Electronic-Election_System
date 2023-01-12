import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import getpass

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

# Querries if a database already exists
def database_exists(mydb, id):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW DATABASES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(id)):
            return True
    return False

# Creates a database, if one does not exist
def create_database(mydb, id):
    if (not database_exists(mydb, id)):
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("CREATE DATABASE {}".format(id))

# Querries if a table already exists
def table_exists(mydb, name):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW TABLES")

    for item in mycursor:
        if (str(item) == "('{}',)".format(name)):
            return True
    return False

# Creates a table, if one does not exist. Two options, emails table or votes table
def create_table(mydb, name):
    mycursor = mydb.cursor(buffered=True)
    if (not table_exists(mydb, name)):
        if (name ==  'emails'):
            mycursor.execute("CREATE TABLE emails (email VARCHAR(255), u_id VARCHAR(255), voted VARCHAR(255))")
        elif (name  == 'votes'):
            mycursor.execute("CREATE TABLE votes (category VARCHAR(255), person VARCHAR(255), u_id VARCHAR(255))")

# Check if an item of type and of value item
def check_for_item(mydb, dbname, type, item):
    mycursor = mydb.cursor(buffered=True)
    sql = "SELECT * FROM {} WHERE {} ='{}'".format(dbname, type, item)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if len(myresult) != 0:
        return True
    return False

# Drops, then recreates a table
def reset_table(mydb, table):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("DROP TABLE IF EXISTS {}".format(table))
    create_table(mydb, table)
    print("SUCCESS, {} resetted".format(table))

# Specifically designed to insert a student
def insert_student(mydb, email):
    mycursor = mydb.cursor(buffered=True)
    if(not check_for_item(mydb, 'emails', 'email', email)):
        u_id = uuid.uuid4()
        while (check_for_item(mydb, 'emails', 'u_id', u_id)):
            u_id = uuid.uuid4() # Generate unique ID

        sql = "INSERT INTO emails (email, u_id, voted) VALUES (%s, %s, %s)"
        val = ("{}".format(email), "{}".format(u_id), "False")
        mycursor.execute(sql, val) # Add to database
        mydb.commit()
        return str(u_id)
    else:
        return "ERROR"

# Check if there are enough arguments, for menu
def check_args(actual, expected):
    if (actual == expected):
        return True
    else:
        print("ERROR, not enough parameters provided")
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

#Count the occurances of a category of value person
def count_all(mydb, table, category, person):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {} WHERE category='{}' AND person='{}'".format(table, category, person))
    result = mycursor.fetchall()
    return len(result)


def main():
    load_dotenv()
    if (len(sys.argv) == 1): #  Check for existence of a command
        print("ERROR, No command given")
        exit()

    command = str(sys.argv[1]) #Grab command
    mydb = connect_database('ctrl_a') #Connect to database

    if (command == 'help'): #Displays list of available commands
        print("""
        $ create_database [db_id]
        $ create_table [db_id] [table_name]
        $ reset_table [db_id] [table_name]
        $ insert_email [db_id] [email (single string)]
        $ set [db_id] [table_name] [u_id] [type] [val]
        $ get [db_id] [table_name] [u_id] [type]
        $ count [db_id] [table_name] [filter] [val]
        $ help
        """)
    else:
        passwd = getpass.getpass("Enter CLI Password: ") #Prompt for password
        real_pass =  os.getenv('CLI_PASSWORD')

        if(passwd == real_pass): #executes the command based off command entered and parameters
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
            elif (command == 'count'):
                if not check_args(len(sys.argv), 6): 
                    exit()
                mydb = connect_database(sys.argv[2])
                print(count_all(mydb, sys.argv[3], sys.argv[4], sys.argv[5]))
            else:
                print("No command found")
        else:
            print("ERROR, password is incorrect")


if __name__ == "__main__":
    main()