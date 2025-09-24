#!/bin/bash

#Create an array of 5 numbers. The script should print the largest number, smallest
#number and sum of all numbers in the array.

arr=( 12 53 86 49 75 )

echo "Array of numbers given :${arr[@]} "

numbers=${arr[@]}

largest=$( echo $numbers | tr ' ' '\n' | sort -n | tail -1 )
echo "largest:$largest"

smallest=$( echo $numbers | tr ' ' '\n' | sort -n | head -1 )
echo "smallest:$smallest"

sum=0

for i in $numbers; do
	sum=$(( sum + i))
done       	
echo "sum:$sum"
