#!/bin/bash

# Make sure that NOBODY can access the server without a password
mysql -e UPDATE mysql.user SET Password = '1234' WHERE User = 'root'
# Kill the anonymous users
mysql -e DROP DATABASE test
# Make our changes take effect
mysql -e FLUSH PRIVILEGES
# Any subsequent tries to run queries this way will get access denied because lack of usr/pwd param