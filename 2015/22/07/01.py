from emulate_tlk import *


def handleWireOrLiteral(term, memory): 
    if term[0] in "0123456789":
        # is lit
        return Literal(int(term)), memory
    else:
        # is wire
        # check if wire is in memory yet:
        if term in memory.keys():
            return memory[term], memory
        else:
            a = Wire(term)
            memory[term] = a
            return a, memory

if __name__ == "__main__":
    data = open("input-fuckery.txt").read()

    # get seperate lines
    lines = data.split("\n")
    lines.remove("") # remove empty string at end of input
    lines = [x.split(" ") for x in lines]

    # Eventually this will map wire labels to wire objects. 
    # All of the wire objects will know their parents. 
    memory = {}

    for line in lines:
        if "OR" in line:
            # ["wire/lit", "OR", "wire/lit", "->", "wire"]
            a, memory = handleWireOrLiteral(line[0], memory)
            b, memory = handleWireOrLiteral(line[2], memory)
            c, memory = handleWireOrLiteral(line[4], memory)
            a_or_b = OR(a, b)
            c.addParent(a_or_b)
        elif "RSHIFT" in line:
            # ["wire/lit", "RSHIFT", "wire/lit", "->", "wire"]
            a, memory = handleWireOrLiteral(line[0], memory)
            b, memory = handleWireOrLiteral(line[2], memory)
            c, memory = handleWireOrLiteral(line[4], memory)
            a_rshift_b = RSHIFT(a, b)
            c.addParent(a_rshift_b)
        elif "LSHIFT" in line:
            # ["wire/lit", "LSHIFT", "wire/lit", "->", "wire"]
            a, memory = handleWireOrLiteral(line[0], memory)
            b, memory = handleWireOrLiteral(line[2], memory)
            c, memory = handleWireOrLiteral(line[4], memory)
            a_lshift_b = LSHIFT(a, b)
            c.addParent(a_lshift_b)
        elif "NOT" in line:
            # ["NOT", "wire/lit", "->", "wire"]
            a, memory = handleWireOrLiteral(line[1], memory)
            c, memory = handleWireOrLiteral(line[3], memory)
            not_a = NOT(a)
            c.addParent(not_a)
        elif "AND" in line:
            # ["wire/lit", "AND", "wire/lit", "->", "wire"]
            a, memory = handleWireOrLiteral(line[0], memory)
            b, memory = handleWireOrLiteral(line[2], memory)
            c, memory = handleWireOrLiteral(line[4], memory)
            a_and_b = AND(a, b)
            c.addParent(a_and_b)
        # no operations in line, so must be literal assingment
        else:
            # ["2", "->", "wire"]
            a, memory = handleWireOrLiteral(line[0], memory)
            c, memory = handleWireOrLiteral(line[2], memory)
            c.addParent(a)
    
    a = memory["a"]
    print(str(a.getValue()))

