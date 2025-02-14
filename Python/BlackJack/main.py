import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? 'yes' or 'no' ")
bust = False
if play:
    print(art.logo)
    userCards = [random.choice(cards), random.choice(cards)]
    compCards = [random.choice(cards)]
    print(f"    Your cards {userCards}, current score: {sum(userCards)}")
    print(f"    Computer's first card: {compCards}")
    anotherCard = 'yes'
    while sum(userCards) <= 21 and anotherCard == 'yes':
        anotherCard = input("Do you want another card? 'yes' or 'no' ").lower()
        if anotherCard == 'yes':
            userCards.append(random.choice(cards))
            print(f"    Your cards {userCards}, current score: {sum(userCards)}")
            if sum(userCards) > 21:
                print(f"    You went bust with {sum(userCards)}, you lose")
                bust = True
                break
    while sum(compCards) < 17 and bust == False:
        compCards.append(random.choice(cards))
    print(f"    Your final hand: {userCards} total: {sum(userCards)}")
    print(f"    Computer final hand {compCards} total: {sum(compCards)}")
    if sum(compCards) > 21 and bust == False:
        print("Opponent went over. You win")
    elif sum(userCards) > sum(compCards) and bust == False:
        print("You win!")
    elif sum(userCards) == sum(compCards) and bust == False:
        print("Draw")
    elif sum(compCards) > sum(userCards) and bust == False:
        print("You lose!")