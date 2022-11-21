
data = open("test.txt").read()
data = data.split("\n")
for line in data:
    # unless...
    # rule 1: must be xxybkxx or xxxx not xxx for some x
    # get all unique letters
    passed_one = False
    passed_both = False
    line_list = [*line]
    char_set = set(line_list)
    for letter in char_set:
        # only check next letter if we havn't passed rule one yet
        if not passed_one:
            all_runs = {}
            current_run = 1
            # don't consider the last char in line
            for i, other_letter in enumerate(line_list[:-1]):
                if other_letter == letter:
                    if other_letter == line_list[i + 1]:
                        # next matches
                        current_run += 1
                    else:
                        # next doesn't match
                        if current_run > 1:
                            # we have some run
                            tag = str(current_run)
                            current_run = 1
                            if tag in all_runs.keys():
                                all_runs[tag] += 1
                            else:
                                all_runs[tag] = 1
        num_2and3s = 0
        if all_runs.get("2"):
            num_2and3s += all_runs["2"]
        if all_runs.get("3"):
            num_2and3s += all_runs["3"]
        if num_2and3s > 1:
            passed_one = True
            if all_runs.get("3"):
                # must have passed rule two as well!
                passed_both = True
        if all_runs.get("4"):
            passed_one = True
            # must have passed rule two as well!
            passed_both = True


    # or, rule 2:
    # for some x, need something like xyx, xax, or even xxx
    passed_two = False

