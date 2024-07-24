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

def delete_transaction(pos_to_delete):

    # Pop the transaction
    global_vars.transactions.pop(pos_to_delete)

def write_to_file():

    #open file for writing
    f = open("Transactions", "w")

    #write the number of elements in transaction
    f.write(str(len(global_vars.transactions)))
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

    #attain length of txt file
    length_of_file = len(txt)

    #find first occurance of seperated character, and indicate which char holds position
    char_pos_1 = txt.index("|")
    number_of_transactions = txt[0:char_pos_1]

    #create transactions based on the number of elements listed at the beginning of file
    for x in range(int(number_of_transactions)):
        pass