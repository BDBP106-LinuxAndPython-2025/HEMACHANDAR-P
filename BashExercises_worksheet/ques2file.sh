#!/bin/bash

#Ask the user for a filename, and check if it exists. If it exists, is the file readable and writable

read -p "Enter filename: " file

if [[ -e $file ]]; then
	echo "File exists"
else 
	echo "File doesn't exist"
fi

if [[ -r $file ]]; then
	echo "File has permission to read"
else
	echo "File has no permission to read"
fi

if [[ -w $file ]]; then
	echo "File has permission to write"
else
	echo "File has no permission to write"
fi





