#!/usr/bin/env python3

def uppercase(str):

    result = ""

    for letter in str:

        if 97 <= ord(letter) <= 122:
            letter = chr(ord(letter) - 32)

        result += letter

    print("{}".format(result))
