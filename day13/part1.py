def print_map(mymap):
    y_max = len(mymap)
    x_max = len(mymap[0])
    for y in range(y_max):
        line = ""
        for x in range(x_max):
            if mymap[y][x] == True:
                line += "#"
            else:
                line += "."
        print(line)

def fold_x(mymap,pos):
    x_orig_len = len(mymap[0])
    #print(mymap)

    part1 = [list(a) for a in zip(*mymap)][:pos]
    part1 = [list(a) for a in zip(*part1)]
    #the middle line gets terminated
    part2 = [list(a) for a in zip(*mymap)][pos + 1:]
    #flip it
    part2 = part2[::-1]
    part2 = [list(a) for a in zip(*part2)]
    
    y_max = len(part1)
    x_max = len(part1[0])

    for y in range(y_max):
        for x in range(x_max):
            part1[y][x] = part1[y][x] | part2[y][x]
    
    return part1

def fold_y(mymap,pos):
    part1 = mymap[:pos]
    #the middle line gets terminated
    part2 = mymap[pos+1:]
    #flip it
    part2 = part2[::-1]

    y_max = len(part1)
    x_max = len(part1[0])

    for y in range(y_max):
        for x in range(x_max):
            part1[y][x] = part1[y][x] | part2[y][x]
    
    return part1

with open("input.txt","r") as myinput:
    points = list()
    #parse points
    for line in myinput:
        if line == "\n":
            break
        line = line.split(",")
        x = int(line[0])
        y = int(line[1])
        points.append([y,x])

    x_max = max(list(zip(*points))[1])
    y_max = max(list(zip(*points))[0])

    folds = list()
    #parse folds
    for line in myinput:
        axis,place = line.split()[2].split("=")
        folds.append([axis,int(place)])

    #create map
    mymap = [[False] * (x_max + 1) for i in range(y_max + 1)]

    #initial fill
    for point in points:
        mymap[point[0]][point[1]] = True
    
    #perform folds:
    for axis,place in folds:
        if axis == "x":
            mymap = fold_x(mymap,place)
        if axis == "y":
            mymap = fold_y(mymap,place)
        #break after the first..
        break
    #print_map(mymap)

    y_max = len(mymap)
    x_max = len(mymap[0])
    counter = 0
    for y in range(y_max):
        for x in range(x_max):
            if mymap[y][x] == True:
                counter +=1
    print(counter)