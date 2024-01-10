from emulate_tlk import *

if __name__ == "__main__":
    data = open("input.txt").read()

    # get seperate lines
    lines = data.split("\n")
    lines.remove("") # remove empty string at end of input

    # test my objects
    x = Wire("x")
    y = Wire("y")
    x_in = Literal(123)
    y_in = Literal(456)
    x.addParent(x_in)
    y.addParent(y_in)
    x_and_y = AND(x, y)
    d = Wire("d")
    d.addParent(x_and_y)
    print(d.getValue())

    # AND works

    not_x = NOT(x)
    h = Wire("h")
    h.addParent(not_x)
    print(h.getValue())

    # NOT works

    two = Literal(2)
    x_lshift_2 = LSHIFT(x, two)
    f = Wire("f")
    f.addParent(x_lshift_2)
    print(f.getValue())

    # LSHIFT works

    y_rshift_2 = RSHIFT(y, two)
    g = Wire("g")
    g.addParent(y_rshift_2)
    print(g.getValue())

    # RSHIFT works

    x_or_y = OR(x, y)
    e = Wire("e")
    e.addParent(x_or_y)
    print(e.getValue())

    # OR works!

