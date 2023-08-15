import random

# /*----- constants -----*/

# 1) Define required constants:

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts'];
ranks = ['02', '03', '04', '05', '06', '07', '08', '09', '10', 'J', 'Q', 'K', 'A'];

# /*----- cached element references -----*/
# 3) Store elements on the page that will be accessed in code more than once in variables to make code more concise, readable and performant:
  
# 3.2) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
# 3.3) If Player and Computer turn up the same card, then invoke a war() function
def war():
    pass
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
#   4.1.4) Create a new deck and then shuffle and show it
    deck = Deck()
    deck.shuffle()
    deck.show()
#   4.1.5) Player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards. FIX CODE.
#   4.1.6) Pull out the card on the deck for the Player
    """
    while deck != None:
        faceUpPlayerCard = deck.draw_card()
        player_cards.append(faceUpPlayerCard)
        print("Player card...")
        faceUpPlayerCard.show()
        faceUpComputerCard = deck.draw_card()
        computer_cards.append(faceUpComputerCard)
        print("Computer card...")
        faceUpComputerCard.show()
        print(f"Player cards... {player_cards}")
        print(f"Computer cards... {computer_cards}")
    """



#	4.2) Build a class for card and deck 

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))
    
    def show(self):
        for c in self.cards:
            c.show()


#   4.3) Get a new Shuffled deck from the random import
    
    def shuffle(self):
        # when we run the loop, we want values 51-1 (length of array minus)
        for i in range(len(self.cards) - 1, 0, -1):
            # create a random number from 0 to i (which is left of our current position as we're going right to left)
            ran = random.randint(0, i)
            self.cards[i], self.cards[ran] = self.cards[ran], self.cards[i]

#   4.4) Create a Draw Card method
    def draw_card(self):
        return self.cards.pop() # will remove the last card from the top of the deck and return that card


start_game()