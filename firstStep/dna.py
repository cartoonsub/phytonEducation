s = input()
count = 1
needLet = ''
num = 0
code = ''
lenght = len(s) - 1
for letter in s:
    nextW = num + 1
    if (nextW > lenght):
        code += (s[num] + str(count))
        break
    if s[nextW] == letter:
        count += 1
    else:
        code += (s[num] + str(count))
        count = 1
    num += 1

print(code)
# препод внизу
genome = input()+' '
s = 0
n=genome[0]
for i in genome:       
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1