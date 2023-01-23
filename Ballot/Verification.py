import mysql.connector
import uuid
import sys
from dotenv import load_dotenv
import os

#import database commands from respective class
from Database_commands import *

def main():
    load_dotenv()
    u_id = str(sys.argv[1]) # Get u_id from input

    try:
        mydb = connect_database('ctrl_a') # Below: Make sure user registered and has not voted yet
        if (check_for_item(mydb, 'emails', 'u_id', u_id) and get_by_u_id(mydb, 'emails', u_id, 'voted') == "False"):
            print("True")
        else:
            print("False")
    except:
        print("ERROR")

if __name__ == "__main__":
    main()