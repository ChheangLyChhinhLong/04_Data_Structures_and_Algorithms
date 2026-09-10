import array as arr

n = int(input("Enter number of elements: "))
numbers = arr.array('d')

for i in range(n):
    val = float(input(f"Enter element {i + 1}: "))
    numbers.append(val)


count = len(numbers)
total_sum = sum(numbers)
avg = total_sum / count
max_val = max(numbers)
min_val = min(numbers)

print("\n--- Array Calculator Results ---")
print(f"1) Number of Elements : {count}")
print(f"2) Sum                : {total_sum}")
print(f"3) Average            : {avg:.2f}")
print(f"4) Maximum            : {max_val}")
print(f"5) Minimum            : {min_val}")