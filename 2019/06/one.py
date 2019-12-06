# dumps orbits into list
def file_reader(file_name):
    orbit_map = []
    with open(file_name) as file_pointer:
        while True:
            line = file_pointer.readline()
            if not line:
                break
            if len(line) == 9:
                orbit_map.append(line[0:8])
    # objects = orbit_map.split(')')
    return orbit_map#, objects


# main program
orbit_map = file_reader('input.txt')      # change filename here!

print(orbit_map)
