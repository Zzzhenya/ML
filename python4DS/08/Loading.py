import os
import time
import sys


def ft_tqdm(lst: range) -> None:
    # copy the function tqdm 
    # with the yield operator
    total = len(lst)

    for i, item in enumerate(lst, 1):
        percent = i  / total * 100
        bar = "█" * i + "-" * (42 - i)
        print(f"\r{bar} {percent}%", end="")
        # os.write(1, f"\r{bar} {i}%".encode())
        yield item



# def main():
#     print("Hello from 08!")


# if __name__ == "__main__":
#     main()
