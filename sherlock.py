import fileinput

def fun(entry):
    final = {}
    for i in entry.strip():
        if (i not in final):
            final[i] = 1
        else:
            final[i] += 1
        
    counts = []
    for i in final:
        counts.append(final[i])
    if (len(counts) < 2):
        return True
    if (abs(counts[0] - counts[1]) > 1):
        return False
    count = counts[0]
    if (counts[0] > counts[1]):
        count = counts[1]
    differingValueFound = False
    for i in counts:
        if (i != count):
            if (differingValueFound or i != count + 1):
                return False
            differingValueFound = True
    return True

for line in fileinput.input():
    print(str(fun(line)).lower())
