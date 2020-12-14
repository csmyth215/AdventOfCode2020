import sys
import copy

def load_file(filename):
    with open(filename) as f:
        my_lines = f.readlines()
        my_lines = [line.replace("\n", "").split(" ") for line in my_lines]
    return my_lines


def apply_an_instruction(operation, argument, accum_value, instruction_number):
    if operation == "acc":
        accum_value += argument
        instruction_number += 1
    elif operation == "jmp":
        instruction_number += argument
    elif operation == "nop":
        instruction_number += 1
    return accum_value, instruction_number


def apply_instructions(instruction_list):
    accum_value = 0
    values = []
    instruction_number = 0
    instruction_numbers = []
    instruction = "x"

    while True:
        if instruction_number in instruction_numbers:
            break
        instruction_numbers.append(instruction_number)
        instruction = instruction_list[instruction_number]
        accum_value, instruction_number = apply_an_instruction(instruction[0], int(instruction[1]), accum_value, instruction_number)
        values.append(accum_value)

    return accum_value


def check_termination(instruction_list):
    accum_value = 0
    values = []
    instruction_number = 0
    instruction_numbers = []
    
    while True:
        if instruction_number in instruction_numbers:
            return False, accum_value
        if instruction_number < 0 or instruction_number >= len(instruction_list) - 1:
            return True, accum_value
        instruction_numbers.append(instruction_number)
        instruction = instruction_list[instruction_number]
        accum_value, instruction_number = apply_an_instruction(instruction[0], int(instruction[1]), accum_value, instruction_number)
        values.append(accum_value)


def check_alternatives(instruction_list):
    for i in range(0, len(instruction_list)):
        if instruction_list[i][0] == 'jmp':
            copied_list = copy.deepcopy(instruction_list)
            copied_list[i][0] = 'nop'
            test = check_termination(copied_list)
            if test[0] is True:
                print(test[1])
                return
        if instruction_list[i][0] == 'nop':
            copied_list = copy.deepcopy(instruction_list)
            copied_list[i][0] = 'jmp'
            test = check_termination(copied_list)
            if test[0] is True:
                print(test[1])
                return
        

instructions = load_file("puzzle_inputs/Day_Eight_textfile.txt")
part_one = apply_instructions(instructions)
part_two = check_alternatives(instructions)