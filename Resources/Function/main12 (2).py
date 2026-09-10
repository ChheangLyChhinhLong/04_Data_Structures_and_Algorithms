def sum4(n):
    if n == 1:
        return 1
    else:
        return ((-1) ** (n - 1)) * n + sum4(n - 1)

n = int(input("Enter number of elements : "))

if n > 0:
    print(f"Sum: 1-2+3-4+...+(-1)^(n-1)n = {sum4(n)}")
else:
    print("Error...")