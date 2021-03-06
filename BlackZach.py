import random
import time


player_bank = [0]
current_bet = [0]





deck_copy = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
the_deck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
deck_values = {'A':11,'K':10,'Q':10,'J':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'X':1}
# X represents an Ace with a value of 1, while uppercase 'A' represents a value of 11
#After each hand, the deck is "shuffled" and recompiled by copying the values of deck_copy to replace the exhausted list, the_deck

my_hand = []
dealers_hand = []
my_value = []
dealers_value = []
### the 'hand' lists are used to represent printable values to show a player what they have and are used to identify keys in the {deck_values} dictionary
### the value lists are used to hold the numeric value of each card, and are summed later in the program to identify proximity to 21



def start_game():
    player_bank[0] += 500
    print ('Welcome to BlackZach\'s Casino!\n'
           '-\n'
           'We\'ll start you with 500 coins.\n'
           '-\n'
           'You must bet 50 to play a round, and you have the option to double the bet after the first cards are dealt'
           'Accumulate 1,500 coins to win the game.')
    start_choice()
### initializes the game with simple description and then sends to start_choice

def start_choice():
    while True:
        begin_game = input('\n\n'
              'Pay 50 coins to buy in? (y/n)\n')
        if begin_game == 'y':
            its_showtime()
        elif begin_game == 'n':
            print('You started with 500 coins and you\'re leaving with',player_bank,'\n***IMPRESSIVE!***\n')
            quit()
### allows users to quit or play





def grab_card():
    total_cards = len(the_deck)-1
    max_card = int(total_cards)
    draw = random.randint(0,max_card)
    card_name = the_deck[draw]
    the_deck.pop(draw)
    return(card_name)
### a function used often, that calculates the number of cards in the_deck and then randomly picks one
# (as if the deck were shuffled) and then removes the card from the list and returns card_name



def dealer_draw():
    print('dealer draw activated')
    card = grab_card()
    dealers_hand.append(card)
    dealers_value.append(deck_values.get(card))

    
def player_draw():
    card = grab_card()
    my_hand.append(card)
    my_value.append(deck_values.get(card))
    time.sleep(.5)
    print('You drew a',card)
### used to call grab_card() and append the card name to your hand list and the card value to your value list
# then prints a message telling you what card you've drawn

def first_cards():

    player_draw()
    player_draw()
    dealer_draw()
    dealer_draw()
    on_the_table()
    double = input('Would you like to double down? (y/n)\n')
    if double == 'y':
        current_bet[0] = 100
        player_bank[0] -= 100
    elif double == 'n':
        current_bet[0] = 50
        player_bank[0] -= 50
    else:
        current_bet[0] = 50
        player_bank[0] -= 50
        # if somehow they screw up this simple input they're probably not smart enough to know when to double down, so i force it
    show_bet()
### gives the player their first two cards and gives the dealer their first two cards (potentially one face down, unsure on blackjack rules)

def on_the_table():
    print('\n\n\nYour Hand:',my_hand)
    print(sum(my_value))
    print('\nDealer is showing a',dealers_hand[0])
    print(sum(dealers_value))
### function to show the player and dealer's hands during play (might need to remove the showing of one of the dealer's cards)
### removed the dealer's hand showing two cards
    

def show_bet():
    print('\nCurrent bet:',current_bet)
    print(player_bank)
    
def ace_check(list,list2):
    if 'A' in list:
        list.remove('A')
        list.append('X')
        list2.append(-10)
    else:
        return
### checks for aces when a player busts, if there is one, it replaces the value of 11 with the value of 1


def dealers_turn():
    while sum(dealers_value) < 17:
        dealer_draw()







### this function activates after the player busts, gets blackjack, or stays. forces the dealer to draw until the value of cards exceeds 17.
# apparently true blackjack would suggest that a dealer hand 17 or over with an ACE needs to continue drawing, might add that later.
### added ace check for the 17-20 range so dealer will continue drawing on a soft 17,18,19 and 20.
# (soft is when the hand contains an ace with a value of 11, because that hand can never bust in one hit)






def hit_stay():
    choice = input('\n\n--Hit (h) or Stay (s)?--\n')
    if choice == 'h':
        player_draw()
        on_the_table()
        value = sum(my_value)
        if value < 21:
            pass
        elif value > 21:
            ace_check(my_hand,my_value)
            if sum(my_value) < 22:
                hit_stay()
            elif sum(my_value) > 21:
                print('\nBUST\n')
                return
        elif value == 21:
            print('BLACKJACK\n')
            print('Let\'s see what the Dealer has...')
            return
        hit_stay()
    elif choice == 's':
        print('\nStayed.\n')
        time.sleep(1)
        print('Dealer\'s Turn...')
        return
    else:
        print('Invalid Input: Try again...\n')
        hit_stay()
### this function offers the player an opportunity to add new cards to their hand or stay.  This function also stops the player 
# when they bust or hit 21





            

def who_wins():
    p = sum(my_value)
    d = sum(dealers_value)
    if p < 22 and p > d:
        player_wins()
    elif d < 22 and d > p:
        dealer_wins()
    elif d > 21 and p > 21:
        dealer_wins()
    elif d == p:
        draw()
### determines the winner of the game, might need to add certain end game scenarios. Might also need to reflect rule that states
# 21 vs 21 is a draw, but getting dealt a 21 off rip is a win for the player.
        
        
def player_wins():
    print('\n***You Win!***\n')
    time.sleep(1)
    print('+',current_bet[0])
    player_bank[0] = player_bank[0] + current_bet[0] + current_bet[0]
    current_bet[0] = 0
    time.sleep(2)
    restart()

def dealer_wins():
    print('\n***Dealer Wins!***\n')
    time.sleep(1)
    print('-',current_bet[0])
    current_bet[0] = 0
    time.sleep(2)
    restart()

def draw():
    print('***It\'s a Draw!***')
    time.sleep(1)
    print('Bet Returned')
    player_bank[0] = player_bank[0] + current_bet[0]
    current_bet[0] = 0
    time.sleep(2)
    restart()
### simple win conditions with restart
### added function to pay out correct bets




def its_showtime():
    first_cards()
    hit_stay()
    dealers_turn()
    who_wins()
### dictates order of events with larger functions

def restart():
    the_deck = deck_copy.copy()
    my_hand.clear()
    my_value.clear()
    dealers_hand.clear()
    dealers_value.clear()
    start_choice()
### resets the_deck list and restarts the function chain

start_game()
### calls the game start function
