with open("input.txt","r") as myinput:
    fishes = myinput.readline().split(",")
    fishes = [int(a) for a in fishes]

    for i in range(80):
        for fishnr,fish in enumerate(fishes):
            if fish == 0:
                #9 because the fish will be counted already on this day
                fishes.append(9)
                fishes[fishnr] = 6
            else:
                fishes[fishnr] -= 1
    print(len(fishes))