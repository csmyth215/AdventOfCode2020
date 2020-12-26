import copy

def load_textfile(filename):
    with open(filename) as f:
        my_lines = f.readlines()
        my_lines = [i.replace('\n', '') for i in my_lines]
    return my_lines

def get_adjacent_addresses(grid_width, grid_length, seat_address):
    addresses = []
    y = seat_address[0]
    x = seat_address[1]

    if y - 1 >= 0:
        addresses.append((y - 1, x))
        if x - 1 >= 0:
            addresses.append((y - 1, x - 1))
        if x + 1 < grid_width:
            addresses.append((y - 1, x + 1))
    
    if y + 1 < grid_length:
        addresses.append((y + 1, x))
        if x - 1 >= 0:
            addresses.append((y + 1, x - 1))
        if x + 1 < grid_width:
            addresses.append((y + 1, x + 1))
    
    if x - 1 >= 0:
        addresses.append((y, x - 1))
    if x + 1 < grid_width:
        addresses.append((y, x + 1))

    return(addresses)

def count_adjacent_occupied_seats(my_seats, seat_list):
    occupied_seat_count = 0
    for y, x in seat_list:
        if my_seats[y][x] == "#":
            occupied_seat_count += 1

    return occupied_seat_count

def count_visible_occupied_seats(seats, seat_list, current_position):
    """Subsequently improved/rewritten/refactored as "cast rays" function"""
    visible = []
    grid_width_across = len(seats[0])
    grid_length_down = len(seats)
    
    for y, x in seat_list:
        relative_y = y - current_position[0]
        relative_x = x - current_position[1]
      
        visible_status = False

        while visible_status == False:

            if seats[y][x]== '#':
                visible.append('#')
                visible_status = True
            
            elif seats[y][x] == 'L':
                visible.append('L')
                visible_status = True

            elif seats[y][x] == '.':
            
                if relative_y == 0:
                    if relative_x > 0:
                        i = 1
                        while (x + i) < grid_width_across:
                            if seats[y][(x + i)] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y][x + i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1


                    else:
                        i = 1
                        while x - i >= 0:
                            if seats[y][x - i] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y][x - i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1


                elif relative_x == 0:
                    if relative_y > 0: 
                        i = 1
                        while y + i < grid_length_down:
                            if seats[y + i][x] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y + i][x] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1

                    else:
                        i = 1
                        while y - i >= 0:
                            if seats[y - i][x] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y - i][x] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1


                elif relative_x > 0:
                    if relative_y > 0:
                        i = 1
                        while y + i < grid_length_down:
                            if seats[y + i][x + i] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y + i][x + i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1

                    else:
                        i = 1
                        while y - i >= 0:
                            if seats[y - i][x + i] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y - i][x + i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1

                
                elif relative_x < 0:
                    if relative_y < 0:
                        i = 1
                        while x - i >= 0:
                            if seats[y - i][x - i] == 'L':
                                visible.append('L')
                                visible_status = True
                                break                      
                            if seats[y - i][x - i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1

                    else:
                        i = 1
                        while x - i >= 0:
                            if seats[y + i][x - i] == 'L':
                                visible.append('L')
                                visible_status = True
                                break
                            if seats[y + i][x - i] == '#':
                                visible.append('#')
                                visible_status = True
                                break
                            else:
                                i += 1
                

            else:
                break

    return visible.count('#')

def cast_ray(seats, origin, vector) -> bool:
    current_y, current_x = origin
        
    while True:
        current_y += vector[0]
        current_x += vector[1]
        if (current_y >= len(seats)) or (current_x >= len(seats[0])) \
            or (current_y < 0) or (current_x < 0):
            return False
        if seats[current_y][current_x]== '#':
            return True
        if seats[current_y][current_x]== 'L':
            return False

def visible_occupied_seats(seats, origin):
    directions = [(0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    visible = 0
    for direction in directions:
        if cast_ray(seats, origin, direction):
            visible += 1
    return visible


def determine_new_occupied_status(seat_collection, seat_y, seat_x, n_visibly_occupied):
    status = seat_collection[seat_y][seat_x]

    if status == 'L' and n_visibly_occupied == 0:
        status = '#'    
    if status == '#' and n_visibly_occupied >= 5:
        status =  'L'
    
    return status

def update_grid(seat_grid):
    grid_string = '-'.join(seat_grid)
    grid_width_across = len(seat_grid[0])
    grid_length_down = len(seat_grid)
    new_seat_grid = copy.deepcopy(seat_grid)
    y = 0
    for seat_row in seat_grid:
        x = 0
        new_seat_row = copy.deepcopy(seat_row)
        for seat in seat_row:
            
            # adjacent_addresses = get_adjacent_addresses(grid_width_across, grid_length_down, (y, x))
            # adjacent_occupied = count_adjacent_occupied_seats(seat_grid, adjacent_addresses)
            # n_visibly_occupied = count_visible_occupied_seats(seat_grid, adjacent_addresses, (y, x))

            n_visibly_occupied = visible_occupied_seats(seat_grid,(y, x))
            # new_seat = determine_new_occupied_status(seat_grid, y, x, adjacent_occupied)
            new_seat = determine_new_occupied_status(seat_grid, y, x, n_visibly_occupied)
            new_seat_row = new_seat_row[:x] + new_seat + new_seat_row[x+1:]
            
            x += 1
        new_seat_grid[y] = new_seat_row

        y += 1

    
    refreshed_grid_string = '-'.join(new_seat_grid)

    if refreshed_grid_string == grid_string:
        occupied = '#'
        occupied_count = 0
        for char in refreshed_grid_string:
            if char == occupied:
                occupied_count += 1
        print(f"There are {occupied_count} occupied seats when seats stop changing.")
        return True

    else: 
        refreshed_grid_string = update_grid(new_seat_grid)
        
initial_seating_grid = load_textfile("puzzle_inputs/Day_Eleven_textfile.txt")
part_one = update_grid(initial_seating_grid)