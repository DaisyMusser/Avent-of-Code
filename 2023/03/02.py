import re

"""
Given an index(x, y) and line length, determines if index will be out of 
bounds or not
"""
def inBounds(index, l) -> bool:
    x = index[0]
    y = index[1]
    if x > -1:
        if y > -1:
            if x < l:
                if y < l:
                    return True
    return False 

"""
Give a range of indices and len of line, returns all the neighbooring 
indices we want to check
"""
def getNeighborIndices(x, y_start, y_end, l) -> list[(int, int)]:
    # top row above the target
    neighbors = [(x - 1, y) for y in range(y_start - 1, y_end + 2) if inBounds((x - 1, y), l)]
    # index in from of target in line
    if inBounds((x, y_start - 1), l):
        neighbors.append((x, y_start - 1))
    # index behind target in line
    if inBounds((x, y_end + 1), l):
        neighbors.append((x, y_end   + 1))
    # row below the target
    neighbors += [(x + 1, y) for y in range(y_start - 1, y_end + 2) if inBounds((x + 1, y), l)]
    return neighbors

"""
Given the index of a digit and the line it's in, returns 
the full number digit belongs to, and list of all indices 
number takes up
"""
def getNumber(i, x, line):
    str_num = line[i]
    indices = [(x, i)]
    # search right
    j = i
    while True:
        j += 1
        if re.search("[0-9]", line[j]) != None:
            str_num += line[j]
            indices.append((x, j))
        else:
            break
    # search left
    while True:
        i -= 1
        if re.search("[0-9]", line[i]) != None:
            str_num = line[i] + str_num
            indices.append((x, i))
        else:
            break
    return int(str_num), indices


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("")
    total = 0
    # line: "617*......"
    for x, line in enumerate(lines):
        # find all the gears in line
        gears = re.findall("\\*", line)
        for z in gears:
            # get first gear in line
            g = line.find("*")
            neighbors = getNeighborIndices(x, g, g, len(line))
            numbers = []
            checked = []
            # check all neighboring indices:
            for nx, ny in neighbors:
                # ignore if checked
                if (nx, ny) in checked:
                    pass
                else:
                    # if its a number:
                    if re.search("[0-9]", lines[nx][ny]) != None:
                        # find complete number
                        num, indices = getNumber(ny, nx, lines[nx])
                        # add number to numbers
                        numbers.append(num)
                        # mark all number's indices as checked 
                        checked += indices
            # if exactly two numbers add gear ratio to total
            if len(numbers) == 2:
                gear_ratio = numbers[0] * numbers[1]
                total += gear_ratio
            # erase gear from line
            mutable_line = list(line)
            mutable_line[g] = "."
            line = "".join(mutable_line)
    print(total)

