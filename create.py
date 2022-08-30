#!/usr/bin/env python3
# Create bulk files
# TO-DO: add optional path feature

'''
Usage:
python3 create.py [options]
[options]: python3 create.py --help

./create.py --help
'''

import os
import random
import string
import argparse

# Possible Patterns
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
integers = string.digits
allCharacters = lowerLetters + upperLetters + integers

# Choose a pattern for filename
def determineCharset(option):
    if option == 'lower':
        return lowerLetters
    elif option == 'upper':
        return upperLetters
    elif option == 'number':
        return integers
    return allCharacters


# Generate a filename
def generateFilename():    
    for i in range(number):
        name = "".join(random.choices(charset,k=namesize))

        while os.path.isfile(name+ext):
            if args.verbose:
                print(f"[-] '{name+ext}' exists.")
            name = "".join(random.choices(charset,k=namesize))

        yield (name)

# Create the files
def create():
    for filename in fileList:
        aFile = filename.strip() + ext

        if args.garbage:
            f = open(aFile, "w")
            garbageData = "".join(random.choices(allCharacters, k=garbageLength))
            f.write(garbageData)
            f.close()
        else:
            open(aFile, "w").close()
        
        # Verbose info 
        if args.verbose:
            print(f"[+] '{aFile}' created")

# Command-line arguments
parser = argparse.ArgumentParser()
exclude = parser.add_mutually_exclusive_group()
parser.add_argument("-n", "--number", type=int,help="Number of files to create (Default: 10)")
parser.add_argument("-e", "--extension", type=str, help="Extension of file (Default: txt)")
parser.add_argument("-l", "--length", type=int, help="Length of the filename (Default: 11)")
exclude.add_argument("-w", "--wordlist", type=str, help="Get filename with extension from a file. (One name per line)")
exclude.add_argument("-p", "--pattern", type=str, help="Name pattern [Possible values: lower, upper, number, mix] (Defaut: mix)")
parser.add_argument("-v", "--verbose", help="Verbose", action="store_true")
parser.add_argument("-g", "--garbage", help="Write random garbage data", action="store_true")
parser.add_argument("-gl", "--garbagelength", type=int, help="No. of garbage characters to write (Default: 100)")
#parser.add_argument("-P", "--path", type=str, help="directory to create files")
args = parser.parse_args()

# Set the required parameters
number = abs(args.number or 10)
ext = "." + (args.extension or "txt")
charset = determineCharset(args.pattern)
namesize = abs(args.length or 11)
wordlist = args.wordlist

fileList = generateFilename()

# If wordlist is given, change fileList
if wordlist and os.path.isfile(wordlist):
    with open(wordlist) as f:
        fileList = f.readlines()[:number]
    ext = ''

if args.garbage:
    garbageLength = args.garbagelength or 100

# Start creating
if __name__ == '__main__':
    create()
