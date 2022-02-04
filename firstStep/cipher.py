inputs = []
for x in range(4):
    inputs.append(input())
# inputs = ['abcd', '*d%#', 'abacabadaba', '#*%*d*%']
cipher = dict(zip(inputs[0], inputs[1]))
decoder = dict(zip(inputs[1], inputs[0]))

for letter in inputs[2]:
    print(cipher[letter], end='')
print()
for letter in inputs[3]:
    print(decoder[letter], end='')