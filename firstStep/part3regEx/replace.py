# s, a, b = input(), input(), input()
s, a, b = [input() for _ in range(3)]
counter = 0
while s.replace(a, b) != s:
    counter += 1
    if counter >= 1000:
        break
    s = s.replace(a, b)

if (s.find(a) == -1):
    print(counter)
else:
    print('Impossible')