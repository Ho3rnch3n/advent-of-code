import ast, math, itertools, copy

def split(number):
    return [number // 2, math.ceil(number / 2)]

def check_explode(data):
    #messy as shit
    for ind_a, a in enumerate(data):
        if type(a) == list:
            for ind_b, b in enumerate(a):
                if type(b) == list:
                    for ind_c, c in enumerate(b):
                        if type(c) == list:
                            for ind_d, d in enumerate(c):
                                if type(d) == list:
                                    #left side
                                    if not ind_d - 1 < 0:
                                        if type(c[ind_d - 1]) == list:
                                            c[ind_d - 1][-1] += d[0]
                                        else:
                                            c[ind_d - 1] += d[0]
                                    elif not ind_c - 1 < 0:
                                        if type(b[ind_c - 1]) == list:
                                            if type(b[ind_c - 1][-1]) == list:
                                                b[ind_c - 1][-1][-1] += d[0]
                                            else:
                                                b[ind_c - 1][-1] += d[0]
                                        else:
                                            b[ind_c - 1] += d[0]
                                    elif not ind_b - 1 < 0:
                                        if type(a[ind_b - 1]) == list:
                                            if type(a[ind_b - 1][-1]) == list:
                                                if type(a[ind_b - 1][-1][-1]) == list:
                                                    a[ind_b - 1][-1][-1][-1] += d[0]
                                                else:
                                                    a[ind_b - 1][-1][-1] += d[0]
                                            else:
                                                a[ind_b -1][-1] += d[0]
                                        else:
                                            a[ind_b - 1] += d[0]
                                    elif not ind_a - 1 < 0:
                                        if type(data[ind_a - 1]) == list:
                                            if type(data[ind_a - 1][-1]) == list:
                                                if type(data[ind_a - 1][-1][-1]) == list:
                                                    if type(data[ind_a - 1][-1][-1][-1]) == list:
                                                        data[ind_a -1][-1][-1][-1][-1] += d[0]
                                                    else:
                                                        data[ind_a -1][-1][-1][-1] += d[0]
                                                else:
                                                    data[ind_a -1][-1][-1] += d[0]
                                            else:
                                                data[ind_a -1][-1] += d[0]
                                        else:
                                            data[ind_a - 1] += d[0]
                                    #right side
                                    if not ind_d + 1 >= len(d):
                                        if type(c[ind_d + 1]) == list:
                                            c[ind_d + 1][0] += d[1]
                                        else:
                                            c[ind_d + 1] += d[1]
                                    elif not ind_c + 1 >= len(c):
                                        if type(b[ind_c + 1]) == list:
                                            if type(b[ind_c + 1][0]) == list:
                                                b[ind_c + 1][0][0] += d[1]
                                            else:
                                                b[ind_c + 1][0] += d[1]
                                        else:
                                            b[ind_c + 1] += d[1]
                                    elif not ind_b + 1 >= len(b):
                                        if type(a[ind_b + 1]) == list:
                                            if type(a[ind_b + 1][0]) == list:
                                                if type(a[ind_b + 1][0][0]) == list:
                                                    a[ind_b + 1][0][0][0] += d[1]
                                                else:
                                                    a[ind_b + 1][0][0] += d[1]
                                            else:
                                                a[ind_b + 1][0] += d[1]
                                        else:
                                            a[ind_b + 1] += d[1]
                                    elif not ind_a + 1 >= len(a):
                                        if type(data[ind_a + 1]) == list:
                                            if type(data[ind_a + 1][0]) == list:
                                                if type(data[ind_a + 1][0][0]) == list:
                                                    if type(data[ind_a + 1][0][0][0]) == list:
                                                        data[ind_a + 1][0][0][0][0] += d[1]
                                                    else:
                                                        data[ind_a + 1][0][0][0] += d[1]
                                                else:
                                                    data[ind_a + 1][0][0] += d[1]
                                            else:
                                                data[ind_a + 1][0] += d[1]
                                        else:
                                            data[ind_a + 1] += d[1]
                                    #delete d
                                    c[ind_d] = 0
    return data


def check_split(data):
    for ind_a, a in enumerate(data):
        if type(a) == list:
            for ind_b, b in enumerate(a):
                if type(b) == list:
                    for ind_c, c in enumerate(b):
                        if type(c) == list:
                            for ind_d, d in enumerate(c):
                                if d >= 10:
                                    c[ind_d] = split(d)
                                    return True, data
                        else:
                            if c >= 10:
                                b[ind_c] = split(c)
                                return True, data
                else:
                    if b >= 10:
                        a[ind_b] = split(b)
                        return True, data
        else:
            if a >= 10:
                data[ind_a] = split(a)
                return True, data
    return False, data


def calc_magnitude(data):
    magnitude = 0
    for ind_a, a in enumerate(data):
        if type(a) == list:
            data[ind_a] = calc_magnitude(a)
    magnitude =  3 * data[0] + 2* data[1]
    return magnitude


with open("input.txt","r") as myinput:
    inputs = [ast.literal_eval(x.strip()) for x in myinput]

    magnitudes = list()
    for next in itertools.permutations(inputs, 2):
        data = copy.deepcopy(next)
        number = data[0]
        for test in data[1:]:
            new_number = [number]
            new_number.append(test)
            number = new_number
            number = check_explode(number)
            res, number = check_split(number)
            while res == True:
                number = check_explode(number)
                res, number = check_split(number)
        magnitudes.append(calc_magnitude(number))
    print(max(magnitudes))