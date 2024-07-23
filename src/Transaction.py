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