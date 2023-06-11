import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import getpass
import argparse
import textwrap

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
    else:
        print("Success, connected to database", file=sys.stderr)

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
    else:
        print("Success, database created", file=sys.stderr)

# List all databases
def list_databases():
    mydb = connect_database("")
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW DATABASES")
    try:
        print("====================\nDatabases:", file=sys.stderr)
        for item in mycursor:
            print(str(item), file=sys.stderr)
        print("====================", file=sys.stderr)
        
    except:
        print("Could not print databses", file=sys.stderr)

# List all tables in a database
def list_tables(mydb):
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SHOW TABLES")
    try:
        print("====================\nTables:", file=sys.stderr)
        for item in mycursor:
            print(str(item), file=sys.stderr)
        print("====================", file=sys.stderr)
        
    except:
        print("Could not print databses", file=sys.stderr)

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
    print(type(name))
    try:
        mycursor = mydb.cursor(buffered=True)
        if (not table_exists(mydb, name)):
            if (name ==  'emails'):
                mycursor.execute("CREATE TABLE emails (email VARCHAR(255), u_id VARCHAR(255), voted VARCHAR(255))")
            elif (name  == 'votes'):
                mycursor.execute("CREATE TABLE votes (category VARCHAR(255), person VARCHAR(255), u_id VARCHAR(255))")
            else:
                print("Error, table name must be 'emails' or 'votes'", file=sys.stderr)
                raise Exception("Error, table name must be 'emails' or 'votes'")
    except:
        print("Error, Could not create table", file=sys.stderr)
    else:
        print("Success, table created", file=sys.stderr)

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
    else:
        print("Success, table reset", file=sys.stderr)

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
    else:
        print("Success, student added", file=sys.stderr)

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
    else:
        print("Success, vote added", file=sys.stderr)

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
    else:
        print("Success, uuid set", file=sys.stderr)

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
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''\
        NOTE: Leave arguments to end

        Commands:
        $ -C list_databases
        $ -C create_database -A [db_id]
        $ -C list_tables -A [db_id]
        $ -C create_table -A [db_id] [table_name]
        $ -C reset_table -A [db_id] [table_name]
        $ -C insert_email -A [db_id] [email (single string)]
        $ -C set -A [db_id] [table_name] [u_id] [type] [val]
        $ -C get -A [db_id] [table_name] [u_id] [type]
        $ -C count -A [db_id] [table_name] [filter] [val]
        '''))
    parser.add_argument("-C", "--command", help="Command", type=str)
    parser.add_argument("-P", "--password", help="CLI Password", type=str)
    parser.add_argument("-A", "--arguments", help="Arguments for Command", nargs='+', default=[])
    args = parser.parse_args()

    if (args.command == None): #  Check for existence of a command
        print("ERROR, No command given. Try 'python Databse_command.py -h'.", file=sys.stderr)
        exit()

    mydb = connect_database('ctrl_a') #Connect to database

    if (args.password == None):
        passwd = getpass.getpass("Enter CLI Password: ") #Prompt for password
    else:
        passwd = args.password
    real_pass =  os.getenv('CLI_PASSWORD')

    if(passwd == real_pass): #executes the command based off command entered and parameters
        if (args.command == 'list_databases'):
            list_databases()
        elif (args.command == 'list_tables'):
            if not check_args(len(args.arguments), 1): 
                exit()
            mydb = connect_database(args.arguments[0])
            list_tables(mydb)              
        elif (args.command == 'create_database'):
            if not check_args(len(args.arguments), 1): 
                exit()
            create_database(mydb, args.arguments[0])
        elif (args.command == 'create_table'):
            if not check_args(len(args.arguments), 2): 
                exit()
            mydb = connect_database(args.arguments[0])
            create_table(mydb, args.arguments[1])
        elif (args.command == 'reset_table'):
            if not check_args(len(args.arguments), 2): 
                exit()
            mydb = connect_database(args.arguments[0])
            reset_table(mydb, args.arguments[1])
        elif (args.command == 'insert_email'):
            if not check_args(len(args.arguments), 2): 
                exit()
            mydb = connect_database(args.arguments[0])
            id = insert_student(mydb, args.arguments[1])
        elif (args.command == 'set'):
            if not check_args(len(args.arguments), 5): 
                exit()
            mydb = connect_database(args.arguments[0])
            set_by_u_id(mydb, args.arguments[1], args.arguments[2], args.arguments[3], args.arguments[4])
        elif (args.command == 'get'):
            if not check_args(len(args.arguments), 4): 
                exit()
            mydb = connect_database(args.arguments[0])
            print(get_by_u_id(mydb, args.arguments[1], args.arguments[2], args.arguments[3]))
        elif (args.command == 'count'):
            if not check_args(len(args.arguments), 4): 
                exit()
            mydb = connect_database(args.arguments[0])
            print(count_all(mydb, args.arguments[1], args.arguments[2], args.arguments[3]))
        else:
            print("No command found, use $py Database_commands.py -h for assistance", file=sys.stderr)
    else:
        print("ERROR, password is incorrect", file=sys.stderr)


if __name__ == "__main__":
    main()