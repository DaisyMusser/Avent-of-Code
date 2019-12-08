# dumps orbits into list
def file_reader(file_name):
    with open(file_name) as file_pointer:
        while True:
            line = file_pointer.read()
            if not line:
                break
            raw_data = line[0:(len(line)-2)]    # strips \n\n from end of line
    return raw_data


# stealing populating method from: https://www.ict.social/python/basics/multidimensional-lists-in-python
def data_processor(raw_data):
    counter = 0
    clean_data = []
    while True:
        layer = []
        for _ in range(6):
            line = []
            for _ in range(25):
                if counter == len(raw_data):
                    return clean_data
                line.append(int(raw_data[counter]))
                counter += 1
            layer.append(line)
        clean_data.append(layer)


# use .count method https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
def zero_counter(data):
    answer = [9999999999, 'ERROR']    # [0]: lowest number of zeros, [1]: layer with that number of zeros
    for layer in data:
        zeros = 0   # lol
        for line in range(6):
            for x in layer[line]:
                if x == 0:
                    zeros += 1
        if zeros < answer[0]:
            answer[0] = zeros
            answer[1] = layer
    return answer[1]



# main program
data = file_reader('input.txt')  # change file name here!
data = data_processor(data)
layer = zero_counter(data)

print(layer)

