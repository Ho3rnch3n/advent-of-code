def follow(locations,cur_location,cur_path):
    paths = []
    cur_path.append(cur_location)

    for next_hop in locations[cur_location]:
        if next_hop == "start":
            continue

        if next_hop == "end":
            paths.append(cur_path + ["end"])
            continue

        if next_hop.islower():
            if next_hop in cur_path:
                continue

        subpaths = follow(locations,next_hop,cur_path[:])
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
            locations[con1] = []
        locations[con1].append(con2)
        if not con2 in locations:
            locations[con2] = []
        locations[con2].append(con1)
    
    paths = follow(locations,"start",[])
    #print_sorted_paths(paths)
    print(len(paths))
    