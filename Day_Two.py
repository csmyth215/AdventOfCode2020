import sys

def load_file(filename):
    with open(filename) as f:
        my_lines = f.readlines()
    return my_lines

lines = load_file("Day_Two_textfile.txt")
lines = [i.strip() for i in lines]
lines = [i.replace(':', '') for i in lines]
lines = [i.replace('-', ' ') for i in lines]

new_lines = []
for i in lines:
    x = i.split()
    new_lines.append(x)

first_valid_password_list = []

for j in new_lines:
    minimum = int(j[0])
    maximum = int(j[1])
    policy_letter = j[2]
    password = j[3]
    policy_letter_count = 0
    for k in range(0, len(password)):
        if password[k] == policy_letter:
            policy_letter_count += 1
    if policy_letter_count >= minimum and policy_letter_count <= maximum:
        first_valid_password_list.append(j)

second_valid_password_list = []

for l in new_lines:
    first_position = int(l[0])
    second_position = int(l[1])    
    policy_letter = l[2]
    password = l[3]
    first_position_letter = password[first_position - 1]
    second_position_letter = password[second_position - 1]
    if first_position_letter == policy_letter or second_position_letter == policy_letter:
        if first_position_letter == policy_letter and second_position_letter == policy_letter:
            continue
        else: 
            second_valid_password_list.append(l)


print(len(second_valid_password_list))




