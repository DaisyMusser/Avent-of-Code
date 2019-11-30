# reads moves array and returns houses_visited 2D array
def translator(moves):
    houses_visited = []
    x = 0
    y = 0
    for i in range(len(moves)):
        if moves[i] == '>':
            x += 1
        if moves[i] == '<':
            x -= 1
        if moves[i] == '^':
            y += 1
        if moves[i] == 'v':
            y -= 1
        houses_visited.append([x, y])
    return houses_visited


# reads file into moves[]
def reader(file):
    with open(file) as fp:
        moves = fp.read()
    return moves


# returns count of unique houses visited (removes doubles)
def house_counter(houses_visited):
    # code adapted form ( https://stackoverflow.com/questions/31053385/get-a-set-of-2d-list-in-python )
    houses_visited = list(set(map(tuple, houses_visited)))
    return len(houses_visited)


# main program
moves = reader('input.txt')   # change here for different file names
houses_visited = translator(moves)
x = house_counter(houses_visited)
print(x)
