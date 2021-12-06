with open("input.txt","r") as myinput:
    horizontal = 0
    vertical = 0
    aim = 0
    for line in myinput:
        line = line.split(" ")
        if line[0] == "forward":
            horizontal += int(line[1])
            vertical += (int(line[1]) * aim)
        elif line[0] == "down":
            aim += int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])
        else:
            pass
print(horizontal * vertical)