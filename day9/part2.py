from pprint import pprint
from collections import Counter

def analyze(data,y,x,old_min):
    if data[y][x]["analyzed"] == True:
        if data[y][x]["height"] < old_min:
            return 0
        if data[y][x]["height"] == old_min:
            return 1
        return 0

    y_max = len(data) - 1
    x_max = len(data[0]) - 1
    neighbours = list()
    if y-1 >= 0:
        neighbours.append([data[y-1][x]["height"],y-1,x])
    if x-1 >= 0:
        neighbours.append([data[y][x-1]["height"],y,x-1])
    if y+1 <= y_max:
        neighbours.append([data[y+1][x]["height"],y+1,x])
    if x+1 <= x_max:
        neighbours.append([data[y][x+1]["height"],y,x+1])
    
    data[y][x]["analyzed"] = True
    if data[y][x]["height"] < min(list(zip(*neighbours))[0]):
        data[y][x]["deepest"] = True
        return 0
    elif data[y][x]["height"] == min(list(zip(*neighbours))[0]):
        to_analyze = []
        for next_neighbour in neighbours:
            if next_neighbour[0] == data[y][x]["height"]:
                to_analyze.append(next_neighbour)
        lowest = True
        for another_one in to_analyze:
            if not analyze(data,another_one[1],another_one[2],another_one[0]):
                lowest = False
        if lowest == True:
            data[y][x]["deepest"] = True
            return 1

def calc_basin(num,data,y,x):
    if data[y][x]["basin"] != None:
        return 0
    if data[y][x]["height"] == 9:
        return 0
    data[y][x]["basin"] = num

    y_max = len(data) - 1
    x_max = len(data[0]) - 1
    neighbours = list()
    if y-1 >= 0:
        neighbours.append([data[y-1][x]["height"],y-1,x])
    if x-1 >= 0:
        neighbours.append([data[y][x-1]["height"],y,x-1])
    if y+1 <= y_max:
        neighbours.append([data[y+1][x]["height"],y+1,x])
    if x+1 <= x_max:
        neighbours.append([data[y][x+1]["height"],y,x+1])
    
    for next_neighbour in neighbours:
        calc_basin(num,data,next_neighbour[1],next_neighbour[2])

with open("input.txt","r") as myinput:
    data = myinput.readlines()
    data = [[{"height": int(y), "deepest": False, "analyzed": False, "basin": None} for y in x.strip()] for x in data]
    
    for y in range(len(data)):
        for x in range(len(data[0])):
            analyze(data,y,x,10)

    basin_num = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]["deepest"] == True:
                calc_basin(basin_num,data,y,x)
                basin_num += 1
    basins = {}
    for i in range(basin_num):
        basins[i] = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]["basin"] != None:
                basins[data[y][x]["basin"]] += 1
    
    sol = 1
    largest = Counter(basins).most_common(3)
    for i in largest:
        sol *= i[1]
    print(sol)