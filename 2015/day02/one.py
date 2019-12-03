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
    total_paper = 0
    box_start = 0
    # // method from:
    # https://stackoverflow.com/questions/19824721/i-keep-getting-this-error-for-my-simple-python-program-typeerror-float-obje
    for i in range((len(presents)-2)//3):
        l = int(presents[box_start])
        w = int(presents[box_start+1])
        h = int(presents[box_start+2])
        total_paper += 2*l*w + 2*w*h + 2*h*l   # surface area of box
        side_one = h*l
        side_two = l*w
        side_three = w*h
        if side_one <= side_two and side_one <= side_three:
            total_paper += side_one
        elif side_two <= side_one and side_two <= side_three:
            total_paper += side_two
        elif side_three <= side_one and side_three <= side_two:
            total_paper += side_three
        box_start += 3
    return total_paper


# main program
presents = file_reader('input.txt')     # change here for different file names
presents = list_formatter(presents)
# done with file formatting

# on to file processing
total = paper_calculator(presents)
print(total)


