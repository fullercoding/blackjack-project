import random
import os

# Cards are delt from the deck(52cards) the dealer(PlayerCasino) and guest (Player1)
# A deck consists of Clubs, Diamonds, Hearts, Spades called suits
    #Each suit has cards 1-9. K=10, Q=10, J=10 and A=11 or 1

#Game rules

#Step 1, dealer shuffles the deck (download randomizer)
    #Turn the 52 cards into a list
#Step 2, the house deals 2 cards ( both cards seen by player 1) and two cards to dealer(1 card is seen by player 1)
#Step 3, Player one will always have the option to HIT or STAND. If player1's hands >21 BUST, END GAME DEALER WINS
#Step 4, Dealer (PlayerCasino) will always hit <=16 but will always STAND on >=17
#Critcal! IF either player HITS 21 ON THE DEAL IT IS BLACKJACK
#A Push(Tie) occurs when both players finish with the same amount

class Blackjack():

    def __init__(self, deck):
        self.deck = deck




    def prepare_deck():
        deck = ['Ace of Heart','2 of Heart','3 of Heart','4 of Heart','5 of Heart','6 of Heart','7 of Heart','8 of Heart','9 of Heart','T of Heart','J of Heart','Q of Heart','K of Heart',
                'Ace of Diamond','2 of Diamond','3 of Diamond','4 of Diamond','5 of Diamond','6 of Diamond','7 of Diamond','8 of Diamond','9 of Diamond','T of Diamond','J of Diamond','Q of Diamond','K of Diamond',
                'Ace of Spade','2 of Spade','3 of Spade','4S of pade','5 of Spade','6 of Spade','7 of Spade','8 of Spade','9 of Spade','T of Spade','J of Spade','Q of Spade','K of Spade',
                'Ace of Club','2 of Club','3 of Club','4 of Club','5 of Club','6 of Club','7 of Club','8 of Club','9 of Club','T of Club','J of Club','Q of Club','K of Club']

        random.shuffle(deck)
        shuffled_deck = deck
        return shuffled_deck

    def deal_cards(deck):
        player_hand = []
        dealer_hand = []
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        return player_hand, dealer_hand
    print(deal_cards(prepare_deck()))
    
    #def deal_cards(deck):
        #cards_to_be_dealt = []
        #player_hand = []
        #dealer_hand = []
        #x = 0
        #while x < 4:
            #cards_to_be_dealt.append(deck.pop)
            #x += 1
        #return cards_to_be_dealt

#print(Blackjack.deal_cards(Blackjack.prepare()))


# #player_hand_value = 0
#     dealer_hand_value = 0

#     for card in player_hand:
#         if card[0] == 'A':
#             player_hand_value += 1
#         elif card[0] == '2':
#             player_hand_value += 2
#         elif card[0] == '3':
#             player_hand_value += 3
#         elif card[0] == '4':
#             player_hand_value += 4
#         elif card[0] == '5':
#             player_hand_value += 5
#         elif card[0] == '6':
#             player_hand_value += 6
#         elif card[0] == '7':
#             player_hand_value += 7
#         elif card[0] == '8':
#             player_hand_value += 8
#         elif card[0] == '9':
#             player_hand_value += 9
#         elif card[0] == 'T':
#             player_hand_value += 10
#         elif card[0] == 'J':
#             player_hand_value += 10
#         elif card[0] == 'Q':
#             player_hand_value += 10
#         elif card[0] == 'K':
#             player_hand_value += 10
        
#     for card in dealer_hand:
#         if card[0] == 'A':
#             dealer_hand_value += 1
#         elif card[0] == '2':
#             dealer_hand_value += 2
#         elif card[0] == '3':
#             dealer_hand_value += 3
#         elif card[0] == '4':
#             dealer_hand_value += 4
#         elif card[0] == '5':
#             dealer_hand_value += 5
#         elif card[0] == '6':
#             dealer_hand_value += 6
#         elif card[0] == '7':
#             dealer_hand_value += 7
#         elif card[0] == '8':
#             dealer_hand_value += 8
#         elif card[0] == '9':
#             dealer_hand_value += 9
#         elif card[0] == 'T':
#             dealer_hand_value += 10
#         elif card[0] == 'J':
#             dealer_hand_value += 10
#         elif card[0] == 'Q':
#             dealer_hand_value += 10
#         elif card[0] == 'K':
#             dealer_hand_value += 10 

#     print(f"Your hand is {player_hand[0]} and {player_hand[1]}")
#     print(f"The dealer's hand is {dealer_hand[0]} and Hidden")

#     change_ace_value = False

#     for card in player_hand:
#         if card[0] == 'A':
#             while change_ace_value == False:
#                 change_ace_answer = input('Would you like your ace to be worth 1 or 11?')
#                 if change_ace_answer == '11':
#                     player_hand_value += 10
#                     change_ace_value = True
#                 elif change_ace_answer == '1':
#                     change_ace_value = True
#                 else:
#                     print('Sorry, invalid input.')



#     print(f"Your total is {player_hand_value}")
#     player_answer = input("Wolud you like to Hit(h) or Stand(s)?")
#     if player_answer == "h":
        
#         print("You hit")
#     elif player_answer == "s":
#         print("You stand")
#     else:
#         print()

#     if player_hand_value > 21:
#         print("You Lose!")
#     else:
#         print("You Win")


#     def main():
#         pass
    
# Blackjack.main()