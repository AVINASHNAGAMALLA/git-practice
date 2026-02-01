
from fastapi import FastAPI
from abc import ABC,abstractmethod

app=FastAPI()
class Account(ABC):
    
    def __init__(self,accn_num,cust_name,blnc):
        self._acc=accn_num
        self._cust=cust_name
        self._blnc=blnc
   
# Abstract methods:

# deposit(amount)

# withdraw(amount)

# get_balance()
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    
    def get_blnc(self):
        return {f'available balance is {self._blnc}'}
    

# 🔹 2. Derived Classes

# Create two account types:

# 🏦 SavingsAccount

# Minimum balance: 500

class Savings(Account):
    min_blnc=500 
    def deposit(self):
        amount=int(input('enter the you want to deposit'))
        self._blnc+=amount
        return {f'the deposit is success,available balance is{self._blnc}'}
    def withdraw(self):
        amount=int(input('enter the amount you want to withdraw'))
        if self._blnc-amount<500:
            print('withdraw is not possible')
        elif self._blnc-amount>500:

            self._blnc-=amount
            return {f'withdraw is success,{amount} is debited from account'}
    # def get_blnc(self):
    #     return {f'available balance is {self._blnc}'}
        

class Current(Account):

    overdraft_blnc=5000
    
    def deposit(self):
        amount=int(input('enter the amount you want to deposit'))
        self._blnc+=amount
        return {f'the deposit is success,available balance is{self._blnc}'}
    def withdraw(self):
        amount=int(input('enter the amount you want to withdraw'))
        if self._blnc-amount<5000:
            print('withdraw is not possible')
        elif self._blnc-amount>5000:
            self._blnc-=amount
            return {f'withdraw is success,{amount} is debited from account'}
    # def get_blnc(self):
    #     return {f'available balance is {self._blnc}'}
    
accounts=[Savings(9067,'Avinash',5000),Current(9067,'avinash',10000)]

for a in accounts:
    #print(a.basic(9067,'Avinash'))
    print(a.deposit())
    print(a.withdraw())
    print(a.get_blnc())
    print('*'*30)
        

# Withdrawal should fail if balance goes below minimum

# 🏢 CurrentAccount

# No minimum balance

# Allow overdraft up to -5000

# 🔹 3. Encapsulation Rules

# Balance must be private

# No direct access to balance from outside the class

# 🔹 4. Polymorphism

# Store different account objects in one list

# Call withdraw() polymorphically