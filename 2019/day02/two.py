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


# parses string into an array
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
def run_opcode(opcode):
    block_start = 0
    output = opcode[:]
    for i in range(math.ceil(len(opcode)/4)):
        if opcode[block_start] == 1:          # add x and y at z
            x = opcode[opcode[block_start+1]]
            y = opcode[opcode[block_start+2]]
            output[opcode[block_start+3]] = x+y
        if opcode[block_start] == 2:          # mult. x and y at z
            x = opcode[opcode[block_start + 1]]
            y = opcode[opcode[block_start + 2]]
            output[opcode[block_start + 3]] = x*y
        if opcode[block_start] == 99:         # end opcode
            break
        opcode = output[:]
        block_start += 4
    return output[0]


# cycles through 0-99 for verbs and nouns until output = 19690720
def noun_verb_checker(run_opcode, opcode):
    for i in range(100):
        dummy = opcode[:]     # reset memory
        dummy[1] = i
        for ii in range(100):
            dummy[2] = ii
            output = run_opcode(dummy)
            if output == 19690720:
                return i, ii
    return -1, -1


# main program:
string_opcode = file_to_string('input.txt')  # change here for different file names
all_commas = comma_finder(string_opcode)
opcode = string_to_array(string_opcode, all_commas)
# done with input formatting

# start input processing
noun, verb = noun_verb_checker(run_opcode, opcode)
if noun == -1:
    print('ERROR: no possible solutions')
else:
    print('Noun: ', noun, '\nVerb: ', verb)
    print('Answer: ', 100*noun+verb)
