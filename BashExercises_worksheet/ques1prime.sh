#!/bin/bash

read -p "Enter a number: " num

if (( num <=1 )); then 
	echo "Not prime"
	exit
fi

if (( num%2 == 0 )); then
	echo "Not prime"
	exit
fi

i=3
while (( i*i<=num )); do
	if (( num%i==0 )); then
		echo "Not prime"
		exit
fi
((i +=2))
done

echo "Prime"



