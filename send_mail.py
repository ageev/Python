#!/usr/bin/env python
# """this script will send HTML formatted mail"""


# Imports
import os
import sys
import smtplib
import logging

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Module Constants
START_MESSAGE = "CLI Inspection Script"
SENDER = 'example@live.com'
SUBJECT = 'Notification: 1 New Messages'
LOG_PATH = 'c:/Temp/phish.log'
SMTP_SERVER = '127.0.0.1'

# Module "Global" Variables
location = os.path.abspath(__file__)

address_file = "addresses.csv" #just a list with emails
html_template_file = "O365quarantine.htm"

# Module Functions and Classes

#logger
logging.basicConfig(
    filename = LOG_PATH,
    format='%(asctime)s %(levelname)-5s %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.DEBUG
    )
logger = logging.getLogger(__name__)

def get_msg(address):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = address

    text = "email Text" # Non HTML email text
    f = open(html_template_file, "r")
    html = f.read()[2:]  # strat from 3rd byte to remove byte order mark
    f.close()
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    return msg.as_string()

def main(*args):
    """My main script function.
    Displays the full patch to this script, and a list of the arguments passed
    to the script.
    """

    print(START_MESSAGE)
    print("Script Location:", location)
    print("Arguments Passed:", args)

    #step 1 read addresses
    with open(address_file) as f:
        addresses = f.read().splitlines()

    #2 prepare the messages https://stackoverflow.com/questions/882712/sending-html-email-using-python
    for i in addresses:
        msg = get_msg(i)

    #3 send it
        smtpObj = smtplib.SMTP(SMTP_SERVER)
        try:
            smtpObj.sendmail(SENDER, i, msg) 
            logger.info("Successfully sent email to " + i)
        except Exception as e:
            print("Error: unable to send email to " + i + " Error: " + str(e))
        smtpObj.quit() 


# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)