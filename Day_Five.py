import sys

def load_file(textfile):
    with open(textfile) as f:
        seats = f.readlines()
    return seats

def determine_row(seat_specification):
    section_front = 0
    section_back = 127
    partitioners = [2, 4, 8, 16, 32, 64, 128]
    count = 0
    for letter in seat_specification[:7]:
        if letter == 'F':
            section_back = int(section_front + (128 / partitioners[count] - 1))
        if letter == 'B':
            section_front = int(section_front + (128 / partitioners[count]))
        count += 1
    if section_front != section_back:
        print("We have a problem")
    return section_front

def determine_column(seat_specification):
    lower_column = 0
    upper_column = 7
    partitioners = [2, 4, 8]
    count = 0
    for letter in seat_specification[7:]:
        if count < 2:
            if letter == 'L':
                upper_column = int(lower_column + (8 / partitioners[count]) - 1)
            if letter == 'R':
                lower_column = int(lower_column + (8 / partitioners[count]))
            count += 1
        else:
            if letter == 'L':
                column = min(lower_column, upper_column)
            if letter == 'R':
                column = max(lower_column, upper_column)
    return column

def determine_seat_ID(this_seat):
    x = determine_row(this_seat)
    y = determine_column(this_seat)
    seat_id = x * 8 + y
    return (seat_id, x, y)

def determine_highest_seat_ID(specifications):
    return max([determine_seat_ID(seat)[0] for seat in specifications])

def list_seat_ids(specifications):
    return [determine_seat_ID(seat) for seat in specifications]   

def list_to_dict(seats_info):
    seats_dict = {}
    for (i, x, y) in seats_info:
        if x not in seats_dict.keys():
            seats_dict[x] = y
        elif type(seats_dict[x]) == list:
            seats_dict[x].append(y)
        else:
            seats_dict[x] = [seats_dict[x], y]
    return seats_dict

### ID (result of x * 8 + y calculation) important; not just coordinates themselves!
# Need to sort seat_ids, determine gap of 2, determine max of very front and very back IDs?        


seat_positions = load_file("puzzle_inputs\Day_Five_textfile.txt")
seat_positions = [seat.strip() for seat in seat_positions]
first_answer = determine_highest_seat_ID(seat_positions)

seat_info = list_seat_ids(seat_positions)
seat_ids = sorted([seat[0] for seat in seat_info])
empty_seat_contenders = []
for i in seat_ids:
    x = i + 1
    y = i - 1
    if x not in seat_ids:
        empty_seat_contenders.append(x)
    if y not in seat_ids:
        empty_seat_contenders.append(y)
print(empty_seat_contenders)


#seats_dictionary = list_to_dict(seat_ids[1:])
