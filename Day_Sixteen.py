test_rules = {"class": [0, 1, 4, 19], "departure row": [0, 5, 8, 19], "departure seat": [0, 13, 16, 19]}
my_test_ticket = [11,12,13]
test_nearby_tickets = [[3,9,18], [15,1,5], [5,14,9]]

def load_ranges(ranges):
    with open(ranges) as r:
        rules = r.readlines()
        rules = [rule.replace('\n', '') for rule in rules]
        rules = [rule.split(': ') for rule in rules]
        rules = [(rule[0], rule[1].replace(' or ', '-')) for rule in rules]
        rules = [(rule[0], [int(x) for x in rule[1].split('-')]) for rule in rules]
        rule_dict = {}
        for rule in rules:
            rule_dict[rule[0]] = rule[1]
        
    return rule_dict


def load_nearby_tickets(ticket_collection):
    with open(ticket_collection) as t:
        tickets = t.readlines()
        tickets = [ticket.replace('\n', '') for ticket in tickets]
        tickets = [[int(x) for x in ticket.split(',')] for ticket in tickets]

    return tickets


def apply_rules(rules, value):
    invalid_fields = 0

    for rule in rules:
        if value < rule[0] or value > rule[3]:
            invalid_fields += 1
        if value > rule[1] and value < rule[2]:
            invalid_fields += 1

    if invalid_fields == len(rules):
        return False
    else:
        return True     
  

def validate_ticket(rules, ticket):
    ticket_error_rate = 0

    for ticket_value in ticket:
        validation = apply_rules(rules, ticket_value)
        if validation == False:
            ticket_error_rate += ticket_value

    return ticket_error_rate


""" Part Two """
    # function to take value and singular rule and return True or False
    # apply to all rules, count of True
    # if count of True == 1, record position of rule that works (dict field position: successful rule), remove it from rules and values list


def identify_successful_rule(this_rule, this_value):

    # if this_value < this_rule[0] or this_value > this_rule[3]:
    #     return False
    # if this_value > this_rule[1] and this_value < this_rule[2]:
    #     return False

    if this_value >= this_rule[0] and this_value <= this_rule[1]:
        return True
    if this_value >= this_rule[2] and this_value <= this_rule[3]:
        return True

    return False


def determine_impossible_positions(rules, tickets):

    impossible_positions = {}

    ticket_count = 0
    while ticket_count < len(tickets):
        value_position = 0
        for field_value in (tickets[ticket_count]):
            rule_validity = {}

            for each_field, each_range in rules.items():
                rule_validity[each_field] = identify_successful_rule(each_range, field_value)

            if False in rule_validity.values():
                for k, v in rule_validity.items():
                    if k not in impossible_positions:
                        impossible_positions[k] = set()
                    if v == False:
                        impossible_positions[k] |= set([value_position])
          
            value_position += 1
        ticket_count += 1

    return impossible_positions



my_rules = load_ranges('puzzle_inputs/Day_Sixteen_Rule_Ranges.txt')
nearby_tickets = load_nearby_tickets('puzzle_inputs/Day_Sixteen_Nearby_Tickets.txt')

error_total = 0
invalid_tickets = []
for each_ticket in nearby_tickets:
    ticket_validity = validate_ticket(my_rules.values(), each_ticket)
    if ticket_validity != 0:
        invalid_tickets.append(each_ticket)
        error_total += ticket_validity

print(f"Part One: Sum of values that are not valid for any field: {error_total}.")

valid_tickets = nearby_tickets[:]
for invalid_ticket in invalid_tickets:
    valid_tickets.remove(invalid_ticket)

imposs = determine_impossible_positions(my_rules, valid_tickets)
valid_positions = {k: set(range(0, 20)) for k in imposs.keys()}
valid_positions = {k: valid_positions[k].difference(imposs[k]) for k in valid_positions.keys()}
final_positions = {}

def has_nonunique_elements(a_dict):
    for k, v in a_dict.items():
        if len(v) > 1:
            return True
    
    return False

while has_nonunique_elements(valid_positions):
    for key, value in valid_positions.items():
        # if len(value) == 0 and key not in final_positions:
        #     raise Exception(f"invalid something: {key, value}")
        if len(value) == 1:
            confirmed = value.copy()
            final_positions[key] = confirmed
            for k in valid_positions.keys():
                valid_positions[k] -= confirmed

indexes = []

flat_indexes = [single.copy().pop() for single in final_positions.values()]

wanted_indexes = range(0, 20)
for i in wanted_indexes:
    if i not in flat_indexes:
        indexes.append(i)


for k, v in final_positions.items():
    if "departure" in k:
        indexes += v

my_ticket = [83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71]

product = 1
for i in indexes:
    product *= my_ticket[i]
print(product)