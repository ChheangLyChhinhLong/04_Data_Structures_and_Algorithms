def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter n: "))

if n > 0:
    result = calculate_sum(n)
    print(f"Sum (1 + 2 + ... + {n}) = {result}")
else:
    print("Please enter a positive integer (n > 0).")