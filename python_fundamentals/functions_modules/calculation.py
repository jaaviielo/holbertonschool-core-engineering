#!/usr/bin/env python3


from calculator_1 import addition, subtraction, multiplication, division


def main():

    a = 10
    b = 5

    print("{}".format(addition(a, b)))
    print("{}".format(subtraction(a, b)))
    print("{}".format(multiplication(a, b)))
    print("{}".format(division(a, b)))


if __name__ == "__main__":
    main()
