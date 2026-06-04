while True:
    num1 = input("Enter first number:")
    num1 =float(num1)

    if type(num1)!= float:
        print("Invalid input")
        exit()
    else:
        num1=float(num1)

    operator = input("Select operator (+,-,*,/):")


    num2= input("Enter second number:")
    num2 =float(num2)

    if type(num2) != float:
        print("Invalid input")
        exit()

    else:
        num2=float(num2)

    if num2 ==0 and operator=="/":
        print("Cannot divide by zero")
        exit()

    if operator=="+":
        print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        print(num1*num2)
    elif operator=="/":
        print(num1/num2)
    else:
        print("Invalid operator")

    again  = input("Run Again? (y/n) ")

    if again == "n":
        break


















