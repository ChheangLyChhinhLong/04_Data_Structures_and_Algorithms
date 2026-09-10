def sum6(n):
    if n == 1:
        return 2 / 9
    else:
        term = ((-1) ** (n - 1)) * ((3 * n - 1) / (4 * n + 5))
        return term + sum6(n - 1)

n = int(input("Enter number of element : "))

if n > 0:
    print(f"Sum: 2/9 - 5/13 + 8/17 + ... = {sum6(n):.4f}")
else:
    print("Error...")