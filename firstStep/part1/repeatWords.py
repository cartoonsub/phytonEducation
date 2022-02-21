# listWords = set()
# allWords = input().split()
# for word in allWords:
#     listWords.add(word.lower())
# print(allWords)
# print(listWords)
def countRepeatWords(allWords, listWords):
    for word in allWords:
        word = word.lower()
        if word in listWords:
            listWords[word] += 1
        else:
            listWords[word] = 1

# allWords = ['a', 'aa', 'abC', 'aa', 'ac', 'abc', 'bcd', 'a']
allWords = input().split()
listWords = {}
countRepeatWords(allWords, listWords)
for key, value in listWords.items():
    print(key, value, end='\n')

# put your python code here
# ЕБАТЬ КОПАТь
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))