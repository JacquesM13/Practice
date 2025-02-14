import random
import art

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

def gameplay(lives):
    number = random.randint(1, 100)
    guessed = False
    while guessed == False and lives > 0:
        print(f"You have {lives} attempt left to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            guessed = True
            break
        elif guess < number:
            print("    Too low.")
            lives -= 1
            if lives > 0:
                print("    Guess again.")
        elif guess > number:
            print("    Too high.")
            lives -= 1
            if lives > 0:
                print("    Guess again.")
    if guessed:
        print("Well done, you guessed right!")
    else:
        print("Better luck next time")

mode = input("Choose a difficulty, 'easy' or 'hard' ")

if mode == 'easy':
    gameplay(10)
elif mode == 'hard':
    gameplay(5)

