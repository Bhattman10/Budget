# Transaction.py

class Transaction:
    def __init__(self, date, transaction_type, amount=None, merchant=None, note=None):
        self.date = date
        self.transaction_type = transaction_type
        self.amount = amount
        self.merchant = merchant
        self.note = note

def __repr__(self):
    return f"Transaction(date={self.date}, type={self.transaction_type}, amount={self.amount}, merchant={self.merchant}, note={self.note})"

def add_transaction(transactions, date, transaction_type, amount, merchant, note):
    transaction = Transaction(date, transaction_type, amount, merchant, note)
    transactions.append(transaction)