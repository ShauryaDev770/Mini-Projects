def Convertor():

    choice = input("Do you want to convert USD into INR or INR into USD? (INR to USD / USD to INR)").lower()
    print(choice)
    if choice == "inr to usd":
        INR  = int(input("Give the INR value: "))
        USD = INR/90
        print("$",USD)

    elif choice == "usd to inr":
        american_money = int(input("Enter the value USD value: "))
        print(american_money*90,"INR")

while True:
    Convertor()
    repeat = input("Do you want to convert more? (y/n)").lower()
    if repeat == "n":
        break