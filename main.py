# main.py

# Import the Transaction class and functions from transactions.py
from Transaction import Transaction, add_transaction

# Version
print("Budget - 0.0.2\n")

# List to store transactions
transactions = []

# Boolean to indiciate menu running
running = True

# List of menu options
menu_options = [
    "1. Add Transaction",
    "2. Delete Transaction",
    "3. Exit Budget"
]

# Function to print menu options
def print_menu(options):

    print("MAIN MENU")
    for option in options:
        print(option)

def print_transactions():
    for transaction in transactions:
        print(f"{transaction['date']}")
        print(f"{transaction['transaction_type']}")
        print(f"{transaction['amount']}")
        print(f"{transaction['merchant']}")
        print(f"{transaction['note']}")

def user_input_add_transaction():

    # Collect user input prior to creating transaction object and appending to list
    date = input("Enter day of transaction: ")
    type = input("Enter 0 for expense, 1 for income: ")
    amount = input("Enter amount of transaction: $")
    merchant = input("Enter transaction merchant: ")
    note = input("Add note for transaction: ")

    #create object and append to list
    add_transaction(transactions, date, type, amount, merchant, note)


# While loop to display menu
while running:

    #display all transactions
    print_transactions()

    #display main menu with options
    print_menu(menu_options)

    # Get user input
    choice = input("Select an option: ")

    # Process the choice
    if choice == "1":
        print("Adding a transaction...")
        user_input_add_transaction()
    elif choice == "2":
        print("Deleting a transaction...")
        # Add code to handle deleting a transaction here
    elif choice == "3":
        print("Exiting Budget...")
        running = False
    else:
        print("Invalid option. Please select a valid option from the menu.")
