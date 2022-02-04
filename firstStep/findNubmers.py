def fundNum(n, k):
    if (k == 0):
        return 1
    if (k > n):
        return 0
    result = fundNum(n - 1, k) + fundNum(n - 1, k -1)
    return result
n, k = map(int, input().split())
result = fundNum(n, k)
print(result)