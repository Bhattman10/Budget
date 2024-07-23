# user_input.py

# Import the Transaction class and functions from transactions.py
from Transaction import Transaction, add_transaction, delete_transaction
# Import print.py
from print import print_menu, print_transactions, print_transactions_with_position

# Collect and test user input for adding transactions
def user_input_add_transaction():

    # Boolean to indicate while loop for testing is running
    testing = True

    # Collect and check year from user
    while(testing):
        year = input("Enter year of transaction: ")
        if len(year) != 4:
            print("Error: invalid input!")
        else:
            testing = False
    
    # Collect and check month from user
    testing = True
    while(testing):
        month = input("Enter month of transaction: ")
        if int(month) > 12 or int(month) < 1:
            print("Error: invalid input!")
        else:
            testing = False

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
        if int(type) > 1 or int(type) < 0:
            print("Error: invalid input!")
        else:
            testing = False

    # Collect and check amount from user
    testing = True
    while(testing):
        amount = input("Enter amount of transaction: $")
        if float(amount) <= 0:
            print("Error: invalid input!")
        else:
            testing = False

    merchant = input("Enter transaction merchant: ")
    note = input("Add note for transaction: ")

    #create object and append to list
    add_transaction(year, month, day, type, amount, merchant, note)

# Collect and test user input for deleting transactions
def user_input_delete_transaction():

    print_transactions_with_position()

    pos_to_delete = input("Select transaction to delete: ")

    delete_transaction(int(pos_to_delete))
