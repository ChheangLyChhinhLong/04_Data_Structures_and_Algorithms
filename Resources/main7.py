salary = float(input("Enter monthly salary in USD ($): "))
if salary <= 350:
    tax = 0
elif salary <= 500:
    tax = 5
elif salary <= 650:
    tax = 5 + 0.01 * (salary - 500)
else:
    tax = 5 + 0.015 * (salary - 650)

print(f"Total Tax = ${tax:.2f}")