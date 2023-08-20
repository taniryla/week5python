import random

# /*----- constants -----*/

# 1) Define required constants:

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
ranks = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14']

# /*----- app's state (variables) -----*/
	
# 2) Define required variables used to track the state of the game:
# 2.1) Create an empty list of player_cards	
player_cards = []
# 2.2) Create an empty list of computer_cards 
computer_cards = []
# 2.3) Each player turns one card face up and one card face down
warPlayerDeck = []
warComputerDeck = []
# 2.4) Create a variable of faceUpPlayerCard 
faceUpPlayerCard = None
# 2.5) Create a variable of faceUpComputerCard
faceUpComputerCard = None

# /*----- functions -----*/

# 3) Upon loading the app should:
def init():
    global player_cards, computer_cards
    winner = None #   Create a variable for winner
    build()
    shuffle_deck()
    menu()
    player_cards, computer_cards = deal_deck() # converting tuple back into a list, now writes to global

#	3.2) Build a list for deck 
deck = []

def build():
    for s in suits:
        for r in ranks:
            deck.append([s, r])
    return deck

#   3.3) Shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

#   3.4) Build a def menu() with 1. Play A Hand 2. Score 3. Exit Game
def menu():
    print("          === War ===          ")
    print("---------------------------------------------")
    print("| 1.    Play Next Hand                      |")
    print("---------------------------------------------")
    print("| 2.    Score                               |")
    print("---------------------------------------------")
    print("| 3.    Exit Game                           |")
    print("---------------------------------------------")

    while True:
        option = input("Choose an option:")
        if option == "1":
            draw()
        elif option == "2":
            score()
        else:
            print("Nice playing. Goodbye!")
            break

#   3.5) Player and Computer turn up one card at the same time from the top of their card stack and the player with the higher card takes both cards and puts on the bottom of their card stack
def deal_deck(): #  Player_cards receives 26 random cards out of a 52 card deck. computer_cards receives 26 random cards. 
    player_cards = deck[0:int(len(deck)/2):] # slice 1 to 26 of deck list into player_cards
    computer_cards = deck[(int(len(deck)/2)+1):52:] # slice remaining 27 to 52 to the list computer_cards
    return player_cards, computer_cards

#   3.5) Each player draws a card
def draw():
    faceUpPlayerCard = player_cards.pop() # the top item is removed from the player_cards list
    faceUpComputerCard = computer_cards.pop()
    determine_winner(faceUpPlayerCard, faceUpComputerCard, warPlayerDeck, warComputerDeck)

#   3.6) If Player and Computer turn up the same card, then invoke a go_to_war() function
def go_to_war():        
    # if tie, three cards face down and then card face-up, winner takes all 10 cards
    if (len(player_cards) or len(computer_cards)) > 3:
        warPlayerDeck.append(player_cards[0])
        warPlayerDeck.append(player_cards[1])
        warPlayerDeck.append(player_cards[2])
        warComputerDeck.append(computer_cards[0])
        warComputerDeck.append(computer_cards[1])
        warComputerDeck.append(computer_cards[2])
        draw()   # If player and computer tie, repeat the go_to_war() function with one card face up and one card face down.if player or computer doesn't have 3 cards to put face-down, then they lose the war
    else:
        if len(player_cards) < 3:
            print("Player does not have enough cards. Player loses!")
        else:
            print("Computer does not have enough cards. Computer loses!")

#   3.7) Helper function in a dictionary form to replace 14 with A, 13 with K, 12 with Q and 11 withh J
def royal_help(arg):
    dict = {14: "A", 13: "K", 12: "Q", 11: "J"}
    if arg in dict.keys():
        return dict[arg]
    else:
        return arg
    
#   3.8) Helper function to keep score
def score():
    pass

#   3.9) Compare Player and Computer cards up to see who wins
def determine_winner(l, m, n, o):
    if int(l[1]) > int(m[1]): # both face up cards by player and computer go to player_cards list
        player_cards.insert(0, l)
        player_cards.insert(1, m)
        if n != None:
            player_cards.insert(2, n)
            player_cards.insert(3, o)
            n = []
            o = []
#   TODO1: Show number of cards for player and include in print below. Check if either player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {royal_help(int(l[1]))} of {l[0]} and computer shows the {royal_help(int(m[1]))} of {m[0]}. Player wins!")
        menu()
    elif int(l[1]) < int(m[1]): # both face up cards by player and computer go to computer_cards list
        computer_cards.insert(0, l)
        computer_cards.insert(1, m)
        if o != None:
            computer_cards.insert(2, n)
            computer_cards.insert(3, o)
            n = []
            o = []
#   TODO1: Show number of cards for computer and include in print below. Check if either player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {royal_help(int(l[1]))} of {m[0]} and computer shows the {royal_help(int(m[1]))} of {l[0]}. Computer wins!")
        menu()
    elif int(l[1]) == int(m[1]):
        go_to_war()


init()