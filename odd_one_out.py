import sys


def odd_one_out(numbers):
    """Determine position of number that is the only odd or only even number in list."""
    evens = list(filter(lambda x: x % 2 == 0, numbers))

    if len(evens) == 1:
        for index, num in enumerate(numbers):
            if num % 2 == 0:
                return index + 1
    else:
        for index, num in enumerate(numbers):
            if num % 2 != 0:
                return index + 1
    

def main(sys_argv):
    """Transform string of numbers into list of ints and input to function."""
    numbers = [int(x) for x in sys.argv[1].split(' ')]
    print(odd_one_out(numbers))


if __name__ == "__main__":
    main(sys.argv)
