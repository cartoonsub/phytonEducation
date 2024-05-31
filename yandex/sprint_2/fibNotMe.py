def find_pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_modulo(n, m):
    pisano_period = find_pisano_period(m)
    n = n % pisano_period

    previous, current = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for i in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

# Пример использования:
n = 1000
m = 5
result = fibonacci_modulo(n, m)
print(result)