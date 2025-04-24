from random import sample
from math import floor


def random_box(bits=8):
    digits = floor(bits/4)
    population = [chr(0x2591 + i) for i in range(3)]
    return "".join(sample(population,digits,counts=[digits for i in population]))

def main():
    # UUID is a 128-bit hexadecimal digit
    output = f"{random_box(32)}-{random_box(16)}-{random_box(16)}-{random_box(16)}-{random_box(48)}"
    print(output)

if __name__ == "__main__":
    main()
