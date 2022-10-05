# Black Jack Capstone Game
import random

def deal_card():
#'''It will generate random number from the list of the number given below'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw :)"
    elif computer_score == 0:
        return "lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score >21:
        return "you went over 21, user lost and computer Win"
    elif computer_score >21:
        return "computer lost, User Win"
    elif user_score > computer_score:
        return "User Win"
    else:
        return "you Lost"


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play():
# empty list for user and computer where 2 random numbers are generated
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" user :{user_cards}, {user_score}")
        print(f"computer : {computer_cards}, {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand : {user_cards}, final score : {user_score}")
    print(f"Computer final  hand : {computer_cards}, final score : {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play BlackJack Game, play 'y' or 'n':  \n ") == 'y':
    play()
