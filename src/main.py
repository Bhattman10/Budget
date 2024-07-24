# main.py

# Import global_vars.py
import global_vars
# Import print.py
from print import print_menu, print_transactions
# Import user_input.py
from user_input import user_input_add_transaction, user_input_delete_transaction

# Version
print()
print("Budget - 0.1.1\n")

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

    #display all transactions, if there are any
    if len(global_vars.transactions) == 0:
        print()
        print("No transactions to display.")
        print()
    else:
        print()
        print_transactions()
        print()

    #display main menu with options
    print_menu(menu_options)

    # Get user input
    choice = input("Select an option: ")

    # Process the choice
    if choice == "1":
        print()
        print("Adding a transaction...")
        user_input_add_transaction()
    elif choice == "2":
        print()
        if len(global_vars.transactions) == 0:
            print("No transactions to delete.")
        else:
            print("Deleting a transaction...")
            user_input_delete_transaction()
    elif choice == "3":
        print()
        print("Exiting Budget...")
        running = False
    else:
        print("Invalid option. Please select a valid option from the menu.")
