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
        count = count + tricheck(line[0], line[1], line[2])
        line = fp.readline()

print(count)




