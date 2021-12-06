with open("input.txt","r") as myinput:
    callednumbers = myinput.readline()[:-1].split(",")
    callednumbers = [int(a) for a in callednumbers]
    _ = myinput.readline()
    data = list()
    board = 0
    #parse inputfile
    for line in myinput:
        #empty lines mean that a new board will begin
        if line == "\n":
            board += 1
            continue
        if len(data) <= board:
            data.append(list())
        line = [int(a) for a in line[:-1].split()]
        for i,num in enumerate(line):
            line[i] = {"value":num, "marked":False}
        data[board].append(line)
    

    #play game
    board_size = 5
    bingo = False
    winners = list()
    for number in callednumbers:
        #first mark new numbers
        for board in data:
            for line in board:
                for num in line:
                    if number == num["value"]:
                        num["marked"] = True
        #check if row or column is all marked
        for board in data:
            for checknr in range(board_size):
                #check rows
                markednums = 0
                for num in board[checknr]:
                    if num["marked"] == True:
                        markednums +=1
                if markednums == board_size:
                    bingo = True
                    break
                #check columns
                columns = list(zip(*board))
                markednums = 0
                for num in columns[checknr]:
                     if num["marked"] == True:
                        markednums +=1
                if markednums == board_size:
                    bingo = True
                    break
            if bingo == True:
                #create list of winners because more than one board can win at one called number
                winners.append(board)
                bingo = False
                
        if len(winners):
            if len(data) == 1:
                unmarkedsum = 0
                for line in data[0]:
                    for num in line:
                        if num["marked"] == False:
                            unmarkedsum += num["value"]
                print(unmarkedsum * number)
                break
            #this is at the end because we also want the last board to win
            for winner in winners:
                data.remove(winner)
            winners = list()