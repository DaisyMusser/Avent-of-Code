import math


# Reads file into string, code adapted from ( https://github.com/imhoffman/advent/blob/master/2015/01/one.py )
def file_to_string(file_name):
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            string_opcode = line
    return string_opcode


# finds commas in string
def comma_finder(string_opcode):
    start_search = 0
    all_commas = []
    while True:
        comma_loc = string_opcode.find(',', start_search)
        if comma_loc == -1:
            break
        all_commas.append(comma_loc)
        start_search = comma_loc + 1
    return all_commas

# parses string into an array
# could be done with .split() way easier, but oh well
def string_to_array(opcode_string, comma_index):
    opcode = []
    buffer = 0
    for i in range(len(comma_index)+1):   # s/d eventually make sure these are all int()
        start = buffer
        if i == len(comma_index):
            end = len(opcode_string)+1
            opcode.append(int(opcode_string[start:end]))
            break
        if i < len(comma_index):
            end = comma_index[i]
        opcode.append(int(opcode_string[start:end]))
        buffer = comma_index[i]+1
    return opcode


# makes number workable by back-filling with 0s
def yarnifier(number):
    yarn = str(number)
    yarn = ("0" * int(5-len(yarn))) + yarn
    return yarn


# returns true if number was a valid opcode, false if not
def opcode_checker(number):
    answer = False                             # default falseyness
    yarn = str(number)                         # string of number
    if len(yarn) > 5:                          # greater than 5 digits c/t be an opcode
        return answer

    if number < 1:                             # 0 or -#s c/t be opcodes
        return answer

    yarn = ("0" * int(5-len(yarn))) + yarn     # fill yarn with 0s

    ones = int(yarn[4])                        # to save some typing and confusion
    tens = int(yarn[3])

    mode_three = int(yarn[0])
    mode_two   = int(yarn[1])
    mode_one   = int(yarn[2])

    # https://stackoverflow.com/questions/148042/using-or-comparisons-with-if-statements
    if ones in (1, 2, 3, 4):
        if tens == 0:
            if mode_three in (0, 1) and mode_two in (0, 1) and mode_one in (0, 1):
                answer = True

    if int(yarn[3:5]) == 99:
        if mode_three in (0, 1) and mode_two in (0, 1) and mode_one in (0, 1):
            answer = True

    return answer

#
def run_program(puzzle):
    skips = 0
    spot = 0
    for number in puzzle:
        if skips == 0:
            if opcode_checker(number):            # might need a "== True"
                yarn = yarnifier(number)

                first  = int(yarn[2])
                second = int(yarn[1])

                if int(yarn[4]) == 1:
                    x = puzzle[spot+1]            # default set to value not address
                    y = puzzle[spot+2]
                    if first == 0:                # x and y updated if modes not 1
                        x = puzzle[x]
                    elif second == 0:
                        y = puzzle[y]
                    puzzle[spot+3] = x+y          # + rule
                    skips += 4

                elif int(yarn[4]) == 2:
                    x = puzzle[spot+1]
                    y = puzzle[spot+2]
                    if first == 0:
                        x = puzzle[x]
                    elif second == 0:
                        y = puzzle[y]
                    puzzle[spot+3] = x*y          # * rule
                    skips += 4

                elif int(yarn[4]) == 3:
                    x = int(input('INPUT: '))
                    puzzle[spot+1] = x
                    skips += 1

                elif int(yarn[4]) == 4:
                    if first == 0:
                        print(puzzle[puzzle[spot+1]])
                    elif first == 1:
                        print(puzzle[spot+1])
                    skips += 1

                elif int(yarn[4]) == 9:
                    return puzzle
        else:
            skips -= 1
        spot += 1
    return puzzle          # now it's really output


# main program:
string_puzzle = file_to_string('input.txt')  # change here for different file names
all_commas = comma_finder(string_puzzle)

puzzle = string_to_array(string_puzzle, all_commas)
# done with input formatting

output = run_program(puzzle)


