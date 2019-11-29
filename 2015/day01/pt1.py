# takes direction list, returns specified floor
def translator(directions):
    flr = 0
    for i in range(len(directions)):
        if directions[i] == '(':
            flr += 1
        if directions[i] == ')':
            flr -= 1
    return flr


# main program
file = 'input.txt'      # This is all you have to change to deal with dif. input file names
with open(file) as fp:
    directions = fp.read()
    proper_floor = translator(directions)
    print("\n Directed to floor: %d \n" % proper_floor)
