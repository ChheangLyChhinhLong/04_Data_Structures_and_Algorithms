import array as arr 

n = int(input("Enter number of elements: "))
number = arr.array('i')

for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    number.append(val)
    
search_val = int(input("Enter value to search: "))

if search_val in number:
    indices = [i for i, x in enumerate(number) if x == search_val]
    print(f"That value is presented in array at index/indices: ", indices)
    
    choice = input("Do you want to update the value? (y/n): ").strip().lower()
    
    if choice == 'y':
        while search_val in number:
            number.remove(search_val)
        print("Array after deletion: ", list(number))
    else:
        print("No change made. Array: ", list(number))
else:
    print("That value is not present in array.")