# gets input
def file_reader(file_name):
    passwords = []
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            puzzle = line.split('-')

            bottom = int(puzzle[0][0:6])                   # silly but helpful
            top    = int(puzzle[1][0:6])

            difference = top - bottom
            for i in range(difference+1):
                passwords.append(int(puzzle[0][0:6]) + i)  # not sure why the redundant int() is needed here?
    return passwords


# checks if password follows adjacent criteria
def aj_criteria(password):
    temp = str(password)
    password = -1
    for i in range(5):
        if temp[i] == temp[i + 1]:
            password = int(temp)
    return password


# main program
passwords = file_reader('input.txt')

x = 101010

password = aj_criteria(x)
print(password)

