
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input())
print(fibonacci(number))
# Fn = Fn-1 + Fn-2 