#!/usr/bin/python3

#(2) One can create a set from several different objects – lists, tuples and dictionaries. Come
#up with an example for each object type, and create a set out of that object using the
#set() function. In the case of a dictionary, what does the set contain?.

list1 = [1,2,3,1,2,3]
tuple1 = (1,1,2,2,3,3)
dict1 = {'a':1,'b':2,'c':3}
a=set(list1)
b=set(tuple1)
c=set(dict1)
print(a)
print(b)
print(c)
#O/P:{1, 2, 3}
#{1, 2, 3}
#{'c', 'b', 'a'}
