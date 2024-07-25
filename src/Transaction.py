# Transaction.py

# Import global_vars.py
import global_vars

class Transaction:
    def __init__(self, year, month, day, type, amount=None, merchant=None, note=None):
        self.year = year
        self.month = month
        self.day = day
        self.type = type
        self.amount = amount
        self.merchant = merchant
        self.note = note

def add_transaction(year, month, day, type, amount, merchant, note):

    # Create transaction
    transaction = Transaction(year, month, day, type, amount, merchant, note)

    # Add transaction to list
    global_vars.transactions.append(transaction)

    #custom function for sorting
    def trans_sort(transaction):
        return transaction.day
    
    #sort transaction list
    global_vars.transactions.sort(key=trans_sort)

def delete_transaction(pos_to_delete):

    # Pop the transaction
    global_vars.transactions.pop(pos_to_delete)

def write_to_file():

    #open file for writing
    f = open("Transactions", "w")

    #write the number of elements in transaction
    f.write(str(len(global_vars.transactions)))
    f.write("|")

    #write the current display/add year
    f.write(global_vars.year)
    f.write("|")

    #write the current display/add month
    f.write(global_vars.month)
    f.write("|")

    #iterate through transactions, adding each element seperated by a "|"
    for transaction in global_vars.transactions:
        f.write(transaction.year)
        f.write("|")
        f.write(transaction.month)
        f.write("|")
        f.write(transaction.day)
        f.write("|")
        f.write(transaction.type)
        f.write("|")
        f.write(transaction.amount)
        f.write("|")
        f.write(transaction.merchant)
        f.write("|")
        f.write(transaction.note)
        f.write("|")

    #close file
    f.close()

def read_from_file():

    #open file for reading
    f = open("Transactions", "r")

    #read entire text file into string txt variable
    txt = f.read()

    #close file
    f.close()

    #read num transactions from first element of txt
    char_pos_1 = txt.index("|")
    number_of_transactions = txt[0:char_pos_1]

    #read global year from second element of txt
    char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
    global_vars.year = txt[char_pos_1+1:char_pos_2]

    #read global month from third element of txt
    char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
    global_vars.month = txt[char_pos_2+1:char_pos_1]

    #create transactions based on the number of elements listed at the beginning of file
    for x in range(int(number_of_transactions)):

        #collect year of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        year = txt[char_pos_1+1:char_pos_2]

        #collect month of transaction
        char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
        month = txt[char_pos_2+1:char_pos_1]

        #collect day of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        day = txt[char_pos_1+1:char_pos_2]

        #collect type of transaction
        char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
        type = txt[char_pos_2+1:char_pos_1]

        #collect amount of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        amount = txt[char_pos_1+1:char_pos_2]

        #collect merchant of transaction
        char_pos_1 = txt.index("|", char_pos_2+1, len(txt))
        merchant = txt[char_pos_2+1:char_pos_1]

        #collect note of transaction
        char_pos_2 = txt.index("|", char_pos_1+1, len(txt))
        note = txt[char_pos_1+1:char_pos_2]

        #set char_pos_1 with value of ending indent, for resent of for loop
        char_pos_1 = char_pos_2

        #creat the transaction
        add_transaction(year, month, day, type, amount, merchant, note)