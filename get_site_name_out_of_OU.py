#!/usr/bin/env python
# """will get site name out of distinguished name"""

# Imports
import os
import sys


# Module Constants
START_MESSAGE = "OU processing script"
finput = "DName.csv"  # before: CN=Drozario\, Chiara,OU=Third Party,OU=Users,OU=AU-DC-Melbourne,OU=SITES,DC=domain,DC=local
foutput = "DName.rzlt" # after: AU-DC-Melbourne


# Module "Global" Variables
location = os.path.abspath(__file__)


# Module Functions and Classes
def main(*args):
    """My main script function.
    Displays the full patch to this script, and a list of the arguments passed
    to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)

    items = list((list(line.rstrip('\n').split(',') for line in open(finput))))

    f = open(foutput,"w")
    for i in items:
    	f.write(i[-4][3:] + "\n")
    f.close()


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)