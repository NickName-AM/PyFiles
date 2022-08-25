# TO-DO: Add optional length of filename

# Create bulk files

'''
Usage: python3 create.py [options]
[options]: python3 create.py --help
'''

import os
import random
import argparse
import sys

# Possible Patterns
lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = lowerLetters.upper()
integers = "0123456788"
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
            name = "".join(random.choices(charset,k=namesize))

        yield (name)

# Create the files
def create():
    for filename in fileList:
        open(filename.strip()+ ext, 'w').close()

# Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int,help="Number of files to create (Default: 10)")
parser.add_argument("-e", "--extension", type=str, help="Extension of file (Default: txt)")
parser.add_argument("-p", "--pattern", type=str, help="Name pattern [Possible values: lower, upper, number, mix] (Defaut: mix)")
parser.add_argument("-l", "--length", type=int, help="Length of the filename (Default: 11)")
parser.add_argument("-w", "--wordlist", type=str, help="Get filename with extension from a file. (One name per line)")
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


# Start creating
if __name__ == '__main__':
    create()
