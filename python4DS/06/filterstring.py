from ft_filter import ft_filter
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


def main(S: str, N: int):
    words = S.split()
    result = list(ft_filter(lambda w: len(w) > N, words))
    print(result)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert isInt(sys.argv[2]), "the arguments are bad"
        # check string only contain letters and space chars,
        # what about numbers?
        # ret = [c.isalnum() or c.isspace() for c in sys.argv[1]]
        ret = [c.isalpha() or c.isspace() for c in sys.argv[1]]
        assert all(ret), "the arguments are bad"
        first_arg = sys.argv[1]
        second_arg = sys.argv[2]
        main(first_arg, int(second_arg))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
