total_amount = float(input("Enter total purchase amount ($): "))

if total_amount <= 100:
    discount_rate = 0.05
elif total_amount <= 200:
    discount_rate = 0.10
else:
    discount_rate = 0.20

discount_money = total_amount * discount_rate
final_payment = total_amount - discount_money

print("-" * 35)
print(f"Total Amount    : ${total_amount:,.2f}")
print(f"Discount Rate   : {int(discount_rate * 100)}%")
print(f"Discount Money  : ${discount_money:,.2f}")
print(f"Final Payment   : ${final_payment:,.2f}")
print("-" * 35)