import sys
from sos import runProg


def testNeg(av: [str]):
    sys.argv = av
    if (runProg() != "AssertionError: the arguments are bad"):
        print(f"neg:\t{av} :\tFailed")
    else:
        print(f"neg:\t{av} :\tPass!")


def testPos(av: [str]):
    sys.argv = av
    if (runProg() == "AssertionError: the arguments are bad"):
        print(f"pos:\t{av} :\tFailed")
    else:
        print(f"pos:\t{av} :\tPass!")


def main():
    testNeg(["sos.py", "H#llo"])
    testNeg(["sos.py", "H$llo"])
    testNeg(["sos.py", "12\""])
    testNeg(["sos.py", "H$llo"])
    testNeg(["sos.py", "\n"])
    testPos(["sos.py", "He llo"])
    testPos(["sos.py", ""])
    testPos(["sos.py", " "])
    testNeg(["sos.py"])
    testNeg(["sos.py", "a", "a"])
    testNeg(["sos.py", "##", "a"])
    testNeg(["sos.py", "", ""])
    testPos(["sos.py", "hello 123 abc12"])


if __name__ == "__main__":
    main()
