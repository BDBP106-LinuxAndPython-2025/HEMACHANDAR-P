#!/usr/bin/python3

#Q8: Interchange even and odd components of a list

#Loop in steps of 2, swap index i and i+1

def interchange(input_list):
    for i in range(0, len(input_list)-1, 2):  # step of 2
        input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    return input_list

input_list = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
print("Interchanged list:", interchange(input_list))
