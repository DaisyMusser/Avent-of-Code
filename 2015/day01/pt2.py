# takes direction list, returns record list of specified floors
def tracker(directions):
    flr = 0
    record = []
    for i in range(len(directions)):
        if directions[i] == '(':
            flr += 1
        if directions[i] == ')':
            flr -= 1
        record.append(flr)
    return record


# returns loc of first instance of -1 in the record
def basement(record):
    x = record.index(-1)
    return x+1


# main program?
file = 'input.txt'      # This is all you have to change to deal with dif. input file names
with open(file) as fp:
    directions = fp.readline()
    record = tracker(directions)
    loc = basement(record)
    print(loc)

