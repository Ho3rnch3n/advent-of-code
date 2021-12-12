import copy

def follow(locations,cur_location,cur_path):
    paths = []
    cur_path.append(cur_location)

    for next_hop in locations[cur_location]["cons"]:
        if next_hop == "start":
            continue

        exception_counter = 0
        exception_hardlimit = False
        for x in locations.keys():
            if not x[0].islower():
                continue
            if locations[x]["visited"] > 1:
                exception_counter += 1
            if locations[x]["visited"] > 2:
                exception_hardlimit = True
        if exception_counter > 1 or exception_hardlimit == True:
            continue

        if next_hop == "end":
            cur_path.append("end")
            paths.append(cur_path)
            continue

        if next_hop.islower():
            # only deepcopy if really needed -> still slow as shit..
            deep_locations = copy.deepcopy(locations)
            deep_locations[next_hop]["visited"] += 1
        else:
            deep_locations = locations

        # copy by reference = bad
        subpaths = follow(deep_locations,next_hop,cur_path[:])
        paths.extend(subpaths)

    return paths

def print_sorted_paths(paths):
    string_paths = []
    for path in paths:
        string_paths.append(",".join(path))
    string_paths = sorted(string_paths)
    for path in string_paths:
        print(path)

with open("input.txt","r") as myinput:
    locations = {}

    for line in myinput:
        con1,con2 = line.strip().split("-")
        if not con1 in locations:
            locations[con1] = {"cons": [], "visited": 0}
        locations[con1]["cons"].append(con2)
        if not con2 in locations:
            locations[con2] = {"cons": [], "visited": 0}
        locations[con2]["cons"].append(con1)
    
    paths = follow(locations,"start",[])
    #print_sorted_paths(paths)
    print(len(paths))
    