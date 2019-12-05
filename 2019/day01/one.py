import math


def fuel_counter(mass):
    # devide by 3 round down then subtract 2
    x = mass/3
    x = math.floor(x)
    x -= 2
    if x < 1:
        x = 0
    return x


# Reads file into modules array, code adapted from ( https://github.com/imhoffman/advent/blob/master/2015/01/one.py )
def file_reader(file_name):
    messy_modules = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            messy_modules.append(line)
    return messy_modules


# removes '\n's and converts to int
def module_tidier(messy_modules):
    tidy_modules = []
    for i in range(len(messy_modules)-1):
        tidy_modules.append(messy_modules[i].replace('\n', ''))
        tidy_modules[i] = int(tidy_modules[i])
    return tidy_modules


# main function
messy_modules = file_reader('input.txt')  # change here for different file_names
tidy_modules = module_tidier(messy_modules)

total_fuel = 0

for i in range(len(tidy_modules)):
    total_fuel += (fuel_counter(tidy_modules[i]))

print(total_fuel)

