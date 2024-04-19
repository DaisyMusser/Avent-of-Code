def find_treasure(file_name):
    with open(file_name, 'r') as f:
        directions = f.read().split(', ')

    x, y = 0, 0
    dx, dy = 0, 1  # initial direction is up
    visited = set()
    path = [(0, 0)]

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
            path.append((x, y))

    return None

print(find_treasure("treasure_hunt.txt"))
