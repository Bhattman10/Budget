# main.py

#bugs & cases
#TODO: when brand new application is loaded in, problems with loading file because it doesn't exist
#TODO: when pasting entire transaction into user input, new line mess up
#TODO: when submitting "ENTER" on delete transaction, error
#TODO: check user input for adding transactions, categories
#TODO: prevent user from inputing '|'
#TODO: allow user to exit from entering transactions
#TODO: when editing category, entering string results in error

#tasks
#TODO: custom saved categories
    #display category limits for the month
    #allow user to add/edit/delete categories
    #when adding transactions, allow user to add from list of categories
    #case: no categories added yet
#TODO: sort deletion of transactions from latest to oldest
#TODO: format transaction print display

import global_vars
from print import print_menu, print_transactions
from user_input import user_input_add_transaction, user_input_delete_transaction, change_month_year, update_categories
from Transaction import write_to_file, read_from_file

# Version
print()
print("Budget - 0.1.11\n")

# Update transaction list by reading from file
read_from_file()

# Boolean to indiciate menu running
running = True

# List of menu options
menu_options = [
    "1. Add Transaction",
    "2. Delete Transaction",
    "3. Update Categories",
    "4. Change Year/Month",
    "5. Exit Budget"
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
        print('{}/{} TRANSACTIONS...'.format(global_vars.month, global_vars.year))
        print_transactions()
        print()

    #update by writing to dated file
    write_to_file()

    #TODO: display category information

    #display main menu with options
    print_menu(menu_options, "MAIN MENU")

    # Get user input
    choice = input("Select an option: ")

    # user inputs add transactions
    if choice == "1":
        print()
        print("Adding a transaction...")
        user_input_add_transaction()
    # user inputs delete transactions
    elif choice == "2":
        print()
        if len(global_vars.transactions) == 0:
            print("No transactions to delete.")
        else:
            print("Deleting a transaction...")
            user_input_delete_transaction()
    # user inputs update category
    elif choice == "3":
        update_categories()
    # user inputs change month/year
    elif choice == "4":
        change_month_year()
    # user inputs exit budget
    elif choice == "5":
        print()
        print("Exiting Budget...")
        running = False
    # user inputs anything besides 1-5
    else:
        print("Error. Please select a valid option from the menu.")
