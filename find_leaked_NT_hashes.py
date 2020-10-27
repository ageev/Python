#!/usr/bin/env python3
# """Will search cross matches between 1 hash file and HAVEIBEENPWND hash DB file, splitted to multiple files"""


# Imports
import os
import sys
import mmap


# Module Constants
START_MESSAGE = "CLI Inspection Script"

HASHFILE_DB = ["PWND.001", "PWND.002", "PWND.003", "PWND.004", "PWND.005", "PWND.006", "PWND.007", "PWND.008", "PWND.009"]
HASHFILE_TO_CHECK = "HASHES.lst"
OUTPUT_FILE = "hashes_found_in_db.lst"


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

    with open(HASHFILE_TO_CHECK, 'r') as f:
        hashes = f.read().splitlines()

    for hash_file in HASHFILE_DB:
        print("[INFO] checking the hash_db file: ", hash_file)
        with open(hash_file, 'r') as f:
            hash_db = f.read().splitlines()

        result = []

        result = set(hashes).intersection(hash_db)

        with open(OUTPUT_FILE, 'a') as f:
            for item in result:
                f.write("%s\n" % item)
        print("[INFO] hashes found: ", len(result))


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)