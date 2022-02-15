def foo():
    x = 5 / 0
try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except AssertionError:
    print("AssertionError")
except ArithmeticError:
    print("ArithmeticError")


try:
    foo()
except (ZeroDivisionError, AssertionError, ArithmeticError) as Error:
    print(Error.args)

try:
    foo()
except Exception as Error:
    print(type(Error).__name__)