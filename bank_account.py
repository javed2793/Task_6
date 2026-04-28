# Base Class
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance   

    # Getter method to check balance
    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


# Savings Account Class
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate

    # Method to calculate interest
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print("Interest:", interest)
        return interest


# Current Account Class
class CurrentAccount(BankAccount):
    def __init__(self, acc_no, balance, min_balance):
        super().__init__(acc_no, balance)
        self.min_balance = min_balance

    # Override withdraw method
    def withdraw(self, amount):
        if amount <= (self.get_balance() - self.min_balance):
            # Accessing private variable using parent method
            super().withdraw(amount)
        else:
            print("Cannot withdraw! Minimum balance should be maintained.")


# ---- Testing ----

print("Savings Account:")
s = SavingsAccount(101, 5000, 5)
s.deposit(1000)
s.withdraw(2000)
s.calculate_interest()
print("Balance:", s.get_balance())

print("\nCurrent Account:")
c = CurrentAccount(102, 5000, 1000)
c.deposit(2000)
c.withdraw(5500)   # Should fail due to min balance
c.withdraw(3000)   # Valid
print("Balance:", c.get_balance())
