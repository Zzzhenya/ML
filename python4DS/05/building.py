import sys


def main(args: list):
    message = None
    if (len(args) == 0):
        # message = input("What is the text to count?\n")
        print("What is the text to count?")
        message = sys.stdin.read()
    try:
        assert len(args) <= 1, "too many arguments"
        if message is None:
            message = args[0]
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    chars = 0
    upper = 0
    lower = 0
    punc = 0
    digits = 0
    spaces = 0

    for c in message:
        chars += 1
        if c.islower():
            lower += 1
        if c.isupper():
            upper += 1
        if not c.isalnum() and not c.isspace():
            punc += 1
        if c.isdigit():
            digits += 1
        if c.isspace():
            spaces += 1

    print(f"The text contains {chars} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main(sys.argv[1:])
