#!/bin/bash

# Ask user for input
read n
i=1
until [ $i -gt 15 ]
do
    echo " $i x $n = $(( n * i ))"
    i=$(( i + 1 ))
done

