from pprint import pprint
with open("input.txt","r") as myinput:
    displays = list()
    for line in myinput:
        digits, sol = line.split(" | ")
        digits = list(map(lambda x: "".join(sorted(x)),digits.split()))
        sol = list(map(lambda x: "".join(sorted(x)),sol.split()))
        displays.append([digits,sol])
    
    #just in case i need it for part2
    segment_output = {"0": "abcefg", "1": "cf", "2": "acdeg", "3": "acdfg", "4": "bcdf", "5": "abdfg", "6": "abdefg", "7": "acf", "8": "abcdefg", "9": "abcdfg"}

    counter = 0
    for display in displays:
        for pattern in display[1]:
            #ugly but working
            if len(pattern) == len(segment_output["1"]) or len(pattern) == len(segment_output["4"]) or len(pattern) == len(segment_output["7"]) or len(pattern) == len(segment_output["8"]):
                counter += 1

    print(counter)