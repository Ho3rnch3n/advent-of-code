import collections

def insert_step(template, rules):
    i = 0
    while i < len(template):
        for match, insert in rules:
            if template[i:i + len(match)] == match:
                template = template[:i+1] + insert + template[i+1:]
                i += 1
                break
        i += 1

    return template
            
with open("input.txt","r") as myinput:
    template = myinput.readline().strip()
    _ = myinput.readline()

    rules = list()
    for line in myinput:
        match, insert = line.split("->")
        rules.append([match.strip(), insert.strip()])
    
    
    for i in range(10):
        template = insert_step(template,rules)
    
    occ = collections.Counter(template)
    most = occ.most_common(1)[0]
    least = occ.most_common()[-1]
    result = most[1] - least[1]
    print(result)