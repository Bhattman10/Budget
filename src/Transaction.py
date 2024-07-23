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

    # Iterate the ID, to create special ID for each transaction
    global_vars.ID+=1

    # Create transaction
    transaction = Transaction(global_vars.ID, year, month, day, type, amount, merchant, note)

    # Add transaction to list
    global_vars.transactions.append(transaction)

    # Update file with transactions
    # write_to_file()

def delete_transaction(ID_to_delete):

    # Iterating through transactions ending with position we want to delete
    iterator = 0

    #Iterate through transactions, breaking when the correct transaction was discovered
    for transaction in global_vars.transactions:
        iterator+=1
        if int(transaction.ID) == int(ID_to_delete):
            break
    
    # Pop the transaction
    global_vars.transactions.pop(iterator-1)

    #Upadate the file
    # write_to_file()

# def write_to_file():

#     # Open month's file
#     f = open("July2024.txt", "w")

#     # Format the global ID

#     #Write the unique ID to the file, which will be loaded-in later
#     f.write(global_vars.ID)

#     #Iterate through list and add elements of transaction one-by-one
#     for transaction in global_vars.transactions:
#         f.write(str(transaction.ID))
#         f.write(str(transaction.year))
#         f.write(str(transaction.month))
#         f.write(str(transaction.day))
#         f.write(str(transaction.type))
#         f.write(str(transaction.amount))
#         f.write(transaction.merchant)
#         f.write(transaction.note)

# def read_from_file():

#     # Char iterator for indicating which char(s) to read next
#     char = 0

#     # Open month's file
#     f = open("July2024.txt", "r")

#     # Read global ID from first char of file
#     # 6 chars alow for 999,999 transaction additions per month
#     global_vars.ID = f.read(6)
#     # Convert ID back to int
#     global_vars.ID = int(global_vars.ID)
#     # Iterate char variable
#     char+=6
#     #TESTING
#     print(global_vars.ID)