
"""
nice string:
    1) at least three from (aeiou)
    2) one char appears twice
    3) does not contain "ab", "cd", "pq", or "xy"
else naughty
"""

vowels  = list("aeiou")
bad_seqs = ["ab", "cd", "pq", "xy"]
data = open("input.txt").read()
data = data.split("\n")
#default true
nice_count = 0
for line in data:
    nice = True
    # 1) vowel check
    num_vowels = 0
    for vowel in vowels:
        num_vowels += line.count(vowel)
    if num_vowels < 3:
        nice = False
    # 2) repeated char check
    double = False
    for i, char in enumerate(line):
        next_i = i + 1
        if next_i < len(line):
            if char == line[next_i]:
                double = True
    if not double:
        nice = False
    # 3) dnc check
    for bad_seq in bad_seqs:
        if bad_seq in line:
            nice = False
    if nice:
        print("add one")
        nice_count += 1
print(nice_count)

