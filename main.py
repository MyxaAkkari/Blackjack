############### Blackjack Project #####################
import random
import os
from art import logo

os.system('clear')
# Gets a random card from deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculates the score and checks if any player got a blackjack -> returns 0, or if a player passed 21 and has a Ace change its value to 1
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
# Compares scores and checks who wins
def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return "Lose, computer has a Blackjack"
    elif userScore == 0:
        return "Win with a Blackjack"
    elif userScore > 21:
        return "You went over, You lose"
    elif computerScore >21:
        return "Computer went over, You win"
    elif userScore > computerScore:
        return "You win"
    else: 
        return "You lose"
# Main function
def playGame():
        print(logo)
        userCards = []
        computerCards = []
        isGameOver = False
        # deals first two cards
        for _ in range(2):
            userCards.append(deal_card())
            computerCards.append(deal_card())
        
        # shows the hand and score to user and check if he wants to draw again
        while not isGameOver:
            userScore = calculate_score(userCards)
            computerScore = calculate_score(computerCards)
            print(f"    Your cards are {userCards}, current score: {userScore}")
            print(f"    Computer's first cards: {computerCards[0]}")


            # checks if any player got a Blackjack or if player went over 21
            if userScore == 0 or computerScore == 0 or userScore > 21:
                isGameOver = True
            else:
                userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
                if userShouldDeal == "y":
                    userCards.append(deal_card())
                else:
                    isGameOver = True 
        # if computer doesn't have a Blackjack and his score is less that 17 it should keep drawing cards
        while computerScore != 0 and computerScore < 17:
            computerCards.append(deal_card())
            computerScore = calculate_score(computerCards)


        print(f"    Your finale hand: {userCards}, final score: {userScore}")
        print(f"    Computer's finale hand: {computerCards}, final score: {computerScore}")
        print(compare(userScore, computerScore))
# Main loop to keep the game running
while input("Do you want to play a game of Blackjack? type 'y' or 'n': ") == "y":
    os.system('clear')
    playGame()