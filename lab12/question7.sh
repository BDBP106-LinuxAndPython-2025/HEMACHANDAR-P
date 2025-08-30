#!/bin/bash 

check_Directory() {
    if [ -e "$filename" ]; then
        echo "$filename exists!"
        ls  "$filename"
    else
        echo "$filename does not exist"
    fi
}

read -p "Enter your directory name: " filename
check_Directory "$filename"


