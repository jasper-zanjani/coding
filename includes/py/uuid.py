from random import random
from math import floor


def random_hex(bits=8):
    return hex(floor(random()*(2**bits-1))).removeprefix('0x')

def main():
    # UUID is a 128-bit hexadecimal digit
    output = f"{random_hex(32)}-{random_hex(16)}-{random_hex(16)}-{random_hex(16)}-{random_hex(48)}"
    print(output)

if __name__ == "__main__":
    main()
