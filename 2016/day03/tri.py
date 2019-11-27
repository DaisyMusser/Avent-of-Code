def tricheck(a, b, c):
    if a+b <= c:
        return 0
    if b+c <= a:
        return 0
    if c+a <= b:
        return 0
    return 1


# main program
# could try a try final block for opening and closeing a file
count = 0
with open('input.txt') as fp:
    line = fp.readline()
    while line:
        a = (line[2]*100) + (line[3]*10) + line[4]
        b = (line[7]*100) + (line[8]*10) + line[9]
        c = (line[12]*100) + (line[13]*10) + line[14]
        count = count + tricheck(a, b, c)
        line = fp.readline()

print(count)


