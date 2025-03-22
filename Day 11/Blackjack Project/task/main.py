import art
import random

def deal_card():
    """Returns random number(card) from list """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes the list of cards and returns 0 if Blackjack, or sum of cards if not blackjack"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(ur_score, bank_score):
    if ur_score == bank_score:
        return "Draw"
    elif bank_score == 0:
        return "Banker has Blackjack, you lose."
    elif ur_score == 0:
        return "You have Blackjack, you win!"
    elif ur_score > 21:
        return "You are bust. You lose."
    elif bank_score > 21:
        return "Banker went bust. You win."
    elif ur_score > bank_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(art.logo)
    your_cards = []
    bankers_cards = []
    bankers_score = -1
    your_score = -1
    game_over = False

    for _ in range(2):
        your_cards.append(deal_card())
        bankers_cards.append(deal_card())

    print(f"Banker's first card: {bankers_cards[0]}")
    while not game_over:
        your_score = calculate_score(your_cards)
        bankers_score = calculate_score(bankers_cards)
        print(f"Your card: {your_cards}, current score: {your_score}")

        if your_score == 0 or bankers_score == 0 or your_score > 21:
            game_over = True
        else:
            another_card = input("Do you want another card? ('y'/'n')")
            if another_card == 'y':
                your_cards.append(deal_card())
            else:
                game_over = True

    while bankers_score != 0 and bankers_score < 17:
        bankers_cards.append(deal_card())
        bankers_score = calculate_score(bankers_cards)

    print(f"Your final hand: {your_cards} and final score: {your_score}")
    print(f"Bankers final hand: {bankers_cards} and final score {bankers_score}")
    print(compare(your_score, bankers_score))

while input("Do you want to play a game again ('y'/'n'): ") == 'y':
    print("\n" * 20)
    play_game()
