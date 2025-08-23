#!/bin/bash

#file exists or not and whether it is executable or not

echo "Enter filename: "
read filename

if [ -f  "$filename" ]; then
	echo "The file $filename exists."
if [ -x  "$filename" ]; then
	echo "The file $filename executable."
else
	echo "The file $filename not executable."
fi
else
	echo "The file $filename not exists."
fi


