import sys

def load_file(filename):
    with open(filename) as f:
        my_lines = f.readlines()
    return my_lines

def two_elements(source_numbers):
    total = 2020
    for x in source_numbers:
        remainder = total - x
        if remainder in source_numbers:
            answer = x * remainder
            print(answer)
            sys.exit(0)

def three_elements(source_numbers):
    for a in source_numbers:
        b_c = 2020 - a
        for b in source_numbers:
            if b == a:
                continue
            if b_c - b in source_numbers:
                c = b_c - b
                if c == b:
                    continue
                answer = a * b * c
                print(answer)
                sys.exit(0)

lines = load_file("Day_One_textfile.txt")
lines = [int(i.strip()) for i in lines]
three_elements(lines)

