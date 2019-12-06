# pulls all possible passwords from range in specified file
def file_reader(file_name):
    passwords = []

    with open(file_name) as fp:  # with open closes file after use
        while True:
            line = fp.read()
            if not line:
                break
            puzzle = line.split('-')

    difference = int(puzzle[1][0:6]) - int(puzzle[0][0:6])
    for i in range(difference + 1):
    passwords.append(int(puzzle[0][0:6]) + i)  # not sure why 2nd int() is needed

    return passwords


# checks if password follows pair criteria (aka the third criteria listed)
def criteria_three(password):
    yarn = str(password)                   # for iterability
    password = -1

    for i in range(5):
        if temp[i] == temp[i + 1]:         # criteria five applied here
            if i == 0:                     # pair at start case
                if temp[i] != temp[i + 2]:
                    password = int(temp)   # recast temp to int
                    break
            elif i == 4:                   # pair at end case
                if temp[i] != temp[i - 1]:
                    password = int(temp)
                    break
            else:                          # all middle cases
                if temp[i] != temp[i - 1] and temp[i] != temp[i + 2]:
                    password = int(temp)
                    break

    return password


# checks if password follows never decreasing left to right rule (aka 4th criteria)
def criteria_four(password):
    temp = []
    dummy = str(password)
    for i in range(6):                # need temp to be iterable but also int
        temp.append(int(dummy[i]))

    for i in range(5):
        if temp[i] > temp[i+1]:
            password = -1
            break

    return password



# main program
# file io
passwords = file_reader('input.txt')

# applies criteria
real_passwords = set()     # set used to remove excess -1s, but no longer really needed
for i in range(len(passwords)):
    if criteria_three(passwords[i]) != -1:
        if criteria_four(passwords[i]) != -1:
            real_passwords.add(passwords[i])

# answer
print(len(real_passwords))
