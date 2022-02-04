string = ''
with open('dataset_3363_2.txt', 'r') as file:
    for line in file:
        string = line.strip()
        
letter = ''
stringCount = ''
count = 0
fuck = ''
for index in range(len(string)):
    if not string[index].isdigit():
        # print((string[index-1]*int(string[index])), end='')
        if stringCount:
            count = int(stringCount)
        if letter and count > 0:
            fuck += (letter * count)
            letter = ''
            count = 0
            stringCount = ''
        letter = string[index]
    else:
        stringCount += string[index]
        # print(stringCount)
    if len(string)-1 == index:
        count = int(stringCount)
        if letter and count > 0:
            fuck += (letter * count)
            letter = ''
            count = 0
            stringCount = ''
            
with open('dataset_3363_2.txt', 'w') as inf:
    inf.write(fuck)