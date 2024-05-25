def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    last_digit = n % 2
    print(last_digit)
    return as_binary_string(n // 2) + str(last_digit) 

as_binary_string(5)