#!/usr/bin/env python
# """Check if IP belongs to range."""

# Imports
import os
import sys
import ipaddress
import csv


# Module Constants
START_MESSAGE = "IP-site mapper"


# Module "Global" Variables
location = os.path.abspath(__file__)
ip_ranges_file = "c:\\\\ip_ranges.csv"
scan_file = "c:\\\\Full.csv"
result_file = "c:\\\\Full_with_sites.csv"


# Module Functions and Classes
def getCountry(ip, ip_ranges):
    country = "not found"
    for site in ip_ranges:
        if (ipaddress.IPv4Address(ip) in ipaddress.IPv4Network(site[0])):
            country = site[1]
    return country

def main(*args):
    """My main script function.
    Displays the full patch to this script, and a list of the arguments passed
    to the script.
    """
    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)


    # step 1
    # read subnet country mapping file
    with open(ip_ranges_file) as csvfile:
        ip_ranges = [row for row in csv.reader(csvfile, delimiter=';')]

    # step 2 
    # read the scan file
    with open(scan_file) as csvfile:
        scanned_ips = [row for row in csv.reader(csvfile, delimiter=',')]

    # step 3
    # iterate through the scan file and update the country field
    for ip in scanned_ips:
        ip.append(getCountry(ip[1], ip_ranges))

    # step 4
    # write the new file
    with open(result_file, "w", newline="") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(["Risk", "Host", "Name", "Country"])  # write header
        writer.writerows(scanned_ips)


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)