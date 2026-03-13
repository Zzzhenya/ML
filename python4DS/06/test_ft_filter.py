from ft_filter import ft_filter


def is_even(n):
    return n % 2 == 0


def is_alpha(a):
    return (True)


def main():
    print(filter.__doc__)
    print(ft_filter.__doc__)
    # print("Hello from 06!")
    # numbers = [1,2,3,4,5,6]
    letters = "abcde"
    # # result = ft_filter(is_even, numbers)
    result1 = ft_filter(is_alpha, letters)
    result2 = filter(is_alpha, letters)
    print(result1, list(result1))
    print(result2, list(result2))
    print(result1, list(result1))
    print(result2, list(result2))
    # print(result)
    # print(list(result))


if __name__ == "__main__":
    main()
