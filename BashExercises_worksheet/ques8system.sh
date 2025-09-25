#!/bin/bash

#A script that prints a mini-system report that includes a) current date and time, b)
#logged-in users, c) system uptime and d) top 5 processes by memory usage.

#a) current date and time
echo
echo "current date and time"
date

#b)logged-in users
echo
echo "logged-in users"
who

#c)system uptime 
echo
echo "system uptime"
uptime -p 
uptime -s

#d)top 5 processes by memory usage.
echo
echo "top 5 processes by memory usage."
ps aux | sort -k4 -n | tail -5 | awk '{print $1,$2,$3,$4,$5,$6}' | sort -nr

