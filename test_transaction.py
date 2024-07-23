import unittest
from Transaction import add_transaction

class TestAdd(unittest.TestCase):
    
    def test_add_normal(self):

        # List to store transactions
        transactions = []

        # Set variables
        year = 2024
        month = 7
        day = 23
        type = 1
        amount = 100.00
        merchant = 'Nike'
        note = 'new shoes!'

        # Add transaction
        add_transaction(transactions, year, month, day, type, amount, merchant, note)

         # Test first transaction
        self.assertEqual(transactions[0].year, 2024)
        self.assertEqual(transactions[0].month, 7)
        self.assertEqual(transactions[0].day, 23)
        self.assertEqual(transactions[0].type, 1)
        self.assertEqual(transactions[0].amount, 100.00)
        self.assertEqual(transactions[0].merchant, 'Nike')
        self.assertEqual(transactions[0].note, 'new shoes!')

if __name__ == '__main__':
    unittest.main()