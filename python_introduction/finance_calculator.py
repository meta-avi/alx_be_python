monthly_income =int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your total monthly expenses"))

Monthly_Savings = monthly_income - monthly_expenses
Projected_savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)


print("Monthly_Savings :$",Monthly_Savings)
print("Projected savings after one year, with interest, is: $",Projected_savings)