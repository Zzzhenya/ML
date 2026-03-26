# import os
# import time
# import sys


# def ft_tqdm(lst: range) -> None:
#     # copy the function tqdm 
#     # with the yield operator
#     total = len(lst)
#     curr = 1
#     for item in lst:
#         percent = (curr / total)
#         num = int((curr/ total) * 40)
#         # filled = int(bar_length * progress)
#         bar = "█" * num + " " * (40 - num)
#         # bar = "█" * num
#         sys.stdout.write(
#             f"\r{int(percent*100):3d}%|{bar}| {curr}/{total} "
#             # f"[{elapsed:05.2f}s<{0.00:05.2f}s, {speed:06.2f}it/s]"
#         )
#         sys.stdout.flush()
#         # print(f"{percent}% | \r{bar} ", end="")
#         curr += 1
#         yield item
    # for i, item in enumerate(lst, 1):
    #     percent = i  / total * 100
    #     bar = "█" * i + "-" * (42 - i)
    #     print(f"\r{bar} {percent}%", end="")
    #     # os.write(1, f"\r{bar} {i}%".encode())
    #     yield item

from datetime import datetime
import sys

def ft_tqdm(lst):
    total = len(lst)
    bar_length = 40
    start_time = datetime.now()

    for i, item in enumerate(lst, 1):
        percent = i / total
        num_filled = int(bar_length * percent)
        bar = "█" * num_filled + " " * (bar_length - num_filled)

        # elapsed time
        elapsed = datetime.now() - start_time
        elapsed_sec = int(elapsed.total_seconds())
        elapsed_str = f"{elapsed_sec//60:02d}:{elapsed_sec%60:02d}"

        # rate
        rate = i / elapsed.total_seconds() #if elapsed.total_seconds() > 0 else 0

        # ETA
        remaining_sec = (total - i) / rate #if rate > 0 else 0
        remaining_str = f"{int(remaining_sec)//60:02d}:{int(remaining_sec)%60:02d}"
        if (not i %20 or i == total):
            sys.stdout.write(
                f"\r{int(percent*100):3d}%|{bar}| {i}/{total} "
                f"[{elapsed_str}<{remaining_str}, {rate:06.2f}it/s]"
            )
        sys.stdout.flush()
        
        yield item

    print()



# def main():
#     print("Hello from 08!")


# if __name__ == "__main__":
#     main()
