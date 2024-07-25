# main.py

#TODO: custom saved categories
#TODO: when brand new application is loaded in, problems with loading file because it doesn't exist
#TODO: when pasting entire transaction into user input, new line mess up
#TODO: when submitting "ENTER" on delete transaction, error
#TODO: check user input for adding transactions
#TODO: format transaction print display
#TODO: add settings that allow you to view and delete from entire transactions list

#TODO: month-by-month transaction tracking
    #TODO: update write and read from file for month/year
    #TODO: display current month/year at top of transactions display
    #TODO: allow deletion of transactions only from month/year

import global_vars
from print import print_menu, print_transactions
from user_input import user_input_add_transaction, user_input_delete_transaction, change_month_year
from Transaction import write_to_file, read_from_file

# Version
print()
print("Budget - 0.1.7\n")

# Update transaction list by reading from file
read_from_file()

# Boolean to indiciate menu running
running = True

# List of menu options
menu_options = [
    "1. Add Transaction",
    "2. Delete Transaction",
    "3. Change Year/Month",
    "4. Exit Budget"
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
        change_month_year()
    elif choice == "4":
        print()
        print("Exiting Budget...")
        running = False
    else:
        print("Error. Please select a valid option from the menu.")
