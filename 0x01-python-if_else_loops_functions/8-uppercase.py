#!/usr/bin/python3
def uppercase(str):
    Upper = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            Upper += chr(ord(char) - 32)
        else:
            Upper += char
    print("{:s}".format(Upper))
