#!/usr/local/bin/python3
import sys


def main():
    """Transform matrix to transpose rows and columns."""
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    return [[row[i] for row in matrix] for i in range(len(matrix)+1)]


if __name__ == "__main__":
    sys.exit(main())
