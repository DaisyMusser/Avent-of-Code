
NO_INPUT = -1

def bitwise_not(n, bits):
    return (1 << bits) - 1 - n


if __name__ == "__main__":
    # data = open("example.txt").read()
    data = open("input.txt").read()

    # get seperate lines
    data = data.split("\n")
    data.remove("") # remove empty string at end of input

    # split up lines into terms
    for index, line in enumerate(data):
        data[index] = line.split(" ")

    # 1ST PASS
    # make dictionary of wires with null starting value (-1)
    wires = {}
    for line in data:
        wires[line[-1]] = NO_INPUT

    # 2ND PASS
    # if line can be executed at this time: execute and overwrite with "DONE"
    # if not, keep in data and move on
    while wires["a"] == -1:
        for index, line in enumerate(data):
            # if line has been executed, skip it
            if line == "DONE":
                continue

            num_of_terms = len(line)

            # literal assignment, viz:
            # 123 -> x
            if num_of_terms == 3:
                if line[0].isalpha():
                    # value is a wire
                    value = wires[line[0]]
                else:
                    # value is a number
                    value = int(line[0])
                # make sure we don't read an empty wire
                if value == NO_INPUT:
                    continue
                wires[line[-1]] = value
                data[index] = "DONE"

            # NOT, viz:
            # NOT x -> h
            if "NOT" in line:
                operand = wires[line[1]]
                if operand == NO_INPUT:
                    # can't execute line yet, skip it
                    continue
                else:
                    # can execute line!
                    wires[line[-1]] = bitwise_not(operand, bits=16)
                    data[index] = "DONE"

            # RSHIFT, viz:
            # y RSHIFT 2 -> g
            if "RSHIFT" in line:
                operand = wires[line[0]]
                if operand == NO_INPUT:
                    # can't execute line yet, skip it
                    continue
                else:
                    # can execute line!
                    wires[line[-1]] = operand >> int(line[2])
                    data[index] = "DONE"

            # LSHIFT, viz:
            # x LSHIFT 2 -> f
            if "LSHIFT" in line:
                operand = wires[line[0]]
                if operand == NO_INPUT:
                    # can't execute line yet, skip it
                    continue
                else:
                    # can execute line!
                    wires[line[-1]] = operand << int(line[2])
                    data[index] = "DONE"

            # OR, viz:
            # x OR y -> e
            if "OR" in line:
                x = wires[line[0]]
                y = wires[line[2]]
                if (x == NO_INPUT) or (y == NO_INPUT):
                    # can't execute line yet, skip it
                    continue
                else:
                    # can execute line!
                    wires[line[-1]] = x | y
                    data[index] = "DONE"

            # AND, viz:
            # x AND y -> d
            if "AND" in line:
                # is x a wire or literal ?
                if line[0].isalpha():
                    # x is wire
                    x = wires[line[0]]
                else:
                    # x is literal
                    x = int(line[0])
                # is y a wire or literal ?
                if line[2].isalpha():
                    # y is wire
                    y = wires[line[2]]
                else:
                    # y is literal
                    y = int(line[2])

                # check if any empty wires
                if (x == NO_INPUT) or (y == NO_INPUT):
                    # can't execute line yet, skip it
                    continue
                else:
                    # can execute line!
                    wires[line[-1]] = x & y
                    data[index] = "DONE"

    print(wires["a"])
