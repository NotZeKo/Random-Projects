import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def blackjack():

    our_hand = []
    dealer_hand = []

    our_hand.append(random.choice(cards))
    our_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))


    print("\n" * 20)
    print(art.logo)
    print(f"Your cards: {our_hand}, current score: {sum(our_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}")
    play = True
    while play == True:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card.lower() == "y":
            our_hand.append(random.choice(cards))
            if sum(our_hand) > 21:
                print(f"Your final hand: {our_hand}, current score: {sum(our_hand)}")
                print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                print(f"You went over. You lose.")
                play = False
            elif sum(our_hand) == 21:
                while sum(dealer_hand) < 21:
                    dealer_hand.append(random.choice(cards))
                    if sum(dealer_hand) == 21:
                        print(f"Your final hand: {our_hand}, final score: {sum(our_hand)}")
                        print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                        print(f"You got blackjack, but so did the dealer. You draw")
                        play = False
                    elif sum(dealer_hand) > 21:
                        print(f"Your final hand: {our_hand}, final score: {sum(our_hand)}")
                        print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                        print(f"You got blackjack. You win")
                        play = False
            elif sum(our_hand) < 21:
                print(f"Your cards: {our_hand}, current score: {sum(our_hand)}")
                print(f"Computer's first card: {dealer_hand[0]}")
        elif new_card.lower() == "n":
            while sum(dealer_hand) < sum(our_hand):
                dealer_hand.append(random.choice(cards))
            if sum(dealer_hand) == 21:
                print(f"Your final hand: {our_hand}, final score: {sum(our_hand)}")
                print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                print(f"The dealer got blackjack. You lose")
                play = False
            elif sum(dealer_hand) > 21:
                print(f"Your final hand: {our_hand}, final score: {sum(our_hand)}")
                print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                print(f"The dealer busted. You win")
                play = False
            elif sum(dealer_hand) > sum(our_hand):
                print(f"Your final hand: {our_hand}, final score: {sum(our_hand)}")
                print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
                print(f"The dealer got more. You lose")
                play = False


while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == "y":
        blackjack()
    elif play_again.lower() != "y":
        print("Thanks for playing!")
        break





