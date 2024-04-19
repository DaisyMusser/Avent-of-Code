def find_treasure(file_name):
    x, y = 0, 0
    direction = (0, 1)  # Initial direction is up the positive y axis

    with open(file_name, 'r') as f:
        directions = f.read().split(', ')

    for direction in directions:
        turn, distance = direction[0], int(direction[1:])
        print(turn)
        print(distance)
        if turn == 'R':
            direction = (-direction[1], direction[0])  # Rotate 90 degrees to the right
        elif turn == 'L':
            direction = (direction[1], -direction[0])  # Rotate 90 degrees to the left
        x += direction[0] * distance
        y += direction[1] * distance

    return x, y

print(find_treasure('treasure_hunt.txt'))  # Replace 'treasure_hunt.txt' with your file name
