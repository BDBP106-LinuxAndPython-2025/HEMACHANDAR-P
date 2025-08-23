#!/bin/bash

val1=Jayashree
val2=Nagesh
if [ $val1 \> $val2 ]; then
echo "$val1 is greater than $val2"
else
echo "$val1 is lesser than $val2"
fi

#in the above program at first without using the symbol(\) the program will take it as redirection and created a newdirectory called NAGESH
#after deleting the directory called NAGESH the program is ran with (\) now this helps to say that just comparison only not to create a directory
`
