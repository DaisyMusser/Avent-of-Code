
class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.h = h
        self.w = w

    def get_area(self):
        # total surface area
        area = 2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l
        # also need the area of smallest side
        front = self.l * self.w
        side  = self.h * self.w
        top   = self.l * self.h
        area += min(front, top, side)
        return area

    """
    gets periment of side with smallest
    """
    def get_min_peri(self):
        peris = []
        peris.append(get_peri(self.l, self.w))
        peris.append(get_peri(self.h, self.w))
        peris.append(get_peri(self.h, self.l))
        return min(peris)
        
    def get_volume(self):
        return self.h * self.l * self.w
        
def get_peri(s1, s2):
    return 2*s1 + 2*s2

ribbon = 0
file = open("input.txt")
for line in file:
    dim_strs = line.strip().split("x")
    dims = [int(i) for i in dim_strs]
    box = Box(dims[0], dims[1], dims[2])
    ribbon = ribbon + box.get_min_peri() + box.get_volume()
print(ribbon)

