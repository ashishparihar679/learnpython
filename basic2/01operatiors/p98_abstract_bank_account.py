
from abc import ABC, abstractmethod


# ==================================
# 1. ABSTRACT CLASS
# ==================================

class BankAccount(ABC):

    # Class Variables
    bank_name = "State Bank of India"
    min_balance = 2000

    def __init__(self, name, acc_no, pin, balance):

        # Instance Variables
        self.name = name
        self.acc_no = acc_no
        self.__pin = pin
        self.balance = balance

        # Separate transaction list for every account
        self.transaction_history = []

    # ==================================
    # PIN VERIFICATION
    # ==================================

    def verify_pin(self, entered_pin):

        if self.__pin == entered_pin:
            return True
        else:
            print("Invalid PIN.")
            return False

    # ==================================
    # ACCOUNT DETAILS
    # ==================================

    def account_details(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print("Bank Name:", BankAccount.bank_name)
        print("Account Holder:", self.name)
        print("Account Number:", self.acc_no)
        print("Account Type:", self.__class__.__name__)
        print("Current Balance: ₹", self.balance)

    # ==================================
    # CHECK BALANCE
    # ==================================

    def check_balance(self):

        print("\nAvailable Balance: ₹", self.balance)

    # ==================================
    # DEPOSIT
    # ==================================

    def deposit(self, amount, entered_pin):

        if not self.verify_pin(entered_pin):
            print("Deposit rejected.")
            return

        if amount <= 0:
            print("Invalid amount.")
            print("Deposit rejected.")
            return

        self.balance += amount

        self.transaction_history.append(
            f"Deposited: ₹{amount}"
        )

        print("Deposit successful.")
        print("Updated Balance: ₹", self.balance)

    # ==================================
    # ABSTRACT WITHDRAW METHOD
    # ==================================

    @abstractmethod
    def withdraw(self, amount, entered_pin):
        pass

    # ==================================
    # TRANSACTION HISTORY
    # ==================================

    def show_transaction_history(self):

        print("\n========== TRANSACTION HISTORY ==========")

        if len(self.transaction_history) == 0:
            print("No transactions available.")

        else:
            for transaction in self.transaction_history:
                print(transaction)

        print("Total Transactions:", len(self.transaction_history))


# ==================================
# 2. SAVINGS ACCOUNT
# ==================================

class SavingsAccount(BankAccount):

    def withdraw(self, amount, entered_pin):

        if not self.verify_pin(entered_pin):
            print("Withdrawal rejected.")
            return

        if amount <= 0:
            print("Invalid amount.")
            print("Withdrawal rejected.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            print("Withdrawal rejected.")
            return

        # Savings Account Minimum Balance Condition
        remaining_balance = self.balance - amount

        if remaining_balance < BankAccount.min_balance:
            print("Minimum balance condition violated.")
            print("Withdrawal rejected.")
            return

        self.balance -= amount

        self.transaction_history.append(
            f"Withdrawn: ₹{amount}"
        )

        print("Withdrawal successful.")
        print("Updated Balance: ₹", self.balance)


# ==================================
# 3. CURRENT ACCOUNT
# ==================================

class CurrentAccount(BankAccount):

    def withdraw(self, amount, entered_pin):

        if not self.verify_pin(entered_pin):
            print("Withdrawal rejected.")
            return

        if amount <= 0:
            print("Invalid amount.")
            print("Withdrawal rejected.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            print("Withdrawal rejected.")
            return

        # Current Account has no minimum balance restriction
        self.balance -= amount

        self.transaction_history.append(
            f"Withdrawn: ₹{amount}"
        )

        print("Withdrawal successful.")
        print("Updated Balance: ₹", self.balance)


# ==================================
# 4. CREATE MULTIPLE ACCOUNTS
# ==================================

savings = SavingsAccount(
    "Ashish",
    1001,
    1234,
    10000
)

current = CurrentAccount(
    "Rahul",
    1002,
    5678,
    10000
)


# ==================================
# 5. ATM MENU
# ==================================

def atm_menu(account):

    while True:

        print("\n========== ATM BANKING SYSTEM ==========")
        print("1. View Account Details")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            account.account_details()

        elif choice == "2":

            account.check_balance()

        elif choice == "3":

            amount = float(input("Enter deposit amount: ₹"))
            pin = int(input("Enter your PIN: "))

            account.deposit(amount, pin)

        elif choice == "4":

            amount = float(input("Enter withdrawal amount: ₹"))
            pin = int(input("Enter your PIN: "))

            account.withdraw(amount, pin)

        elif choice == "5":

            account.show_transaction_history()

        elif choice == "6":

            print("Thank you for using ATM.")
            break

        else:

            print("Invalid choice. Please try again.")


# ==================================
# 6. ACCOUNT SELECTION
# ==================================

while True:

    print("\n========== SELECT ACCOUNT ==========")
    print("1. Savings Account")
    print("2. Current Account")
    print("3. Exit")

    choice = input("Select your account: ")

    if choice == "1":

        atm_menu(savings)

    elif choice == "2":

        atm_menu(current)

    elif choice == "3":

        print("Thank you. Banking system closed.")
        break

    else:

        print("Invalid account choice.")
