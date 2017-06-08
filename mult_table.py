import sys


def main(script):
    try:
        row = int(sys.argv[1])
        col = int(sys.argv[2])
    except IndexError:
        print("python3 mult_table.py [# of rows] [# of columns]")
    else:
        solution = []
        for x in range(1, row+1):
            data = []
            for y in range(1, col+1):
                data.append(x*y)
            solution.append(data)
        return solution

if __name__ == "__main__":
    sys.exit(main(sys.argv))
