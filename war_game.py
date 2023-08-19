import random

# /*----- constants -----*/

# 1) Define required constants:

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
ranks = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']

# /*----- app's state (variables) -----*/
	
# 2) Define required variables used to track the state of the game:
# 2.1) 
#	2.2) Create an empty array of player_cards	
player_cards = []
# 2.3) Create an empty array of computer_cards 
computer_cards = []
# 2.4) Each player turns one card face up and one card face down
warPlayerDeck = []
warComputerDeck = []
# 2.5) Create a variable of faceUpPlayerCard 
faceUpPlayerCard = None
# 2.6) Create a variable of faceUpComputerCard
faceUpComputerCard = None

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
# 3.1) The value of cards
#		3.3.1) J counts as 11 points
#       3.3.2) Q counts as 12 points
#       3.3.3) K counts as 13 points
#       3.3.4) Aces count as 14 points.
#       3.3.5) Count cards from 2-10 ‘as-is’.
#       3.1.2.3) Count the K, Q, J cards as 10 points.

# /*----- functions -----*/

# 4) Upon loading the app should:
def init():
#	4.1) Initialize the state variables:
#  
#   4.1.3) Create a variable for winner
    winner = None
    build()
    shuffle_deck()
    deal_deck()
    draw(0)

#	4.2) Build a list for deck 
deck = []

def build():
    for s in suits:
        for r in ranks:
            deck.append((s, r))

#   4.3) Shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

#   4.4) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
def deal_deck(): #  Player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards. 
    player_cards.append(deck[0:int(len(deck)/2)]) # splice 1 to 26 of deck list into player_cards
    computer_cards.append(deck[(int(len(deck)/2)+1):52]) # splice remaining 27 to 52 to the list computer_cards

#   4.5) Each player draws a card
def draw(x):
    faceUpPlayerCard = player_cards[x].pop() # the top item is removed from the player_cards list
    player_face_value = faceUpPlayerCard[1]
    faceUpComputerCard = computer_cards[x].pop()
    computer_face_value = faceUpComputerCard[1]
    determine_winner(player_face_value, computer_face_value, faceUpPlayerCard, faceUpComputerCard)

#   4.6) If Player and Computer turn up the same card, then invoke a go_to_war() function
def go_to_war():        
    # if tie, three cards face down and then card face-up, winner takes all 10 cards
    warPlayerDeck.append(player_cards[0])
    warPlayerDeck.append(player_cards[1])
    warPlayerDeck.append(player_cards[2])
    warComputerDeck.append(computer_cards[0])
    warComputerDeck.append(computer_cards[1])
    warComputerDeck.append(computer_cards[2])
    draw(3)   # If player and computer tie, repeat the go_to_war() function with one card face up and one card face down.
    print(f"Hidden Cards... {warPlayerDeck} {warComputerDeck}")

    # TODO1: if player or computer doesn't have 3 cards to put face-down, then they lose the war

#   4.7) Compare Player and Computer cards up to see who wins
def determine_winner(j, k, l, m):
    if j > k: # both face up cards by player and computer go to player_cards list
        player_cards.insert(0, l)
        player_cards.insert(1, m)
#   OPTIONAL TODO2: Add J, Q, K and A back into the 11, 12, 13 and 14 values
        # TODO3: Show number of cards for player and include in print below. Check if ekther player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {l[1]} of {m[0]} and computer shows the {m[1]} of {l[0]}. (Ace is 14, King is 13, Queen is 12, and Jack is 11). Player wins!")
        l = None
        m = None
        draw(0)
    elif j > k: # both face up cards by player and computer go to computer_cards list
        computer_cards.insert(0, l)
        computer_cards.insert(1, m)
        # TODO4: Show number of cards for computer and include in print below. Check if ekther player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {l[1]} of {m[0]} and computer shows the {m[1]} of {l[0]}. (Ace is 14, King is 13, Queen is 12, and Jack is 11). Computer wins!")
        l = None
        m = None
        draw(0)
    elif j == k:
        go_to_war()



init()