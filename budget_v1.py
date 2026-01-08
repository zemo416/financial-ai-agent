print("Personal Budget Assistant V1")

income = float(input("Please enter your monthly income: "))
fixed_expenses = float(input("Please enter your fixed expenses: "))
saving_goal = float(input("Please enter your saving goal: "))


remaining = income - fixed_expenses

print(" Budget Summary ")
print("Income:", income)
print("Fixed expenses:", fixed_expenses)
print("Saving goal:", saving_goal)

if remaining <= 0:
    print("Warning: Your expenses exceed your income.")
elif saving_goal > remaining:
    print("Warning: Your saving goal is not achievable with current expenses.")
elif saving_goal > income:
    print("Warning: Your saving goal is too high based on your current expenses. ")
else:
    print("Your saving goal is achiveable.")
    print("Recommended saving retio:", round((saving_goal / income) * 100, 2), 
    "%"
)
    
print(" Suggestions:")
print(" Try to keep savings between 20% and 40% of income")
print(" Reduce non-seesntial spending if needed")
print(" Build an emergency fund for 3-6 months of expenses")

input(" Process finished. Press Enter to exit...")
    


