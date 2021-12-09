with open("input.txt","r") as myinput:
    data = myinput.readline().split(",")
    data = [int(a) for a in data]

    minx = min(data)
    maxx = max(data)
    fuel = {}
    for pos in range(minx,maxx + 1):
        fuel[pos] = 0
        for i in data:
            fuel[pos] += abs(i-pos)
    
    minfuel = min(fuel.values())
    print(minfuel)