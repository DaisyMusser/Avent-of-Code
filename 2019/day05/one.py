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


# runs the opcode and returns a modified opcode
# def run_opcode(opcode):
#    block_start = 0
#    output = opcode[:]
#    for i in range(math.ceil(len(opcode)/4)):
#        if opcode[block_start] == 1:              # add x and y at z
#            x = opcode[opcode[block_start+1]]
#            y = opcode[opcode[block_start+2]]
#            output[opcode[block_start+3]] = x+y
#        if opcode[block_start] == 2:              # mult. x and y at z
#            x = opcode[opcode[block_start + 1]]
#            y = opcode[opcode[block_start + 2]]
#            output[opcode[block_start + 3]] = x*y
#        if opcode[block_start] == 99:             # end opcode
#            break
#        opcode = output[:]
#        block_start += 4
#    return output[0]

# returns true if number was a valid opcode, false if not
def opcode_checker(number):
    answer = False                             # default falseyness
    yarn = str(number)                         # string of number
    if len(yarn) > 5:                          # greater than 5 digits c/t be an opcode
        return answer

    yarn = ("0" * int(5-len(yarn))) + yarn     # fill yarn with 0s

    ones = int(yarn[4])                        # to save some typing and confusion
    tens = int(yarn[3])

    mode_three = int(yarn[0])
    mode_two   = int(yarn[1])
    mode_one   = int(yarn[2])

    print(yarn)

    # https://stackoverflow.com/questions/148042/using-or-comparisons-with-if-statements
    if ones in (1, 2, 3, 4):
        if tens == 0:
            if mode_three in (0, 1) and mode_two in (0, 1) and mode_one in (0, 1):
                answer = True

    if int(yarn[3:5]) == 99:
        if mode_three in (0, 1) and mode_two in (0, 1) and mode_one in (0, 1):
            answer = True

    return answer



# main program:
string_puzzle = file_to_string('input.txt')  # change here for different file names
all_commas = comma_finder(string_puzzle)

puzzle = string_to_array(string_puzzle, all_commas)
# done with input formatting

number = opcode_checker(10199)
print(number)

