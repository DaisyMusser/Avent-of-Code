# dumps orbits into list
def file_reader(file_name):
    orbit_map = []
    with open(file_name) as file_pointer:
        while True:
            line = file_pointer.readline()
            if not line:
                break
            orbit_map.append(line[0:8])
    return orbit_map


def orbit_sorter(old_orbit_map):
    objects = set()
    orbit_map = []
    for orbit in old_orbit_map:          # removes newline from each item of list
        if orbit != '\n':                # removes newline item from end of list
            orbit_map.append(orbit.replace('\n', ''))

    for orbit in orbit_map:
        x = orbit.split(')')
        for i in range(2):
            objects.add(x[i])

    return orbit_map, objects


# main program
orbit_map = file_reader('input.txt')      # change filename here!
orbit_map, objects = orbit_sorter(orbit_map)

print(len(objects)-1)
