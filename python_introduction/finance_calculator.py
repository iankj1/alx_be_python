# savings_calculator.py

# Prompt the user for input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Output the results
print(f"Your monthly savings are: {monthly_savings}")
print(f"Your projected annual savings (with 5% interest) are: {projected_annual_savings}")
