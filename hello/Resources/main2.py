import math
import cmath

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total_expense = quantity * price

if quantity > 1000:
    discount = total_expense * 0.20
    total_expense = total_expense - discount

print(f"Total Expense = ${total_expense:.2f}")