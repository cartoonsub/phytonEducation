a = int(input())
b = int(input())
c = int(input())
d = int(input())

for row in range (0, 11):
    if row == 0:
        print('', end='\t')
        for x in range(c, d + 1):
            print(x, end='\t')
        print()
        continue
    for n in range(a, b + 1):
        if n == row:
            print(n, end='\t')
            for col in range(c, d + 1):
                print(col * n, end='\t')
            print()
    
    
    