# day 03: manhattan distance and crossed wires

# reads file into one string:      ['R1000,D940,L143, ... D182']
def file_reader(file_name):
    directions = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:           # little bit of error checking
                break
            directions.append(line)
    return directions


# splits directions around commas: ['L668', 'D443', 'R705', ... 'D793']
def formatter(directions):
    #directions = list(directions)
    for i in range(2):
        directions[i] = directions[i].split(',')
    for i in range(2):
        for ii in range(len(directions[i])):
            directions[i][ii] = directions[i][ii].strip()   # strips off \n
    return directions


# turns directions into a list of locations describing the paths of the two wires
def path_finder(directions):
    green_path = []
    red_path = []

    # fills green_path with all the corners of the green path
    green = [0, 0]
    x = green[0]     # symbolic
    y = green[1]
    green_directions = directions[0]
    for inst in green_directions:
        value = int(inst[1:len(inst)])   # symbolic again
        if inst[0] == 'R':
            x += value
        elif inst[0] == 'U':
            y += value
        elif inst[0] == 'L':
            x -= value
        elif inst[0] == 'D':
            y -= value
        green_path.append([x, y])

    # fills red_path with all the corner of the red path
    red = [0, 0]
    x = red[0]
    y = red[1]
    red_directions = directions[1]
    for inst in red_directions:
        value = int(inst[1:len(inst)])
        if inst[0] == 'R':
            x += value
        elif inst[0] == 'U':
            y += value
        elif inst[0] == 'L':
            x -= value
        elif inst[0] == 'D':
            y -= value
        red_path.append([x, y])

    return red_path, green_path


# returns the gaps between two spots
def find_single_gap(old_spot, new_spot):
    gaps = []

    old_x = old_spot[0]     # symbolic
    old_y = old_spot[1]
    new_x = new_spot[0]
    new_y = new_spot[1]

    if old_x != new_x:
        difference = abs(old_x - new_x)
        if old_x > new_x:
            for i in range(difference):
                gaps.append([old_x - i, old_y])
        elif old_x < new_x:
            for i in range(difference):
                gaps.append([old_x + i, old_y])
    elif old_y != new_y:
        difference = abs(old_y - new_y)
        if old_y > new_y:
            for i in range(difference):
                gaps.append([old_x, old_y - i])
        elif old_y < new_y:
            for i in range(difference):
                gaps.append([old_x, old_y + i])

    return gaps


# returns path with all gaps filled
def find_all_gaps(path):
    all_gaps = []
    for i in range(len(path) - 1):
        gaps = find_single_gap(path[i], path[i + 1])
        for xy in gaps:
            all_gaps.append(xy)
    for xy in all_gaps:
        path.append(xy)
    return path


# find the intersections between red and green wires
def spot_checker(red_path, green_path):
    r_set = set()
    g_set = set()
    for xy in red_path:
        r_set.add(tuple(xy))
    for xy in green_path:
        g_set.add(tuple(xy))
    intersections = g_set.intersection(r_set)
    return intersections


def path_sorter(path):


# checks relative length
def rel_length_checker(xy):
    return


# main program
# file io / formatting
directions = file_reader('input.txt')    # change here for different file names
directions = formatter(directions)

# converts directions into all red and green corners
red_path, green_path = path_finder(directions)

# fills gaps of red and green paths
red_path = find_all_gaps(red_path)
green_path = find_all_gaps(green_path)

# finds intersections
intersections = spot_checker(red_path, green_path)

