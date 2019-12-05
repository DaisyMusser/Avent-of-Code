# gets input
def file_reader(file_name):
    passwords = []

    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            puzzle = line.split('-')

            difference = int(puzzle[1][0:6]) - int(puzzle[0][0:6])
            for i in range(difference + 1):
                passwords.append(int(puzzle[0][0:6]) + i)  # not sure why 2nd int() is needed

    return passwords


# checks if password follows pair criteria
def criteria_three(password):
    temp = str(password)
    password = -1

    for i in range(5):
        if temp[i] == temp[i + 1]:         # criteria five applied here
            if i == 0:
                if temp[i] != temp[i + 2]:
                    password = int(temp)
                    break
            elif i == 4:
                if temp[i] != temp[i - 1]:
                    password = int(temp)
                    break
            else:
                if temp[i] != temp[i - 1] and temp[i] != temp[i + 2]:
                    password = int(temp)
                    break

    return password


# checks if password follows never decreasing left to right rule
def criteria_four(password):
    temp = []
    dummy = str(password)
    for i in range(6):
        temp.append(int(dummy[i]))

    for i in range(5):
        if temp[i] > temp[i+1]:
            password = -1
            break

    return password


# checks if password follows pt 2 rule
# def criteria_five(password):
#    temp = str(password)
#    password = -1
#
#    for i in range(4):
#        if temp[i] == temp[i + 1] == temp[i + 2]:
#            password = int(temp)
#            break
#
#    return password


# main program
# file io
passwords = file_reader('input.txt')

# applies rules
real_passwords = set()
for i in range(len(passwords)):
    if criteria_three(passwords[i]) != -1:
        if criteria_four(passwords[i]) != -1:
            real_passwords.add(passwords[i])       # there is now no reason this has to be a set

# answer
print(len(real_passwords))
