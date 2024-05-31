import time
import math

def fibonacci(n):
    numbers = [1, 1]
    if n < 2:
        return 1
    else:
        counter = 0
        while counter < n - 1:
            summ = (numbers[0] + numbers[1])
            print(summ)
            numbers[0] = numbers[1]
            numbers[1] = summ
            fib = summ
            counter += 1
        return fib

# def fibonacci(n):
#     sqrt_5 = math.sqrt(5)
#     phi = (sqrt_5 + 1) / 2
#     value = (phi ** n) % 10
#     return int((value / sqrt_5 + 0.5))
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# number, commits = map(int, input().split())
number, commits = map(int, '506277 6'.split())
number, commits = map(int, '8 6'.split())

timeStart = time.time()
result = fibonacci(number) % (10 ** commits)
end_time = time.time()
print(f"Time: {end_time - timeStart}")
print(result)
# Fn = Fn-1 + Fn-2 
