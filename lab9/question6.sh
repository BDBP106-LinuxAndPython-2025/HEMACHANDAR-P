#!/bin/bash

echo "$HOME"

result=$(bc << EOF
scale=55659
23934/44343
EOF
)
echo "Calculation 23934/44343 = $result"


echo "Files in $HOME starting with 'D':"
ls "$HOME"/D*

echo "Lines in /etc/passwd with username '$USER':"
grep "^$USER:" /etc/passwd
