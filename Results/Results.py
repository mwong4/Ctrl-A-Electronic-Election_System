import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import getpass
import json

#import database commands from respective class
sys.path.append('../../Ctrl_A_EES')
from Database_commands import connect_database, count_all

def main():
    load_dotenv()

    try:
        # Source file for ballot generation
        SOURCE_FILE=str(os.getenv('SOURCE_FILE'))

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
    except:
        print("Error, failed to count results")


if __name__ == "__main__":
    main()