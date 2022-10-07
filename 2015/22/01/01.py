
file = open("input.txt", "r")
data = file.read()
floor = 0
for move in data:
    if move == "(":
        floor += 1
    else:
        floor -= 1
print(floor)

