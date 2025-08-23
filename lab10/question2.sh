#!/bin/bash

echo "Input a number"
read n
if [ "$n" -ge 18 ]; then
	echo "You are an adult"
else
	echo "You are a minor"
fi

