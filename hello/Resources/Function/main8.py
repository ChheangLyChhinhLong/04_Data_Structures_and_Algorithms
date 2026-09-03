def sum_even(n):
    total = 0
    for i in range(1, n + 1):
        total += 2 * i
    return total

n = int(input("Enter n: "))
print(f"Sum = {sum_even(n)}")