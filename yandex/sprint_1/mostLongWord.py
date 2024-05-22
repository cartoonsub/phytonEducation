

lenght = int(input())
text = input().split(' ')

# lenght = 19
# text = 'frog jumps from river'.split(' ')

mostLongWord = {
    'lenght': 0,
    'word': ''
}

for word in text:
    lenght = len(word)
    if lenght > mostLongWord['lenght']:
        mostLongWord['lenght'] = lenght
        mostLongWord['word'] = word

print(mostLongWord['word'])
print(mostLongWord['lenght'])
