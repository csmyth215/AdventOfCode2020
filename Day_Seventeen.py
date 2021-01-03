import copy

def load_textfile(my_puzzle_input):
    with open(my_puzzle_input) as f:
        two_d = f.readlines()
        two_d = [l.replace('\n', '') for l in two_d]
    return two_d


def create_structure(x_range, y_range, z_range):
    structure = {}
    for x in x_range:
        for y in y_range:
            for z in z_range:
                structure[(x, y, z)] = '.'
    return structure

def insert_initial_structure(my_input, empty_config):
    initial_length = len(my_input) 
    initial_width = len(my_input[0])

    y = 0
    while y < initial_length:
        x = 0
        while x < initial_width:
            initial_status = my_input[y][x]
            my_key = (x, y, 0)
            empty_config[my_key] = initial_status
            x += 1
        y += 1

    return empty_config


def cast_ray(config, origin, vector, dimension_ranges) -> bool:
    """ Returns true if cube is active """
    current_x, current_y, current_z = origin
        
    while True:
        current_x += vector[0]
        current_y += vector[1]
        current_z += vector[2]
        if (current_z not in dimension_ranges[2]) or (current_y not in dimension_ranges[1]) \
         or (current_x not in dimension_ranges[0]):
            return False
        if config[(current_x, current_y, current_z)] == '#':
            return True
        else:
            return False


def count_adjacent_active_cubes(config, current_position, dimension_ranges):
    directions = [(0, 1, 0), (0, 1, 1), (0, 1, -1),
    (-1, 1, 0), (-1, 1, 1), (-1, 1, -1),
    (-1, 0, 0), (-1, 0, 1), (-1, 0, -1),
    (-1, -1, 0), (-1, -1, 1), (-1, -1, -1),
    (0, -1, 0), (0, -1, 1), (0, -1, -1),
    (1, -1, 0), (1, -1, 1), (1, -1, -1),
    (1, 0, 0), (1, 0, 1), (1, 0, -1),
    (1, 1, 0), (1, 1, 1), (1, 1, -1),
    (0, 0, 1), (0, 0, -1)]
    
    active_cube_count = 0
    for direction in directions:
        if cast_ray(config, current_position, direction, dimension_ranges):
            active_cube_count += 1
    return active_cube_count


def update_status(cube, neighbours_active):
    if cube == "#":
        if neighbours_active == 2 or neighbours_active == 3:
            cube = '#'
        else:
            cube = '.'
    elif cube == '.':
        if neighbours_active == 3:
            cube = '#'
        else:
            cube = '.'

    return cube    


def update_config(config, dimension_ranges):
    new_config = copy.deepcopy(config)

    for z in dimension_ranges[2]:
        for y in dimension_ranges[1]:
            for x in dimension_ranges[0]:
                this_key = (x, y, z)
                active_neighbours = count_adjacent_active_cubes(config, this_key, dimension_ranges)
                current_char = config[this_key]
                new_char = update_status(current_char, active_neighbours)
                new_config[this_key] = new_char
    
    print(list(new_config.values()).count('#'))
    return new_config

def create_formatted_textfile(current_grid, stage):
    new_f = open(f'puzzle_inputs/Day_Seventeen_{stage}.txt', "w")
    for key, value in current_grid.items():
        my_string = f"{key}, {value}\n"
        new_f.write(my_string)
    new_f.close()


ultimate_width = 8
ultimate_length = 8
ultimate_depth = 6

ultimate_ranges = []

ultimate_x_range = range(-6, 15)
ultimate_y_range = range(-6, 15)
ultimate_z_range = range(-6, 7)

ultimate_ranges.append(ultimate_x_range)
ultimate_ranges.append(ultimate_y_range)
ultimate_ranges.append(ultimate_z_range)

test_width = 3
test_length = 3
test_depth = 2

test_ranges = []

test_x_range = range((-test_width), (test_width+1))
test_y_range = range((-test_length), (test_length+1))
test_z_range = range((-test_depth), (test_depth+1))

test_ranges.append(test_x_range)
test_ranges.append(test_y_range)
test_ranges.append(test_z_range)

initial_layer = load_textfile('puzzle_inputs/Day_Seventeen_textfile.txt')
starting_config = create_structure(ultimate_x_range, ultimate_y_range, ultimate_z_range)
starting_grid = insert_initial_structure(initial_layer, starting_config)

print(list(starting_grid.values()).count('#'))
cycle = update_config(starting_grid, ultimate_ranges)
for i in range(0, 5):
    cycle = update_config(cycle, ultimate_ranges)