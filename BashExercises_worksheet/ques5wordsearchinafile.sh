#!/bin/bash

read -p "Enter word: " word
read -p "Enter filename: " file
grep -n "$word" "$file"

