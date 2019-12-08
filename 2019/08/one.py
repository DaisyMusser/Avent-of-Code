# dumps orbits into list
def file_reader(file_name):
    with open(file_name) as file_pointer:
        while True:
            line = file_pointer.read()
            if not line:
                break
            raw_data = line[0:(len(line)-2)]    # strips \n\n from end of line
    return raw_data


def data_processor(raw_data):
    clean_data = []
    counter = -1
    while True:
        counter += 1
        for line in range(6):
            for digit in range(25):
                clean_data[]

    return clean_data


# main program
raw_data = file_reader('input.txt')  # change file name here!

