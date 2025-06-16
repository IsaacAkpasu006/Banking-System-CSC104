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
    def __init__(self, initial_balance):
        self.balance = initial_balance

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

    def get_balance(self):
        return self.balance


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BINGHAM BANKING SYSTEM")
        
        self.savings = SavingsAccount(1520000, 500000)
        self.current = CurrentAccount(2500000)

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        label = tk.Label(self.root, text="ACCOUNT PROFILE", font=("Time New Roman", 20))
        label.pack(pady=20)

        btn_savings = tk.Button(self.root, text="SAVINGS ACCOUNT", width=30, command=self.savings_menu)
        btn_savings.pack(pady=10)

        btn_current = tk.Button(self.root, text="CURRENT ACCOUNT", width=30, command=self.current_menu)
        btn_current.pack(pady=10)
    


if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
