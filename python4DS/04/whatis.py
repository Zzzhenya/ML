# script takes arguments, execute and print assertion errors
import sys


def isInt(val: any) -> bool:
    '''
    Check whether a given value can be converted to an integer.

    Parameters : val (any)
        The value to check. Can be of any type (string, float, etc.).
    Returns: bool
        True if `val` can be converted to an integer, False otherwise.
    '''
    try:
        int(val)
        return True
    except ValueError:
        return False


def main(args: list):
    '''
    Checks whether the argument passed to the program is an odd
    or an even integer and prints the result

    Parameters : args (list)
        List of arguments passed to the program in a list
    Returns: void
    Output :
        if more than one argument or argument is not an integer prints
        an AssertionError
    '''
    if len(args) == 0:
        return
    try:
        assert len(args) == 1, "more than one argument provided"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    try:
        assert isInt(args[0]), "argument is not an integer"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    if (int(args[0]) % 2):
        print("I'm Odd.")
    else:
        print("I'm Even.")

    # print(isInt.__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
