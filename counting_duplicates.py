import sys


def main(script):
    """Count if an int or char is repeated more than once in input string"""
    try:
        text = sys.argv[1]
    except IndexError:
        print("python counting_duplicates.py [input string]")
    else:
        # ensure all chars are lower case
        text = text.lower()
        # create dictionary for each char and initialize count to 0
        text_dict = {x:0 for x in text}
        # loop though list and count the number of occurances of the char
        for char in text:
            if char in text_dict:
                text_dict[char] += 1
        # if a value in the dictionary is greater than 1, add to count
        count = 0
        for key in text_dict:
            if text_dict[key] > 1:
                count += 1
        print(count)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
