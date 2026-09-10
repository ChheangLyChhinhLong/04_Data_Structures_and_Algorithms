def sum_odd(n):
    total = 0
    for i in range(1, n + 1):
        total += (2 * i - 1)
    return total

n = int(input("Enter n: "))

if n > 0:
    result = sum_odd(n)
    print(f"Sum (1 + 3 + 5 + ... + {2*n - 1}) = {result}")
else:
    print("Please enter a positive integer (n > 0).")