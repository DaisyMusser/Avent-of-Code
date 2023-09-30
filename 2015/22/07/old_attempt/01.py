
from classy import *
from tqdm import tqdm

# given and address name, gets the address
def get_address(new_addr_name, mem):
    for addr in mem:
        if addr.name == new_addr_name:
            return addr
    new_addr = address(new_addr_name)
    mem.append(new_addr)
    return new_addr

# given a child, adds addr/number parent
def add_addr_num(child, string):
        if string.isnumeric():
            child.addParent(value(int(string)))
        else:
            child.addParent(get_address(string, mem))
    
# list of addr objects
mem = []

data = open("example.txt").read()
data = data.split("\n")
for line in tqdm(data):
    if line == "STOP":
        print("at end")
        for addr in mem:
            if addr.name == "a":
                print("a: " + str(addr.getValue()))
                exit(0)
    else:
        spaces = line.count(" ")
        words = line.split(" ")
        # lines with 2 spaces are:
        # addr/number -> addr
        if spaces == 2:
            child = get_address(words.pop(), mem)
            add_addr_num(child, words[0])
        # lines with 3 spaces are:
        # NOT addr/number -> addr
        elif spaces == 3:
            child = get_address(words.pop(), mem)
            not_oppr = opperation("NOT")
            child.addParent(not_oppr)
            add_addr_num(not_oppr, words[1])
        # lines with 4 spaces are:
        # addr/number OPPR addr/number = addr
        elif spaces == 4:
            child = get_address(words.pop(), mem)
            oppr = opperation(words[1])
            child.addParent(oppr)
            add_addr_num(oppr, words[0])
            add_addr_num(oppr, words[2])

