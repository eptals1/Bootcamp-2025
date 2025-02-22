print('''
----------------------------------------
Welcome to BANCO DE ONG YIU!           |
----------------------------------------
''')

deposit_amount = 0
withdraw_amount = 0
balance = 1000
login_retry = 3


# class BankAccounts:
#     def __init__(self, pin_number, balance):
#         self.pin_number = pin_number
#         self.balance = balance

#     def login(self, login_retry):
#         while login_retry > 0:
#             user_pin = input("Enter your pin: ")
#             if user_pin == self.pin_number:
#                 print("Login successful!")
#                 break
#             else:
#                 print("Invalid pin. Please try again.")
#                 login_retry -= 1
#                 if login_retry == 0:
#                     print("Too many attempts. Account blocked.")

# if __name__ == "__main__":
#     account = BankAccounts("1234", 1000)
#     account.login(login_retry)

def start_transaction(deposit_amount, withdraw_amount, balance):
    user_selection = input("What do you want to do? \n Deposit [1] \n Withdraw [2] \n Check balance [3] \n Exit [4]: ")
    if user_selection == "1":
        deposit_amount = int(input("Enter deposit amount: "))
        balance += deposit_amount
        print("Your new balance is: ", balance, "\nDeposit successful!")
    elif user_selection == "2":
        withdraw_amount = int(input("Enter withdraw amount: "))
        balance -= withdraw_amount
        print("Your new balance is: ", balance, "\nWithdraw successful!")
    elif user_selection == "3":
        print("Your balance is: ", balance)
    elif user_selection == "4":
        print("Exiting...")
    else:
        print("Invalid selection. Please try again.")

def login(login_retry):
    while login_retry > 0:
        user_pin = int(input('Enter your 4-digit PIN: '))
        if user_pin == 1234:    
            start_transaction(deposit_amount, withdraw_amount, balance)
        else:
            login_retry -= 1
            print("Incorrect PIN. Please try again.")
            if login_retry == 0:
                print("Too many attempts. Account blocked.")

login(login_retry)