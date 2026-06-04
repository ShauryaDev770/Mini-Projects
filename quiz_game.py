Q1= input("What is the capital of France?").lower()

if Q1 == "Paris":
    Score1= 5
else:
    Score1 = 0

Q2 = input("What is the capital of Japan?").lower()
if Q2 == "Tokyo":
    Score2 = 5
else:
    Score2 = 0

Q3 = input("What is the capital of India?").lower()
if Q3 == "New Delhi":
    Score3 = 5
else:
    Score3 = 0

Q4 = input("What is the capital of England?").lower()
if Q4 == "London":
    Score4 = 5
else: 
    Score4 =0

Q5 = input("What is the capital of America?").lower()
if Q5 == "Washington DC":
    Score5 = 5
else: 
    Score5 =0

Final_score =  Score1+Score2+Score3+Score4+Score5
print(f"Your final score is {Final_score} out of 25")

