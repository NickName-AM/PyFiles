# Working with files

## create.py ([Implementation in Go](https://github.com/NickName-AM/GoFiles))
```
- Create Bulk Files
- Usage: python3 create.py --help
```

### Example:
This will create 100 files with extension of jpg and random filename(lowercase) of length 10
```
python3 create.py -n 100 -e jpg -p lower -l 10
```

## rename.py
```
- Rename Bulk Files
- Usage: python3 rename.py --help
```

### Example:
This will rename all the files(not folders) in '/tmp' to numbers with extension of jpg. (Ex: 0.jpg, 1.jpg)
```
python3 rename.py -P /tmp -p number -e jpg
```

## copyfiles.py
```
- Starting from the given root directory, search for files with the given extension(s) and copy them to given path
- Usage: python3 copyfiles.py --help
- Ex: python3 copyfiles.py /home/user/Documents /home/user/Pictures --ext jpg,png
	# This will traverse every directory starting from /home/user/Documents
	# and copy the files with the extension of 'jpg' or 'png' to /home/user/Pictures
```
### Example
This will traverse every directory starting from '/home/user/Documents' and copy all the files that have the extension 'pdf' to /tmp
```
python3 copyfiles.py /home/user/Documents /tmp --ext pdf
```