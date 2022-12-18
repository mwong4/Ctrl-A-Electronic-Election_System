import sys

SUCCESS_RESPONSE = "Ballot has been succesfully sent. Please vote with link sent to: "
ERROR_NOT_WATERLOO = "ERROR, the following is not a Waterloo email: "
ERROR_DNE = "ERROR, system was unable to send to the following email: "
ERROR_ALREADY_EXISTS = "ERROR, the following email has already been used: "

EMAIL_FILTER = "@uwaterloo.ca"

def main():
    email = str(sys.argv[1])

    if email != None and EMAIL_FILTER in email:
        response = SUCCESS_RESPONSE
    else:
        response = ERROR_NOT_WATERLOO

    print(response + email)
    


if __name__ == "__main__":
    main()