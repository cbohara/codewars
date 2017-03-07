import sys


def odd_one_out(numbers):
    """Determine position of number that is the only odd or only even number in list."""
    


def main(sys_argv):
    numbers = [int(x) for x in sys.argv[1].split(' ')]
    odd_one_out(numbers)


if __name__ == "__main__":
    main(sys.argv)
