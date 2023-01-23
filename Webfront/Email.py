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

#import database commands from respective class
sys.path.append('../../Ctrl_A_EES')
from Database_commands import connect_database, database_exists, create_database, table_exists, create_table, check_for_item, reset_table, insert_student 


SUCCESS_RESPONSE = "Ballot has been succesfully sent. Please vote with link sent to: "
ERROR_NOT_WATERLOO = "ERROR, the following is not a Waterloo email: "
ERROR_DND = "ERROR, system was unable to send to the following email: "
ERROR_ALREADY_EXISTS = "ERROR, the following email has already been used: "

EMAIL_FILTER = "@uwaterloo.ca"
DEBUG = False

def main():
    load_dotenv()
    email = str(sys.argv[1]) # Gets email fro input

    port = 465  # For SSL
    password = os.getenv('APP_PASSWORD')
    sender = os.getenv('SENDER_EMAIL')

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to databse
        mydb = connect_database('')
        create_database(mydb, 'ctrl_a')
        mydb = connect_database('ctrl_a')
        create_table(mydb, 'emails')
    except:
        print("Error, Could not connect to database/table", file=sys.stderr)

    # Check that email is a waterloo one
    if (email != None and EMAIL_FILTER in email and email.endswith(EMAIL_FILTER)) or DEBUG:
        # Check if account has been registered in database yet
        if (check_for_item(mydb, 'emails', 'email', email)):
            response = ERROR_ALREADY_EXISTS
        else:
            id_code = insert_student(mydb, email)
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server: # Login and prepare to send email
                server.login(sender, password)
                try:
                    message = MIMEMultipart("alternative") # Message template
                    message["Subject"] = "Ctrl-A Election Ballot"
                    message["From"] = sender
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

                    server.sendmail(sender, email, message.as_string()) # Send Email
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