# reads each line as a separate item onto raw_map ll
def file_reader(file_name):
    raw_data = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            raw_data.append(line)
    return raw_data


def asteroid_finder(raw_map):
    asteroid_xy = set()
    for i in range(len(raw_map)):
        for ii in range(len(raw_map[i])):
            if raw_map[i][ii] == '#':
                xy = (ii, i)                  # xy's are tuples
                asteroid_xy.add(xy)
    return asteroid_xy


# main program
raw_map = file_reader('input.txt')            # change file name here
asteroid_xy = asteroid_finder(raw_map)

print(asteroid_xy)
print(len(asteroid_xy))

