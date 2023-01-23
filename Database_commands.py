import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import getpass

# Connects to database, connecting to localhost by default
def connect_database(database):
    try:
        if (database == ""): #Default, without database specified
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('PORT')
            )
        else:
            mydb = mysql.connector.connect(
                host=os.getenv('HOST'),
                user=os.getenv('USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('PORT'),
                database="{}".format(database)
            )
        return mydb
    except:
        print("Error, Could not connect to database", file=sys.stderr)

# Querries if a database already exists
def database_exists(mydb, id):
    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SHOW DATABASES")

        for item in mycursor:
            if (str(item) == "('{}',)".format(id)):
                return True
        return False
    except:
        print("Error, Could not check database", file=sys.stderr)

# Creates a database, if one does not exist
def create_database(mydb, id):
    try:
        if (not database_exists(mydb, id)):
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute("CREATE DATABASE {}".format(id))
    except:
        print("Error, Could not create database", file=sys.stderr)

# Querries if a table already exists
def table_exists(mydb, name):
    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SHOW TABLES")

        for item in mycursor:
            if (str(item) == "('{}',)".format(name)):
                return True
        return False
    except:
        print("Error, Could not check table", file=sys.stderr)

# Creates a table, if one does not exist. Two options, emails table or votes table
def create_table(mydb, name):
    try:
        mycursor = mydb.cursor(buffered=True)
        if (not table_exists(mydb, name)):
            if (name ==  'emails'):
                mycursor.execute("CREATE TABLE emails (email VARCHAR(255), u_id VARCHAR(255), voted VARCHAR(255))")
            elif (name  == 'votes'):
                mycursor.execute("CREATE TABLE votes (category VARCHAR(255), person VARCHAR(255), u_id VARCHAR(255))")
    except:
        print("Error, Could not create table", file=sys.stderr)

# Check if an item of type and of value item
def check_for_item(mydb, dbname, type, item):
    try:
        mycursor = mydb.cursor(buffered=True)
        sql = "SELECT * FROM {} WHERE {} ='{}'".format(dbname, type, item)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()

        if len(myresult) != 0:
            return True
        return False
    except:
        print("Error, Could not check item", file=sys.stderr)

# Drops, then recreates a table
def reset_table(mydb, table):
    try:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("DROP TABLE IF EXISTS {}".format(table))
        create_table(mydb, table)
        print("SUCCESS, {} resetted".format(table), file=sys.stderr)
    except:
        print("Error, Could not reset table", file=sys.stderr)

# Specifically designed to insert a student
def insert_student(mydb, email):
    try:
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
    except:
        print("Error, Could not insert student", file=sys.stderr)

# Insert function specifically 
def insert_vote(mydb, u_id, category, person):
    try:
        mycursor = mydb.cursor(buffered=True)
        if(get_by_u_id(mydb, 'emails', u_id, 'voted') == 'False'): # Make sure person is registered
            sql = "INSERT INTO votes (category, person, u_id) VALUES (%s, %s, %s)"
            val = ("{}".format(category), "{}".format(person), "{}".format(u_id))
            mycursor.execute(sql, val)
            mydb.commit()
            return True
        else:
            return False
    except:
        print("Error, Could not insert vote", file=sys.stderr)

# Check if there are enough arguments, for menu
def check_args(actual, expected):
    if (actual == expected):
        return True
    else:
        print("ERROR, not enough parameters provided", file=sys.stderr)
        return False

# Setter for any database value, using u_id to query
def set_by_u_id(mydb, table, u_id, type, val):
    try:
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE {} SET {} = '{}' WHERE u_id = '{}'".format(table, type, val, u_id))
        mydb.commit()
    except:
        print("Error, Could not set item", file=sys.stderr)

# getter for any database value, using u_id to query
def get_by_u_id(mydb, table, u_id, type):
    try:
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
    except:
        print("Error, Could not get item", file=sys.stderr)

#Count the occurances of a category of value person
def count_all(mydb, table, category, person):
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM {} WHERE category='{}' AND person='{}'".format(table, category, person))
        result = mycursor.fetchall()
        return len(result)
    except:
        print("Error, Could not count items", file=sys.stderr)


def main():
    load_dotenv()
    if (len(sys.argv) == 1): #  Check for existence of a command
        print("ERROR, No command given", file=sys.stderr)
        exit()

    command = str(sys.argv[1]) #Grab command
    mydb = connect_database('ctrl_a') #Connect to database

    if (command == 'help'): #Displays list of available commands
        print("""
        Command format:
        py Database_commands.py [commands] [Arguments]

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
                print("No command found, use $py Database_commands.py help for assistance", file=sys.stderr)
        else:
            print("ERROR, password is incorrect", file=sys.stderr)


if __name__ == "__main__":
    main()