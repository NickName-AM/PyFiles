# TO-DO: A lot

# Rename bulk files

'''
Usage: python3 rename.py
'''

import os
import argparse
import sys


def rename():
    c=0
    for file in dirList:
        oldFilePath = os.path.join(dPATH, file)

        ext = file.split('.')[-1]
        newFilePath = os.path.join(dPATH, f'{c}.{ext}')
        os.rename(oldFilePath, newFilePath)
        c+=1


parser = argparse.ArgumentParser()
parser.add_argument('-P', '--path', type=str, help='Path to directory with files to rename.')
args = parser.parse_args()


dPATH = args.path or '.'

# Get The files in the directory
dirList = os.listdir(dPATH)

# Remove the name of this file from the list
if sys.argv[0] in dirList:
    dirList.remove(sys.argv[0])



if __name__ == '__main__':
    rename()
