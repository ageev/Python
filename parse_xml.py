#!/usr/bin/env python
# """Parse XML"""


# Imports
import os
import sys
import xml.etree.ElementTree as ET


# Module Constants
START_MESSAGE = "XML parsing string"


# Module "Global" Variables
location = os.path.abspath(__file__)
keynames_interested = ['Name', 'Key']
xmlfile = 'KeysExport.xml'
outputfile = 'Keys.csv'


# Module Functions and Classes
def main(*args):
    """My main script function.
    Displays the full patch to this script, and a list of the arguments passed
    to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)

    root = ET.parse(xmlfile).getroot()
    keys = []
    out = ""

    for child in root[1]:
        out += child.attrib['Name'] + ";" + child[0].text + "\n"

    with open(outputfile, 'w') as f:
        f.write(out)

# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)