# Working with files

## create.py ([Implementation in Go](https://github.com/NickName-AM/GoFiles))
	- Create Bulk Files
	- Usage: python3 create.py --help
	

## rename.py
	- Rename Bulk Files
	- Usage: python3 rename.py --help

## copyfiles.py
	- Starting from the given root directory, search for files with the given extension(s) and copy them to given path
	- Usage: python3 copyfiles.py --help
	- Ex: python3 copyfiles.py /home/user/Documents /home/user/Pictures --ext jpg,png
		# This will traverse every directory starting from /home/user/Documents
		# and copy the files with the extension of 'jpg' or 'png' to /home/user/Pictures