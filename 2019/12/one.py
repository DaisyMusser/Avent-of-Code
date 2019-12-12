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
    x = ''
    for string in list_of_strings:
        x += string
    return int(x)


def formatter(locations):
    formatted_loc = []
    for i in range(4):
        x_start = (locations[i].index('x')) + 2
        dummy = []
        for ii in range(10):
            x = locations[i][x_start + ii]
            if x == ',':
                break
            dummy.append(x)
        x_value = int_maker(dummy)

        y_start = (locations[i].index('y')) + 2
        dummy = []
        for ii in range(100):
            x = locations[i][y_start + ii]
            if x == ',':
                break
            dummy.append(x)
        y_value = int_maker(dummy)

        z_start = (locations[i].index('z')) + 2
        dummy = []
        for ii in range(100):
            x = locations[i][z_start + ii]
            if x == '>':
                break
            dummy.append(x)
        z_value = int_maker(dummy)

        formatted_loc.append([x_value, y_value, z_value])
    return formatted_loc


class JupMoon(object):
    def __init__(self, x, y, z):
        self.loc = [x, y, z]
        self.x = x
        self.y = y
        self.z = z
        return

    def apply_gravity(self, moon_one, moon_two, moon_three):   # pass in loc of other three moons
       for i in range(3)

    def apply_velocity(self):



# main program
locations = file_to_string('input.txt')    # change file names here
locations = formatter(locations)

print(locations)
