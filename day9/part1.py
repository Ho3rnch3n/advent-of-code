from pprint import pprint

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

with open("input.txt","r") as myinput:
    data = myinput.readlines()
    data = [[{"height": int(y), "deepest": False, "analyzed": False} for y in x.strip()] for x in data]
    
    for y in range(len(data)):
        for x in range(len(data[0])):
            analyze(data,y,x,10)

    risk = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]["deepest"] == True:
                risk += data[y][x]["height"] + 1
    #pprint(data)
    print(risk)