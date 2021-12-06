with open("input.txt","r") as myinput:
    data = myinput.readlines()
    #remove trailing newline
    data = list(map(lambda x: x[:-1], data))
    #get a list with lists of each bit
    data = list(zip(*data))
    #black magic
    result = "".join(list(map(lambda x: max(set(x),key = x.count), data)))
    #convert from string to int
    gamma = int(result,2)
    epsilon = gamma ^ 0xfff
    print(gamma * epsilon)