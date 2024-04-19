def find_treasure(file_name):
    with open(file_name, 'r') as f:
        directions = f.read().split(', ')

    x, y = 0, 0
    dx, dy = 0, 1  # initial direction is up

    for direction in directions:
        turn, distance = direction[0], int(direction[1:])
        if turn == 'R':
            dx, dy = dy, -dx
        elif turn == 'L':
            dx, dy = -dy, dx

        x += dx * distance
        y += dy * distance

    return x, y

print(find_treasure('treasure_hunt.txt'))  # replace 'your_file.txt' with your actual file name
