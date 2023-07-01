#!/bin/bash

# credentials
db_passwd=<db_passwd>
cli_passwd=<cli_passwd>
email=donotreply.ctrla@gmail.com
email_passwd=<email_passwd>



# Make sure that NOBODY can access the server without a password
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$db_passwd';"
# Kill the anonymous users
mysql --user=root --password=$db_passwd -e "DROP DATABASE test"
# Make our changes take effect
mysql --user=root --password=$db_passwd -e "FLUSH PRIVILEGES"
# Any subsequent tries to run queries this way will get access denied because lack of usr/pwd param
# Create ctrl-a database
mysql --user=root --password=$db_passwd -e  "CREATE DATABASE ctrl_a"

# Set up env file
cat << EOF > /var/www/html/Ctrl-A-Electronic-Election_System/.env 
APP_PASSWORD=$email_passwd
CLI_PASSWORD=$db_passwd
DB_PASSWORD=$db_passwd
SOURCE_FILE=../Ballot/Generating_Templates/input.json
SENDER_EMAIL=$email
HOST=localhost
USER=root
PORT=3306
EOF