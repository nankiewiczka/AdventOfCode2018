lines = [line.rstrip('\n') for line in open('../dataFiles/day2.txt')]
twiceAppearAmount = 0
threeTimeAppearAmount = 0


# first part
for line in lines:
    signs = dict()
    for sign in line:
        if sign in signs.keys():
            signs[sign] += 1
        else:
            signs[sign] = 1

    if 2 in signs.values():
        twiceAppearAmount += 1
    if 3 in signs.values():
        threeTimeAppearAmount += 1

print(twiceAppearAmount * threeTimeAppearAmount)


# second part
for i in range(len(lines)):
    line = lines[i]
    for j in range(i+1, len(lines)):
        differences = 0
        comparedLine = lines[j]
        for k in range(len(line)):
            if line[k] != comparedLine[k]:
                differences += 1
        if differences == 1:
            for k in range(len(line)):
                if line[k] == comparedLine[k]:
                    print(line[k], end='')
            break
    else:
        continue
    break





