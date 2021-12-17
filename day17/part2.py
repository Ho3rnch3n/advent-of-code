with open("input.txt","r") as myinput:
    x_range, y_range = myinput.readline().strip().split(":")[1].split(",")
    x_range = [int(a) for a in x_range.split("=")[1].split("..")]
    y_range = [int(a) for a in y_range.split("=")[1].split("..")]
    
    in_area = 0
    for x in range(x_range[1] + 1):
        for y in range(y_range[0], -y_range[0]):
            x_pos = 0
            y_pos = 0
            next_x = x
            next_y = y
            while True:
                x_pos += next_x
                y_pos += next_y
                #check if in
                if x_range[0] <= x_pos <= x_range[1] and y_range[0] <= y_pos <= y_range[1]:
                    in_area += 1
                    break
                #check if beyond
                if x_range[1] < x_pos or y_range[0] > y_pos:
                    break
                #calc new values
                next_x -= 1
                if next_x < 0:
                    next_x = 0
                next_y -= 1
    print(in_area)