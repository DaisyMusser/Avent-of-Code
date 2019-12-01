# rules:
def feul_counter(mass):
    # devide by 3 round down then subtract 2
    return 0


# Reads file into modules array, code adapted from ( https://github.com/imhoffman/advent/blob/master/2015/01/one.py )
def file_reader(file_name):
    modules = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            modules.append(line)
    return modules


# main function
print(file_reader('input.txt'))
