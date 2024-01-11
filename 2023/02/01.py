import re

class Game():
    def __init__(self, record: str):
        self.id = int(re.search("^Game .*:", record).group(0)[5:-1])
        greens = [int(c) for c in re.findall("[0-9]+(?= green)", record)]
        self.maxgreen = sorted(greens)[-1]
        blues = [int(c) for c in re.findall("[0-9]+(?= blue)", record)]
        self.maxblue = sorted(blues)[-1] 
        reds = [int(c) for c in re.findall("[0-9]+(?= red)", record)]
        self.maxred = sorted(reds)[-1]
    
    def isValid(self) -> bool:
        greencubes = 13
        bluecubes  = 14
        redcubes   = 12
        if self.maxgreen <= greencubes:
            if self.maxblue <= bluecubes:
                if self.maxred <= redcubes:
                    return True
        return False


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("")
    total = 0 
    for line in lines:
        g = Game(line)
        if g.isValid():
            total += g.id
    print(total)


