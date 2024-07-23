import unittest
# Import the Transaction class and functions from transactions.py
from Transaction import Transaction, add_transaction, delete_transaction
# Import global_vars.py
import global_vars
# Import print.py
from print import print_menu, print_transactions

class TestAddDelete(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_add_delete_basic(self):

        # Add transaction
        add_transaction(2024, 7, 23, 1, 100.00, 'Nike', 'new shoes!')

        # Test first transaction
        self.assertEqual(global_vars.transactions[0].year, 2024)
        self.assertEqual(global_vars.transactions[0].month, 7)
        self.assertEqual(global_vars.transactions[0].day, 23)
        self.assertEqual(global_vars.transactions[0].type, 1)
        self.assertEqual(global_vars.transactions[0].amount, 100.00)
        self.assertEqual(global_vars.transactions[0].merchant, 'Nike')
        self.assertEqual(global_vars.transactions[0].note, 'new shoes!')

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 1)

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 0)

    def test_add_delete_normal(self):

        # Add transactions
        add_transaction(2024, 7, 23, 1, 100.00, 'Nike', 'new shoes!')
        add_transaction(2024, 7, 24, 1, 100.00, 'Puma', 'new shoes!')
        add_transaction(2024, 7, 25, 1, 100.00, 'Crocs', 'new shoes!')

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 2)

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 1)

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 0)

    def test_add_delete_complex(self):

        # Add transaction
        add_transaction(2024, 7, 23, 1, 100.00, 'Nike', 'new shoes!')

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 0)

        # Add transactions
        add_transaction(2024, 7, 23, 1, 100.00, 'Nike', 'new shoes!')
        add_transaction(2024, 7, 23, 1, 100.00, 'Adidas', 'new shoes!')
        add_transaction(2024, 7, 23, 1, 100.00, 'Puma', 'new shoes!')

        # Delete transaction
        delete_transaction(0)

        # Test first transaction
        self.assertEqual(global_vars.transactions[0].merchant, 'Adidas')
        self.assertEqual(global_vars.transactions[1].merchant, 'Puma')

        # Delete transaction
        delete_transaction(0)

        # Delete transaction
        delete_transaction(0)

        # Test size of list
        self.assertEqual(len(global_vars.transactions), 0)

if __name__ == '__main__':
    unittest.main()