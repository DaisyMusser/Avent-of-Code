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
raw_map = file_reader('input.txt')            # change file name here!
asteroid_xy = asteroid_finder(raw_map)


class Asteroid:
    # an asteroid has an xy position, a map, and a relative map
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

    # turns a relative xy into an absolute xy
    def relative_to_absolute(self, rel_xy):     # if the answer is wrong, check that this is doing what it s/d
        abs_xy = []
        abs_xy.append(rel_xy[0] - (self.x * -1))
        abs_xy.append(rel_xy[1] - (self.y * -1))
        return abs_xy

    # counts the number of other asteroids that can be seen from the spec Asteroid object
    def look_for_asteroids(self):
        asteroids_found = {}
        for asteroid in self.relative_map:
            x = asteroid[0]
            y = asteroid[1]
            if x == 0:
                if y > 0:
                    if 'UP' in asteroids_found:
                        asteroids_found['UP'].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found['UP'] = [self.relative_to_absolute(asteroid)]
                else:
                    if 'DOWN' in asteroids_found:
                        asteroids_found['DOWN'].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found['DOWN'] = [self.relative_to_absolute(asteroid)]
            elif y == 0:
                if x > 0:
                    if 'RIGHT' in asteroids_found:
                        asteroids_found['RIGHT'].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found['RIGHT'] = [self.relative_to_absolute(asteroid)]
                else:
                    if 'LEFT' in asteroids_found:
                        asteroids_found['LEFT'].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found['LEFT'] = [self.relative_to_absolute(asteroid)]
            elif y < 0:
                if x < 0:
                    if ('III', float(asteroid[0])/float(asteroid[1])) in asteroids_found:
                        asteroids_found[('III', float(asteroid[0])/float(asteroid[1]))].append[self.relative_to_absolute(asteroid)]
                    else:
                        asteroids_found[('III', float(asteroid[0])/float(asteroid[1]))] = [self.relative_to_absolute(asteroid)]
                else:
                    if ('IV', float(asteroid[0])/float(asteroid[1])) in asteroids_found:
                        asteroids_found[('IV', float(asteroid[0])/float(asteroid[1]))].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found[('IV', float(asteroid[0])/float(asteroid[1]))] = [self.relative_to_absolute(asteroid)]
            else:
                if x > 0:
                    if float(asteroid[0]) / float(asteroid[1]) in asteroids_found:
                        asteroids_found[('I', float(asteroid[0]) / float(asteroid[1]))].append[self.relative_to_absolute(asteroid)]
                    else:
                        asteroids_found[('I', float(asteroid[0]) / float(asteroid[1]))] = [self.relative_to_absolute(asteroid)]
                else:
                    if float(asteroid[0]) / float(asteroid[1]) in asteroids_found:
                        asteroids_found[('II', float(asteroid[0]) / float(asteroid[1]))].append(self.relative_to_absolute(asteroid))
                    else:
                        asteroids_found[('II', float(asteroid[0]) / float(asteroid[1]))] = [self.relative_to_absolute(asteroid)]
        return asteroids_found

    # for i in range(200):


# main program two:
most_seen = ['xy', 0]
for xy in asteroid_xy:
    spot = Asteroid(xy)
    seen = len(spot.look_for_asteroids())
    if seen > most_seen[1]:
        most_seen = [xy, seen]
print(most_seen[0])     # answer for part one, need to use as input to part two code


