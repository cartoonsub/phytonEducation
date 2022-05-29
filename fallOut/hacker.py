


allWords = [
    'PERSONALITY', 'RESIDENTIAL', 'IMMEDIATELY', 'TEMPERATURE', 'DEVASTATION', 
    'EXAMINATION', 'RECOGNITION', 'RADIOACTIVE', 'ACCOMPANIED', 'PERSECUTION',
    'RELUCTANTLY', 'THREATENING', 'EXPLANATION', 'DESTRUCTION', 'COMBINATION',
    'AGRICULTURE', 'INFORMATION',
]

def compareWord(mainWord, comparedWord):
    if len(mainWord) != len(comparedWord):
        return 0
    
    num = 0
    for index, letter in enumerate(mainWord):
        if letter == comparedWord[index]:
            num += 1
    return num

sortedWords = []
pattern = 'DESTRUCTION'#5
for index, word in enumerate(allWords):
    num = compareWord(pattern, word)
    if num > 4:
        sortedWords.append(word)
print(sortedWords)