# Reads file into modules array, code adapted from ( https://github.com/imhoffman/advent/blob/master/2015/01/one.py )
def file_reader(file_name):
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            string_opcode = line
    return string_opcode


# main program:
x = file_reader('input.txt')
print(x)
