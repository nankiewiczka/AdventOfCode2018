SIZE = 1000


def main():
    lines = [line.rstrip('\n') for line in open('../dataFiles/day3.txt')]
    array = [[0 for x in range(1000)] for y in range(1000)]

    for line in lines:
        read_data = extract_data_from_line(line)
        x = read_data[0]
        y = read_data[1]
        width = read_data[2]
        height = read_data[3]
        for i in range(x, x+width):
            for j in range(y, y+height):
                mark_taken_place(i, j, array)

    print(count_marked_more_than_once(array))


def extract_data_from_line(line):
    from_left_edge = int(line[line.index('@')+2: line.index(',')])
    from_top_edge = int(line[line.index(',')+1: line.index(':')])
    width = int(line[line.index(':')+1:line.index('x')])
    height = int(line[line.index('x')+1:])
    return [from_left_edge, from_top_edge, width, height]


def mark_taken_place(x, y, array):
    array[x][y] = array[x][y]+1


def count_marked_more_than_once(array):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] > 1:
                sum += 1
    return sum


main()