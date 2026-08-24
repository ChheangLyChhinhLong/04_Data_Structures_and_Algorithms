def total_expense(quantity, price):
    total = quantity * price
    

    if quantity > 1000:
        discount = total * 0.20
        total -= discount
        
    return total

qty = int(input("Enter Quantity: "))
unit_price = float(input("Enter Price per unit ($): "))

final_expense = total_expense(qty, unit_price)
print(f"Total Expense = ${final_expense:,.2f}")