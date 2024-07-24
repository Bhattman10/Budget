# main.py

#TODO: custom saved categories
#TODO: month-by-month transaction tracking

import global_vars
from print import print_menu, print_transactions
from user_input import user_input_add_transaction, user_input_delete_transaction
from Transaction import write_to_file, read_from_file

# Version
print()
print("Budget - 0.1.3\n")

# Update transaction list by reading from file
read_from_file()

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

    #update by writing to dated file
    write_to_file()

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
