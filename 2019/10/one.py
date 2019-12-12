# to polish steal commets and other updates from two.pyZz
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
                xy = (ii, -i)                 # xy's are tuples
                asteroid_xy.add(xy)           # asteroid_xy is a set
    return asteroid_xy


# main program one: file io and makes asteroid_xy
raw_map = file_reader('input.txt')            # change file name here
asteroid_xy = asteroid_finder(raw_map)


class Asteroid:
    def __init__(self, xy):
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.absolute_map = asteroid_xy         # currently includes the spec asteroid object
        relative_map = []
        for asteroid in self.absolute_map:
            rel_x = asteroid[0] + (self.x * -1)
            rel_y = asteroid[1] + (self.y * -1)
            relative_xy = (rel_x, rel_y)        # relative xy's are tuples
            relative_map.append(relative_xy)
        relative_map.remove((0, 0))
        self.relative_map = relative_map
        return

    def look_for_asteroids(self):
        asteroids_found = set()
        for asteroid in self.relative_map:
            x = asteroid[0]
            y = asteroid[1]
            if x == 0:
                if y > 0:
                    asteroids_found.add('UP')
                else:
                    asteroids_found.add('DOWN')
            elif y == 0:
                if x > 0:
                    asteroids_found.add('RIGHT')
                else:
                    asteroids_found.add('LEFT')
            elif y < 0:
                if x < 0:
                    asteroids_found.add(('III', float(asteroid[0])/float(asteroid[1])))
                else:
                    asteroids_found.add(('IV', float(asteroid[0])/float(asteroid[1])))
            else:
                asteroids_found.add(float(asteroid[0])/float(asteroid[1]))
        return len(asteroids_found)


# main program two:
most_seen = 0
for xy in asteroid_xy:
    spot = Asteroid(xy)
    seen = spot.look_for_asteroids()
    if seen > most_seen:
        most_seen = seen
print(most_seen)    # answer
