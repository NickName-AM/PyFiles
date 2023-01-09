#!/usr/bin/env python3

# Create bulk files

"""
Usage:
python3 create.py [options]
[options]: python3 create.py --help

./create.py --help
"""

import os
import random
import string
import argparse

extensionList = (".aif", ".cda", "mp3",".wav",".7z",".rar",".rpm",".tar.gz",".zip",".iso",".csv",".sql",".xml",".log",".db",".cgi",".bat",".bin",".py",".c",".go",".jar",".exe",".ttf",".otf",".bmp",".jpeg",".jpg",".png",".ps",".svg",".gif",".ico",".php",".js",".css",".html",".pptx",".cpp",".h",".sh",".xlsx",".bak",".cfg",".dll",".mp4",".mkv",".mpeg",".docx",".txt",".pdf")

# Possible Patterns
lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
integers = string.digits
allCharacters = lowerLetters + upperLetters + integers

# Choose a pattern for filename
def determineCharset(option):
    if option == "lower":
        return lowerLetters
    elif option == "upper":
        return upperLetters
    elif option == "number":
        return integers
    return allCharacters


# Generate a filename
def generateFilename():
    global ext    
    for i in range(number):
        name = "".join(random.choices(charset,k=namesize))
        if args.randomextension:
            ext = random.choice(extensionList)
        while os.path.isfile(name+ext):
            
            print(f"[-] '{name+ext}' exists.")
            name = "".join(random.choices(charset,k=namesize))

        yield (name)

# Create the files
def create():
    for filename in fileList:
        aFile = prefix + filename.strip() + suffix + ext
        fileWithPath = os.path.join(dPATH, aFile)

        f = open(fileWithPath, "w")
        if args.garbage:
            garbageData = customgarbage or "".join(random.choices(allCharacters, k=garbageLength))
            f.write(garbageData)
        f.close()
        
        # Verbose info 
        if args.verbose:
            print(f"[+] '{aFile}' created")

# Command-line arguments
parser = argparse.ArgumentParser()
exclude = parser.add_mutually_exclusive_group()
parser.add_argument("-n", "--number", type=int,help="Number of files to create (Default: 10)")
parser.add_argument("-e", "--extension", type=str, help="Extension of file (Default: txt)")
parser.add_argument("-r", "--randomextension", help="Use random extensions (Default: Off)", action="store_true")
parser.add_argument("-l", "--length", type=int, help="Length of the filename (Default: 11)")
exclude.add_argument("-w", "--wordlist", type=str, help="Get filename with EXTENSION from a file. (One name per line)[Doesn't work with --pattern]")
exclude.add_argument("-p", "--pattern", type=str, help="Name pattern [Possible values: lower, upper, number, mix] (Defaut: mix)")
parser.add_argument("--prefix", type=str, help="Prefix for the filename")
parser.add_argument("--suffix", type=str, help="Suffix for the filename")
parser.add_argument("-v", "--verbose", help="Verbose (Default: Off)", action="store_true")
parser.add_argument("-g", "--garbage", help="Write random garbage data (Default: Off)", action="store_true")
parser.add_argument("--garbagelength", type=int, help="No. of garbage characters to write (Default: 100)")
parser.add_argument("--customgarbage", type=str, help="Write your own data in the created files.(Use with '-g')")
parser.add_argument("-P", "--path", type=str, help="directory to create files. (Default: '.' current directory)")
args = parser.parse_args()


# Set the required parameters
# Number of files to create
number = 10
if args.number:
    if args.number > 0:
        number = args.number
    else:
        print("Number should be greater than 0.")
        exit(-1)


# Extension of the files
if args.extension:
    ext = f".{args.extension}"
else:
    ext = ".txt"


# Charset to use
charset = determineCharset(args.pattern)


# length of filename (without ext)
namesize = 11
if args.length:
    if args.length > 0:
        namesize = args.length
    else:
        print("Length of file name should be greater than 0.")
        exit(-1)


# wordlist with filenames
wordlist = args.wordlist


# User-provided data to write
customgarbage = args.customgarbage


# Directory to create files in
if args.path:
    # If the directory exists choose that path, else choose the current working directory
    dPATH = os.path.isdir(args.path) and args.path   
else:
    dPATH = os.getcwd()


# If wordlist is given, use that wordlist instead of default generator
if wordlist and os.path.isfile(wordlist):
    with open(wordlist) as f:
        fileList = f.readlines()[:number]
    ext = ""
else:
    fileList = generateFilename()

# length of garbage data to write
garbageLength = 100
if args.garbage and args.garbagelength:
    if args.garbagelength > 0:
        garbageLength = args.garbagelength
    else:
        print("Length of data to write should be greater than 0. (--garbagelength)")
        exit(-1)

# Prefix and Suffix
prefix = args.prefix or ""
suffix = args.suffix or ""

if args.verbose:
    print(f"Number of files to create: {number}")
    print(f"Extension: {ext}")
    print(f"Length of filename: {namesize}")
    print(f"Charset: {charset}")
    print(f"Wordlist: {wordlist}")
    print(f"Path to create files in : {dPATH}")

# Start creating
if __name__ == "__main__":
    create()
 