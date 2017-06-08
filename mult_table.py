import sys


def main(script):
    try:
        row = int(sys.argv[1])
        col = int(sys.argv[2])
    except IndexError:
        print("python3 mult_table.py [# of rows] [# of columns]")
    else:
        return [[x*y for y in range(1, col+1)] for x in range(1, row+1)]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
