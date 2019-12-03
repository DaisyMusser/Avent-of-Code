# 
def file_reader(file_name):
    presents = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            presents.append(line)
    return presents


# main program
presents = file_reader("input.txt")
print(presents)
