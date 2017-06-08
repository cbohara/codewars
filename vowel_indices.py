import sys


def main(script):
    try:
        word = sys.argv[1]
    except IndexError:
        print("python3 vowel_indices.py [input text]")
    else:
        return [index for index, char in enumerate(word, start=1) if char.lower() in 'aeiouy']


if __name__ == "__main__":
    sys.exit(main(sys.argv))
