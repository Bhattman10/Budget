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

    #write to dated file
    write_to_file()

def delete_transaction(pos_to_delete):

    # Pop the transaction
    global_vars.transactions.pop(pos_to_delete)

def write_to_file():

    #open file
    f = open("July2024", "w")

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