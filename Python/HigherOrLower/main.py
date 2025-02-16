import game_data
import random
import art
import os

print(art.logo)

wrong = False
score = 0

def format_data(data):
    return f"{data['name']}, a {data['description']}, from {data['country']}"

def check_answer(user_guess, compareA, compareB):
    if compareA['follower_count'] > compareB['follower_count']:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

while not wrong:
    compareA = random.choice(game_data.data)
    compareB = random.choice(game_data.data)
    if compareB == compareA:
        compareB = random.choice(game_data.data)
    print(f"Compare A: {format_data(compareA)}.")
    print(art.vs)
    print(f"Against B: {format_data(compareB)}.")
    if check_answer(input("Who has more followers, A or B? ").lower(), compareA, compareB):
        score +=1
        print("\n" * 30)
        print(art.logo)
        print(f"You're right! Current score {score}")
    else:
        wrong = True
print("\n" * 30)
print(art.logo)
print(f"Sorry that's wrong, final score: {score}")
