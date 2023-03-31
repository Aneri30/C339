#!/usr/bin/env python
# Group assignment
# Date: March 9, 2022
# Group 1: Lucas, Aneri, Johannes, Lina
#######
import sys
class User:
    def __init__(self, name, account_number, balance, pin):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.pin = pin
        self.remainingTries = 3
        
        self.validPin = False

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance
    
    ##################################

    def setPinValidity(self, valid):
        self.validPin = valid   

    def authenticate(self):
        while self.remainingTries > 0:
            inputPin = int(input("Please enter your pin: "))
            if inputPin == self.pin:
                self.setPinValidity(True)
                return True
            else:
                self.remainingTries = self.remainingTries - 1
                print(f"Pin is wrong. Enter your pin again. You have {self.remainingTries} attempts left.")
        
        print("Maximum number of attempts reached. Login failed")
        raise SystemExit

class CreditCard:
     def __init__(self, name, account_number) -> None:
          self.name = name
          self.account_number = account_number
    
class ATM_SESSION:
    def __init__(self, users):
        self.remainingTries = 3
        self.users = users
        self.active_user: User= None 

    def withdraw(self):
        withdraw_amount = 0
        try:
            withdraw_amount = int(input("Type the amount you wish to withdraw: "))
        except:
            print(f"Please choose a valid amount to withdraw")
            self.withdraw()

        if withdraw_amount > self.active_user.get_balance(): 
                print(f"You canot withdraw {withdraw_amount}. You current available funds are: {self.active_user.balance} Euro.")
                return False
        else:
            new_balance = self.active_user.get_balance() - withdraw_amount
            self.active_user.set_balance(new_balance) 
            print(f"Your current available funds are: {self.active_user.get_balance()} Euro.")
            return True
        
    def checkBalance(self):
        print(f"Your current available funds are: {self.active_user.get_balance()} Euro.")
        return True

    def changePin(self):
        pin1 = input("Type your new pin: ")
        pin2 = input("Type again your new pin: ")

        if (pin1 == pin2):
            self.active_user.pin = pin1
            print("PIN change succesfull!")
            return True
        else:
            print("Pin numbers do not match. Nothing changed!")
            return False
        
    def makeDeposit(self):
        depositAmount = int(input("Enter the amount you want to deposit: "))
        new_deposit_amount = self.active_user.get_balance() + depositAmount
        self.active_user.set_balance(new_deposit_amount)
        print(f"Your new balance is {self.active_user.get_balance()} Euro.")
        return True
    
    def exit(self):
        print("Thank you for choosing ABC bank! Bye!")
        raise SystemExit
        # TODO start session again?
            #self.start_session()
    
    def start_session(self, credit_card:CreditCard):
        operationMenu = {
            "1": { 
                "title": "Withdraw",
                "message": "How much would you like to withdraw today?",
                "function": self.withdraw
            },
            "2": { 
                "title": "Check Balance",
                "message": "You have requested to see your balance",            
                "function": self.checkBalance
            },
            "3": {
                "title": "Change Pin",
                "message": "Please enter your new pin.",
                "function": self.changePin
            },
            "4": {
                "title": "Make Deposit",
                "message": "How much would you like to deposit today?",
                "function": self.makeDeposit                
            },
            "5": {
                "title": "Exit",
                "message": "Thank you for your choosing ABC Bank. Bye!",
                "function": self.exit,
            }
        }

        #match credit card with user
        for user in self.users:
            if user.account_number == credit_card.account_number:
                self.active_user = user
                break
        if not self.active_user:
            print("User not found")
            raise SystemExit

        if self.active_user.authenticate():
            while(True):
                print()
                for option in operationMenu:
                    print(f"Choose {option} for operation '{operationMenu[option]['title']}'")
    
                print()
                chosen_option = input(f"Hi {self.active_user.name}. Type the number of the operation you wish to perform: ")
                try:
                    print(operationMenu[chosen_option]['message'])
                    result = operationMenu[chosen_option]['function']()
                except KeyError:
                    print("Option not recognized.")
                    self.exit()

                if result:
                    print("Operation successful!")
                else:
                    print("Operation failed!")

        else:
            self.exit()

    
def main():
    #We have different users stored in a database
    u1 = User(name="Tom", account_number=0, balance=3467, pin=5555)
    u2 = User(name="Tim", account_number=1, balance=2356, pin=1234)
    u3 = User(name="Tam", account_number=2, balance=8643, pin=6475)
    users = [u1, u2, u3]
    atm1 = ATM_SESSION(users)


    c1 = CreditCard(name="Tim", account_number=1)
    c2 = CreditCard(name="Tim", account_number=999)
    c3 = CreditCard(name="Tam", account_number=2)

    atm1.start_session(c3)

if __name__ == '__main__':
    sys.exit(main())  