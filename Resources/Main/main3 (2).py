import math
import cmath

name = input("Enter employee name: ")
hours = float(input("Enter total working hours: "))
rate = float(input("Enter hourly rate: "))

if hours > 48:
    normal_hours = 48
    overtime_hours = hours - 48
    total_wage = (normal_hours * rate) + (overtime_hours * rate * 2)
else:
    total_wage = hours * rate

print("\n--- Total Wage Calculation Result ---")
print(f"Employee Name : {name}")
print(f"Total Hours   : {hours} hours")
print(f"Total Wage    : ${total_wage:,.2f}")