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
                xy = (ii, -i)                  # xy's are tuples
                asteroid_xy.add(xy)           # asteroid_xy is a set
    return asteroid_xy


# main program one: file io and makes asteroid_xy
raw_map = file_reader('input.txt')            # change file name here
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

    # counts the number of other asteroids that can be seen from the spec Asteroid object
    def look_for_asteroids(self):
        asteroids_found = {}
        for asteroid in self.relative_map:
            x = asteroid[0]
            y = asteroid[1]
            if x == 0:
                if y > 0:
                    if 'UP' in asteroids_found:
                        asteroids_found['UP'] += 1
                    else:
                        asteroids_found['UP'] = 1
                else:
                    if 'DOWN' in asteroids_found:
                        asteroids_found['DOWN'] += 1
                    else:
                        asteroids_found['DOWN'] = 1
            elif y == 0:
                if x > 0:
                    if 'RIGHT' in asteroids_found:
                        asteroids_found['RIGHT'] += 1
                    else:
                        asteroids_found['RIGHT'] = 1
                else:
                    if 'LEFT' in asteroids_found:
                        asteroids_found['LEFT'] += 1
                    else:
                        asteroids_found['LEFT'] = 1
            elif y < 0:
                if x < 0:
                    if ('III', float(asteroid[0])/float(asteroid[1])) in asteroids_found:
                        asteroids_found[('III', float(asteroid[0])/float(asteroid[1]))] += 1
                    else:
                        asteroids_found[('III', float(asteroid[0])/float(asteroid[1]))] = 1
                else:
                    if ('IV', float(asteroid[0])/float(asteroid[1])) in asteroids_found:
                        asteroids_found[('IV', float(asteroid[0])/float(asteroid[1]))] += 1
                    else:
                        asteroids_found[('IV', float(asteroid[0])/float(asteroid[1]))] = 1
            else:
                if float(asteroid[0])/float(asteroid[1]) in asteroids_found:
                    asteroids_found[float(asteroid[0])/float(asteroid[1])] += 1
                else:
                    asteroids_found[float(asteroid[0])/float(asteroid[1])] = 1
        return len(asteroids_found)

    # def zap(self):


# main program two:
most_seen = ['xy', 0]
for xy in asteroid_xy:
    spot = Asteroid(xy)
    seen = spot.look_for_asteroids()
    if seen > most_seen[1]:
        most_seen = [xy, seen]
print(most_seen[0])    # answer
