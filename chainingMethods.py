
# * Craig Burke - Assignment: Chaining Methods


class User:
    bank_name = "First National Dojo"

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(
            f"{self.name}, Your deposit of {amount} has been accepted,\nYour balance is {self.account_balance}.\nThank You!")
        print("")
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(
            f"{self.name}, Your withdrawal of {amount} has been accepted,\nYour balance is {self.account_balance}.\nThank You!")
        print("")
        return self

    def display_user_balance(self):
        print(
            f"{self.name}, Your balance is: {self.account_balance}.\nThank You!")
        print("")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(
            f"{self.name}, the transfer to {other_user.name}\nfor the amount of {amount}, has been processed.\nThank You!")
        print("")
        return self


""" 
#// 1. Update your previous assignment so that each instance's methods are chained
"""

jbgoode = User("Johnny B Goode", "jbgoode@berrymail.com", 24)
guido = User("Guido van Rossum", "guido@python.com", 36)
monty = User("Monty Python", "monty@python.com", 42)


jbgoode.make_deposit(600).make_deposit(100).make_deposit(
    70).make_withdrawal(200).display_user_balance()

guido.make_deposit(200).make_deposit(100).make_withdrawal(
    37).make_withdrawal(125).display_user_balance()

monty.make_deposit(400).make_withdrawal(20).make_withdrawal(
    153).make_withdrawal(67).display_user_balance()


jbgoode.transfer_money(monty, 80).display_user_balance()
monty.display_user_balance()
