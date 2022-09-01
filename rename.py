# TO-DO: A lot

# Rename bulk files

'''
Usage: python3 rename.py
'''

import os
import argparse
import sys

dPATH = '.'

# Get The files in the directory
dirList = os.listdir(dPATH)

# Remove the name of this file from the list
dirList.remove(sys.argv[0])

c=0
for file in dirList:
    ext = file.split('.')[-1]
    os.rename(file, f'{c}.{ext}')
    c+=1
