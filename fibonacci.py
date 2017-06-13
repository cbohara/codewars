#!/usr/local/bin/python3
import sys


def main(args):
    """Print the Fibonacci series up to n."""
    try:
        n = int(sys.argv[1])
    except IndexError:
        print("python3 fibonacci.py n")
    else:
        a, b = 0, 1
        while a < n:
            print(a, end=" ")
            a, b = b, a+b
        print()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
