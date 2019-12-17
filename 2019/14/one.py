# day 14: how much ore is needed for fuel?

# file io
def grab_input(file_name):
    reactions = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            if line == '\n':
                break
            reactions.append(line.rstrip())
    return reactions


# formatting data
def clean_up(raw):
    for i in range(len(raw)):
        raw[i] = raw[i].split('=>')
    return raw


# main program
raw = grab_input('input.txt')      # change file_name here 
raw = clean_up(raw)
for line in raw:
    print(line)
            
