# day 10 part two:
# with station build on asteroid (part one) zap asteroids counter clockwise, and report xy of 200th asteroid

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
        self.asteroids_found = 'NULL'

        # I fill these later, but they need to be some value, hence the zeros
        self.up = 0
        self.right = 0
        self.down = 0
        self.left = 0
        self.i = 0
        self.ii = 0
        self.iii = 0
        self.iv = 0
        return

    # turns a relative xy into an absolute xy
    def relative_to_absolute(self, rel_xy):     # if the answer is wrong, check that this is doing what it s/d
        dummy = []
        dummy.append(rel_xy[0] - (self.x * -1))
        dummy.append(rel_xy[1] - (self.y * -1))
        abs_xy = (dummy[0], dummy[1])
        return abs_xy

    # returns how many asteroids can be seen from a given asteroid
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

    # similar to look_for_asteroids, but formats data so as to be more conveniently zapped
    def generate_zappable_asteroids(self):
        up = []
        right = []
        down = []
        left = []
        i = {}      # these are the quadrants
        ii = {}
        iii = {}
        iv = {}
        for asteroid in self.relative_map:     # there is no 0,0 in rel_map, also all tuples
            rel_rock = self.relative_to_absolute(asteroid)
            x = asteroid[0]
            y = asteroid[1]

            if x == 0:
                if y > 0:      # MAKE ALL OF 'UP' 'DOWN' 'II'... SEPARATE DICTIONARIES W/ KEY: RATIO, VALUE: TUPLE(XY)ZZ
                    up.append(rel_rock)
                else:
                    down.append(rel_rock)
            elif y == 0:
                if x > 0:
                    right.append(rel_rock)
                else:
                    left.append(rel_rock)
            else:   # needs the separate branch to avoid dividing by zero
                ratio = float(asteroid[0])/float(asteroid[1])  # ratio is x/y
                if y < 0:
                    if x < 0:
                        if ratio in iii:
                            iii[ratio].append(rel_rock)
                        else:
                            iii[ratio] = [rel_rock]
                    else:
                        if ratio in iv:
                            iv[ratio].append(rel_rock)
                        else:
                            iv[ratio] = [rel_rock]
                if y > 0:
                    if x > 0:
                        if ratio in i:
                            i[ratio].append(rel_rock)
                        else:
                            i[ratio] = [rel_rock]
                    else:
                        if ratio in ii:
                            ii[ratio].append(rel_rock)
                        else:
                            ii[ratio] = [rel_rock]

        # saves all asteroids into self
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        self.i = i
        self.ii = ii
        self.iii = iii
        self.iv = iv
        return

    def zap_one_asteroid(self, rocks, last_rock, end):   # i think last_asteroid should be the tuple key
        if last_rock == 'FIRST':
            if 'UP' in rocks:
                return
            # fuck i don't know how to do this


    def zap_asteroids(self):
        rocks = self.asteroids_found
        for i in range(200):
            return


# main program two: does other stuff...
most_seen = ['xy', 0]
for xy in asteroid_xy:
    spot = Asteroid(xy)
    seen = spot.look_for_asteroids()
    if seen > most_seen[1]:
        most_seen = [xy, seen]

base = Asteroid(most_seen[0])          # correct asteroid to build a base on
base.generate_zappable_asteroids()


