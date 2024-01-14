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


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("")
    total = 0 
    for xlines, line in enumerate(lines):
        # get all numbers in the line
        nums = re.findall("(?<![0-9])[0-9]+(?![0-9])", line)
        if len(nums) != len(set(nums)):
            q = 0
        for num in nums:
            y_start = line.find(num)
            y_end = y_start + len(num) - 1
            # use getNeighborIndices to see what you have to check
            neighbors = getNeighborIndices(xlines, y_start, y_end, len(line))
            # check those indices for symbols.
            for x, y in neighbors:
                # If any found, halt, add number to total
                if re.search("\\.|[0-9]", lines[x][y]) == None:
                    total += int(num)
                    break
            # need to erase visited numbers 
            mutableLine = list(line)
            for y in range(y_start, y_end + 1):
                mutableLine[y] = "."
            line = "".join(mutableLine)
    print(total)

# 556822 wrong
# 556461 is too high
# 276860 is too low
