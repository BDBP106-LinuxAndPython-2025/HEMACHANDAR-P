#!/bin/bash

read n
while [ "$n" -gt 5 ]
do 
	IFS=$n+$n
	echo $
done
#function addnosinarow {
#    if [ $# -eq 0 ] || [ $# -gt 2 ]; then
#        echo -1
#      if [ $# -eq 1 ]; then
#        echo $(($1 + $1))
#    elif [ $# -eq 2 ]; then
#        echo $(($1 + $2))
#    fi
#}

#echo -n "Adding numbers: "
#value=$(addnosinarow $1 $2)
#echo $value


#!/bin/bash

#read n
#while [ "$n" -lt 11 ]
#do
#    echo $n
#    n=$(( n+1 ))
#done




# Ask user for input
#read n
#i=1
#until [ $i -gt 15 ]
#do
#    echo " $i x $n = $(( n * i ))"
#    i=$(( i + 1 ))
#done

