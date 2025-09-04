#!/bin/bash


sed -n '/and/p' question1.txt


sed 's/language/lang/g' question1.txt


sed '/is/d' question1.txt


nl question1.txt


sed '=' question1.txt | sed 'N;s/\n/ /'


sed '1,2d' question1.txt


sed -n 'p;n' question1.txt


sed 's/Python/python/;s/language/lang/' question1.txt

