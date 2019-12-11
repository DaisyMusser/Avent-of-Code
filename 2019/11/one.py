
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
    for _ in range(3000):
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
def opcode_processor(pointer, program, relative_base, inputs, outputs):
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
            x = inputs
            if first == 0:
                program[program[pointer + 1]] = x
            elif first == 2:
                program[program[pointer + 1] + relative_base] = x
            pointer += 2

        elif int(yarn[4]) == 4:  # print rule
            if first == 0:
                outputs.append(program[program[pointer + 1]])
            if first == 1:
                outputs.append(program[pointer + 1])
            elif first == 2:
                outputs.append(program[program[pointer + 1] + relative_base])
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
            return 'END', program, relative_base, outputs
    else:
        print("--- ERORR ---")
        print("@ adress: ", pointer, "which is int: ", opcode)
        return 'DONE', 'ERROR', 0, 0

    return pointer, program, relative_base, outputs


# runs program until END
def run_program(pointer, program, relative_base, inputs, outputs):
    while True:
        pointer, program, relative_base, outputs = opcode_processor(pointer, program, relative_base, inputs, outputs)
        if len(outputs) == 2:
            return pointer, program, relative_base, outputs   # this is the modified pointer and program,
        if pointer == 'END':                   # both can be fed back in to restart program at same spot
            return pointer, program, relative_base, outputs


class Robot:
    def __init__(self, panels):
        self.location = (0, 0)
        self.facing = 0
        self.panels = panels

    def move(self):
        new_location = []       # added this bc location has to be a tuple, so must be replaced
        new_location.append(self.location[0])
        new_location.append(self.location[1])
        if self.facing == 0:        # up
            new_location[1] += 1
        elif self.facing == 1:      # right
            new_location[0] += 1
        elif self.facing == 2:      # down
            new_location[1] -= 1
        elif self.facing == 3:      # left
            new_location[0] -= 1
        self.location = tuple(new_location)
        return

    def turning(self, turn):
        if turn == 1:
            self.facing += 1
        else:
            self.facing -= 1

    def paint(self, abs_program):
        pointer = 0
        rel_program = abs_program[:]
        relative_base = 0
        outputs = []
        inputs = 0
        while pointer != 'END':
            pointer, rel_program, relative_base, outputs = run_program(pointer, rel_program, relative_base, inputs, outputs)

            # add self.location as a key to the dict self.panels, then set outputs[0] to the value for that key
            self.panels[self.location] = outputs[0]

            # updates self.facing and then moves self.loctation
            self.turning(outputs[1])
            self.move()

            # now we need to change inputs to be right
            if self.location in self.panels:
                inputs = self.panels[self.location]
            else:
                inputs = 0
        return self.panels


# main program:
program = file_to_string('input.txt')  # change file name here!
all_commas = comma_finder(program)
program = string_to_array(program, all_commas)
program = add_memory(program)
panels = {}
# done with file io / formatting

robot = Robot(panels)
answer = robot.paint(program)
