#!/bin/bash

read -p "Enter the filename: " file

if [[ -f $file ]]; then
        wc $file
else
	echo "File not exist"
fi
