
try:
    print(10 / x)
except BaseException as E:
    print(E.args)
    print('fuck')