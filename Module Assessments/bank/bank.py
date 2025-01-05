class BankAccount:
    def __init__(self, account_number, holder_name, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = 0.0
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def get_account_type(self):
        return self.account_type

    def get_account_number(self):
        return self.account_number

    def get_holder_name(self):
        return self.holder_name

    def get_transaction_history(self):
        return self.transaction_history

    def display_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)


account = BankAccount("123456789", "Ahmed Essam", "Savings")

account.deposit(500)

account.withdraw(200)

account.check_balance()

print(f"Account Type: {account.get_account_type()}")
print(f"Account Number: {account.get_account_number()}")
print(f"Holder Name: {account.get_holder_name()}")

account.display_transaction_history()