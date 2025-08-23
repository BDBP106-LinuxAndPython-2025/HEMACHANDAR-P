#!/bin/bash
echo "Input a number: "
read n
if [[ "$n" -gt 100 ]]; then
echo "The number is greater than 100."
else
echo "The number is not greater than 100."
fi


#In the above line there is no semicolon because of that it will not execute
#in the above line the brackets are wrong ;because of that the code will not work
#We dont need two if blocks as the both aresame and the conditions are also same
