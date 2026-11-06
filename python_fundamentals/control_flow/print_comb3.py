#!/usr/bin/env python3

first_time = True

for first_digit in range(10):

    for second_digit in range(10):
 
        if second_digit > first_digit:

            if first_time:
                print("{}{}".format(first_digit, second_digit), end="")
                first_time = False

            else:
                print(", {}".format(first_digit) +
                      "{}".format(second_digit), end="")

print (" ", end="")                
