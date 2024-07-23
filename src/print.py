# print.py

# Function to print menu options
def print_menu(options):

    print("MAIN MENU")
    for option in options:
        print(option)

def print_transactions(transactions):

    for transaction in transactions:

        #variable to print indication of type
        if(transaction.type == '0'):
            print_type = '-'
        else:
            print_type = '+'
        
        #variable to display date in readable format
        date = transaction.month + '/' + transaction.day + '/' + transaction.year

        print('{} {} ${} {} {}'.format(date, print_type, transaction.amount, transaction.merchant, transaction.note))