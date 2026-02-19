from NULL_not_found import NULL_not_found

def basic():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))


def TEST(obj: any, expected: int)->int:
    ret = NULL_not_found(obj)
    if (ret != 0):
        print(f"{type(obj)} {obj} returned 1")
    else:
        print(f"{type(obj)} {obj} returned 0")
    
    if (expected != ret):
        print("\033[31mFailed\033[0m")
        return (1)
    return (0)


def allNullCases():
    ret = 0
    ret += TEST(None, 0)
    ret += TEST(int(0), 0)
    ret += TEST(-0, 0)
    ret += TEST(float(0), 0)
    ret += TEST(float(0.0), 0)
    ret += TEST(float(-0), 0)
    ret += TEST(complex(0), 0)
    ret += TEST(complex(-0), 0)
    ret += TEST(False, 0)
    ret += TEST('', 0)
    ret += TEST(list(), 0)
    ret += TEST(tuple(), 0)
    ret += TEST(dict(), 0)
    ret += TEST(set(), 0)
    ret += TEST(frozenset(), 0)
    
    if (ret > 0):
        print("\033[31mNUll cases Failed\033[0m")
    else:
        print("\033[32mNUll cases Passed\033[0m")

def otherCases():
    ret = 0
    ret += TEST('Hello', 1)
    ret += TEST('0', 1)
    ret += TEST(1, 1)
    ret += TEST(10000, 1)
    ret += TEST(-1, 1)
    ret += TEST(float(1.34), 1)
    ret += TEST(True, 1)
    ret += TEST([0], 1)
    ret += TEST([0, 1], 1)
    ret += TEST((0,0), 1)
    ret += TEST((0,1), 1)
    if (ret > 0):
        print("\033[31mOther cases Failed {ret} \033[0m")
    else:
        print("\033[32mOther cases Passed\033[0m")

def extra():
    allNullCases()
    otherCases()


def main():
    basic()
    # extra()




if __name__ == "__main__":
    main()
