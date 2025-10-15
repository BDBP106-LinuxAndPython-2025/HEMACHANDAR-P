#!/usr/bin/python3

#11. How to read and write binary data? Example programs:
#Writing binary:
with open("hems.bin", "wb") as f:
    f.write(b'\x00\x01\x02\x03')
#Reading binary:
with open("hems.bin", "rb") as f:
    data = f.read()
    print(data)
