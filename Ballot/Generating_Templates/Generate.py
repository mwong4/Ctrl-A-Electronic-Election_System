import jinja2
from jinja2 import Template
import json
import sys
import os

def main():
    source_location = sys.argv[1]
    source_file = open(str(source_location))
    data = json.load(source_file)
    
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "Ballot_Template.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(data=data)

    try:
        print("Clearig old ballots")
        os.remove("Ballot.php")
    except:
        print("Generating...")
    out_file = open("Ballot.php", "a")
    out_file.write(outputText)
    out_file.close()
    source_file.close()
    print("Ballot generated!")


if __name__ == "__main__":
    main()

