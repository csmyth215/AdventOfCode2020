import sys

def load_file(filename):
    with open(filename) as f:
        my_lines = f.read()
        my_lines = my_lines.replace("\r", "")
        my_lines = my_lines.split("\n\n")
        my_lines = [i.replace("\n", " ") for i in my_lines]
    return my_lines

def format_lines(lines):
    passports = []
    for i in lines:
        fields = {}
        elements = i.split(" ")
        for element in elements:
            key_value_pair = element.split(":")
            key = key_value_pair[0]
            value = key_value_pair[1]
            fields[key] = value
        passports.append(fields)
    return passports

def validate_passport(information):
    all_required_fields = []
    valid_passport_count = 0
    for passport in information:
        field_count = len(passport)
        if field_count == 8:
            all_required_fields.append(passport)
            valid_passport_count += 1
        if field_count == 7:
            if 'cid' not in passport.keys():
                all_required_fields.append(passport)
                valid_passport_count += 1

    return all_required_fields, valid_passport_count    


def validate_year(abc):
    n_digits = len(abc)
    if n_digits != 4:
        return False
    return True


def validate_height(abc):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    unit = abc[-2:]
    if unit not in ["cm", "in"]:
        return False
    magnitude = int(abc[:-2])
    if unit == "cm":
        if magnitude < 150 or magnitude > 193:
            return False
    if unit == "in":
        if magnitude < 59 or magnitude > 76:
            return False
    return True


def validate_hair(abc):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    abc = str(abc)
    initialiser = abc[0]
    characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    if initialiser != "#" or len(abc) != 7:
        return False
    for i in abc[1:]:
        if i not in characters:
            return False
    return True


def validate_eye(abc):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if len(abc) != 3 or abc not in colours:
        return False
    return True


def validate_passport_id(abc):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    string_value = len(str(abc))
    if string_value != 9:
        return False
    try:
        int(abc)
    except ValueError:
        return False
    return True


def validate_all_fields(passport):
    for key, value in passport.items():
        if key == "byr":
            # byr (Birth Year) - four digits; at least 1920 and at most 2002.
            if not validate_year(value):
                return False
            if int(value) < 1920 or int(value) > 2002:
                return False
        elif key == "iyr":
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            if not validate_year(value):
                return False
            if int(value) < 2010 or int(value) > 2020:
                return False
        elif key == "eyr":                        
            # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
            if not validate_year(value):
                return False
            if int(value) < 2020 or int(value) > 2030:
                return False
        elif key == "hgt":
            if not validate_height(value):
                return False
        elif key == "hcl":
            if not validate_hair(value):
                return False
        elif key == "ecl":
            if not validate_eye(value):
                return False
        elif key == 'pid':
            if not validate_passport_id(value):
                return False
    return True

def second_validation(candidate_passports):
    return [candidate for candidate in candidate_passports if validate_all_fields(candidate)] 

my_text = load_file("Day_Four_textfile.txt")
passport_list = format_lines(my_text)
first_validation = validate_passport(passport_list)
first_valid_count = first_validation[1]
second_validated_data = second_validation(first_validation[0])
for i in second_validated_data:
    print(i['pid'])
print(len(second_validated_data))