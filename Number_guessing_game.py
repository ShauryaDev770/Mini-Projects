import random
number = random.randint(1,10)


guess= input("Guess the number between 1 to 10: ")

if not guess.isdigit():
    print ("invalid input")                 # If i put -5 as input, isdigit will give me False because it minus sign is not a number. And same thing with float ex 7.2 .
    exit()                                     #Spaces in isdigit does not mean 0. Ex- ""isdigit() will give False
else:
    guess =int(guess)

if guess>10 or guess<1:
    print("Number is out of range")
    exit()

if guess == number:
    print("Correct!")

elif guess > number:
    print("too high")

else:
    print("too low")


