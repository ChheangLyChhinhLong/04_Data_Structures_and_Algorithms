a = float(input("Input a = "))
b = float(input("Input b = "))

if a != 0:
    x = -b / a
    print(f"x = {x}")
else:
    if b == 0:
        print("Infinite solutions")
    else:
        print("No solution")