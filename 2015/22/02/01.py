
def get_area(l, w, h):
    # total surface area
    area = 2*l*w + 2*w*h + 2*h*l
    # also need the area of smallest side
    front = l * w
    side  = h * w
    top   = l * h
    area += min(front, top, side)
    return area

total_area = 0
file = open("input.txt")
for line in file:
    dim_strs = line.strip().split("x")
    dims = [int(i) for i in dim_strs]
    total_area += get_area(dims[0], dims[1], dims[2])
print(total_area)

