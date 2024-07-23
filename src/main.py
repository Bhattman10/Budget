# main.py

from src.print import print_menu, print_transactions
# Import user_input.py
from src.user_input import user_input_add_transaction

# Version
print("Budget - 0.0.5\n")

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

# While loop to display menu
while running:

    #display all transactions
    print_transactions(transactions)

    #display main menu with options
    print_menu(menu_options)

    # Get user input
    choice = input("Select an option: ")

    # Process the choice
    if choice == "1":
        print("Adding a transaction...")
        user_input_add_transaction(transactions)
    elif choice == "2":
        print("Deleting a transaction...")
        # Add code to handle deleting a transaction here
    elif choice == "3":
        print("Exiting Budget...")
        running = False
    else:
        print("Invalid option. Please select a valid option from the menu.")
