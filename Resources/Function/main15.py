def p8(n):
    if n == 1:
        return 3
    else:
        return (5 * n - 2) * p8(n - 1)

n = int(input("Enter number of element : "))

if n > 0:
    print(f"Product: 3 * 8 * 13 * ... = {p8(n)}")
else:
    print("Error...")