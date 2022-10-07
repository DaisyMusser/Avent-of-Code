
file = open("input.txt", "r")
data = file.read()
floor = 0
for i, move in enumerate(data):
    if move == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(str(i + 1))
        break
print(floor)

