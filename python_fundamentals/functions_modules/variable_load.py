#!/usr/bin/env python3

def main():

    try:
        from variable_load_5 import a
        print("{}".format(a))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
