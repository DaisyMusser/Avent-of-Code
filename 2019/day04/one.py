# gets input
def file_reader(file_name):
    with open(file_name) as fp:
        while True:
            line = fp.read()
            if not line:
                break
            puzzle = line.split('-')
    return puzzle



# main program
range = file_reader('input.txt')
print(range)