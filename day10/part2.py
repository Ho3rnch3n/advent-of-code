def analyze(line):
    brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}

    while len(line) > 0:
        if line[0] in brackets.keys():
            opening_char = line[0]
        else:
            return line, 0

        line, score = analyze(line[1:])
        if score == -1:
            return line, score
        if len(line) <= 0:
            score = score * 5 + scores[brackets[opening_char]]
            return line, score

        if line[0] != brackets[opening_char]:
            return line, -1

        line = line[1:]
    
    return "",0


with open("input.txt","r") as myinput:
    scores = list()
    for line in myinput:
        line = line.strip()
        _, linescore = analyze(line)
        if linescore != -1:
            scores.append(linescore)
    scores = sorted(scores)
    middle = (len(scores) - 1) // 2
    print(scores[middle])