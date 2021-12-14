import collections, copy

def insert_step(template_dict, rules):
    new_template_dict = copy.deepcopy(template_dict)
    for match, insert in rules:
        if match in template_dict:
            if match[0] + insert in new_template_dict:
                new_template_dict[match[0] + insert] += template_dict[match]
            else:
                new_template_dict[match[0] + insert] = template_dict[match]

            if insert + match[1] in new_template_dict:
                new_template_dict[insert + match[1]] += template_dict[match]
            else:
                new_template_dict[insert + match[1]] = template_dict[match]
            
            new_template_dict[match] -= template_dict[match]

    return new_template_dict
            
with open("input.txt","r") as myinput:
    template = myinput.readline().strip()
    _ = myinput.readline()

    rules = list()
    for line in myinput:
        match, insert = line.split("->")
        rules.append([match.strip(), insert.strip()])
    
    template_dict = {}
    for i in range(len(template) - 1):
        next_key = template[i:i + len(match) - 1]
        if next_key in template_dict:
            template_dict[next_key] += 1
        else:
            template_dict[next_key] = 1
    
    for i in range(40):
        template_dict = insert_step(template_dict,rules)

    res = {}
    for key,value in template_dict.items():
        if key[0] in res:
            res[key[0]] += value
        else:
            res[key[0]] = value
    res[template[-1]] += 1

    occ = collections.Counter(res)
    most = occ.most_common(1)[0]
    least = occ.most_common()[-1]
    result = most[1] - least[1]
    print(result)