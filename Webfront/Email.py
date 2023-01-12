import os
import sys
import smtplib, ssl
from smtplib import SMTPException
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
from mysql.connector import Error
import pandas as pd
import mysql.connector
import uuid

SUCCESS_RESPONSE = "Ballot has been succesfully sent. Please vote with link sent to: "
ERROR_NOT_WATERLOO = "ERROR, the following is not a Waterloo email: "
ERROR_DND = "ERROR, system was unable to send to the following email: "
ERROR_ALREADY_EXISTS = "ERROR, the following email has already been used: "

EMAIL_FILTER = "@uwaterloo.ca"
SENDER = "donotreply.ctrla@gmail.com"
DEBUG = False

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


def main():
    load_dotenv()
    email = str(sys.argv[1]) # Gets email fro input

    port = 465  # For SSL
    password = os.getenv('APP_PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to databse
    mydb = connect_database('')
    create_database(mydb, 'ctrl_a')
    mydb = connect_database('ctrl_a')
    create_table(mydb, 'emails')

    # Check that email is a waterloo one
    if (email != None and EMAIL_FILTER in email and email.endswith(EMAIL_FILTER)) or DEBUG:
        # Check if account has been registered in database yet
        if (check_for_item(mydb, 'emails', 'email', email)):
            response = ERROR_ALREADY_EXISTS
        else:
            id_code = insert_student(mydb, email)
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: # Login and prepare to send email
                server.login(SENDER, password)
                try:
                    message = MIMEMultipart("alternative") # Message template
                    message["Subject"] = "Ctrl-A Election Ballot"
                    message["From"] = SENDER
                    message["To"] = email
                    html = """\
                    <html>
                        <body>
                            <p>Subject: Ctrl-A Election Ballot<br>
                            This is your custom url to the election site:<br>
                            <a href="http://localhost/Ballot/Ballot_Verification.php?u_id={}">http://localhost/Ballot/Ballot_Verification.php?u_id={}</a> 
                            </p>
                        </body>
                    </html>
                    """.format(id_code, id_code) #Important! The above has the email with the u_id embedded in the URL
                    package = MIMEText(html, "html")
                    message.attach(package)

                    server.sendmail(SENDER, email, message.as_string()) # Send Email
                    response = SUCCESS_RESPONSE
                except SMTPException as e:
                    error_code = e.smtp_code # Display error codes, if failed
                    error_message = e.smtp_error
                    if DEBUG:
                        response = "<" + error_code + "> " + error_message + " || " + ERROR_DND
                    else:
                        response = ERROR_DND
    else:
        response = ERROR_NOT_WATERLOO

    print(response + email)
    

if __name__ == "__main__":
    main()