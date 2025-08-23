#!/bin/bash

#file exists or not and whether it is executable or not

echo "Enter filename: "
read filename

if [ -f  "$filename" ]; then
        echo "The file $filename exists."
	
	exit 200


else
        echo "The file $filename not exists."

	exit 201
fi

#4.1 .How do you check if the correct exit code is executed?
#by checking the exit code what we gave in if condition and else condition and after the result if we are givving echo $? we can check whether the given statement is correct or not

#4.2 . No, If i add echo$? after the if statment it wont execute as we can modify only the exit code and by giving echo $? we can check the exit code only and it wont execute in the output and it will show only the error

#4.3 .yes , it will execute because of exit code , when it cross the exit it will go out of the statement and it wont go to the next line
