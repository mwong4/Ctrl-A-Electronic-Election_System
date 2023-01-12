import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import getpass
import json

# Source file for ballot generation
SOURCE_FILE='../Ballot/Generating_Templates/input.json'

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

#Count the occurances of a category of value person
def count_all(mydb, table, category, person):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {} WHERE category='{}' AND person='{}'".format(table, category, person))
    result = mycursor.fetchall()
    return len(result)

def main():
    mydb = connect_database('ctrl_a') # Connet to database
    source_file = open(SOURCE_FILE)
    data = json.load(source_file) # Load json

    output_dict = {}

    # parse json data, finding corresponding SQL data and embeding into a dictionary
    for category in data:
        internal_dict = {}
        for person in data[category]:
            count = count_all(mydb, 'votes', category, person)
            internal_dict[person] = int(count)
        output_dict[category] = internal_dict
    
    print(output_dict)
    source_file.close()


if __name__ == "__main__":
    main()