class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit (self,amount):
        if amount>=0:
            self.balance+=amount
            print(f"Deposited:{amount}.Newbalance:{self.balance}")
        else :
            print("Deposit should be positive ")
    def withdrawal(self,amount):
        if amount <=self.balance and amount>0:
            print(f"Withdrawal :{amount}.Newbalance:{self.balance}")
        else :
            print ("INsufficient balance or INvalid")
    def display_account_info(self):
        print("\n ---account information----")
        print(f"Account Holder :{self.account_holder}")
        print(f"Current balance:{self.balance}")
account1=BankAccount("John Doe",1000)
account1.display_account_info()
account1.deposit(500)
account1.withdrawal(200)
account1.display_account_info()
