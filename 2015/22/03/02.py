
dic = {(0, 0): 1}
santa  = [0, 0]
robo   = [0, 0]

data = open("input.txt").read()
roboturn = True
for move in data:
    if roboturn:
        if move == ">":
            robo[0] += 1
        elif move == "<":
            robo[0] -= 1
        elif move == "^":
            robo[1] += 1
        else:
            robo[1] -= 1
        house = (robo[0], robo[1])
    else:
        if move == ">":
            santa[0] += 1
        elif move == "<":
            santa[0] -= 1
        elif move == "^":
            santa[1] += 1
        else:
            santa[1] -= 1
        house = (santa[0], santa[1])
    if house in dic.keys():
        dic[house] += 1
    else:
        dic[house] = 1
    roboturn = not roboturn
atleastone = [i for i in dic.keys() if dic[i] >= 1]
print(len(atleastone))

