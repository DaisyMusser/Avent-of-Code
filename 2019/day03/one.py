# reads file into array
def file_reader(file_name):
    directions = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            directions.append(line)
    return directions


# splits directions around commas
def formatter(directions):
    for i in range(2):
        directions[i] = directions[i].split(',')
    return directions


# turns directions into a list of locations describing the paths of the two wires
def path_finder(directions):
    green_path = []
    red_path = []

    green = [0, 0]
    for i in range(len(directions[0])):    # have to deal with last el specail
        if directions[0][i][len(directions[0][i])-1] != 'n':
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
        if directions[1][i][len(directions[1][i]) - 1] != 'n':
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


# main program
directions = file_reader('input.txt')    # change here for different file names
directions = formatter(directions)

red_path, green_path = path_finder(directions)
x = 0
for i in range(len(red_path)//2):
    print(red_path[x], ' ', red_path[x+1])
    x += 2
