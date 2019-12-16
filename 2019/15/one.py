# day 15: the droid in the maze
import time
start_time = time.time()


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
# MIGHT NEED MORE MEMORY
def add_memory(program):
    # for _ in range(math.floor(len(program)/2)):
    for _ in range(7000):
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
    outputs = 'null'
    inputs = 'null'
    opcode = program[pointer]         # purely symbolic
    if opcode_checker(opcode):        # this is only helpful for debugging
        yarn = yarnifier(opcode)
        first = int(yarn[2])
        second = int(yarn[1])
        third = int(yarn[0])

        if int(yarn[4]) == 1:
            # used this page to figure out an error message:
            # https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
            # used this to figure out another error:
            # https://www.reddit.com/r/adventofcode/comments/e8aw9j/2019_day_9_part_1_how_to_fix_203_error/
            x = program[pointer + 1]    # default set to value not address (mode 1)
            y = program[pointer + 2]
            if first == 0:                   # x and y updated if modes not 1
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            address = program[pointer + 3]
            if third == 2:
                address = program[pointer + 3] + relative_base
            program[address] = x + y      # + rule
            pointer += 4

        elif int(yarn[4]) == 2:
            x = program[pointer + 1]   # default x and y set to raw (mode 1)
            y = program[pointer + 2]
            if first == 0:
                x = program[x]
            elif first == 2:
                x = program[x + relative_base]
            if second == 0:
                y = program[y]
            elif second == 2:
                y = program[y + relative_base]
            address = program[pointer + 3]
            if third == 2:
                address = program[pointer + 3] + relative_base
            program[address] = x * y  # * rule
            pointer += 4

        elif int(yarn[4]) == 3:  # get input rule
            x = get_inputs()
            inputs = x
            if first == 0:
                program[program[pointer + 1]] = x
            elif first == 2:
                program[program[pointer + 1] + relative_base] = x
            pointer += 2

        elif int(yarn[4]) == 4:  # print rule
            if first == 0:
                outputs = program[program[pointer + 1]]
            if first == 1:
                outputs = program[pointer + 1]
            elif first == 2:
                outputs = program[program[pointer + 1] + relative_base]
            pointer += 2

        elif int(yarn[4]) == 5:   # jump-if-true
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
            if x != 0:
                pointer = y
            else:
                pointer += 3

        elif int(yarn[4]) == 6:   # jump-if-false
            x = program[pointer + 1]  # default mode 1
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
            else:
                pointer += 3

        elif int(yarn[4]) == 7:   # less-than rule
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
            address = program[pointer + 3]
            if third == 2:
                address = program[pointer + 3] + relative_base
            if x < y:
                program[address] = 1
            else:
                program[address] = 0
            pointer += 4

        elif int(yarn[4]) == 8:   # equal-to rule
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
            address = program[pointer + 3]
            if third == 2:
                address = program[pointer + 3] + relative_base
            if x == y:
                program[address] = 1
            else:
                program[address] = 0
            pointer += 4

        elif int(yarn[3:5]) == 9:   # relative base modifier rule
            # leading 0s not allowed https://stackoverflow.com/questions/36386346/syntaxerror-invalid-token
            value = program[pointer + 1]
            if first == 0:
                value = program[value]
            elif first == 2:
                value = program[value + relative_base]
            relative_base += value
            pointer += 2

        elif int(yarn[3:5]) == 99:
            return 'END', program, relative_base, outputs, inputs
    else:
        print("--- ERORR ---")
        print("@ adress: ", pointer, "which is int: ", opcode)
        return 'DONE', 'ERROR', 0, 0, 0
    return pointer, program, relative_base, outputs, inputs


# runs program until outputs or inputs are used then returns all
def run_program(ram, pointer, rel_base):
    while True:
        pointer, ram, rel_base, outputs, inputs = opcode_processor(pointer, ram, rel_base)
        if outputs != 'null' or inputs != 'null':
            return outputs, inputs, pointer, ram, rel_base
        if pointer == 'END':           # for day15 this should never happen
            print('END OF PROGRAM')
            return


def program_io_manager(ram):
    pointer = 0
    rel_base = 0
    maze = MazeMap()
    counter = 0
    while True:    # this will only return when outputs is full
        outputs, inputs, pointer, ram, rel_base = run_program(ram, pointer, rel_base)
        maze.update_history(outputs, inputs)
        #maze.render_maze()
        counter += 1
        if counter == 100:
            print('FYI: this program never ends. Hit ctrl c to terminate.')


# gets input from user
def get_inputs():
    move = input('MOVE: ')
    if move in ['w', 'a', 's', 'd']:
        if move == 'w':
            move = 1
        if move == 'd':
            move = 4
        if move == 's':
            move = 2
        if move == 'a':
            move = 3
        return move
    else:
        print('Use w a s d to move')
        return get_inputs()        # not properly tail called cuz python sucks sometimes


class MazeMap(object):
    def __init__(self):
        self.history = []
        self.spot = 'null'
        return

    def update_history(self, inputs, outputs):
        if inputs != 'null':
            self.history.append(inputs)
        elif outputs != 'null':
            self.history.append(outputs)
        return

    # needs to read history and determine: h, l, loc, walls, then print all
    # it's gunna go i o i o i o ...
    def render_maze(self):
        loc = (0, 0)
        walls = []
        oxy = 'null'
        spaces = []

        # generates walls, loc, oxy
        for i in range(len(self.history)):
            number = self.history[i]             # symbolic
            if i == 0 or i % 2 == 0:    # this means it's an input
                if number == 1:
                    self.spot = (loc[0], loc[1] + 1)
                elif number == 2:
                    self.spot = (loc[0], loc[1] - 1)
                elif number == 3:
                    self.spot = (loc[0] - 1, loc[1])
                elif number == 4:
                    self.spot = (loc[0] + 1, loc[1])
            else:                       # this means it's an output
                if number == 0:    # spot is wall, no change in loc
                    walls.append((self.spot[0], self.spot[1]))
                elif number == 1:    # spot is space, loc = spot
                    loc = (self.spot[0], self.spot[1])
                    spaces.append(loc[0], loc[1])
                elif number == 2:    # spot is oxy, loc = spot
                    loc = (self.spot[0], self.spot[1])
                    oxy = (loc[0], loc[1])

        # finds l and h, x_max _min , y_max _min
        x_min = 9999
        x_max = 0
        y_min = 9999
        y_max = 0
        for wall in walls:
            if wall[0] > x_max:
                x_max = wall[0]
            if wall[0] < x_min:
                x_min = wall[0]
            if wall[1] > y_max:
                y_max = wall[1]
            if wall[1] < y_min:
                y_min = wall[1]
        for space in spaces:
            if space[0] > x_max:
                x_max = space[0]
            if space[0] < x_min:
                x_min = space[0]
            if space[1] > y_max:
                y_max = space[1]
            if space[1] < y_min:
                y_min = space[1]
        l = abs(x_min - x_max)
        h = abs(y_min - y_max)

    # print maze
        # vv makes a blank map that's the right size
        blank_map = []
        for _ in range(h):
            line = []
            for _ in range(l):
                line.append('.')
            blank_map.append(line)

        # converts to address
        x_shift = -1 * x_min
        y_shift = -1 * y_max
        walls = convert(walls, x_shift, y_shift)
        spaces = convert(spaces, x_shift, y_shift)
        if oxy != 'null':
            oxy = (oxy[0] + x_shift, oxy[1] + y_shift)
        loc = (loc[0] + x_shift, loc[1] + y_shift)

        # fills blank_map
        for wall in walls:
            blank_map[wall[1]][wall[0]] = '#'
        for space in spaces:
            blank_map[space[1]][space[0]] = ' '
        if oxy != 'null':
            blank_map[oxy[1]][oxy[0]] = '*'
        blank_map[loc[1]][loc[0]] = 'o'
        color_map = blank_map    # just for fun

        # prints map
        for line in color_map:
            print(line)
        return


# converts to address
def convert(subject, x_shift, y_shift):
    for elem in subject:
        elem = list(elem)
        elem[0] += x_shift
        elem[1] += y_shift
    return subject


# main program:
program = file_to_string('input.txt')  # change file name here!
all_commas = comma_finder(program)
program = string_to_array(program, all_commas)
program = add_memory(program)
# done with file io / formatting

program_io_manager(program)

