import budget
from budget import create_spend_chart

# Create instances of Category
groceries = budget.Category("Groceries")
groceries.deposit(500, "initial deposit")
groceries.withdraw(50.75, "weekly groceries")
groceries.withdraw(20.30, "snacks and beverages")

entertainment = budget.Category("Entertainment")
groceries.transfer(30, entertainment)
entertainment.deposit(100, "movie night")
entertainment.withdraw(15, "popcorn and drinks")

clothing = budget.Category("Clothing")
entertainment.transfer(40, clothing)
clothing.withdraw(60, "new shirt")
clothing.withdraw(25.50, "jeans")

auto = budget.Category("Auto")
auto.deposit(800, "initial deposit")
auto.withdraw(50, "gas")
auto.withdraw(30, "car wash")

# Print the string representation of each category
print(groceries)
print(entertainment)
print(clothing)
print(auto)

# Print the spending chart for the categories
print(create_spend_chart([groceries, entertainment, clothing, auto]))