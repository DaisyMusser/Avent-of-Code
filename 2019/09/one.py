import math
import itertools

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


# adds memory to the end of the program
def add_memory(program):
    for _ in range(math.floor(len(program)/2)):
        program.append(0)
    return program


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

    yarn = ("0" * int(5-len(yarn))) + yarn     # backfill yarn with 0s, just like yarnifier

    opcode     = int(yarn[3:5])                # purely symbolic
    mode_three = int(yarn[0])
    mode_two   = int(yarn[1])
    mode_one   = int(yarn[2])

    # https://stackoverflow.com/questions/148042/using-or-comparisons-with-if-statements
    if opcode in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        if mode_three in (0, 1, 2) and mode_two in (0, 1, 2) and mode_one in (0, 1, 2):
            answer = True

    if opcode == 99:
        answer = True

    return answer


# given a pointer and a program, executes instructions and returns modified program + pointer
def opcode_processor(pointer, program, relative_base):
    opcode = program[pointer]         # purely symbolic
    if opcode_checker(opcode):        # this is only helpful for debugging
        yarn = yarnifier(opcode)
        first = int(yarn[2])
        second = int(yarn[1])
        third = int(yarn[0])

        if int(yarn[4]) == 1:
            # used this page to figure out an error message:
            # https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
            x = int(program[pointer + 1])  # default set to value not address
            y = int(program[pointer + 2])
            if first == 0:                 # x and y updated if modes not 1
                x = int(program[x])
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = int(program[y])
            elif second == 2:
                y = program[y + relative_base]
            if third == 0:
                address = program[pointer + 3]
            elif third == 2:
                address = program[pointer + 3] + relative_base
            program[address] = x + y      # + rule
            pointer += 4

        elif int(yarn[4]) == 2:
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            if third == 0:
                address = program[pointer + 3]
            elif third == 2:
                address = program[pointer + 3] + relative_base
            program[address] = x * y  # * rule
            pointer += 4

        elif int(yarn[4]) == 3:  # get input rule
            x = input('INPUT: ')
            if first == 0:
                program[program[pointer + 1]] = x
            elif first == 2:
                program[program[pointer + 1] + relative_base] = x
            pointer += 2

        elif int(yarn[4]) == 4:  # print rule
            if first == 0:
                print(program[program[pointer + 1]])
            elif first == 1:
                print(program[pointer + 1])
            elif first == 2:
                print(program[program[pointer + 1] + relative_base])
            pointer += 2

        elif int(yarn[4]) == 5:   # jump-if-true
            x = program[pointer+1]
            y = program[pointer+2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            if x != 0:
                pointer = y
            else:
                pointer += 3

        elif int(yarn[4]) == 6:   # jump-if-false
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            if x == 0:
                pointer = y
            else:                 # this might need to be something else
                pointer += 3

        elif int(yarn[4]) == 7:
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            if third == 0:
                address = program[pointer + 3]
            elif third == 2:
                address = program[pointer + 3] + relative_base
            if x < y:
                program[address] = 1
            else:
                program[address] = 0
            pointer += 4

        elif int(yarn[4]) == 8:
            x = program[pointer + 1]
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            if third == 0:
                address = program[pointer + 3]
            elif third == 2:
                address = program[pointer + 3] + relative_base
            if x == y:
                program[address] = 1
            else:
                program[address] = 0
            pointer += 4

        elif int(yarn[3:5]) == 9:
            # leading 0s not allowed https://stackoverflow.com/questions/36386346/syntaxerror-invalid-token
            if first == 0:
                value = program[program[pointer + 1]]
            elif first == 1:
                value = program[pointer + 1]
            elif first == 2:
                value = program[program[pointer + 1] + relative_base]
            relative_base += value
            pointer += 2

        elif int(yarn[3:5]) == 99:
            return 'END', program, relative_base
    else:
        print("--- ERORR ---")
        print("@ adress: ", pointer, "which is int: ", opcode)
        return 'DONE', 'ERROR', 0, 0

    return pointer, program, relative_base


# runs program until END
def run_program(program):
    pointer = 0
    relative_base = 0
    while True:
        pointer, program, relative_base = opcode_processor(pointer, program, relative_base)
        if pointer == 'END':
            return program


# main program:
program = file_to_string('input.txt')  # change file name here!
all_commas = comma_finder(program)
program = string_to_array(program, all_commas)
program = add_memory(program)
# done with file io / formatting

run_program(program)


