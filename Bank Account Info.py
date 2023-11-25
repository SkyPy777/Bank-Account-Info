

# Dictionary to store bank account information
bank_accounts = {}

def create_account():
    account_number = input("Enter account number: ")

    # Check if the account number is already in use
    if account_number in bank_accounts:
        print("Account number already exists. Please choose a different one.")
        return

    # Account with a balance of 0
    bank_accounts[account_number] = {'balance': 0}
    print(f'Account {account_number} created successfully.')

def check_balance():
    account_number = input("Enter your account number: ")

    # Check if the account number exists
    if account_number in bank_accounts:
        balance = bank_accounts[account_number]['balance']
        print(f'Your account balance is: ${balance}')
    else:
        print("Account not found. Please check your account number.")

def deposit_money():
    account_number = input("Enter your account number: ")

    # Check if the account number exists
    if account_number in bank_accounts:
        amount = float(input("Enter the amount to deposit: "))
        bank_accounts[account_number]['balance'] += amount
        print(f'${amount} deposited successfully. Your new balance is: ${bank_accounts[account_number]["balance"]}')
    else:
        print("Account not found. Please check your account number.")

def withdraw_money():
    account_number = input("Enter your account number: ")

    # Check if the account number exists
    if account_number in bank_accounts:
        balance = bank_accounts[account_number]['balance']
        amount = float(input(f'Enter the amount to withdraw (current balance: ${balance}): '))

        # Check if there is enough balance to withdraw
        if amount <= balance:
            bank_accounts[account_number]['balance'] -= amount
            print(f'${amount} withdrawn successfully. Your new balance is: ${bank_accounts[account_number]["balance"]}')
        else:
            print("Insufficient funds.")
    else:
        print("Account not found. Please check your account number.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Create a New Account")
    print("2. Check Account Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_account()
    elif choice == '2':
        check_balance()
    elif choice == '3':
        deposit_money()
    elif choice == '4':
        withdraw_money()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")










