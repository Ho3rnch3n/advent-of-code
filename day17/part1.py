with open("input.txt","r") as myinput:
    x_range, y_range = myinput.readline().strip().split(":")[1].split(",")
    x_range = [int(a) for a in x_range.split("=")[1].split("..")]
    y_range = [int(a) for a in y_range.split("=")[1].split("..")]
    
    #after some thinking this is the easiest solution, probably not the intended solution
    print(sum(range(-y_range[0])))