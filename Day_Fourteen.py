import copy

def load_file(textfile):
    with open(textfile) as f:
        my_lines = f.readlines()
        my_lines = [i.strip('\n') for i in my_lines]
        my_orders = []
        get_bin = lambda x, n: format(x, 'b').zfill(n)
        for i in my_lines:
            i, j = i.split('=')
            i, j = i.strip(), j.strip()

            if i[:3] == 'mem':
                a = 'mem'
                b = get_bin(int(i[4:-1]), 36)
                c = get_bin(int(j), 36)

                my_orders.append((a, b, c))

            else:
                my_orders.append((i, j))

    return my_orders

def create_formatted_textfile(formatted_instructions):
    new_f = open('puzzle_inputs/Day_Fourteen_formatted.txt', "w")
    for instruction in formatted_instructions:
        third = None    
        if len(instruction) > 2:
            third = instruction[2]
        my_string = "{} -- {} -- {}\n".format(instruction[0], instruction[1], third)
        new_f.write(my_string)
    new_f.close()


def mask_my_mem(this_mask, this_value):
    new_value = []
    for n in range(0, 36):
        if this_mask[n] == 'X':
            new_value.append(this_value[n])
        else:
            new_value.append(this_mask[n])
    
    return "".join(new_value)


def mask_variants(this_mask):
    if not 'X' in this_mask:
        return [this_mask]
    
    results = []
    i = this_mask.index('X')
    zero_mask = this_mask[:i] + "0" + this_mask[i+1:]
    one_mask = this_mask[:i] + "1" + this_mask[i+1:]
    results.extend(mask_variants(zero_mask))    
    results.extend(mask_variants(one_mask))

    return results

def mask_my_mem_key(this_mask, this_key):

    new_key = []

    for n in range(0, 36):
        if this_mask[n] == '0':
            new_key.append(this_key[n])
        elif this_mask[n] == '1':
            new_key.append('1')
        elif this_mask[n] == 'X':
            new_key.append('X')
    
    new_key = "".join(new_key)

    expanded_keys = mask_variants(new_key)
    return expanded_keys


def write_to_mem(my_mask, my_memory, my_key, my_value):
    my_new_value = mask_my_mem(my_mask, my_value)
    my_memory[my_key] = my_new_value


def write_to_mem_two(my_mask, my_memory, my_key, my_value):
    my_new_keys = mask_my_mem_key(my_mask, my_key)
    for key in my_new_keys:
        my_memory[key] = my_value


my_instructions = load_file('puzzle_inputs/Day_Fourteen_textfile.txt')
my_instruction_copy = my_instructions[:]

# Part One
memory= {}
current_mask = 0
for instruction in my_instructions:
    action = instruction[0]
    if action == 'mask':
        current_mask = instruction[1]
    elif action == 'mem':
        write_to_mem(current_mask, memory, instruction[1], instruction[2])

part1_total = sum([int(value, 2) for value in memory.values()])

print(f"""Part One: the sum of all values left in memory 
after the initialisation programme completed is {part1_total}.""")


# Part Two
memory_2 = {}
mask_two = 0
for instruction in my_instruction_copy:
    action = instruction[0]
    if action == 'mask':
        mask_two = instruction[1]
    elif action == 'mem':
        write_to_mem_two(mask_two, memory_2, instruction[1], instruction[2])

part2_total = sum([int(value, 2) for value in memory_2.values()])

print(f"""Part Two: the sum of all values left in memory 
after the initialisation programme completed is {part2_total}.""")