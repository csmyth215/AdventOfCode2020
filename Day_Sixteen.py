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


my_rules = load_ranges('puzzle_inputs/Day_Sixteen_Rule_Ranges.txt')
nearby_tickets = load_nearby_tickets('puzzle_inputs/Day_Sixteen_Nearby_Tickets.txt')

error_total = 0
for each_ticket in nearby_tickets:
    ticket_validity = validate_ticket(my_rules.values(), each_ticket)
    error_total += ticket_validity

print(f"Part One: Sum of values that are not valid for any field: {error_total}.")