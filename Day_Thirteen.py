def load_file(textfile):
    with open(textfile) as f:
        file_lines = f.readlines()
        running_buses = [int(bus) for bus in file_lines[1].split(',') if bus != 'x']
    return (int(file_lines[0].strip()), running_buses)


def waiting_time(start, min_multiplier, bus_id):
    multiplier = min_multiplier
    while True:
        product = bus_id * multiplier
        if product >= start:
            return (product - start)
        else:
            multiplier += 1


departure, buses = load_file('puzzle_inputs/Day_Thirteen_textfile.txt')
min_journeys_undertaken = int(departure / max(buses)) - 1

best_bus = 0
min_wait = 0

for bus in buses:
    this_waiting_time = waiting_time(departure, min_journeys_undertaken, bus)
    if min_wait == 0:
        best_bus == bus
        min_wait = this_waiting_time
    else:
        if this_waiting_time < min_wait:
            best_bus = bus
            min_wait = this_waiting_time
        

print(f"The ID of the earliest bus ({best_bus}) multiplied by minutes to wait ({min_wait}) is {best_bus * min_wait}.")