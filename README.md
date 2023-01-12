# Ctrl-A-EES
Electronic Election System for Ctrl-A
status: Prototype, in development

###### General Information

This is a electornic election system built for the Ctrl-A club at the University of Waterloo.

## Settup

Prior to usage, a few configurations must be completed. First, ensure that python is installed.
```
$ python -V
> Python 3.10.5
```

next, ensure that all pip requirements have been met

```
$ cd /directory/where/files/are/located
$ pip install -r requirements.txt
```

[with current prototype version, system is only functional on localhost]
Use xampp to host the dynamic website and database

###### json configuration

Before ballots can be distributed, they must be generated from a config file, written in json. Below is an example:

```
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

In the example, we have a position of "president" with two individuals running for the position. "Treasurer" has 1 person running and "Promotional Manager" has none.
Each individual also has a custom description. Please write this file, and ensure that it is in ./Ballot/Generating_Templates.

Once ready, run the python script to generate the ballot:
```
$ cd ./Ballot/Generating_Templates
$ py Generate.py <input_file.json>
> Generating...
> Ballot generated!
```

With this command, a Ballot.php will apear in this directory. Open this file in a browser to confirm the layout is correct, then move the file to ./Ballot

Now, the ballot is ready!

###### Script configurations

In this current location (project folder, where README is located), create a .env file and fill in the following fields:
```
.env

APP_PASSWORD=<do not reply email password>
CLI_PASSWORD=<set a password for the database commands>
DB_PASSWORD=<fill in the database password configured on xampp, default is empty>
SOURCE_FILE=<../Ballot/Generating_Templates/input.json>
```
Reminder that the source_file is the same json file used in the ballot generation

## Usgae
