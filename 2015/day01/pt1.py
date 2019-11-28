# takes direction list, returns specified floor
def translator(directions):
    flr = 0
    for i in range(len(directions)):
        if directions[i] == '(':
            flr += 1
        if directions[i] == ')':
            flr -= 1
    return flr


# takes a document and copies it to a list
def copier(doc):
    directions = []
    for i in doc:
        directions.append(doc[i])
    return directions


# main program?
file = 'input.txt'      # This is all you have to change to deal with dif. input file names
with open(file) as fp:
    directions = fp.readline()
    print(directions)
    properFloor = translator(directions)
    print(properFloor)
