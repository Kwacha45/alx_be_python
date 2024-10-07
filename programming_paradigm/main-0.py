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
    print("Insufficient funds. Withdrawal declined.")
else:
  print(f"Invalid operation: {operation}")

bank_account.display_balance()