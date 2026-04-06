import sys

'''
Take string as argument and encode it to Morse Code

* support space & alphanumeric
* alpha numertic char -> dots and dashes
* Morse chars are seperated by a single space
* space -> /

* store morse code in a dictionary

* if more than 1 arg or type of arg is wrong -> Assertion Error


'''


def getDict() -> dict:
    morse = {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
        "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
        "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
        "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
        "Z": "--..",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",

        ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
        ":": "---...", ";": "-.-.-.", "'": ".----.", "\"": ".-..-.",
        "-": "-....-", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
        "&": ".-...",  "=": "-...-",  "+": ".-.-.",  "_": "..--.-",
        "$": "...-..-", "@": ".--.-.",

        " ": "/"
    }
    return morse


def encode(msg: str) -> str:
    text = msg.upper()
    morse = getDict()
    encoded = " ".join(morse[c] for c in text if c in morse)
    return (encoded)


def checkError() -> bool:
    if len(sys.argv) != 2:
        return (False)
    ret = [c.isalnum() or c == " " for c in sys.argv[1]]
    if not all(ret):
        return (False)
    return (True)


def runProg() -> str:
    try:
        assert checkError(), "the arguments are bad"
        return (encode(sys.argv[1]))
    except AssertionError as e:
        return (f"AssertionError: {e}")


def main():
    print(runProg())


if __name__ == "__main__":
    main()
