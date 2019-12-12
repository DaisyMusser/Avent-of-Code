# day 12: tracking the moons
def file_to_string(file_name):
    locations = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:         # a little bit of error catching
                break
            locations.append(line)
    return locations


def int_maker(list_of_strings):
    return int(list_of_strings[0:len(list_of_strings)])


def formatter(locations):
    formatted_loc = []
    for i in range(4):

        x_start = (locations[i].index('x')) + 2
        dummy = []
        for i in range(100):
            x = locations[x_start + i]
            if x == ',':
                break
            dummy.append(x)
        x_value = int_maker(dummy)

        y_start = (locations[i].index('y')) + 2
        dummy = []
        for i in range(100):
            x = locations[y_start + i]
            if x == ',':
                break
            dummy.append(x)
        y_value = int_maker(dummy)

        z_start = (locations[i].index('z')) + 2
        dummy = []
        for i in range(100):
            x = locations[z_start + i]
            if x == '>':
                break
            dummy.append(x)
        z_value = int_maker(dummy)

        formatted_loc.append([x_value, y_value, z_value])
    return formatted_loc


# main program
locations = file_to_string('input.txt')    # change file names here
locations = formatter(locations)

print(locations)
