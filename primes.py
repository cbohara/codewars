#!/usr/local/bin/python3
import sys


def main():
    """Identify prime numbers, or one set of factors for a non-prime number."""
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number.')


if __name__ == "__main__":
    sys.exit(main())
