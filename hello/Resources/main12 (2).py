# create an array has N_arry with typecode "integer"
# - By entering nuber of its elements via keyboard.
# - Typing all elements via keyboad and output that array.

import array as arr

n = int(input("Enter array: "))
n_array = arr.array('i')

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    n_array.append(value)

print(n_array)