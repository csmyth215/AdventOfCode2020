import time

t = time.process_time()

puzzle_input = [5,1,9,18,13,8,0]

def save_part_one_output(puzzle_data):
    new_f = open('puzzle_inputs/Day_Fifteen_Part_One.txt', "w")
    for n in range(0, (max(puzzle_data) + 1)):
        my_string = f"There are {puzzle_data.count(n)} instances of {n} spoken.\n"
        new_f.write(my_string)
    new_f.close()

last_occurrences = {}
for i in puzzle_input[:-1]:
    last_occurrences[i] = puzzle_input.index(i)

last_position = len(puzzle_input) - 1
i = puzzle_input[-1]
while last_position < (30000000 - 1):
    if i not in last_occurrences.keys():
        last_occurrences[i] = last_position
        i = 0
    else:
        turns_apart = last_position - last_occurrences[i]
        last_occurrences[i] = last_position
        i = turns_apart

    last_position += 1

print(f"The 30000000th number spoken is {i}.")
elapsed_time = time.process_time() - t
print(f"This code took {elapsed_time}s to run.")