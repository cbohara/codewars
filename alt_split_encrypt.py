import sys


def encrypt_pattern(text):
    """Return encrypted text."""
    even_index = ""
    odd_index = ""
    for index, char in enumerate(text):
        if index % 2 == 0:
            even_index += char
        else:
            odd_index += char
    return odd_index + even_index


def encrypt(text, n):
    """Repeat encryption pattern n number of times."""
    encrypt_text = text
    for i in range(n):
        encrypt_text = encrypt_pattern(encrypt_text)
    return encrypt_text


def main(args):
    """Implement alternating split encryption pattern."""
    text = sys.argv[1]
    n = sys.argv[2]
    return encrypt(text, n)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
