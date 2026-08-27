def calculate_water_bill(w):
    if w <= 7:
        cost = 550 * w
    elif w <= 15:
        cost = 3850 + 770 * (w - 7)
    elif w <= 50:
        cost = 9240 + 1010 * (w - 15)
    else:
        cost = 44590 + 1270 * (w - 50)
        
    return cost

water_usage = float(input("Enter water usage in m^3 (w): "))

total_bill = calculate_water_bill(water_usage)
print(f"Total Water Bill = {total_bill:,.0f} Riels")
