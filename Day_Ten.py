import copy

def loadfile(filename):
    # open file and convert to list of integers
    with open(filename) as f:
        my_lines = f.readlines()
        my_lines = [int(line.replace('\n', '')) for line in my_lines]
    return my_lines

def determine_differences(joltages):
    # find difference in joltage relative to next adapter in list
    joltage_count = len(joltages) 
    a = 0
    b = 1
    differences = [0, ]
    while b < joltage_count:
        difference = joltages[b] - joltages[a]
        differences.append(difference)
        a += 1
        b += 1
    return differences


def determine_valid_arrangements(adapter_joltages, target_joltage, a, this_path=[], valid_paths=[]):
    """Recursive solution. Not appropriate."""
    current = adapter_joltages[a]
    differences = [1, 2, 3]
    this_path.append(current)
    for difference in differences:
        next_adapter = current + difference
        if next_adapter not in adapter_joltages:
            continue

        if next_adapter == target_joltage:
            valid_paths.append(this_path)
        else:
            address = adapter_joltages.index(next_adapter)
            valid_paths = determine_valid_arrangements(adapter_joltages, target_joltage, address, this_path=copy.deepcopy(this_path), valid_paths=copy.deepcopy(valid_paths))

    return valid_paths


def create_groups(list_of_jolt_diffs):
    # split list where jump between joltages == 3 to get smaller, manageable groups:
    grouped_jolts = []
    inner = []
    for x, y in list_of_jolt_diffs:
        if x != 3:
            inner.append(y)
        else:
            grouped_jolts.append(copy.copy(inner))
            inner = [y]
    if len(inner):
        grouped_jolts.append(copy.copy(inner))
    return grouped_jolts     


# Load and parse puzzle input: 
my_joltages = loadfile("puzzle_inputs/Day_Ten_textfile.txt")

# Add built-in joltage adapter: 3 jolts higher than the highest-rate adapter:
x = max(my_joltages) + 3
my_joltages.append(x)

# Add charging outlet near seat: effective joltage rating of 0:
my_joltages.append(0)

# Sort adapters in ascending joltage:
my_joltages.sort()

# Find differences:
my_differences = determine_differences(my_joltages)

# Count instances of difference == 1:
ones = my_differences.count(1)

# Count instances of difference == 3:
threes = my_differences.count(3)

# Answer Part One: What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
part_one = ones * threes

# Create list of jolt-diff tuples
jolts_and_diffs = list(zip(my_differences, my_joltages))

# Create list of smaller lists; difference between list_1[-1] and list_2[0] is 3:
grouped_joltages = create_groups(jolts_and_diffs)

""" We know the first and last element of each smaller list needs to be anchored, as 3 is the maximum difference between joltages in the list.  
We can calculate the number of other possible combinations of each smaller list (elements can be left out), with that anchoring in mind"""
# Create list of number of possible combinations for each smaller list:
factorials = []
for group in grouped_joltages:
    this_group_factorial = 1
    length = len(group)
    if length == 1 or length == 2:
        this_group_factorial = this_group_factorial * 1
    if length == 3:
        this_group_factorial = this_group_factorial * 2
    if length == 4:
        this_group_factorial = this_group_factorial * 4
    if length == 5:
        this_group_factorial = this_group_factorial * 7
    factorials.append(this_group_factorial)

# Calculate total combinations i.e. the product of all smaller list combination Ns:
total_combos = 1
for factorial in factorials:
    total_combos = total_combos * factorial

part_two = total_combos
print(part_two)