#!/bin/bash

gawk '{if ($2<25) print $1 }' textfile.txt

gawk '{if ($3=="Physics") print $1 }' data.csv

gawk '{ print $1" "  $2" "  $3 }' textfile.txt > data.csv

