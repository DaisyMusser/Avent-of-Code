# reads file into array
def file_reader(file_name):
    directions = []
    with open(file_name) as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            directions.append(line)
    return directions


directions = file_reader('input.txt')    # change here for different file names
print( directions )
print( len(directions) )
