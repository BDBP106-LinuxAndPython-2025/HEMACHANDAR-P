#!/usr/bin/python3

#(3) Write a script to check if a given number, N, is prime or not

N=int(input("Enter a number: "))

if N<=1:
    print(f'{N} :Not a prime number')
elif N==2 or N==3 or N==5:
    print(f'{N} :It is a prime number')
elif N%2==0:
    print(f'{N} :It is not a prime number')
elif N>2:
        H = N // 2
        for i in range(H,2,-1):
            if N%i==0:
                print(f'{N} :It is not a prime number')
                break
            else:
                print(f'{N} :It is a prime number')
                break
