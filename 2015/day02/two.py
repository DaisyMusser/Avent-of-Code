import sys

# reads file into present array
def file_reader(file_name):
    presents = []
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            presents = line
    return presents


# converts str to array
def list_formatter(presents):
    presents = presents.replace('x', ' ')
    presents = presents.replace('\n', ' ')
    presents = presents.split(' ')
    return presents


def paper_calculator(presents):
    total_ribbon = 0
    box_start = 0
    # // method from:
    # https://stackoverflow.com/questions/19824721/i-keep-getting-this-error-for-my-simple-python-program-typeerror-float-obje
    for i in range((len(presents)-2)//3):
        length = int(presents[box_start])
        width = int(presents[box_start+1])
        height = int(presents[box_start+2])
        total_ribbon += length*width*height                     # volume of the box (bow)
        side_one = 2*height+2*length
        side_two = 2*length+2*width
        side_three = 2*width+2*height
        if side_one <= side_two and side_one <= side_three:
            total_ribbon += side_one
        elif side_two <= side_one and side_two <= side_three:
            total_ribbon += side_two
        elif side_three <= side_one and side_three <= side_two:
            total_ribbon += side_three
        box_start += 3
    return total_ribbon


# main program
presents = file_reader('input.txt')     # change here for different file names
presents = list_formatter(presents)
# done with file formatting

# on to file processing
total = paper_calculator(presents)
print(total)


