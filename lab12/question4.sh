#!/bin/bash

read -ra numbers < nums.txt
for num in "${numbers[@]}"
do
	echo $(( num * 2 ))
done
