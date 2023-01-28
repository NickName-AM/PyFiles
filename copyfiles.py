#!/usr/bin/env python3

# Copy a bunch of files

# Looks for files with matching pattern in the given directory (or recursively)

'''
python3 copyfiles.py --help
'''

import argparse
import os
import shutil

# Command-line argruments
parser = argparse.ArgumentParser()
parser.add_argument('startpath', help='Start searching from the given path')
parser.add_argument('copyto', type=str, help='Copy the matching files to the given path')
parser.add_argument('--ext', type=list, help='extensions(s) to search for')
parser.add_argument('--startswith', type=str, help='Filename starting with the given string and ending with given extension')
parser.add_argument('--endswith', type=str, help='Filename ending with the given string and extension')
parser.add_argument('--exclude-files', type=str, help='List of filenames to exclude (seperated by comma)')
parser.add_argument('--exclude-dirs', type=str, help='List of directories to exclude (seperated by comma)')
parser.add_argument('-r', '--recursive', help='Copy files recursively. (Default: Off)', action='store_true')
args = parser.parse_args()

# Path to start the search from
start_dir = args.startpath

# Path to copy to
dst_dir = args.copyto

# List of user-provided extensions
## If no exts are given, returns ['']
ext_list_raw = ''.join(args.ext or []).split(',')

if ext_list_raw != ['']:
    ext_list = ['.'+e for e in ext_list_raw]
else:
    ext_list = ext_list_raw

# Startswtih
starts_with = args.startswith or ''

# Endswith
ends_with = args.endswith or ''

exclude_files = []
if args.exclude_files:
    exclude_files = args.exclude_files.split(',')

exclude_dirs = []
if args.exclude_dirs:
    exclude_dirs = args.exclude_dirs.split(',')

# This might be the only place where I have used De-Morgan's Law
if not (os.path.exists(start_dir) and os.path.exists(dst_dir)):
    print('[-] STARTPATH_OR_DESTINATIONPATH_DOES_NOT_EXIST')
    exit(-1)

# Main
for root, dirs, files in os.walk(args.startpath):

    excluded_dir = [i for i in exclude_dirs if i in root]
    if excluded_dir:
        continue    

    # Gather file(s) with the given ext(s) from the current dir
    ## I know the below code is messy, but I was practicing list comprehension
    files_to_copy = [os.path.join(root, file) for file in files for e in ext_list if file.startswith(starts_with) and file.endswith(f'{ends_with}{e}')]

    # If there are files with given ext in that dir, copy them to dst_dir
    if files_to_copy:
        for f in files_to_copy:
            if f.split('/')[-1] in exclude_files:
                continue
            
            shutil.copy2(f, dst_dir)
    
    if not args.recursive:
        break
