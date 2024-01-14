
class Triangle():
    def __init__(self, sides):
        self.a = sides[0] 
        self.b = sides[1] 
        self.c = sides[2] 
        self.isValid = False
        if self.a + self.b > self.c:
            if self.b + self.c > self.a:
                if self.a + self.c > self.b:
                    self.isValid = True


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("")
    total = 0
    c = 0 # keeps track of where we are in a given block of 3
    # lines should look like [[int, int, int], [int, int, int], ... ]
    lines = [line.split(" ") for line in lines]
    for line in lines:
        line = [int(x) for x in line if not x == ""]
        match c:
            case 0:
                # 1st side of new triangles
                # make place to store sides, and add first sides
                t0 = [int(line[0])]
                t1 = [int(line[1])]
                t2 = [int(line[2])]
            case 1:
                # add secound sides
                t0.append(int(line[0]))
                t1.append(int(line[1]))
                t2.append(int(line[2]))
            case 2:
                # make triangles with final side, add if valid
                t0.append(int(line[0]))
                t1.append(int(line[1]))
                t2.append(int(line[2]))
                t0 = Triangle(t0)
                t1 = Triangle(t1)
                t2 = Triangle(t2)
                if t0.isValid:
                    total += 1
                if t1.isValid:
                    total += 1
                if t2.isValid:
                    total += 1
        # update c
        if c < 2:
            c += 1
        else:
            c = 0
    print(total)
