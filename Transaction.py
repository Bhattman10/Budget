# Transaction.py

class Transaction:
    def __init__(self, year, month, day, type, amount=None, merchant=None, note=None):
        self.year = year
        self.month = month
        self.day = day
        self.type = type
        self.amount = amount
        self.merchant = merchant
        self.note = note

def add_transaction(transactions, year, month, day, type, amount, merchant, note):
    transaction = Transaction(year, month, day, type, amount, merchant, note)
    transactions.append(transaction)