# print.py

# Import global_vars.py
import global_vars

# Function to print menu options
def print_menu(options):

    print("MAIN MENU")
    for option in options:
        print(option)

def print_transactions():

    for transaction in global_vars.transactions:

        #variable to print indication of type
        if(transaction.type == '0'):
            print_type = '-'
        else:
            print_type = '+'
        
        #variable to display date in readable format
        date = transaction.month + '/' + transaction.day + '/' + transaction.year

        print('{} {} ${} {} {}'.format(date, print_type, transaction.amount, transaction.merchant, transaction.note))

def print_transactions_with_position():

    #iterator for indicating position to delete
    itt = 0

    for transaction in global_vars.transactions:

        #variable to print indication of type
        if(transaction.type == '0'):
            print_type = '-'
        else:
            print_type = '+'
        
        #variable to display date in readable format
        date = transaction.month + '/' + transaction.day + '/' + transaction.year

        print('[{}] {} {} ${} {} {}'.format(itt, date, print_type, transaction.amount, transaction.merchant, transaction.note))

        #iterate
        itt+=1