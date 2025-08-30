#!/bin/bash
n=1
while [ "$n" -le 50 ]
do
	if (( n%2 == 0 )); then
		echo $n
	fi
	n=$(( n+1 ))
done

