import math

# Reads file into string, code adapted from ( https://github.com/imhoffman/advent/blob/master/2015/01/one.py )
def file_to_string(file_name):
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:         # a little bit of error catching
                break
            string_opcode = line
    return string_opcode


# finds commas in string
# could be done with .split(), but oh well
def comma_finder(string_opcode):
    start_search = 0
    all_commas = []
    while True:
        comma_loc = string_opcode.find(',', start_search)
        if comma_loc == -1:                   # breaks out of loop once all commas found
            break
        all_commas.append(comma_loc)
        start_search = comma_loc + 1
    return all_commas


# parses string into an array
# could be done with .split()
def string_to_array(opcode_string, comma_index):
    opcode = []
    buffer = 0
    for i in range(len(comma_index)+1):
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


# makes number str and back-fills with 0s
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

    yarn = ("0" * int(5-len(yarn))) + yarn     # fill yarn with 0s, just like yarnifier

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


# given a pointer and a program, executes instructions and returns modified program + pointer
def opcode_processor(pointer, program):
    opcode = program[pointer]         # purely symbolic
    if opcode_checker(opcode):        # this is only helpful for debugging
        yarn = yarnifier(opcode)
        first = int(yarn[2])
        second = int(yarn[1])

        print(program)
        print('pointer: ', pointer)

        if int(yarn[4]) == 1:
            x = program[pointer + 1]  # default set to value not address
            y = program[pointer + 2]
            if first == 0:            # x and y updated if modes not 1
                x = program[x]
            if second == 0:
                y = program[y]
            program[program[pointer + 3]] = x + y  # + rule
            pointer += 4

        elif int(yarn[4]) == 2:
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            if second == 0:
                y = program[y]
            program[program[pointer + 3]] = x * y  # * rule
            pointer += 4

        elif int(yarn[4]) == 3:  # get input rule
            x = int(input('INPUT: '))  # always adress mode
            program[program[pointer + 1]] = x
            pointer += 2

        elif int(yarn[4]) == 4:  # print rule
            if first == 0:
                print(program[program[pointer + 1]])
            if first == 1:  # originally this was elif :|
                print(program[pointer + 1])
            pointer += 2

        elif int(yarn[4]) == 5:   # jump-if-true
            x = program[pointer+1]
            y = program[pointer+2]
            if first == 0:
                x = program[x]
            if second == 0:
                y = program[y]
            if x != 0:
                pointer = y
            else:                 # this might need to be something else
                pointer += 3

        elif int(yarn[4]) == 6:   # jump-if-false
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            if second == 0:
                y = program[y]
            if x == 0:
                pointer = y
            else:                 # this might need to be something else
                pointer += 3

        elif int(yarn[4]) == 7:
            x = program[pointer + 1]
            y = program[pointer + 2]
            program[program[pointer + 3]] = 0
            if first == 0:
                x = program[x]
            if second == 0:
                y = program[y]
            if x < y:
                program[program[pointer+3]] = 1
            pointer += 4

        elif int(yarn[4]) == 8:
            x = program[pointer + 1]
            y = program[pointer + 2]
            program[program[pointer + 3]] = 0
            if first == 0:
                x = program[x]
            if second == 0:
                y = program[y]
            if x == y:
                program[program[pointer+3]] = 1
            pointer += 4

        elif int(yarn[4]) == 9:
            return 'DONE', program
    else:
        print("--- ERORR ---")
        print("@ adress: ", pointer, "which is int: ", opcode)
        return 'DONE', 'ERROR'

    return pointer, program


# feeds pointers and programs into opcode_processor until 'DONE'
def run_program(program):
    pointer = 0
    while True:
        pointer, program = opcode_processor(pointer, program)
        if pointer == 'DONE':
            break
    return program


# main program:
string_puzzle = file_to_string('eight.txt')  # change here for different file names
# done with file io

all_commas = comma_finder(string_puzzle)
program = string_to_array(string_puzzle, all_commas)
# done with input formatting

# prints answer
final_program_state = run_program(program)


