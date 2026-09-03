# 1. បង្កើត Function សម្រាប់គណនាថ្លៃភ្លើង
def calculate_electricity_bill(u):
    if u <= 50:
        cost = 610 * u
    else:
        cost = 30500 + 720 * (u - 50)
    return cost

# 2. ទទួលទិន្នន័យពី User
units = float(input("Enter electricity usage (kWh): "))

# 3. ហៅ Function និងបង្ហាញលទ្ធផល
total_cost = calculate_electricity_bill(units)
print(f"Total Electricity Bill = {total_cost:,.0f} KHR")