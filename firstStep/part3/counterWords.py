

def counterWords(s, t):
    counter = 0
    for start in range(len(s)):
        isFounded = s.find(t, start, (start + len(t)))
        if isFounded == -1:
            continue
        counter += 1
    return counter

s = input()
t = input()
print(counterWords(s, t))

s, t = ['abababa','aba']

count = 0
while s.find(t) != -1:
    s = s[s.find(t) + 1:]
    count += 1

print(count)