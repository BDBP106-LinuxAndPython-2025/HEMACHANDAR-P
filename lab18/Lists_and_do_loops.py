#!/usr/bin/python3

#(i) Using a simple do loop structure or list comprehension, find the sum of elements
#in the above list a.
a = [i for i in range(1, 51)]
sum=0
for i in a:
    sum=sum+i
print(sum)

#(ii) Define another list b (using list comprehension again!) containing prime numbers
#from 1 to 50.
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # even numbers greater than 2 are not prime

    for i in range(3, int(num ** 0.5) + 1, 2):  # check only odd divisors
        if num % i == 0:
            return False
    return True
b = [x for x in range(1, 51) if is_prime(x)]
print(b)

#(iii) Using a do loop structure, collect all the common numbers in a and b into a new
#list c.
c = []  # empty list to store common elements
for num in a:
    if num in b:
        c.append(num)
print(c)
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
