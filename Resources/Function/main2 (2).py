# 1. បង្កើត Function ដោយបន្ថែម parameter name
def totalwage(name, hour, rate):
    if hour > 48:
        overtime = hour - 48
        wage = (48 * rate) + (overtime * rate * 2)
    else:
        wage = hour * rate

    print("=========================")
    print(f"Name : {name}\nWage : ${wage:,.2f}")


emp_name = str(input("Enter Name : "))
a = int(input("Enter time (hours) : "))
b = float(input("Enter rate ($) : "))

totalwage(emp_name, a, b)