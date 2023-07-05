import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os
import json

#import database commands from respective class
sys.path.append('../')
from Database_commands import connect_database, database_exists, create_database, table_exists, create_table, check_for_item, reset_table, insert_student, insert_vote, check_args, set_by_u_id, get_by_u_id

def main():
    load_dotenv()
    try:
        data = str(sys.argv[1]) # get data from input
        data = data.replace('\\', '') # Process it so that it will be accepted as json data
        data = data.replace('[ ', '["')
        data = data.replace(' ]', '"]')
        data = data.replace(' }', '"}')
        data = data.replace('{ ', '{"')
        data = data.replace(' , ', '","')
        data = data.replace(', ', ', "')
        data = data.replace(' :', '" :')
        data = data.replace('u_id" : ', 'u_id" : "')
        res = json.loads(data) #load it as json data
    except:
        print("Error, Could not parse json data", file=sys.stderr)

    try:
        u_id = res["u_id"]
        mydb = connect_database('ctrl_a')
        create_table(mydb, 'votes')
        
        # Parse the inputted json data, and insert into database
        for group in list(res):
            if (group != "u_id"):
                for item in res[group]:
                    result = insert_vote(mydb, u_id, group, item)
                    if (result == False):
                        print("ERROR, already voted")
                        exit()
        set_by_u_id(mydb, 'emails', u_id, 'voted', 'True') # Set voted to true
        print("Vote Submitted Succesfully -> {}".format(data))
    except:
        print("Could not submit vote", file=sys.stderr)


if __name__ == "__main__":
    main()