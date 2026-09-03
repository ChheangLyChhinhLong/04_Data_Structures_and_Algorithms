n = int(input("Enter n: "))

total_sum = 0
current = 1
sign = 1

for i in range(n):
    total_sum += sign * current
    current += 5
    sign *= -1

print("Sum =", total_sum)