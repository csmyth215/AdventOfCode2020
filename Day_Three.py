import sys

def load_file(filename):
    with open(filename) as f:
        my_lines = f.readlines()
    return my_lines

def count_trees(grid, x_change, y_change):
    x = 0
    y = 0
    contacted = []
    string_length = len(grid[0])
    for i in grid:
        if y > len(grid) - 1:
            break
        contact_item = grid[y][x % string_length]
        contacted.append(contact_item)
        x += x_change
        y += y_change
    tree_count = contacted.count("#")
    return tree_count

lines = load_file("Day_Three_textfile.txt")
lines = [i.strip() for i in lines]

# # Part 1
# ## 3 right, 1 down
first_route = count_trees(lines, 3, 1)

# # Part 2
# ## 1 right, 1 down
a = count_trees(lines, 1, 1)

# ## 3 right, 1 down
b = first_route

# ## 5 right, 1 down
c = count_trees(lines, 5, 1)

# ## 7 right, 1 down
d = count_trees(lines, 7, 1)

# ## 1 right, 2 down
e = count_trees(lines, 1, 2)

# ##Take product
second_answer = a * b * c * d * e
print(a, b, c, d, e)
print(second_answer)