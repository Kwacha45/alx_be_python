class BankAccount:

  def __init__(self, initial_balance=0):

    self.account_balance = initial_balance

  def deposit(self, amount):

    self.account_balance += amount

  def withdraw(self, amount):

    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      print("Insufficient funds. Withdrawal declined.")
      return False

  def display_balance(self):

    print(f"Your current balance is: ${self.account_balance:.2f}")

from bank_account import BankAccount

import sys

if len(sys.argv) != 3:
  print("Usage: python main-0.py <account_name> <operation amount>")
  exit(1)

account_name = sys.argv[1]
operation = sys.argv[2]
amount = float(sys.argv[3])
bank_account = BankAccount()

if operation == "deposit":
  bank_account.deposit(amount)
  print(f"Deposited: ${amount:.2f} to {account_name}'s account.")
elif operation == "withdraw":
  if bank_account.withdraw(amount):
    print(f"Withdrew ${amount:.2f} from {account_name}'s account.")
else:
  print(f"Invalid operation: {operation}")
  print(f"Current Balance: ${self.account_balance:.2f}")
bank_account.display_balance()