#!/usr/bin/python3

n=int(input('Enter the number to convert to binary number: '))
binary=""
remainder=0
if n==0:
    print ('The decimal number is 0')
else:
    while n>0:
          remainder=n%2
          binary = str(remainder)+binary
          n=n//2

print ("The binary number is ",binary)

count=0

for i in binary:
    if i=='1':
        count=count+1
print (f'The number(1) in the binary is {count} ')