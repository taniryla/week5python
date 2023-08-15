import random

# /*----- constants -----*/

# 1) Define required constants:

suits = ['s', 'c', 'd', 'h'];
ranks = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K', 'A'];
# masterDeck = buildMasterDeck();

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
#	3.1) player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards.  


# 3.2) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
# 3.3) If Player and Computer turn up the same card, then invoke a war() function

# The player with the higher card takes all six cards
# If player turns up the same again, repeat the war() function with one card face up and one card face down.

# 3.3) The value of cards
#		3.3.1) J counts as 11 points
#       3.3.2) Q counts as 12 points
#       3.3.3) K counts as 13 points
#       3.3.4) Aces count as 14 points.
#       3.3.5) Count cards from 2-10 ‘as-is’.
#       3.1.2.3) Count the K, Q, J cards as 10 points.

# 3.4) The winner is the player who wins all of the cards


# /*----- functions -----*/
# init()

# /*----- app's state (variables) -----*/
	
# 2) Define required variables used to track the state of the game:
# 2.1) Create an init function
def init():
#	2.2) Create an empty array of player_cards = [ ]	
    player_cards = []
# 2.3) Create an empty array of computer_cards = [ ]
    computer_cards = []
# 2.4) Each player turns one card face up and one card face down
    warPlayerDeck = []
    warComputerDeck = []

# 4) Upon loading the app should:
def startGame():
#	4.1) Initialize the state variables:
#   4.1.1) Create a variable of faceUpPlayerCard 
    faceUpPlayerCard = None
#   4.1.2) Create a variable of faceUpComputerCard
    faceUpComputerCard = None
#   4.1.3) Create a variable for winner
    winner = None
#   4.1.4) Store shuffled deck in a variable
    # shuffled_deck = getNewShuffledDeck(deck)
#   4.1.5) 


#	4.2) Build a class for card and deck 

class Card:
    def __init__(self):
        pass

class Deck:
    def __init__(self):
        pass
    
#   4.3) Get a new Shuffled deck from the random import
    
def getNewShuffledDeck(deck):
    random.shuffle(deck)
    """
    if len(deck) >= 26:
        player_cards.append()
        print(player_cards)
    else:
        computer_cards.append()
        print(player_cards)
    """