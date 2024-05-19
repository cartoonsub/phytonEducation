

lenght = int(input())
temperatures = list(map(int, input().split()))

def calculate_chaotic_days(n, temperatures):
    if n == 1:
        return 1
    
    n = len(temperatures)
    
    chaotic_days = 0
    
    # Check the first day
    if temperatures[0] > temperatures[1]:
        chaotic_days += 1
    
    # Check the days from 2 to n-1
    for i in range(1, n - 1):
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            chaotic_days += 1
    
    # Check the last day
    if temperatures[n - 1] > temperatures[n - 2]:
        chaotic_days += 1
    
    return chaotic_days

print(calculate_chaotic_days(lenght, temperatures))  # Output: 2
