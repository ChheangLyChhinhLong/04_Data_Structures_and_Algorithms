import math
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a != 0:
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("X1 =", x1)
        print("X2 =", x2)
    elif delta == 0:
        x = -b / (2 * a)
        print("X1 = X2 =", x)
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print("Complex X1 =", x1)
        print("Complex X2 =", x2)
else:
    print("Not a quadratic equation")