# print.py

# Import global_vars.py
import global_vars

# Function to print menu options
def print_menu(options, menu_title):

    print(menu_title)
    for option in options:
        print(option)

def print_transactions():

    # variable to store total left to spend
    left_to_spend = 0
    # variable to store total expense
    total_expense = 0
    # variable to store total income
    total_income = 0

    for transaction in global_vars.transactions:

        if(transaction.year != global_vars.year):
            pass
        elif(transaction.month != global_vars.month):
            pass
        else:
            #variable to use for computing totals, in place of amount str
            amount_int = float(transaction.amount)

            #indicate type for printing and summing totals
            if(transaction.type == '0'):
                #indicate type
                print_type = '-'
                #sum totals
                left_to_spend-=amount_int
                total_expense+=amount_int
            else:
                #indicate type
                print_type = '+'
                #sum totals
                left_to_spend+=amount_int
                total_income+=amount_int
            
            #variable to display date in readable format
            date = transaction.month + '/' + transaction.day + '/' + transaction.year

            print('{} {} ${} {} {}'.format(date, print_type, transaction.amount, transaction.merchant, transaction.note))
        
    #print totals
    print()
    print('Left to Spend: ${} / Total Spent: ${} / Total Income: ${}'.format(round(left_to_spend, 2), round(total_expense, 2), round(total_income, 2)))

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