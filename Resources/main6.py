# V.
def calculate_electricity_cost(u):
    if u <= 50:
        cost = 610 * u
    else:
        cost = 30500 + 720 * (u - 50)
    return cost

try:
    u = float(input("Enter electricity consumption (kWh): "))
    if u < 0:
        print("Consumption cannot be negative!")
    else:
        total_cost = calculate_electricity_cost(u)
        print(f"Total Electricity Cost: {total_cost:,.0f} KHR")
except ValueError:
    print("Please enter a valid number!")