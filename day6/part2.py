with open("input.txt","r") as myinput:
    fishes = myinput.readline().split(",")
    startfishes = [int(a) for a in fishes]

    fishes = {}
    for i in range(9):
        fishes[i] = 0
    
    for fish in startfishes:
        fishes[fish] += 1
    
    for i in range(256):
        newfishes = {}
        for i in range(8):
            newfishes[i] = fishes[i+1]
        newfishes[6] += fishes[0]
        newfishes[8] = fishes[0]
        fishes = newfishes

    sumfishes = 0
    for i in range(9):
        sumfishes += fishes[i]
    print(sumfishes)