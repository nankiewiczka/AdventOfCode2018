lines = [int(line.rstrip('\n')) for line in open('../dataFiles/day1.txt')]

# first part
startFrequency = 0;
for x in lines:
    startFrequency = startFrequency + x;

print(startFrequency);


# second part
startFrequency = 0;
frequencies = [int(startFrequency)];
while True:
    for x in lines:
        startFrequency = startFrequency + x;
        if startFrequency in frequencies:
            break;
        else:
            frequencies.append(startFrequency);

    else:
        continue;
    break;

print(startFrequency);
