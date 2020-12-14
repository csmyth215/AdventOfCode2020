import re

def is_number(text):
    try:
        a = int(text)
        return True
    except ValueError:
        return False

def load_file(filename):
    with open(filename) as f:
        my_lines = f.readlines()
        my_lines = [line.replace("\n", "") for line in my_lines]
        my_lines = [line.replace(".", "") for line in my_lines]
        my_lines = [line.replace("bags", "").strip() for line in my_lines]
        my_lines = [line.replace("bag", "").strip() for line in my_lines]
        my_dict = {}
        for line in my_lines:
            bags = [l.strip() for l in line.split("contain")]
            outer_bag = bags[0]
            inner_bags = [bag.strip() for bag in bags[1].split(',')]
            inner_bags = [re.sub("^\d+ ", "", i) for i in inner_bags]
            my_dict[outer_bag] = inner_bags
    return my_dict

def load_file_two(filename):
    with open(filename) as f:
        my_lines = f.readlines()
        my_lines = [line.replace("\n", "") for line in my_lines]
        my_lines = [line.replace(".", "") for line in my_lines]
        my_lines = [line.replace("bags", "").strip() for line in my_lines]
        my_lines = [line.replace("bag", "").strip() for line in my_lines]
        my_dict = {}
        for line in my_lines:
            bags = [l.strip() for l in line.split("contain")]
            outer_bag = bags[0]
            inner_bags = [bag.strip() for bag in bags[1].split(',')]
            inner_bags_expanded = []
            for inner_bag in inner_bags:
                if "no other" in inner_bag:
                    inner_bags_expanded.append(inner_bag)
                else:
                    instances_adj_colour = [x.strip() for x in inner_bag.split(' ')]
                    instances = int(instances_adj_colour[0])
                    adj_colour = re.sub("^\d+ ", "", inner_bag)
                    count = 0
                    while count < instances:
                        inner_bags_expanded.append(adj_colour)
                        count += 1
            my_dict[outer_bag] = inner_bags_expanded
    return my_dict



def containing_bags(target_bag, all_bags):
    if "no other" in all_bags[target_bag]:
        return set([])        

    target_set = set(all_bags[target_bag])
    for bag in all_bags[target_bag]:
        target_set |= containing_bags(bag, all_bags)

    return target_set


def get_shiny_gold_contents(target_bag, all_bags):
    if "no other" in all_bags[target_bag]:
        return []

    target_contents = list(all_bags[target_bag])
    for bag in all_bags[target_bag]:
        target_contents += get_shiny_gold_contents(bag, all_bags)
    
    return target_contents

bag_contents_two = load_file_two("puzzle_inputs/Day_Seven_textfile.txt")
shiny_contents = get_shiny_gold_contents("shiny gold", bag_contents_two)
print(len(shiny_contents))

# bag_contents = load_file("puzzle_inputs/Day_Seven_textfile.txt")

# bag_children = {}
# count = 0
# for key in bag_contents.keys():
#     bag_children[key] = containing_bags(key, bag_contents)

# for key in bag_children.keys():
#     if "shiny gold" in bag_children[key]:
#         count += 1
# print(count)