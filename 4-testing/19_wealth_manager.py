import unittest

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a positive amount from the account if sufficient balance is available."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                raise ValueError("Insufficient balance for withdrawal.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Create a BankAccount instance with an initial balance of 100
        self.account = BankAccount(initial_balance=100)

    def test_initial_balance(self):
        """Verify that the initial balance is set correctly."""
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        """Test depositing a positive amount and verify the updated balance."""
        self.assertEqual(self.account.deposit(50), 150)  # New balance should be 150

    def test_deposit_zero_amount(self):
        """Attempt to deposit zero amount (should raise ValueError)."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative_amount(self):
        """Attempt to deposit negative amount (should raise ValueError)."""
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_withdraw_sufficient_funds(self):
        """Test withdrawing a valid amount and verify the updated balance."""
        self.assertEqual(self.account.withdraw(30), 70)  # New balance should be 70

    def test_withdraw_insufficient_funds(self):
        """Attempt to withdraw more than available balance (should raise ValueError)."""
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_withdraw_zero_amount(self):
        """Attempt to withdraw zero amount (should raise ValueError)."""
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_withdraw_negative_amount(self):
        """Attempt to withdraw negative amount (should raise ValueError)."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

if __name__ == '__main__':
    unittest.main()
