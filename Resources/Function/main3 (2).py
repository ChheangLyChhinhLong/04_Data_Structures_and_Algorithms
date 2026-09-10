def calculate_commission(sales_amount):
    commission = sales_amount * 0.05
    
    if sales_amount > 10000:
        commission += 100
        
    return commission

sales = float(input("Enter total weekly sales ($): "))

total_commission = calculate_commission(sales)
print(f"Total Commission = ${total_commission:,.2f}")