
from tqdm import tqdm

# represents a single light
# doesn't know location
class Light:
    # lights start off
    def __init__(self):
        self.status = 0

    def toggle(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0

    def set(self, new_status):
        self.status = new_status

# represents a 1000x1000 grid of lights
class Grid:
    def __init__(self):
        # make all the lights
        self.lights = []
        for x in range(1000):
            row = []
            for y in range(1000):
                l = Light()
                row.append(l)
            self.lights.append(row)

    def countLit(self):
        litCount = 0
        for row in self.lights:
            for light in row:
                litCount += light.status
        return litCount

# make grid
grid = Grid()

# start reading
data = open("input.txt").read()
data = data.split("\n")
for line in tqdm(data):
    if line == "":
        continue

    # get start_loc and stop_loc as ({int}, {int})
    arr = line.split(" ")
    stop_s = arr[len(arr) - 1].split(",")
    stop = (int(stop_s[0]), int(stop_s[1]))
    start_s = arr[len(arr) - 3].split(",")
    start = (int(start_s[0]), int(start_s[1]))

    for y in range(start[1], stop[1] + 1):
        for x in range(start[0], stop[0] + 1):
            # lines starting with "turn off"
            if "turn off" in line:
                grid.lights[x][y].set(0)
            # lines starting with "turn on"
            elif "turn on" in line:
                grid.lights[x][y].set(1)
            # lines starting with "toggle"
            else:
                grid.lights[x][y].toggle()

print(grid.countLit())

