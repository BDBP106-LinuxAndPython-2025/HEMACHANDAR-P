#!/bin/bash
#Define variables var1 with value ”Testing” and var2 with value ’testing”
var1="Testing"
var2="testing"

if [ "$var1" > "$var2" ]; then 
       	echo "$var1 is greater than $var2"
else 
	echo "$var1 is lesser than $var2"
fi

