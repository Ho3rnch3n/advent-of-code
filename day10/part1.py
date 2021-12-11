def analyze(line):
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 3, "]":57, "}": 1197, ">": 25137}

    while len(line) > 0:
        if line[0] in brackets.keys():
            opening_char = line[0]
        else:
            return line, 0

        line, score = analyze(line[1:])
        if score > 0 or len(line) <= 0:
            return line,score

        if line[0] != brackets[opening_char]:
            return line, scores[line[0]]

        line = line[1:]
    
    return "",0


with open("input.txt","r") as myinput:
    score = 0
    for line in myinput:
        line = line.strip()
        _, linescore = analyze(line)
        score += linescore
    print(score)