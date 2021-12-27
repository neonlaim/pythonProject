import random
# Press the green button in the gutter to run the script.

print("Guess the number game")

rangeStarts=input("range starts from: ")
rangeStarts=int(rangeStarts)
rangeLimit=input("range limits by: ")
rangeLimit=int(rangeLimit)
attempt=10
number=0

x=random.randint(rangeStarts,rangeLimit)
attempts=0
print(x)
#attempt=input("how many attempts?")

while attempts<attempt:
    guess=input("Try to guess: ")
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
    print("You are correct!")
if guess != x:
    print("You are not right")