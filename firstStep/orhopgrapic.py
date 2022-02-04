vocabulary = {input() for i in range(int(input()))}
# num = int(input())
# if num != 0:
#     for i in range(num):
#         vocabulary.append(input().strip().lower())

words = []
num = int(input())
if num != 0:
    for i in range(num):
        sentence = input().strip().split(' ')
        for word in sentence:
            words.append(word.lower())

mistakes = {}
for word in words:
    if word not in vocabulary:
        mistakes[word] = word

for mistake in mistakes.keys():
    print(mistake)