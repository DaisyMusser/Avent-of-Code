# reads each line as a separate item onto raw_map ll
# called in asteroids __init__
def file_reader(file_name):
    raw_data = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            raw_data.append(line)
    return raw_data


# takes the input data and finds all the asteroids
# called in asteroids __init__
def asteroid_finder(raw_map):
    asteroid_xy = set()
    for i in range(len(raw_map)):
        for ii in range(len(raw_map[i])):
            if raw_map[i][ii] == '#':
                xy = (ii, -i)                 # xy's are tuples (immutable)
                asteroid_xy.add(xy)           # asteroid_xy is a set
    return asteroid_xy


class Asteroid:
    def __init__(self, xy, asteroid_xy):
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.absolute_map = asteroid_xy
        relative_map = []
        for asteroid in self.absolute_map:
            rel_x = asteroid[0] + (self.x * -1)
            rel_y = asteroid[1] + (self.y * -1)
            relative_xy = (rel_x, rel_y)                 # relative xy's are tuples
            relative_map.append(relative_xy)
        relative_map.remove((0, 0))
        self.relative_map = relative_map
        return

    # returns number of visible asteroids
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


# main program
raw_map = file_reader('input.txt')               # change file_name here
asteroid_xy = asteroid_finder(raw_map)

most_seen = ['xy', 0]
for xy in asteroid_xy:
    seen = []
    spot = Asteroid(xy, asteroid_xy)
    seen.append(xy)
    seen.append(spot.look_for_asteroids())
    if seen[1] > most_seen[1]:
        most_seen = seen
print('answer: ', most_seen[1])    # answer

