class Category:

    def __init__(self, category_name):
        # Initialize a new category with a given name
        self.category_name = category_name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit entry
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="", category_name=""):
        # Attempt to withdraw funds and add a withdrawal entry if successful
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        # Calculate and return the current balance of the category
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, category):
        # Transfer funds to another category and record the transaction
        if self.withdraw(amount, f"Transfer to {category.category_name}", category.category_name):
            category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        # Check if there are sufficient funds for a given amount
        return self.get_balance() >= amount

    def __str__(self):
        # Generate a string representation of the category
        output = ""
        output += self.category_name.center(30, "*") + "\n"

        total = 0
        for i in self.ledger:
            total += i['amount']
            output += i['description'].ljust(23, " ")[:23]
            output += "{0:>7.2f}".format(i['amount'])
            output += "\n"
        output += "Total: " + "{0:.2f}".format(total)
        return output


def create_spend_chart(categories):
    # Generate a spending chart for a list of categories
    output = "Percentage spent by category\n"

    total = 0
    expenses = []
    labels = []
    len_labels = 0

    for item in categories:
        # Calculate total expenses and find the maximum label length
        expense = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
        total += expense

        if len(item.category_name) > len_labels:
            len_labels = len(item.category_name)

        expenses.append(expense)
        labels.append(item.category_name)

    # Calculate percentages and pad labels
    expenses = [(x / total) * 100 if total != 0 else 0 for x in expenses]
    labels = [label.ljust(len_labels, " ") for label in labels]

    # Generate the chart
    for c in range(100, -1, -10):
        output += str(c).rjust(3, " ") + '|'
        for x in expenses:
            output += " o " if x >= c else "   "
        output += " \n"

    output += "    " + "---" * len(labels) + "-\n"

    for i in range(len_labels):
        output += "    "
        for label in labels:
            output += " " + label[i] + " "
        output += " \n"

    return output.strip("\n")