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
    n = random.choice(range(9,12))
    name = "".join(random.choices(charset,k=n))

    while os.path.isfile(os.path.join(os.getcwd(), name+'.'+ext)):
        name = "".join(random.choices(charset,k=n))

    return (name+'.'+ext)

# Create the files
def create():
    for i in range(number):
        filename = generateFilename()
        open(filename, 'w').close()

# Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int,help="Number of files to create (Default: 10)")
parser.add_argument("-e", "--extension", type=str, help="Extension of file (Default: txt)")
parser.add_argument("-p", "--pattern", type=str, help="Name pattern [Possible values: lower, upper, number, mix] (Defaut: mix)")
args = parser.parse_args()

# Set the required parameters
number = args.number or 10
ext = args.extension or 'txt'
charset = determineCharset(args.pattern)

# Start creating
if __name__ == '__main__':
    create()