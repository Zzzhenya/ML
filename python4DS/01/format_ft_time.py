# module : from datetime import datetime

# built in
import time

def main():

    secs = time.time()

    print(f"Seconds since January 1, 1970: {secs:,.4f} or {secs:.2e} in scientific notation")
    print(time.strftime("%b %d %Y", time.localtime(secs)))


if __name__ == "__main__":
    main()