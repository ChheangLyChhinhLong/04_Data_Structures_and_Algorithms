def product_powers_of_two(n):
    total = 1
    for i in range(1, n + 1):
        total *= (2 ** i)
    return total

n = int(input("Enter n: "))
print("Product =", product_powers_of_two(n))