def sum5(n):
    if n == 1:
        return 1
    else:
        term = ((-1) ** (n - 1)) * (5 * n - 4)
        return term + sum5(n - 1)

n = int(input("Enter number of element : "))

if n > 0:
    print(f"Sum: 1-6+11-... = {sum5(n)}")
else:
    print("Error...")