def p9(n):
    if n == 1:
        return 2
    else:

        return (2 ** n) * p9(n - 1)

n = int(input("Enter number of element : "))

if n > 0:
    print(f"Product: 2 * 4 * 8 * ... = {p9(n)}")
else:
    print("Error...")