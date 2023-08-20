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
war_player_deck = []
war_computer_deck = []
# 2.4) Create a variable of faceUpPlayerCard 
faceup_player_card = None
# 2.5) Create a variable of faceUpComputerCard
faceup_computer_card = None
# 2.6) Keep track of the card count for Player and Computer
player_card_count = 26
computer_card_count = 26

# /*----- functions -----*/

# 3) Upon loading the app should:
def init():
    global player_cards, computer_cards, player_card_count, computer_card_count
    winner = None #   Create a variable for winner
    build()
    shuffle_deck()
    menu()
    player_cards, computer_cards = deal_deck() # converting tuple back into a list, now writes to global
    draw()

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
    print("| 2.    Card Tally                          |")
    print("---------------------------------------------")
    print("| 3.    Exit Game                           |")
    print("---------------------------------------------")

    while True:
        option = input("Choose an option:")
        if option == "1":
            draw()
        elif option == "2":
            card_tally()
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
    while True:
        if player_card_count != 0 or computer_card_count != 0:
            faceUpPlayerCard = player_cards.pop() # the top item is removed from the player_cards list
            faceUpComputerCard = computer_cards.pop()
            determine_winner(faceup_player_card, faceup_computer_card, war_player_deck, war_computer_deck, player_card_count, computer_card_count)
        else:
            if player_card_count == 0:
                print("Player has no cards left. Computer has won!")
                break
            else:
                print("Computer has no cards left. Player has won!")
                break

#   3.6) If Player and Computer turn up the same card, then invoke a go_to_war() function
def go_to_war():        
    # if tie, three cards face down and then card face-up, winner takes all 10 cards
    if (len(player_cards) or len(computer_cards)) > 3:
        war_player_deck.append(player_cards[0])
        war_player_deck.append(player_cards[1])
        war_player_deck.append(player_cards[2])
        war_computer_deck.append(computer_cards[0])
        war_computer_deck.append(computer_cards[1])
        war_computer_deck.append(computer_cards[2])
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
    
#   3.8) Helper function to keep track of the card count for Player and Computer
def card_tally():
    print(f"Player cards remaining... {player_card_count}")
    print(f"Computer cards remaining... {computer_card_count}")
    menu()

#   3.9) Compare Player and Computer cards up to see who wins
def determine_winner(faceup_player_card, faceup_computer_card, war_player_deck, computer_player_deck, player_card_count, computer_card_count):
    if int(faceup_player_card[1]) > int(faceup_computer_card[1]): # both face up cards by player and computer go to player_cards list
        player_cards.insert(0, faceup_player_card)
        player_cards.insert(1, faceup_computer_card)
        player_card_count += 2
        computer_card_count -=2
        if war_player_deck != None: # if went to war
            player_cards.insert(2, war_player_deck)
            player_cards.insert(3, war_computer_deck)
            player_card_count += 6
            computer_card_count -= 6
            war_player_deck= []
            war_computer_deck = []
#   Show number of cards for player and include in print below. Check if either player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {royal_help(int(faceup_player_card[1]))} of {faceup_player_card[0]} and Computer shows the {royal_help(int(faceup_computer_card[1]))} of {faceup_computer_card[0]}. Player wins! Player has {player_card_count} cards and Computer has {computer_card_count} cards.")
        menu()
    elif int(faceup_player_card[1]) < int(faceup_player_card[1]): # both face up cards by player and computer go to computer_cards list
        computer_cards.insert(0, faceup_player_card)
        computer_cards.insert(1, faceup_computer_card)
        computer_card_count += 2
        player_card_count -= 2
        if war_computer_deck != None:
            computer_cards.insert(2, war_player_deck)
            computer_cards.insert(3, war_computer_deck)
            computer_card_count += 6
            player_card_count -=6
            war_player_deck = []
            war_computer_deck = []
#   TODO2: Show number of cards for computer and include in print below. Check if either player_cards or computer_cards is empty and if either are empty determine winner
        print(f"Player shows the {royal_help(int(faceup_player_card[1]))} of {faceup_player_card[0]} and Computer shows the {royal_help(int(faceup_computer_card[1]))} of {faceup_computer_card[0]}. Computer wins! Player has {player_card_count} cards and Computer has {computer_card_count} cards.")
        menu()
    elif int(faceup_player_card[1]) == int(faceup_computer_card[1]):
        go_to_war()


init()