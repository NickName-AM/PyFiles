#!/usr/bin/env python3

# Copy a bunch of files

'''
python3 copyfiles.py --help
'''

import argparse
import os
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('startpath', help='Start searching from the given path')
parser.add_argument('copyto', type=str, help='Copy the matching files to the given path')
parser.add_argument('--ext', type=list, help='extensions(s) to search for')
parser.add_argument('--startswith', type=str, help='Filename starting with the given string and ending with given extension')
args = parser.parse_args()

# Path to start the search from
start_dir = args.startpath

# Path to copy to
dst_dir = args.copyto

# List of user-provided extensions
ext_list = ''.join(args.ext).split(',')

# Startswtih
starts_with = args.startswith or ''

# This might be the only place where I have used De-Morgan's Law
if not (os.path.exists(start_dir) and os.path.exists(dst_dir)):
    print('STARTPATH_OR_DESTINATIONPATH_DOES_NOT_EXIST')
    exit(-1)

# Main
for root, dirs, files in os.walk(args.startpath):

    # Gather file(s) with the given ext(s) from the current dir
    files_to_copy = [os.path.join(root, file) for file in files for e in ext_list if file.endswith(e) and file.startswith(starts_with)]
    
    # If there are files with given ext in that dir, copy them to dst_dir
    if files_to_copy:
        for f in files_to_copy:
            shutil.copy2(f, dst_dir)
