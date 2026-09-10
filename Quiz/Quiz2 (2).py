import array as arr

number = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

search_val = int(input("Enter value to search: "))

if search_val in number:
    indices = [i for i, x in enumerate(number) if x == search_val]
    print(f"That value is presented in array at index/indices: {indices}")
    
    new_val = int(input("Enter new value to update: "))
    updated_count = 0
    
    for i in range(len(number)):
        if number[i] == search_val:
            number[i] = new_val
            updated_count += 1
            
    print("Array after update: ", list(number))
    print(f"Count of updated elements: {updated_count}")
    
    sorted_number = arr.array('i', sorted(number))
    print("Array after sorted: ", list(sorted_number))
    
else:
    print("That value is not present in array.")