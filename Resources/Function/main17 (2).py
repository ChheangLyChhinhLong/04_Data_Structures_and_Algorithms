def sum11(n):
    if n == 1:
        return 1.0
    else:
        return (1 / (n ** 3)) + sum11(n - 1)

n = int(input("Enter number of element : "))

if n > 0:
    print(f"Sum: .... = {sum11(n):.4f}")
else:
    print("Error...")