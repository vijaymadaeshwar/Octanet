class ATM:
    def __init__(self):
        self.users = {
            '123456': {'pin': '1234', 'balance': 1000, 'transactions': []},
            '789012': {'pin': '5678', 'balance': 1500, 'transactions': []}
        }
        self.current_user = None

    def authenticate_user(self):
        user_id = input("Enter User ID: ")
        pin = input("Enter PIN: ")
        if user_id in self.users and self.users[user_id]['pin'] == pin:
            self.current_user = user_id
            print("Authentication successful!")
            return True
        else:
            print("Invalid User ID or PIN.")
            return False

    def display_menu(self):
        print("\n ATM Menu:")
        print("1. View Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Money")
        print("5. View Transaction History")
        print("6. Quit")

    def view_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"Your current balance is: Rs{balance}")

    def withdraw_money(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.users[self.current_user]['balance']:
            print("Insufficient funds.")
        else:
            self.users[self.current_user]['balance'] -= amount
            self.users[self.current_user]['transactions'].append(f"Withdrawn Rs{amount}")
            print("Transaction successful.")

    def deposit_money(self):
        amount = float(input("Enter amount to deposit: "))
        self.users[self.current_user]['balance'] += amount
        self.users[self.current_user]['transactions'].append(f"Deposited Rs{amount}")
        print("Transaction successful.")

    def transfer_money(self):
        recipient_id = input("Enter recipient's User ID: ")
        if recipient_id not in self.users:
            print("Recipient not found.")
            return
        amount = float(input("Enter amount to transfer: "))
        if amount > self.users[self.current_user]['balance']:
            print("Insufficient funds.")
        else:
            self.users[self.current_user]['balance'] -= amount
            self.users[recipient_id]['balance'] += amount
            self.users[self.current_user]['transactions'].append(f"Transferred Rs{amount} to {recipient_id}")
            self.users[recipient_id]['transactions'].append(f"Received Rs{amount} from {self.current_user}")
            print("Transaction successful.")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.users[self.current_user]['transactions']:
            print(transaction)

    def start(self):
        print("Welcome to the ATM!")
        while True:
            if self.authenticate_user():
                while True:
                    self.display_menu()
                    choice = input("Enter your choice: ")
                    if choice == '1':
                        self.view_balance()
                    elif choice == '2':
                        self.withdraw_money()
                    elif choice == '3':
                        self.deposit_money()
                    elif choice == '4':
                        self.transfer_money()
                    elif choice == '5':
                        self.view_transaction_history()
                    elif choice == '6':
                        print("Thank you for using the ATM. Goodbye!")
                        return
                    else:
                        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.start()
