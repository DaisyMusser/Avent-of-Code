
from classy import *

# test
x0  = value(123)
x1  = value(456)
x2  = value(2)
x3  = address("x")
x4  = address("y")
x5  = value(2)
x6  = opperation("NOT")
x7  = opperation("LSHIFT")
x8  = opperation("AND")
x9  = opperation("OR")
x10 = opperation("RSHIFT")
x11 = opperation("NOT")
x12 = address("h")
x13 = address("f")
x14 = address("d")
x15 = address("e")
x16 = address("g")
x17 = address("i")

x17.addParent(x11)
x16.addParent(x10)
x15.addParent(x9)
x14.addParent(x8)
x13.addParent(x7)
x12.addParent(x6)
x6.addParent(x3)
x7.addParent(x3)
x7.addParent(x2)
x8.addParent(x3)
x8.addParent(x4)
x9.addParent(x3)
x9.addParent(x4)
x10.addParent(x4)
x10.addParent(x5)
x11.addParent(x4)
x3.addParent(x0)
x4.addParent(x1)

circut = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17]

for n in circut:
    if isinstance(n, address):
        print(n.name + ": " + str(n.getValue()))
