#!/bin/bash
#Write in a shell script, an if statement involving > comparison of the two strings.Remember to use the \ with the operator as in the last question. Use appropriate echo statements

var1="Testing"
var2="testing"

if [ "$var1" > "$var2" ]; then
        echo "$var1 is greater than $var2"
else
        echo "$var1 is lesser than $var2"
fi

          
