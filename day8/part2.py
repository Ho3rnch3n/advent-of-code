from pprint import pprint
import re

with open("input.txt","r") as myinput:
    displays = list()
    for line in myinput:
        digits, sol = line.split(" | ")
        digits = list(map(lambda x: "".join(sorted(x)),digits.split()))
        sol = list(map(lambda x: "".join(sorted(x)),sol.split()))
        displays.append([digits,sol])
    
    segment_output = {"0": "abcefg", "1": "cf", "2": "acdeg", "3": "acdfg", "4": "bcdf", "5": "abdfg", "6": "abdefg", "7": "acf", "8": "abcdefg", "9": "abcdfg"}

    counter = 0
    for display in displays:
        result_digit = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None}
        undecided, solve = display
        undecided = sorted(undecided,key=len)
        #1
        result_digit["c"] = undecided[0]
        result_digit["f"] = undecided[0]
        #7
        res = undecided[1]
        for char in undecided[0]:
            res = res.replace(char,"")
        result_digit["a"] = res
        #4
        res = undecided[2]
        for char in undecided[0]:
            res = res.replace(char,"")
        result_digit["b"] = result_digit["d"] = res
        #2,3,5
        for digit in undecided[3:6]:
            #test if it is a 3
            res = digit
            for char in undecided[0]:
                res = res.replace(char,"")
            if len(res) == 3:
                #its a 3
                digit_3 = digit
                continue
            #test if it is a 5
            res = digit
            for char in undecided[2]:
                res = res.replace(char,"")
            #this works because of the contiune at 3
            if len(res) == 2:
                #its a 5
                digit_5 = digit
                continue
            #this works because of the continues
            digit_2 = digit


        #use number 3 to fixate more
        #fixate d
        not_d = result_digit["d"]
        for char in digit_3:
            not_d = not_d.replace(char,"")
        result_digit["d"] = result_digit["d"].replace(not_d,"")
        result_digit["b"] = not_d
        #fixate g
        g = digit_3
        #remove a and d which are now known
        g = g.replace(result_digit["a"],"").replace(result_digit["d"],"")
        for char in undecided[0]:
            g = g.replace(char,"")
        result_digit["g"] = g

        #use 2 and 3 to fixate e
        e = digit_2
        for char in digit_3:
            e = e.replace(char,"")
        result_digit["e"] = e
        #use 2 to fixate c and f
        f = result_digit["f"]
        for char in digit_2:
            f = f.replace(char,"")
        result_digit["f"] = f
        result_digit["c"] = result_digit["c"].replace(f,"")

        #digit restored
        #jeah this is also ugly
        row_value = ""
        for digit in solve:
            solved_digit = ""
            for char in digit:
                for key,value in result_digit.items():
                    if char == value:
                        solved_digit += key
                        break
            solved_digit = "".join(sorted(solved_digit))

            for key,value in segment_output.items():
                if solved_digit == value:
                    row_value += key
                    break
        counter += int(row_value)

    print(counter)