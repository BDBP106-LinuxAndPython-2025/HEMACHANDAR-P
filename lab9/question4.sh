#!/bin/bash

var1=$(date ; echo $?)
echo "The output is:" $var1
var2=$(who ; echo $0)
echo "The output is:" $var2
var3=$(date ; echo $#)
echo "The output is:" $var3
var4=$(who ; echo $@)
echo "The output is:" $var4

