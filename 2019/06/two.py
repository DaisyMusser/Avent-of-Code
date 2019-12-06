# from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
import time
start_time = time.time()

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


# parses orbit_map into a more workable orbit_map and the set of all objects
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


# given the base orbit it counts its way up and returns the number of orbits
def orbit_counter_upper(object, orbit_map):
    orbit_tree = []
    one_up = object
    while base_search(one_up, orbit_map) != -1:
        x = base_search(one_up, orbit_map)
        one_up = x[0:3]
        orbit_tree.append(x[0:3])
    return orbit_tree


# returns base orbit of an object
def base_search(object, orbit_map):
    for orbit in orbit_map:
        if orbit[4:7] == object:
            return orbit
    return -1


# finds orbital path between x and y
def orbital_route_calculator(orbit_map, x, y):
    orbital_route = []

    me_tree = orbit_counter_upper(x, orbit_map)
    san_tree = orbit_counter_upper(y, orbit_map)

    done = False
    for me_object in me_tree:
        if not done:                       # not totally sure why this is needed, but it really is
            for san_object in san_tree:
                if me_object == san_object:
                    my_intersection = me_tree.index(me_object)
                    san_intersection = san_tree.index(san_object)
                    done = True

    my_route = me_tree[0:my_intersection]
    san_route = san_tree[0:san_intersection+1]
    san_route.reverse()      # for space flight convenience

    for c in my_route:
        orbital_route.append(c)
    for c in san_route:
        orbital_route.append(c)

    return orbital_route


# main program
orbit_map = file_reader('input.txt')      # change filename here!
orbit_map, objects = orbit_sorter(orbit_map)
objects.remove('COM')

orbital_route = orbital_route_calculator(orbit_map, 'YOU', 'SAN')
print('Answer: ', len(orbital_route)-1)

