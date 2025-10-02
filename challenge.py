# challenge.py

balance = 1000
withdrawal_count = 0
max_withdrawals = 3

while True:
    print("\nATM Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = input("Enter deposit amount: P")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance = balance + amount
                print("Deposit successful!")
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    elif choice == "2":
        if withdrawal_count >= max_withdrawals:
            print("Withdrawal limit reached (3).")
            continue

        amount = input("Enter withdrawal amount: P")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                if amount <= balance:
                    balance = balance - amount
                    withdrawal_count = withdrawal_count + 1
                    print("Withdrawal successful!")
                else:
                    print("Insufficient balance.")
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    elif choice == "3":
        print("Your balance is: P", balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
