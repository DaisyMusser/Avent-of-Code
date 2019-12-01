import math


# takes mass and returns fuel required for that mass alone
def fuel_counter(mass):
    # devide by 3 round down then subtract 2
    print(mass)
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


# big problem with this that I d/t even know how to articulate
def recursive_fuel_calculator(module_fuel, fuel_counter):
    total_fuel = 0
    total_fuel += module_fuel
    last_fuel = module_fuel
    while True:
        current_fuel = fuel_counter(last_fuel)
        if current_fuel == 0:
            break
        total_fuel += current_fuel
        last_fuel = current_fuel
    return total_fuel



   # total_fuel = 0
   # total_fuel += module_fuel
   # last_fuel = module_fuel
   # while fuel_counter(last_fuel) > 0:
   #     total_fuel += fuel_counter(total_fuel)
   #     last_fuel = fuel_counter(total_fuel)
   # return total_fuel


# main function
messy_modules = file_reader('input.txt')  # change here for different file_names
tidy_modules = module_tidier(messy_modules)

total_module_fuel = 0

for i in range(len(tidy_modules)):
    total_module_fuel += (fuel_counter(tidy_modules[i]))

total_fuel = recursive_fuel_calculator(total_module_fuel, fuel_counter)
print(total_fuel)



