#!/usr/bin/python3

#(4) One can use sets or lists or tuples as values in a dictionary. For example, let’s define the
#following dictionary
#studentmarks={
#"Rahul":{49,58, 35,64}, "Sandeep":{80,92,94,83},"Sita":{44,65,76,54}}
#Write a script to check and print the name of the student if the student has scored above
#60 in all subjects.

studentmarks={
        "Rahul":{49,58, 35,64},
        "Sandeep":{80,92,94,83},
        "Sita":{44,65,76,54}}
for student,marks in studentmarks.items():
 if all(mark>60 for mark in marks):
  print(student,marks)
