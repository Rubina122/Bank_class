
from abc import ABC,abstractmethod

class Bank(ABC):
    acc_no=0
    name=" "
    phone=""
    type=""
    balance=0
    @abstractmethod
    def create_account(self):
        pass
    def deposit_amount(self,amount):
        pass
    def withdraw(self,bal):
        pass
    def transfer(self,amount):
        pass

    def close(self):
        pass

class Customer(Bank):
    def create_account(self):
        self.acc_no = int(input("Enter the acc_no: "))
        self.name = input("Enter the Account Holder name: ")
        self.type = input("Enter the Account Type: ")
        self.balance = int(input("Enter The initial amount: "))
        print("\nAccount Created Successfully")

    def deposit_amount(self, amount):
        self.balance = self.balance + amount
        print(amount,"Deposited Succssfully")
        print("Total Amount is: ",self.balance)

    def withdraw(self, bal):
        if bal <= self.balance:
            self.balance = self.balance - bal
            print("withdraw successfully:",+bal)
            print("Availabe balance is:",self.balance)
        else:
            print("Insufficient funds are available ")

    def transfer(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.acc_no = int(input("Enter the acc_no: "))
            self.name = input("Enter the Account Holder name: ")
            self.balance = int(input("Enter The initial amount: "))
            print("Transaction Completed Succesfully")
        else:
            print("Insufficient Amount to transfer")

    def close(self):
        self.acc_no = int(input("Enter the acc_no: "))
        self.name = input("Enter the Account Holder name: ")
        self.phone = int(input("Enter the phone no: "))
        print("Account closed Successfully.")

cust1=Customer()
cust2=Customer()
cust1.create_account()
cust1.deposit_amount(500)
cust1.withdraw(100)
cust1.transfer(1000)
cust1.close()
cust2.create_account()
cust2.deposit_amount(600)
cust2.deposit_amount(600)
cust2.withdraw(500)
cust2.transfer(800)






