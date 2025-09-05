#!/bin/bash

read $1 $2 $3 $4


if [ $# -ne 4 ];  then
	echo " No of argument is wrong"
	exit 1 
else
	echo "$1"
	echo "$2"
	echo "$3"
	echo "$4"

fi
