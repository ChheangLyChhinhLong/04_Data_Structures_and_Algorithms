def sum_series_5(n):
    total = 0
    for i in range(1, n + 1):
        term = 5 * i - 4
        total += ((-1) ** (i - 1)) * term
    return total

n = int(input("Enter n: "))
print("Sum =", sum_series_5(n))