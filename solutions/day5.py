with open('../dataFiles/day5.txt', 'r') as text_file:
    read_text = text_file.read()

# first part
text = read_text
flag = True
while flag:
    index = 0
    length = len(text)
    flag = False
    while index < length-1:
        if abs(ord(text[index]) - ord(text[index + 1])) == 32:
            if index + 2 < len(text):
                text = text[:index] + text[index + 2:]
                index = index + 2
            else:
                text = text[:index]
            flag = True
        else:
            index = index + 1
        length = len(text)

print(len(text))



