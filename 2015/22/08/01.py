import re

# given a string and a sub, returns a copy of string with sub removed
def eatSub(s, sub):
    i   = s.find(sub)
    sub = list(sub)
    s   = list(s)
    for x in range(len(sub)):
        s[i + x] = "-"
    return "".join(s)

# Given string s and a sub, replaces sub with r
def repSub(s, sub, r):
    i   = s.find(sub)
    sub = list(sub)
    s   = list(s)
    r   = list(r)
    for x in range(len(sub)):
        s.pop(i)
    r.reverse()
    for r_char in r:
        s.insert(i, r_char)
    return "".join(s) 


if __name__ == "__main__":
    lines = open("input.txt").read().split("\n")
    lines.remove("")

    total_code = 0
    total_mem  = 0
    
    for s in lines:
        total_code += len(s)
        # now replace all code with literals 
        # drop quotes
        s = s[1:-1]
        while r"\\" in s:  # rep with \
            s = repSub(s, r"\\", "*")
        while r"\"" in s:  # rep with "
            s = repSub(s, r"\"", "*")
        #m = re.findall("\x(([0-9]|[A-F]){2})", s) # rep with '
        m = re.findall(r"\\x[0-9A-Fa-f]{2}", s) # rep with '
        for sub in m:
            s = repSub(s, sub, "*")
        total_mem += len(s)

    print(total_code)
    print(total_mem)
    print(total_code - total_mem)

# 872 is too low.
# 1385 is too high.
