# reads moves array (as santa) and returns houses_visited 2D array
def human_translator(moves):
    human_houses_visited = []
    x = 0
    y = 0
    for i in range(len(moves)):
        index = 0
        if moves[index] == '>':
            x += 1
        if moves[index] == '<':
            x -= 1
        if moves[index] == '^':
            y += 1
        if moves[index] == 'v':
            y -= 1
        index += 2
        human_houses_visited.append([x, y])
    return human_houses_visited


# reads moves array (as robo-santa) and returns houses_visited 2d array
def robo_translator(moves):
    robo_houses_visited = []
    x = 0
    y = 0
    for i in range(len(moves)):
        index = 1
        if moves[index] == '>':
            x += 1
        if moves[index] == '<':
            x -= 1
        if moves[index] == '^':
            y += 1
        if moves[index] == 'v':
            y -= 1
        index += 2
        robo_houses_visited.append([x, y])
    return robo_houses_visited


# reads file into moves[]
def reader(file):
    with open(file) as fp:
        moves = fp.read()
    return moves


# returns count of unique houses visited (removes doubles)
def house_counter(human_houses_visited, robo_houses_visited):
    # code adapted form ( https://stackoverflow.com/questions/31053385/get-a-set-of-2d-list-in-python )
    human_houses_visited = list(set(map(tuple, human_houses_visited)))
    robo_houses_visited = list(set(map(tuple, robo_houses_visited)))
    total_houses_visited = human_houses_visited.union(robo_houses_visited)
    return len(total_houses_visited)


# main program
moves = reader('input.txt')   # change here for different file names

human_houses_visited = human_translator(moves)
robo_houses_visited = robo_translator(moves)

print(house_counter(human_houses_visited, robo_houses_visited))


