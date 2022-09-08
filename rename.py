# TO-DO: Decreased a bit

# Rename bulk files

'''
Usage: python3 rename.py
'''

import os
import argparse
import string
import sys
import random

# Possible Patterns
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
integers = string.digits
allCharacters = lowerLetters + upperLetters + integers
c = 0

# Choose a pattern for filename
def determineCharset(option):
    if option == 'lower':
        return lowerLetters
    elif option == 'upper':
        return upperLetters
    elif option == 'mix':
        return allCharacters
    return 'number'


def generateFilename(ext):
    global c
    if charset == 'number':
        file = f"{c}.{ext}"
        c+=1
    else:
        r = 0
        name = ''.join(random.choices(charset,k=namesize))
        file = f'{name}.{ext}'
        while os.path.isfile(os.path.join(dPATH, file)):
            print(f'[-] \'{name}.{ext}\' exists.')
            name = ''.join(random.choices(charset,k=namesize))
            r+=1
            if r > 10:
                print('Too many repeats. Exiting.')
                exit(-1)
        
    fullPathFile = os.path.join(dPATH, file)

    return fullPathFile



def rename(dPATH, dirList):
    for file in dirList:
        oldPathFile = os.path.join(dPATH, file)
        ext = file.split('.')[-1]
        
        newPathFile = generateFilename(ext)
        
        os.rename(oldPathFile, newPathFile)



parser = argparse.ArgumentParser()
parser.add_argument('-P', '--path', type=str, help='Path to directory with files to rename.')
parser.add_argument('-p', '--pattern', type=str, help='Name pattern [Possible values: lower, upper, number, mix] (Defaut: number)')
parser.add_argument('-l', '--length', type=int, help='Length of name of the files. (Default: 11)')
args = parser.parse_args()


charset = determineCharset(args.pattern)
namesize = abs(args.length or 11)
dPATH = '.'

if args.path:
    dPATH = (os.path.isdir(args.path) and args.path) or '.'

# Get The files in the directory
dirList = os.listdir(dPATH)

# Remove the name of this file from the list
if sys.argv[0] in dirList:
    dirList.remove(sys.argv[0])



if __name__ == '__main__':
    rename(dPATH, dirList)
