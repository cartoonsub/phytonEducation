dataFromFile = []
with open('dataset_3363_3.txt', 'r') as file:
    for line in file:
        dataFromFile += line.strip().lower().split()
listWords = {0:[]}
for word in set(dataFromFile):
    key = dataFromFile.count(word)
    if key in listWords:
        listWords[key] += [word]
    else:
        listWords[key] = [word]

listKeys = list(listWords.keys())
listKeys.sort()
data = listWords[listKeys[-1]]
data.sort()
print(data)
maxWord = ''
for let in data:
    if let > maxWord:
        maxWord = let
print(maxWord, listKeys[-1], end= ' ')