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


    def savings_deposit(self):
        try:
            amount = float(self.savings_deposit_entry.get())
            if self.savings.deposit(amount):
                messagebox.showinfo("Success", f"Successful Deposit Of {amount}")
            else:
                messagebox.showerror("Error", "Invalid amount")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
        self.update_savings_balance()

    def savings_withdraw(self):
        try:
            amount = float(self.savings_withdraw_entry.get())
            if self.savings.withdraw(amount):
                messagebox.showinfo("Success", f"Success Withdrewal Of {amount}")
            else:
                messagebox.showerror("Error", f"Exceed Withdrawal limit")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number")
        self.update_savings_balance()

    def update_savings_balance(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text").startswith("Savings Account:"):
                widget.config(text=f"Savings Account: {self.savings.get_balance()}")

    def current_menu(self):
        self.clear_window()

        label = tk.Label(self.root, text=f"Current Account: {self.current.get_balance()}", font=("Arial", 12))
        label.pack(pady=10)

        deposit_frame = tk.Frame(self.root)
        deposit_frame.pack(pady=5)
        tk.Label(deposit_frame, text="Deposit Amount:").pack(side=tk.LEFT)
        self.current_deposit_entry = tk.Entry(deposit_frame)
        self.current_deposit_entry.pack(side=tk.LEFT)

        withdraw_frame = tk.Frame(self.root)
        withdraw_frame.pack(pady=5)
        tk.Label(withdraw_frame, text="Withdraw Amount:").pack(side=tk.LEFT)
        self.current_withdraw_entry = tk.Entry(withdraw_frame)
        self.current_withdraw_entry.pack(side=tk.LEFT)

        btn_deposit = tk.Button(self.root, text="DEPOSIT", command=self.current_deposit)
        btn_deposit.pack(pady=10)

        btn_withdraw = tk.Button(self.root, text="WITHDRAWAL", command=self.current_withdraw)
        btn_withdraw.pack(pady=10)

        btn_back = tk.Button(self.root, text="RETURN", command=self.create_main_menu)
        btn_back.pack(pady=10)

        self.update_current_balance()

    def current_deposit(self):
        try:
            amount = float(self.current_deposit_entry.get())
            if self.current.deposit(amount):
                messagebox.showinfo("Success", f"Succesful Deposit Of {amount}")
            else:
                messagebox.showerror("Error",f"Invalid amount")
        except ValueError:
            messagebox.showerror("Error",f"Enter a valid number")
        self.update_current_balance()

    def current_withdraw(self):
        try:
            amount = float(self.current_withdraw_entry.get())
            if self.current.withdraw(amount):
                messagebox.showinfo("Success", f"Withdrew {amount}")
            else:
                messagebox.showerror("Error",f"insufficient balance")
        except ValueError:
            messagebox.showerror("Error",f"Enter a valid number")
        self.update_current_balance()

    def update_current_balance(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text").startswith("Account Balance:"):
                widget.config(text=f"Account Balance: {self.current.get_balance()}")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
