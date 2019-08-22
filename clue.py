import fileinput

def clue(suspects, weapons, rooms, clues):
    for i in range(0, len(clues)):
        if (clues[i].startswith('not ')):
            clues[i] = clues[i][4::]
        if (clues[i].startswith('the ')):
            clues[i] = clues[i][4::]
    for i in suspects:
        if i not in clues:
            s = i
    for i in weapons:
        if i not in clues:
            w = i
    for i in rooms:
        if i not in clues:
            r = i
    print(s)
    print('in the '+w)
    print('with the '+r)

clues = []
for line in fileinput.input:
    if (line.startswith('Suspects:'):
        suspects = line[9::].split(',')
    else if (line.startswith('Weapons:'):
        weapons = line[8::].split(',')
    else if (line.startswith('Rooms:'):
        rooms = line[6::].split(',')
    else if (line != "clues:"):
        clues.append(line)
clue(suspects, weapons, rooms, clues)
