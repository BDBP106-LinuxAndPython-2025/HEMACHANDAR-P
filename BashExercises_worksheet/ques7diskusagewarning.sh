#!/bin/bash

usage=$(df -h | sort -k5 -n | tail -n 1 | gawk '{print $5}' | sed 's/%/ /')
	echo "$usage%"
if [[ $usage -gt 80 ]]; then
	echo "Usage is above 80%"
fi
