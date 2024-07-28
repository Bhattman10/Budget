# user_input.py

from Transaction import Transaction, add_transaction, delete_transaction
from print import print_menu, print_transactions, print_transactions_with_position, print_categories_with_position
import global_vars
from Category import Category, add_category, edit_category, delete_category, category_write_to_file

# Collect and test user input for adding transactions
def user_input_add_transaction():

    print()

    # Boolean to indicate while loop for testing is running
    testing = True

    # Collect and check day from user
    testing = True
    while(testing):
        day = input("Enter day of transaction: ")
        if int(day) > 31 or int(day) < 1:
            print("Error: invalid input!")
        else:
            testing = False

    # Collect and check type from user
    testing = True
    while(testing):
        type = input("Enter 0 for expense, 1 for income: ")
        if not type.isnumeric():
            print("Error: invalid input!")
        elif int(type) > 1 or int(type) < 0:
            print("Error: invalid input!")
        else:
            testing = False
    
    # Collect and check category from user
    testing = True
    while(testing):
        #first, display categories
        print_categories_with_position()
        #then, recieve input from user on selection of category
        category_index = input("Select category index of transaction: ")
        #test user input, breaking loop if input looks OK
        if int(category_index) > (len(global_vars.categories)-1) or int(category_index) < 0:
            print("Error: invalid input.")
        else:
            category = global_vars.categories[int(category_index)].name
            testing = False


    # Collect and check amount from user
    testing = True
    while(testing):
        amount = input("Enter amount of transaction: $")
        #check if string can be casted to float
        fail_test = False
        try:
            float(amount)
        except ValueError:
            fail_test = True
        if fail_test:
            print("Error: invalid input!")
        elif float(amount) <= 0:
            print("Error: invalid input!")
        else:
            testing = False

    merchant = input("Enter transaction merchant: ")
    note = input("Add note for transaction: ")

    #create object and append to list
    add_transaction(global_vars.year, global_vars.month, day, type, category, amount, merchant, note)

# Collect and test user input for deleting transactions
def user_input_delete_transaction():

    print()

    print_transactions_with_position()

    print()

    pos_to_delete = input("Select transaction to delete: ")

    if int(pos_to_delete) > (len(global_vars.transactions)-1) or int(pos_to_delete) < 0:
        print("Error: invalid input.")
    else:
        delete_transaction(int(pos_to_delete))

def change_month_year():

    # Boolean to indicate while loop for testing is running
    testing = True

    # Collect and check year from user
    while(testing):
        year = input("Select YEAR to display and add transactions to: ")
        if len(year) != 4:
            print("Error: invalid input!")
        else:
            testing = False

    #set global year
    global_vars.year = year
    
    # Collect and check month from user
    testing = True
    while(testing):
        month = input("Select MONTH to display and add transactions to: ")
        if int(month) > 12 or int(month) < 1:
            print("Error: invalid input!")
        else:
            testing = False

    #set global month
    global_vars.month = month

def update_categories():

    running = True

    # List of menu options
    menu_options = [
        "1. Edit Category",
        "2. Add Category",
        "3. Delete Category",
        "4. Exit to Main Menu",
    ]

    while running:

        #TODO: display categories for the month

        #display main menu with options
        print_menu(menu_options, "CATEGORY MENU")

        # Get user input
        choice = input("Select an option: ")

        # user inputs edit category
        if choice == "1":
            if len(global_vars.categories) == 0:
                print("No categories to edit.")
            else:
                print("Editing category...")
                user_input_edit_category()
        # user inputs add cateogry
        elif choice == "2":
            print("Adding category...")
            user_input_add_category()
        # user inputs delete cateogry
        elif choice == "3":
            if len(global_vars.categories) == 0:
                print("No categories to delete.")
            else:
                print("Deleting category...")
                user_input_delete_category()
        # user inputs exit to main menu
        elif choice == "4":
            print("Exiting to Main Menu...")
            running = False
        # user inputs anything besides 1-4
        else:
            print("Error. Please select a valid option from the menu.")

# Collect and test user input for adding category
def user_input_add_category():

    # Collect and check name from user
    name = input("Enter category name: ")

    # Collect and check goal amount from user
    testing = True
    while(testing):

        goal = input("Enter goal amount of category: $")

        #check if string can be casted to float
        fail_test = False

        try:
            float(goal)
        except ValueError:
            fail_test = True
        if fail_test:
            print("Error: invalid input!")
        elif float(goal) <= 0:
            print("Error: invalid input!")
        else:
            testing = False
        
    #set year to global year
    year = global_vars.year
    #set month to global month
    month = global_vars.month
    #set value to global zero
    value = 0

    add_category(year, month, name, goal, value)

    # Update by writing to category file
    category_write_to_file()

def user_input_edit_category():

    #display all categories, allowing the user to select which category to edit
    print_categories_with_position()

    pos_to_edit = input("Select cateogry to edit: ")

    if int(pos_to_edit) > (len(global_vars.categories)-1) or int(pos_to_edit) < 0:
        print("Error: invalid input.")
    else:

        #collect goal and name to edit transaction with
        goal = input("Enter goal for category: ")
        name = input("Enter name for category: ")

        #call edit cateogry function
        edit_category(pos_to_edit, name, goal)

        # Update by writing to category file
        category_write_to_file()

def user_input_delete_category():

    #display all categories, allowing the user to select which category to edit
    print_categories_with_position()

    pos_to_delete = input("Select cateogry to delete: ")

    if int(pos_to_delete) > (len(global_vars.categories)-1) or int(pos_to_delete) < 0:
        print("Error: invalid input.")
    else:
        delete_category(pos_to_delete)

        # Update by writing to category file
        category_write_to_file()
