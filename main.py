

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def transfer(self, amount, target_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.deposit(amount)
            return True
        return False
    
    def account_holder(self, name):
        self.name = name
        return self.name

    def get_balance(self):
        return self.balance
    
# Example usage
if __name__ == "__main__":
    George = BankAccount(1000)
    Chaplin = BankAccount(500)

    print("Initial balance of account1:", George.get_balance())
    print("Initial balance of account2:", Chaplin.get_balance())

    # Deposit money
    George.deposit(200)
    print("Balance after deposit in account1:", George.get_balance())

    # Withdraw money
    George.withdraw(300)
    print("Balance after withdrawal in account1:", George.get_balance())

    # Transfer money
    George.transfer(200, Chaplin)
    print("Balance after transfer from account1 to account2:")
    print("George Washington:", George.get_balance())
    print("Chaplin McThresher:", Chaplin.get_balance())