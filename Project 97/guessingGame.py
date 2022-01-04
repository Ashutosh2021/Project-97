import random

num = random.randint(1,9)
chances=5

print("Number Guessing Game")
print("Guess a number between 1-9")

while chances > 0 :
    guess=int(input("Enter your guess : "))
    chances=chances-1
    if guess==num :
        print("CONGRACTULATIONS !! You guessed it right")
        chances=-2
    elif guess > num :
        print("Your guess was too high , Try guessing a lower number")
    elif guess < num :
        print("Your guess was too low , Try guessing a higher number")
    
    if chances==0 :
        print("You Lose !! the number is",num)