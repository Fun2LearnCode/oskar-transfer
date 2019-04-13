import random
number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10:"))
while guess != number:
    if guess < number:
        print(guess,"was too low. Guess again.")
    if guess > number:
        print(guess,"was too high. guess again.")
    guess=int(input("guess again:"))
print(guess,"was the right number!Way to go!")
