# Ctrl-A-EES
Electronic Election System for Ctrl-A
status: Prototype, in development

### General Information

This is an electornic election system built for the Ctrl-A club at the University of Waterloo.

**NOTE**: For local testing, you can refer to the README in the Vagrant-Deployment folder.

## Settup

Before usage, a few configurations must be completed. First, ensure that Python is installed.
```bash
$ python -V
> Python 3.10.5
```

next, ensure that all pip requirements have been met

```bash
$ cd /directory/where/files/are/located
$ pip install -r requirements.txt
```

included in the home directory is "index.html". This redirects to Initial.php

Move this file to the landing directory:

```bash
cd /<path>/Ctrl-A-Electronic-Election_System
mv ./index.html ./../index.html
```

[with the current prototype version, the system is only functional on localhost]
Use xampp or the Vagrant-Deployment in order to test.

### json configuration

Before ballots can be distributed, they must be generated from a config file, written in json. Below is an example:

```json
{
    "president": {
        "Joel": {
            "description": "Hi, my name is Joel. I code."
        },
        "Sasha": {
            "description": "Hello, my name is Sasha. I like art."
        }
    },
    "treasurer": {
        "K": {
            "description": "Hey, I'm K. I really like anime... and maybe money."
        }
    },
    "promotion manager": {

    }
}
```

In the example, we have the position of "president" with two individuals running for the position. "Treasurer" has 1 person running and "Promotional Manager" has none.
Each individual also has a custom description. Please write this file, and ensure that it is in ./Ballot/Generating_Templates.

Once ready, run the Python script to generate the ballot:
```bash
$ cd ./Ballot/Generating_Templates
$ py Generate.py <input_file.json>
> Generating...
> Ballot generated!
```

With this command, a Ballot.php will appear in this directory. Open this file in a browser to confirm the layout is correct, then move the file to ./Ballot

Now, the ballot is ready!

### Script configurations

In this current location (project folder, where README is located), create a .env file and fill in the following fields:
```bash
.env

APP_PASSWORD=<do not reply email password>
CLI_PASSWORD=<set a password for the database commands>
DB_PASSWORD=<fill in the database password>
SOURCE_FILE=<../Ballot/Generating_Templates/input.json>
SENDER_EMAIL=<email being used to send ballots>
HOST=<database ip>
USER=<database user, default is root>
PORT=<database port>
```
A reminder that the source_file is the same json file used in the ballot generation

## Usage

There are 3 main components to the system: The initial page, the ballot, and the results page.

The initial page is where the end user, the voter, goes to submit their Waterloo email to confirm their identity
The ballot page is then sent to each user via email. This ballot double-checks the user's identity and allows them to vote
The results page is where the user can go to check the present results of the election.

[**Administration Terminal**]
On the website, go to ../Ctrl-A-Electronic-Election_System/terminal.php to make direct commands to the database.
```bash
Commands:
$ -C list_databases
$ -C create_database -A [db_id]
$ -C list_tables -A [db_id]
$ -C create_table -A [db_id] [table_name]
$ -C reset_table -A [db_id] [table_name]
$ -C insert_email -A [db_id] [email (single string)]
$ -C list_data -A [db_id] [table_name]
$ -C set -A [db_id] [table_name] [u_id] [type] [val]
$ -C get -A [db_id] [table_name] [u_id] [type]
$ -C count -A [db_id] [table_name] [filter] [val]
```