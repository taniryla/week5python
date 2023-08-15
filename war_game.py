import random

# /*----- constants -----*/

# 1) Define required constants:

deck = ['02s', '03s', '04s', '05s', '06s', '07s', '08s', '09s', '10s', 'Js', 'Qs', 'Ks', 'As', '02c', '03c', '04c', '05c', '06c', '07c', '08c', '09c', '10c', 'Jc', 'Qc', 'Kc', 'Ac', '02d', '03d', '04d', '05d', '06d', '07d', '08d', '09d', '10d', 'Jd', 'Qd', 'Kd', 'Ad','02h', '03h', '04h', '05h', '06h', '07h', '08h', '09h', '10h', 'Jh', 'Qh', 'Kh', 'Ah']

# /*----- app's state (variables) -----*/
	
# 2) Define required variables used to track the state of the game:
# 2.1) Declare a Shuffle deck variable “shuffleDeck”
#	2.2) Create an empty array of player_cards = [ ]	
player_cards = []
# 2.3) Create an empty array of computer_cards = [ ]
computer_cards = []
 

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
#	3.1) player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards.  


# 3.2) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
# 3.3) If Player and Computer turn up the same card, then invoke a war() function
# Each player turns one card face up and one card face down
warPlayerDeck = []
warComputerDeck = []
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
# def init ():

# 4) Upon loading the app should:
def getNewShuffledDeck(deck):
#	4.1) Initialize the state variables:
#   4.1.1) Create a variable of faceUpPlayerCard 
    faceUpPlayerCard = None
#   4.1.2) Create a variable of faceUpComputerCard
    faceUpComputerCard = None
#   4.1.3) Create a variable for winner
    winner = None
#	4.2) Get a new Shuffled deck from the random import.
    random.shuffle(deck)
    while len(deck) <= 26:
        player_cards.append(shuffled_deck)
        print(player_cards)
    computer_cards.append(shuffled_deck)
    print(player_cards)
