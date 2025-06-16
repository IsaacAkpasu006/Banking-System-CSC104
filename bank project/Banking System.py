import tkinter as tk
from tkinter import messagebox

class SavingsAccount:
    def __init__(self, initial_balance, withdrawal_limit):
        self.balance = initial_balance
        self.withdrawal_limit = withdrawal_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.withdrawal_limit and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class CurrentAccount:

class BankApp:
    


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
