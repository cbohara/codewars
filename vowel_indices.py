import sys


def main(script):
    try:
        word = sys.argv[1]
    except IndexError:
        print("python3 vowel_indices.py [input text]")
    else:
        vowel = ['a', 'e', 'i', 'o', 'u', 'y']

        solution = []
        for index, char in enumerate(word):
            if char in vowel:
                solution.append(index + 1)

        return solution


if __name__ == "__main__":
    sys.exit(main(sys.argv))
