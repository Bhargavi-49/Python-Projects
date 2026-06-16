Balance = 1000
while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    choice = input("Enter your choice(1/2/3/4): ")
    if choice == "1":
        print(f"Current Balance: {Balance}")
    elif choice == "2":
        Deposit_Money = float(input("please enter your deposit amount: "))
        Balance += Deposit_Money
    elif choice == "3":
        Withdraw_Money = float(input("please enter your withdraw amount: "))
        Balance -= Withdraw_Money
    elif choice == "4":
        break
    else:
        print("Please enter valid choice")