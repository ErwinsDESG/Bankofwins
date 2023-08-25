class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
#Pou m mete lajan
    def deposit(self,amount):
        if(amount>499):
            self.balance=self.balance+amount
        else:
            print("The first deposit must not be less than 500.00 HTG")
#Pou m retire lajan
    def withdraw(self,amount):
        if (amount<self.balance):
            self.balance=self.balance-amount
        else:
            print("You don't have enough money in your account. ")
#Pou m afiche kont lan(yo)     
    def __str__(self):
        return f"account_number:{self.account_number}\naccount_holder:{self.account_holder}\nbalance:{self.balance:.2f}HTG\n"
#Premye kont pou enonse a      
account1=BankAccount("00340203","Lub Lorry",10000.00)
account1.deposit(500)
account1.withdraw(200)
print(account1)



#Ese ak non pam poum teste kondisyon m yo
"""account2=BankAccount("00340204","Erwins DESGRANGES",00.00)
account2.deposit(300)
account2.withdraw(400)
print(account2)"""
