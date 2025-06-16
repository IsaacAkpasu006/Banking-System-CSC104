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

    def savings_menu(self):
        self.clear_window()

        label = tk.Label(self.root, text=f"Savings Account Balance: {self.savings.get_balance()}", font=("Time New Roman", 20))
        label.pack(pady=10)

        deposit_frame = tk.Frame(self.root)
        deposit_frame.pack(pady=10)
        tk.Label(deposit_frame, text="Deposit Amount:").pack(side=tk.LEFT)
        self.savings_deposit_entry = tk.Entry(deposit_frame)
        self.savings_deposit_entry.pack(side=tk.LEFT)

        withdraw_frame = tk.Frame(self.root)
        withdraw_frame.pack(pady=10)
        tk.Label(withdraw_frame, text="Withdraw Amount:").pack(side=tk.LEFT)
        self.savings_withdraw_entry = tk.Entry(withdraw_frame)
        self.savings_withdraw_entry.pack(side=tk.LEFT)

        btn_deposit = tk.Button(self.root, text="DEPOSIT", command=self.savings_deposit)
        btn_deposit.pack(pady=10)

        btn_withdraw = tk.Button(self.root, text="WITHDRAW", command=self.savings_withdraw)
        btn_withdraw.pack(pady=10)

        btn_back = tk.Button(self.root, text="RETURN", command=self.create_main_menu)
        btn_back.pack(pady=10)

        self.update_savings_balance()



if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
