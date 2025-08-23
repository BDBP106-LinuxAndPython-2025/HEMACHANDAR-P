#!/bin/bash

mystring=""

if [ -z "$mystring" ]; then
	echo " The string is empty."
else 
	echo " The string is not empty."
fi

#here checking the string is not empty
if [ -n "$mystring" ]; then
	echo " The string is not empty."
else 
	echo " The string is empty."
fi

