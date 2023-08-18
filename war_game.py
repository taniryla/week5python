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

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
  

# 3.1) The value of cards
#		3.3.1) J counts as 11 points
#       3.3.2) Q counts as 12 points
#       3.3.3) K counts as 13 points
#       3.3.4) Aces count as 14 points.
#       3.3.5) Count cards from 2-10 ‘as-is’.
#       3.1.2.3) Count the K, Q, J cards as 10 points.

# 3.2) The winner is the player who wins all of the cards




# /*----- functions -----*/

# 4) Upon loading the app should:
def start_game():
#	4.1) Initialize the state variables:
#   4.1.1) Create a variable of faceUpPlayerCard 
    faceUpPlayerCard = None
#   4.1.2) Create a variable of faceUpComputerCard
    faceUpComputerCard = None
#   4.1.3) Create a variable for winner
    winner = None
#   

#	4.2) Build a list for deck 

deck = []


def build():
    for s in suits:
        for r in ranks:
            deck.append((s, r))

build()
print(deck)
    

#       4.3) Shuffle the deck

random.shuffle(deck)

        # 4.4) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
def deal_war():
#  Player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards. FIX CODE.
    # splice 1 to 26 of master_deck list into player_cards
    for x in range(0, int(len(self.cards)/2)):
        player_cards.append()
        # print(player_cards)
    # splice remaining 27 to 52 to the list computer_cards
    for y in range(int(len(self.cards)/2) + 1, 52):
        computer_cards.append(y)
        # print(computer_cards)
 
#   4.5) Each player draws a card

#   4.6) Compare Player and Computer cards up to see who wins

#   4.7) If Player and Computer turn up the same card, then invoke a go_to_war() function

        # while player_cards and computer_cards:
            



    # The player with the higher card takes all six cards
    
    # If player turns up the same again, repeat the war() function with one card face up and one card face down.



#   4.8) Add J, Q, K and A back into the 11, 12, 13 and 14 values
# 
#   4.9) Check if ekther player_cards or computer_cards is empty and if either are empty determine winner



start_game()