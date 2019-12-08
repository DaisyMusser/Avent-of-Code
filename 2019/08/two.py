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


# takes new_layer and background, and returns new background
def layer_reader(new_layer, background):
    new_background = []
    for line in range(6):
        new_line = []
        for digit in range(25):
            if new_layer[line][digit] == 0:
                new_line.append(0)
            elif new_layer[line][digit] == 1:
                new_line.append(1)
            elif new_layer[line][digit] == 2:
                new_line.append(background[line][digit])
        new_background.append(new_line)
    return new_background


# generates image
def image_generator(data):
    data.reverse()
    layer_counter = 0
    for layer in data:
        if layer_counter == 0:
            background = layer
        else:
            background = layer_reader(layer, background)
        layer_counter += 1
    image = background       # symbolic
    return image


def image_printer(image):
    fancy_image = []        # this is all very fancy
    for line in range(6):
        fancy_line = ''
        for digit in range(25):
            if image[line][digit] == 1:
                fancy_line = fancy_line + '#'
            elif image[line][digit] == 0:
                fancy_line = fancy_line + ' '
            else:
                print('--- ERROR ---')
                return
        fancy_image.append(fancy_line)
    for line in fancy_image:
        print(line)
    return


# main program
# file io and data formatting
data = file_reader('input.txt')  # change file name here!
data = data_processor(data)

# image printing
image = image_generator(data)
image_printer(image)


