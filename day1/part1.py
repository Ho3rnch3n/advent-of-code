with open("input.txt","r") as myinput:
    data = myinput.readlines()
    data = [int(a) for a in data]
    inc = 0
    for a,d in zip(data, data[1:]):
        if a < d:
            inc +=1
print("Part 1: " + str(inc))