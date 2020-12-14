def loadfile(filename):
    with open(filename) as f:
        numbers = f.readlines()
        numbers = [int(number.replace('\n', '')) for number in numbers]
    return numbers


def validate_sum(number, numbers, start_position, end_position):
    test_range = numbers[start_position:end_position]
    for i in test_range:
        count = 1
        while count < len(test_range):
            b = test_range[count]
            total = i + b
            if total == number:
                return True
            else:
                count += 1
    return False


def validate_numbers(number_list):
    start = 0
    end = 25
    for i in number_list[25:]:
        validity = validate_sum(i, number_list, start, end)
        if validity == False:
            return i
        start += 1
        end += 1


def find_contiguous_set(target_number, list_of_numbers):
    remaining_list_length = len(list_of_numbers)
    start = 0
    for i in list_of_numbers:
        count = 1
        running_total = i
        total_components = [i, ]
        while count < remaining_list_length:
            b = list_of_numbers[start:][count]
            running_total += b
            total_components.append(b)
            if running_total == target_number:
                return total_components
            else:
                count += 1
        remaining_list_length -= 1
        start += 1


transmissions = loadfile('puzzle_inputs/Day_Nine_textfile.txt')
first_answer = validate_numbers(transmissions)
contiguous_set = find_contiguous_set(first_answer, transmissions)
encrytion_weakness = min(contiguous_set) + max(contiguous_set)
print(encrytion_weakness)