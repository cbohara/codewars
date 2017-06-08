import sys


def main(script):
    """Count duplicate chars and ints in input string"""
    try:
        text = sys.argv[1]
    except IndexError:
        print("python3 counting_duplicates.py [input string]")
    else:
        print(text)



if __name__ == "__main__":
    sys.exit(main(sys.argv))
