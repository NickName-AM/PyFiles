#!/usr/bin/env python3

# Rename bulk files

'''
Usage: python3 rename.py --help
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
        file = f"{prefix}{c}{suffix}{ext}"
        c+=1
    else:
        r = 0
        name = prefix + ''.join(random.choices(charset,k=namesize)) + suffix
        file = f'{name}{ext}'
        while os.path.isfile(os.path.join(dPATH, file)):
            print(f'[-] \'{name}{ext}\' exists.')
            name = ''.join(random.choices(charset,k=namesize))
            r+=1
            if r > 10:
                print('Too many repeats. Exiting.')
                exit(-1)

    return file



def rename(dPATH):
    global ext
    for root, dirs, files in os.walk(dPATH):
        for file in files:
            if (file == FILENAME):
                continue
            
            new_filename = generateFilename(ext)
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_filename)
            os.rename(old_file_path, new_file_path)
            if args.verbose:
                print(f'{file} renamed to {new_filename}')
        
        if not args.recursive:
            break



parser = argparse.ArgumentParser()
parser.add_argument('-P', '--path', type=str, help='Path to directory with files to rename.')
parser.add_argument('-p', '--pattern', type=str, help='Name pattern for new files [Possible values: lower, upper, number, mix] (Defaut: number)')
parser.add_argument('-e', '--extension', type=str, help='Extension to give to new files.')
parser.add_argument('-l', '--length', type=int, help='Length of name of the files. (Default: 11)')
parser.add_argument("--prefix", type=str, help="Prefix for the new filename")
parser.add_argument("--suffix", type=str, help="Suffix for the new filename")
parser.add_argument('-v', '--verbose', help='Verbose (Default: off)', action='store_true')
parser.add_argument('-r', '--recursive', help='Recursive (Default: off)', action='store_true')
args = parser.parse_args()

FILENAME = sys.argv[0]
ext = ''
if args.extension:
    ext = '.' + args.extension

charset = determineCharset(args.pattern)
namesize = abs(args.length or 11)
dPATH = '.'


if args.path:
    dPATH = (os.path.isdir(args.path) and args.path) or '.'

if args.verbose:
    print(f'Extension: {bool(ext)}')
    print(f'Pattern: {charset}')
    print(f'Path: {dPATH}')
    print(f'Length: {namesize}')

prefix = args.prefix or ''
suffix = args.suffix or ''


if __name__ == '__main__':
    rename(dPATH)
