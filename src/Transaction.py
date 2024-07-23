# Transaction.py

# Import global_vars.py
import global_vars

class Transaction:
    def __init__(self, ID, year, month, day, type, amount=None, merchant=None, note=None):
        self.ID = ID
        self.year = year
        self.month = month
        self.day = day
        self.type = type
        self.amount = amount
        self.merchant = merchant
        self.note = note

def add_transaction(year, month, day, type, amount, merchant, note):
    global_vars.ID+=1
    transaction = Transaction(global_vars.ID, year, month, day, type, amount, merchant, note)
    global_vars.transactions.append(transaction)

def delete_transaction(ID_to_delete):

    iterator = 0
    itt_to_delete = 0

    for transaction in global_vars.transactions:
        iterator+=1
        if int(transaction.ID) == int(ID_to_delete):
            itt_to_delete = iterator
            break
    
    global_vars.transactions.pop(itt_to_delete-1)