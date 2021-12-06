from pprint import pprint

scan = [[0] * 1000 for i in range(1000)]
with open("input.txt","r") as myinput:
    #parse data
    data = list()
    for line in myinput:
        parts = line.split(" -> ")
        line = list()
        for x in parts:
            nums = x.split(",")
            nums = [int(x) for x in nums]
            line.append(nums)
        data.append(line)
    
    #build scan
    for line in data:
        #vertical line
        if line[0][0] == line[1][0]:
            smaller = min([line[0][1],line[1][1]])
            bigger = max([line[0][1],line[1][1]])
            #the +1 to also include the last field
            for y in range(smaller,bigger + 1):
                scan[y][line[0][0]] += 1
        #horizontal line
        elif line[0][1] == line[1][1]:
            smaller = min([line[0][0],line[1][0]])
            bigger = max([line[0][0],line[1][0]])
            #the +1 to also include the last field
            for x in range(smaller,bigger + 1):
                scan[line[0][1]][x] += 1
        #diagonal line
        else:
            change = max([line[0][0],line[1][0]]) - min([line[0][0],line[1][0]])
            for delta in range(change + 1):
                x = line[0][0]
                y = line[0][1]
                if line[0][0] < line[1][0] and line[0][1] < line[1][1]:
                    scan[y+delta][x+delta] += 1
                elif line[0][0] > line[1][0] and line[0][1] < line[1][1]:
                    scan[y+delta][x-delta] += 1
                elif line[0][0] < line[1][0] and line[0][1] > line[1][1]:
                    scan[y-delta][x+delta] += 1
                elif line[0][0] > line[1][0] and line[0][1] > line[1][1]:
                    scan[y-delta][x-delta] += 1
            
    #analyze scan
    dangerous = 0
    for y in range(1000):
        for x in range(1000):
            if scan[y][x] >= 2:
                dangerous += 1
    print(dangerous)
