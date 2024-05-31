import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    numbers = [1, 1]
    if n < 2:
        return 1
    else:
        counter = 0
        while counter < n - 1:
            summ = (numbers[0] + numbers[1])
            numbers[0] = numbers[1]
            numbers[1] = summ
            fib = summ
            counter += 1
        return fib
    

# number, commits = map(int, input().split())
number, commits = map(int, '506277  6'.split())

timeStart = time.time()
result = fibonacci(number) % (10 ** commits)
result = fibonacci(number) % (10 ** commits)
end_time = time.time()
print(f"Time: {end_time - timeStart}")
print(result)
# Fn = Fn-1 + Fn-2 
