import os
import sys
import smtplib, ssl
from smtplib import SMTPException
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SUCCESS_RESPONSE = "Ballot has been succesfully sent. Please vote with link sent to: "
ERROR_NOT_WATERLOO = "ERROR, the following is not a Waterloo email: "
ERROR_DND = "ERROR, system was unable to send to the following email: "
ERROR_ALREADY_EXISTS = "ERROR, the following email has already been used: "

EMAIL_FILTER = "@uwaterloo.ca"
SENDER = "donotreply.ctrla@gmail.com"
DEBUG = True

def main():
    email = str(sys.argv[1])

    load_dotenv()
    port = 465  # For SSL
    password = os.getenv('APP_PASSWORD')

    # Create a secure SSL context
    context = ssl.create_default_context()

    message = MIMEMultipart("alternative")
    message["Subject"] = "Ctrl-A Election Ballot"
    message["From"] = SENDER
    message["To"] = email
    html = """\
    <html>
        <body>
            <p>Subject: Ctrl-A Election Ballot<br>
            This is your custom url to the election site:<br>
            <a href="https://www.google.com/">https://www.google.com/</a> 
            </p>
        </body>
    </html>
    """
    package = MIMEText(html, "html")
    message.attach(package)


    if (email != None and EMAIL_FILTER in email) or DEBUG:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(SENDER, password)
            try:
                server.sendmail(SENDER, email, message.as_string())
                response = SUCCESS_RESPONSE
            except SMTPException as e:
                error_code = e.smtp_code
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