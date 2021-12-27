import random
# Press the green button in the gutter to run the script.


print("Guess the number game")

# print("how many attempts?")
rangeStarts=input("range starts from: ")
rangeLimit=input("range limits by: ")
attempt=10
number=0


x=random.randint(1,100)
attempts=0
print(x)
#attempt=input("how many attempts?")



while attempts<attempt:
    guess=input("Try to guess")
    guess=int(guess)
    attempts += 1
    if guess<x:
        print("Higher")
    if guess>x:
        print("Lower")
    if guess==x:
        print("Correct")
    break

if guess==x:
    print("You are correct")
if guess != x:
    print("You are not right")