class bank_account:
  def __init__(self,account_number,balance=0):
    self.account_number=account_number
    self.balance=balance
  def deposit(self,amount):
    self.balance+=amount
    print(f"Deposited ${amount}. New balance is ${self.balance}")
  def withdraw(self,amount):
    if amount<=self.balance:
      self.balance-=amount
      print(f"Withdrew ${amount}. New balance is ${self.balance}")
    else:
      print("Insufficient funds")
  def check_balance(self):
    print(f"Account balance for account number {self.account_number}: ${self.balance}")

account = bank_account("123456789")
account.deposit(1000)
account.withdraw(500)
account.check_balance()
account.withdraw(1500)
account.check_balance()
