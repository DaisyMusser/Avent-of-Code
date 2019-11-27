def tricheck(a, b, c):
    if a+b < c:
        return 0
    if b+c < a:
        return 0
    if c+a < b:
        return 0
    return 1


# main program
print(tricheck(5, 5, 5))
print(tricheck(1, 50, 2))



