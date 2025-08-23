#!/bin/bash

#to check whether the number is positive or negative or zero

echo "give a number"
read n

if [ "$n" -gt 0 ]; then
	echo "The number is positive"
elif [ "$n" == 0 ]; then
	echo "The number is zero"
else 
	echo "The number is negative"
fi
