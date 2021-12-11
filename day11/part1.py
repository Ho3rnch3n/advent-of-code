def flash_grid(grid):
    y_max = len(grid)
    x_max = len(grid[0])
    flashes = 0
    for y in range(y_max):
        for x in range(x_max):
            if grid[y][x][0] > 9 and grid[y][x][1] == False:
                grid[y][x][1] = True
                flashes += 1
                #jeah this is a mess but ¯\_(ツ)_/¯
                #y-1
                if y-1 >= 0:
                    if x-1 >= 0:
                        grid[y-1][x-1][0] += 1
                    grid[y-1][x][0] += 1
                    if x+1 < x_max:
                        grid[y-1][x+1][0] += 1
                #y
                if x-1 >= 0:
                    grid[y][x-1][0] += 1
                if x+1 < x_max:
                    grid[y][x+1][0] += 1
                #y+1
                if y+1 < y_max:
                    if x-1 >= 0:
                        grid[y+1][x-1][0] += 1
                    grid[y+1][x][0] += 1
                    if x+1 < x_max:
                        grid[y+1][x+1][0] += 1
    return flashes

def calc_round(grid):
    y_max = len(grid)
    x_max = len(grid[0])
    #initial increase
    for y in range(y_max):
        for x in range(x_max):
            grid[y][x][0] += 1
    #as many rounds of flashes as there are
    flashes = 0
    while True:
        new_flashes = flash_grid(grid)
        flashes += new_flashes
        if not new_flashes:
            break
    
    #reset flashed flag
    for y in range(y_max):
        for x in range(x_max):
            if grid[y][x][1] == True:
                grid[y][x][1] = False
                grid[y][x][0] = 0
    
    return flashes

def print_grid(grid):
    y_max = len(grid)
    for y in range(y_max):
        print("".join([str(x[0]) for x in grid[y]]))




with open("input.txt","r") as myinput:
    grid = list()
    for line in myinput:
        line = line.strip()
        grid.append([[int(i),False] for i in line])
    
    flashes = 0
    for i in range(100):
        flashes += calc_round(grid)
    #print_grid(grid)
    print(flashes)