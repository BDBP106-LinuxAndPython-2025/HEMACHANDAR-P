#!/bin/bash

# Function to find maximum of two numbers
maximum() {
    
	local num1=$1
	local num2=$2

	if [ $num1 -gt $num2 ]; then
		echo $num1
	else
		echo $num2
	fi

}

read -p "enter 1st number: " n1
read -p "enter 2nd number: " n2

max=$(maximum "$n1" "$n2")
echo "The maximuim number is $max"

