import heapq

with open("input.txt","r") as myinput:
    cave_map_old = [[{"risk": int(x), "visited": False} for x in line.strip()] for line in myinput]
    
    y_max_old = len(cave_map_old)
    x_max_old = len(cave_map_old[0])

    cave_map = [[{"risk": 0, "visited": False} for j in range(5 * len(cave_map_old[0]))] for i in range(5 * len(cave_map_old))]
    
    for y in range(len(cave_map)):
        for x in range(len(cave_map[0])):
            cave_map[y][x]["risk"] = ((cave_map_old[y % y_max_old][x % x_max_old]["risk"] + y // y_max_old + x // x_max_old) - 1) % 9 + 1

    y_max = len(cave_map) - 1
    x_max = len(cave_map[0]) - 1

    queue = [(0,[0,0])]
    heapq.heapify(queue)

    while True:
        risk,(y,x) = heapq.heappop(queue)
        
        if cave_map[y][x]["visited"]:
            continue

        cave_map[y][x]["risk"] = risk
        cave_map[y][x]["visited"] = True

        if y == y_max and x == x_max:
            print(cave_map[y][x]["risk"])
            break

        for dy,dx in [[y,x-1],[y-1,x],[y,x+1],[y+1,x]]:
            if dy < 0 or dx < 0 or y_max < dy or x_max < dx:
                continue
            if cave_map[dy][dx]["visited"]:
                continue
            heapq.heappush(queue,(risk + cave_map[dy][dx]["risk"],[dy, dx]))