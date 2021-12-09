#this is slow...
with open("input.txt","r") as myinput:
    data = myinput.readline().split(",")
    data = [int(a) for a in data]

    minx = min(data)
    maxx = max(data)
    fuel = {}
    for pos in range(minx,maxx + 1):
        fuel[pos] = 0
        for i in data:
            fuel[pos] += sum(list(range(abs(i-pos)+1)))
    
    minfuel = min(fuel.values())
    print(minfuel)