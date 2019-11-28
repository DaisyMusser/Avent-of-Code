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
file = 'input.txt'       # only need to change here to use dif. input
count = 0
with open(file) as fp:
    try:
        line1 = fp.readline()
        line2 = fp.readline()
        line3 = fp.readline()
        # print(line1,line2,line3)        line1, 2, 3 are fine at this point
        while line1:
            line1 = linefix(line1)
            line2 = linefix(line2)
            line3 = linefix(line3)
            for i in range(3):
                index = 0
                a = (line1[index+2]*100) + (line1[index+3]*10) + line1[index+4]
                b = (line2[index+2]*100) + (line2[index+3]*10) + line2[index+4]
                c = (line3[index+2]*100) + (line3[index+3]*10) + line3[index+4]
                index += 5
                count += tricheck(a, b, c)
            line1 = fp.readline()
            line2 = fp.readline()
            line3 = fp.readline()
    finally:
        fp.close()
print(count)