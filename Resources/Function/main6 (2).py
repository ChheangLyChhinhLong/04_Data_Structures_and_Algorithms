def calculate_tax(salary):
    if salary <= 350:
        tax = 0
    elif salary <= 500:
        tax = 5
    elif salary <= 650:
        tax = 5 + (salary - 500) * 0.01
    else:
        tax = 5 + (salary - 650) * 0.015
        
    return tax

emp_salary = float(input("Enter monthly salary ($): "))

tax_amount = calculate_tax(emp_salary)
net_salary = emp_salary - tax_amount

print("\n--- Monthly Tax Payment Summary ---")
print(f"Gross Salary : ${emp_salary:,.2f}")
print(f"Tax Payment  : ${tax_amount:,.2f}")
print(f"Net Salary   : ${net_salary:,.2f}")