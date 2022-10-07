
class box:
    def __init__(self, l, w, h):
        self.l = l
        self.h = h
        self.w = w

    def get_area():
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
    def get_min_peri():
        peris = []
        for 

        
    def get_volume():
        return self.h * self.l * self.w
        
def get_peri(s1, s2):
    return 2*s1 + 2*s2

total_area = 0
file = open("input.txt")
for line in file:
    dim_strs = line.strip().split("x")
    dims = [int(i) for i in dim_strs]
    total_area += get_area(dims[0], dims[1], dims[2])
print(total_area)

