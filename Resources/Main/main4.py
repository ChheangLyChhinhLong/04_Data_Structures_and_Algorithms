total_sales = float(input("Enter total weekly sales ($): "))

commission = total_sales * 0.05

if total_sales > 10000:
    commission += 100

print(f"Total Commission = ${commission:,.2f}")