import copy

def follow(locations,cur_location,cur_path):
    paths = []
    cur_path.append(cur_location)

    for next_hop in locations[cur_location]["cons"]:
        if locations[next_hop]["visited"] == True:
            continue

        if next_hop == "end":
            cur_path.append("end")
            paths.append(cur_path)
            continue

        if next_hop.islower():
            # only deepcopy if really needed
            deep_locations = copy.deepcopy(locations)
            deep_locations[next_hop]["visited"] = True
        else:
            deep_locations = locations

        # copy by reference = bad
        subpaths = follow(deep_locations,next_hop,cur_path[:])
        paths.extend(subpaths)

    return paths


with open("input.txt","r") as myinput:
    locations = {}

    for line in myinput:
        con1,con2 = line.strip().split("-")
        if not con1 in locations:
            locations[con1] = {"cons": [], "visited": False}
        locations[con1]["cons"].append(con2)
        if not con2 in locations:
            locations[con2] = {"cons": [], "visited": False}
        locations[con2]["cons"].append(con1)
    
    locations["start"]["visited"] = True
    paths = follow(locations,"start",[])
    print(len(paths))
    