# savings_calculator.py

# Prompt the user for input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Output the results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected annual savings (with 5% interest) are: {projected_annual_savings}")
