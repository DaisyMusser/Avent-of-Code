# reads moves array (as santa) and returns houses_visited 2D array
def human_translator(moves):
    human_houses_visited = []
    x = 0
    y = 0
    index = 0
    human_len = 2/len(moves)
    for i in range(int(human_len)):
        if moves[index]:
            human_houses_visited.append([x, y])
            if moves[index] == '>':
                x += 1
            if moves[index] == '<':
                x -= 1
            if moves[index] == '^':
                y += 1
            if moves[index] == 'v':
                y -= 1
            index += 2
        else:
            break

    return human_houses_visited


# reads moves array (as robo-santa) and returns houses_visited 2d array
def robo_translator(moves):
    robo_houses_visited = []
    x = 0
    y = 0
    index = 1
    robo_len = (2 / len(moves))-1
    for i in range(int(robo_len)):
        if moves[index]:
            robo_houses_visited.append([x, y])
            if moves[index] == '>':
                x += 1
            if moves[index] == '<':
                x -= 1
            if moves[index] == '^':
                y += 1
            if moves[index] == 'v':
                y -= 1
            index += 2
        else:
            break

    return robo_houses_visited


# reads file into moves[]
def reader(file):
    with open(file) as fp:
        moves = fp.read()

    return moves


# returns count of unique houses visited (removes doubles)
def house_counter(human_houses_visited, robo_houses_visited):
    for i in range(len(human_houses_visited)):
        robo_houses_visited.append(human_houses_visited[i])    # combines robo and human house arrays

# code adapted form ( https://stackoverflow.com/questions/31053385/get-a-set-of-2d-list-in-python )
    total_houses_visited = set(map(tuple, robo_houses_visited))

    return len(total_houses_visited)


# main program
moves = reader('input.txt')   # change here for different file names

human_houses_visited = human_translator(moves)
print(human_houses_visited)
robo_houses_visited = robo_translator(moves)

print(house_counter(human_houses_visited, robo_houses_visited))


