def find_treasure(file_name):
    with open(file_name, 'r') as f:
        directions = f.read().split(', ')

    x, y = 0, 0
    dx, dy = 0, 1  # initial direction is up
    visited = set()
    visited.add((x, y))  # add the starting point to the visited set

    for direction in directions:
        turn, distance = direction[0], int(direction[1:])
        if turn == 'R':
            dx, dy = dy, -dx
        elif turn == 'L':
            dx, dy = -dy, dx

        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in visited:
                return x, y
            visited.add((x, y))

    return None  # if no intersection is found

print(find_treasure('input.txt'))  # replace 'your_file.txt' with your actual file name
