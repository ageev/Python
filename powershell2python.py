#!/usr/bin/env python3
# """  script runs powershell cmdlets via Python and grabs the result

import subprocess

args = ["powershell.exe", "-Command", r"-"]
cmdlet = "Get-ADUser -Filter{displayName -like 'Artem Ageev'} \r\n"

def main():
    print(run_cmdlet(cmdlet))

def run_cmdlet(cmdlet):
    process = subprocess.Popen(args, stdin = subprocess.PIPE, stdout =   subprocess.PIPE) 
    process.stdin.write(str.encode(cmdlet))
    result = process.communicate()[0].decode("utf-8").replace("\r\n", "\n")
    return result

if __name__ == '__main__':
    main()
