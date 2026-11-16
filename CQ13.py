#In any function in class we must have self as a variable
#self refers too the class it belongs to
class SavingsAccount:

    def __init__(self, account_id, balance, previous_balance, annual_interest_rate): #constructor function
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate

    def set_interest_rate(self, updated_interest_rate): #setters, functions that start with set
        self.annual_interest_rate = updated_interest_rate

    def get_monthly_interest_rate (self): #getters, functions that start with get
        return (self.annual_interest_rate / 12) / 100

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()

    def get_balance_change_percent(self):
        return ((self.balance - self.previous_balance) / self.previous_balance)*100

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount



def main():
     account = SavingsAccount(1122,20000.0,18500.0,4.5)   
     account.withdraw(2500)
     account.deposit(3000)
     print(f"Account Id: {account.account_id}")
     print(f"Current Balance: {account.balance}")
     print(f"Monthly Interest rate: {account.get_monthly_interest_rate()*100}%")
     print(f"Monthly Interest: {account.get_monthly_interest()}")
     print(f"Percent Change: {account.get_balance_change_percent()}%")
if __name__ == '__main__':
    main()