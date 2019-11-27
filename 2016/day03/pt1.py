# returns 0 for not a triangle and 1 for triangle
def tricheck(a, b, c):
    if a+b <= c:
        return 0
    if b+c <= a:
        return 0
    if c+a <= b:
        return 0
    return 1


# makes line all int
def linefix(line):
    fixedline = []
    for i in range(15):
        if line[i] == ' ':
            fixedline.append(0)
        if line[i] != ' ':
            fixedline.append(int(line[i]))
    return fixedline


# main program
# could try a try final block for opening and closing a file
file = 'input.txt' # only need to change here to use dif. input
count = 0
with open(file) as fp:
    try:
        line = fp.readline()
        while line:
            line = linefix(line)
            a = (line[2]*100) + (line[3]*10) + line[4]
            b = (line[7]*100) + (line[8]*10) + line[9]
            c = (line[12]*100) + (line[13]*10) + line[14]
            count = count + tricheck(a, b, c)
            line = fp.readline()
    finally:
        fp.close()
print(count)


