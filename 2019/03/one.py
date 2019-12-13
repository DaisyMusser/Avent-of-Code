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

    green = [0, 0]
    x = green[0]
    y = green[1]
    green_directions = directions[0]
    for inst in green_directions:        # have to deal with last specail
        if inst[len(inst)-1] != 'n':     # if not at last inst
            if directions[0][i][0] == 'R':
                green[0] += int(directions[0][i][1:len(directions[0][i])])
            elif directions[0][i][0] == 'U':
                green[1] += int(directions[0][i][1:len(directions[0][i])])
            elif directions[0][i][0] == 'L':
                green[0] -= int(directions[0][i][1:len(directions[0][i])])
            elif directions[0][i][0] == 'D':
                green[1] -= int(directions[0][i][1:len(directions[0][i])])
            green_path.append(green[0])
            green_path.append(green[1])
        else:
            break

    red = [0, 0]
    for i in range(len(directions[1])):
        if directions[1][i][len(directions[1][i]) - 1] != 'n':        # so much easier jesus christ
            if directions[1][i][0] == 'R':
                red[0] += int(directions[1][i][1:len(directions[1][i])])
            elif directions[1][i][0] == 'U':
                red[1] += int(directions[1][i][1:len(directions[1][i])])
            elif directions[1][i][0] == 'L':
                red[0] -= int(directions[1][i][1:len(directions[1][i])])
            elif directions[1][i][0] == 'D':
                red[1] -= int(directions[1][i][1:len(directions[1][i])])
            red_path.append(red[0])
            red_path.append(red[1])
        else:
            break

    return red_path, green_path


# finds the gaps between two spots
def baby_fill(two_spots):
    old_x = two_spots[0]     # this is totally nuts but i'm bad at reading code so i need it
    old_y = two_spots[1]
    new_x = two_spots[2]
    new_y = two_spots[3]

    if old_x != new_x:

        difference = abs(old_x - new_x)

        if old_x > new_x:
            counter = 1
            for i in range(difference-1):
                gaps = [old_x-counter, old_y]
                counter += 1

        elif old_x < new_x:
            counter = 1
            for i in range(difference-1):
                gaps = [old_x+counter, old_y]
                counter += 1

    elif old_y != new_y:

        difference = abs(old_y - new_y)

        if old_y > new_y:
            counter = 1
            for i in range(difference - 1):
                gaps = [old_x, old_y - counter]
                counter += 1

        elif old_y < new_y:
            counter = 1
            for i in range(difference - 1):
                gaps = [old_x, old_y + counter]
                counter += 1

    return gaps


def teen_fill(path, baby_fill):
    all_gaps = []
    counter = 0
    for i in range((len(path)//2)-1):
        two_spots = path[counter:counter+4]       # remember +4 because ranges need to go one further
        for i in range(2):
            all_gaps.append(baby_fill(two_spots)[i])
        counter += 2
    return all_gaps


# needs to fill the gaps in red and green wire paths
def grown_ass_man_fill(green_path, red_path, teen_fill, baby_fill):

    all_green_gaps = teen_fill(green_path, baby_fill)
    print(all_green_gaps)
    #for i in range(len(all_green_gaps)):
    #    green_path.append(all_green_gaps[i])

    all_red_gaps = teen_fill(red_path, baby_fill)
    print(all_red_gaps)
    #for i in range(len(all_red_gaps)):
    #    red_path.append(all_red_gaps[i])

    return red_path, green_path


# find the intersections between red and green wires
def spot_checker(red_path, green_path):
    intersections = []
    x = 0
    for i in range(len(red_path)//2):
        y = 0
        for ii in range(len(green_path)//2):
            if green_path[y] == red_path[x]:
                if green_path[y+1] == red_path[x+1]:
                    loc = [green_path[y], green_path[y+1]]
                    intersections.append(loc)
            y += 2
        x += 2
    return intersections


# main program
directions = file_reader('input.txt')    # change here for different file names
directions = formatter(directions)
print(directions)

# red_path, green_path = path_finder(directions)
# red_path, green_path = grown_ass_man_fill(green_path, red_path, teen_fill, baby_fill)

# intersections = spot_checker(red_path, green_path)


