#!/usr/bin/python3
#n = int(input("Enter a number: "))
#binary = bin(n)[2:]  # Removes the '0b' prefix
#print(f'The binary representation of {n} is {binary}')


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