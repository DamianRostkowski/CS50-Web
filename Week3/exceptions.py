import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("error: You have to input numbers")
    sys.exit(1)

try: 
    result = x/y
except ZeroDivisionError:
    print("Error: you can't divide by zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")