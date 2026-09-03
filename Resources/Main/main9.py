n = int(input("Enter n: "))

sum = 0

for i in range(1, 2 * n, 2):
    sum = sum + i

print("Sum =", sum)