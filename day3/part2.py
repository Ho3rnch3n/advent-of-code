with open("input.txt","r") as myinput:
    data = myinput.readlines()
    #remove trailing newline
    data = list(map(lambda x: x[:-1], data))
    max_iter = len(data[0])

    #calculate oxygen (max number)
    remaining = data
    for i in range(max_iter):
        if len(remaining) <= 1:
            break
        #get a list with lists of each bit
        bytelists = list(zip(*remaining))
        #check if there are more 1 or 0 in the nth bit
        if bytelists[i].count('1') >= bytelists[i].count('0'):
            #if there are more or equal 1s keep all with 1
            remaining = [x for x in remaining if x[i].startswith('1')]
        else: #keep all with 0
            remaining = [x for x in remaining if not x[i].startswith('1')]
    oxygen = int(remaining[0],2)
    
    #calculate co2 (min number)
    remaining = data
    for i in range(max_iter):
        if len(remaining) <= 1:
            break
        #get a list with lists of each bit
        bytelists = list(zip(*remaining))
        #check if there are more 1 or 0 in the nth bit
        if bytelists[i].count('1') >= bytelists[i].count('0'):
            #if there are less or equal 0s keep all with 0
            remaining = [x for x in remaining if x[i].startswith('0')]
        else: #keep all with 1
            remaining = [x for x in remaining if not x[i].startswith('0')]
    co2 = int(remaining[0],2)
    
    print(oxygen * co2)