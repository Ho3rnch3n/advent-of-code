with open("input.txt","r") as myinput:
    horizontal = 0
    vertical = 0
    for line in myinput:
        line = line.split(" ")
        if line[0] == "forward":
            horizontal += int(line[1])
        elif line[0] == "down":
            vertical += int(line[1])
        elif line[0] == "up":
            vertical -= int(line[1])
        else:
            pass
print(horizontal * vertical)