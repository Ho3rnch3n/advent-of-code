'''
with open("input.txt","r") as myinput:
    a = int(myinput.readline())
    b = int(myinput.readline())
    c = int(myinput.readline())
    old = a + b + c
    increases = 0
    for line in myinput:
        line = int(line)
        mysum = b + c + line
        if mysum > old:
            increases += 1
        old = mysum
        a = b
        b = c
        c = line
print(increases)
'''

with open("input.txt","r") as myinput:
    data = myinput.readlines()
    data = [int(a) for a in data]
    inc = 0
    for a,d in zip(data, data[3:]):
        if a < d:
            inc +=1
print("Part 2: " + str(inc))