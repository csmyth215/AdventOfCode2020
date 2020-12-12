import sys

def load_file_no_spaces(filename):
    with open(filename) as f:
        my_lines = f.read()
        my_lines = my_lines.replace("\r", "")
        my_lines = my_lines.split("\n\n")
        my_lines = [i.replace("\n", "") for i in my_lines]
    return my_lines

def load_file_with_spaces(filename):
    with open(filename) as f:
        my_lines = f.read()
        my_lines = my_lines.replace("\r", "")
        my_lines = my_lines.split("\n\n")
        my_lines = [i.replace("\n", " ") for i in my_lines]
    return my_lines

def count_unique_letters(single_string):
    unique_list = []
    for i in single_string:
        if i in unique_list:
            continue
        else:
            unique_list.append(i)
    return len(unique_list)

def count_intersection_letters(single_string):
    # "xyz abcde fghi xklt"
    subgroups = single_string.split(" ")    
    my_sets = []
    for group in subgroups:
        my_set = set([i for i in group])
        my_sets.append(my_set)
    
    intersection_set = my_sets[0]
    for this_set in my_sets:
        intersection_set = intersection_set & this_set
    return len(intersection_set)

customs_raw = load_file_no_spaces("puzzle_inputs/Day_Six_textfile.txt")
sum_of_counts = 0
for element in customs_raw:
    count = count_unique_letters(element)
    sum_of_counts += count

customs_raw_two = load_file_with_spaces("puzzle_inputs/Day_Six_textfile.txt")
sum_of_intersection_count = 0
for element in customs_raw_two:
    count = count_intersection_letters(element)
    sum_of_intersection_count += count
print(sum_of_intersection_count)