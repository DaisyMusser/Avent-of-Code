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


# counts zeros in layers and returns layer with fewest zeros
# would have been simpler and more idiomatic to use .count
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

    # formats layer conveniently
    real_answer = []
    for line in answer[1]:
        for x in range(25):
            real_answer.append(line[x])
    return real_answer


# main program
data = file_reader('input.txt')  # change file name here!
data = data_processor(data)
layer = zero_counter(data)

# https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
print((layer.count(1))*(layer.count(2)))


