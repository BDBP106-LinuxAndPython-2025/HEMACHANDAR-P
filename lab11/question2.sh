#!/bin/bash
#distinguish between -e,-s,-f

touch newfile
echo "Hemachandar" > newnewfile
mkdir newdirof

echo "Enter fileofname: "
read file

#here below i am checking for -e
if [ -e newfile ]; then
	echo "Empty file exists"
else 
	echo "empty file does not exists"
fi

#here below i am checking for -s

if [ -s newfile ]; then
	echo "emptyfile is not empty"
else 
	echo "empty is not at ll empty"
fi

if [ -s newnewfile ]; then
	echo "datafile is not empty"
fi

#here below i am checking for -f
if [ -f newnewfile ]; then
	echo "newnewfile is a regular file"
fi

if [ -f newdiraof ]; then
	echo "newdir is a regular file"
else
	echo "newdir is not a regularfile"
fi


