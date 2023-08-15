
# /*----- constants -----*/

#v 1) Define required constants:

suits = ['s', 'c', 'd', 'h']
ranks = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K', 'A']

# /*----- app's state (variables) -----*/
	
# 2) Define required variables used to track the state of the game:
# 2.1) Declare a Shuffle deck variable “shuffleDeck”
#	2.2) Create an empty array of playerCards = [ ]	
# 2.3) Create an empty array of computerCards = [ ]
# 2.4) Create a variable of faceUpPlayerCard 
# 2.5) Create a variable of faceUpComputerCard 

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
#	3.1) playerCards receives 26 random cards out of a 52 card deck. computerCards receives 26 random cards.  
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
init()
def init ():

# 4) Upon loading the app should:
#	4.1) Initialize the state variables:
#		4.1.1) Get a new Shuffled deck.
def getNewShuffledDeck():
    print("Placeholder")