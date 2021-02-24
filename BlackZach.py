import random
import time


deck_copy = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
the_deck = ['A','A','A','A','K','K','K','K','Q','Q','Q','Q','J','J','J','J','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','10','10','10','10']
deck_values = {'A':11,'K':13,'Q':12,'J':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'a':1}

my_hand = []
dealers_hand = []
my_value = []
dealers_value = []




def start_game():
    print ('Welcome to BlackZach\'s Casino!\n'
           '-\n'
           'We\'ll start you with 500 coins.\n'
           '-\n'
           'You must bet 50 to play a round, and you have the option to double the bet after the first cards are dealt'
           'Accumulate 1,500 coins to win the game.')
    start_choice()


def start_choice():
    the_deck = deck_copy.copy()
    begin_game = input('\n\n'
          'Would you like to play? (y/n)\n')
    if begin_game == 'y':
        its_showtime()
    elif begin_game == 'n':
        print('Thanks for stopping by, see you next time!')
        quit()
    else:
        start_choice()






def grab_card():
    total_cards = len(the_deck)-1
    max_card = int(total_cards)
    draw = random.randint(0,max_card)
    card_name = the_deck[draw]
    card_value = deck_values[card_name]
    the_deck.pop(draw)
    return(card_name)


def discard(position):
    the_deck.remove(position)





def dealer_draw():
    card = grab_card()
    dealers_hand.append(card)
    dealers_value.append(deck_values.get(card))
    discard(card)
    time.sleep(.5)
    print('Dealer drew a',card)
    time.sleep(1)

def player_draw():
    card = grab_card()
    my_hand.append(card)
    my_value.append(deck_values.get(card))
    discard(card)
    time.sleep(.5)
    print('You drew a',card)
    time.sleep(1)


def first_cards():
    player_draw()
    player_draw()
    dealer_draw()
    dealer_draw()
    on_the_table()


def on_the_table():
    print('\n\n\nYour Hand:',my_hand)
    print(sum(my_value))
    time.sleep(2)
    print('\nDealer\'s Hand:',dealers_hand)
    print(sum(dealers_value))


def ace_check(list,dict):
    if 'A' in list:
        list.pop('A')
        list.append('a')
    else:
        pass
    if sum(dict) > 21:
        ace_check(list,dict)
    else:
        pass






def hit_stay():
    time.sleep(2)
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
                dealers_turn()
            return
        elif value == 21:
            print('BLACKJACK\n')
            time.sleep(2)
            print('Let\'s see what the Dealer has...')
            dealers_turn()
            return
        hit_stay()
    elif choice == 's':
        print('\nStayed.\n')
        time.sleep(1)
        print('Dealer\'s Turn...')
        time.sleep(2)
        dealers_turn()
    else:
        print('Invalid Input: Try again...\n')
        time.sleep(2)
        hit_stay()





def dealers_turn():
    if sum(dealers_value) < 17:
        dealer_draw()
        dealers_turn()
    elif sum(dealers_value) > 17 & sum(dealers_value) < 21:
        who_wins()
    elif sum(dealers_value) == 21:
        print('BLACKJACK')
        time.sleep(.5)
        print('BLACKJACK')
        time.sleep(.5)
        print('BLACKJACK')
        time.sleep(.5)
        who_wins()
    elif sum(dealers_value) > 21:
        ace_check(dealers_hand,dealers_value)
        if sum(dealers_value) < 22:
            dealers_turn()
        elif sum(dealers_value) > 21:
            who_wins()


def who_wins():
    p = sum(my_value)
    d = sum(dealers_value)
    if p < 22 & p > d:
        player_wins()
    elif d < 22 & d > p:
        dealer_wins()
    elif d > 21 & p > 21:
        dealer_wins()
    elif d == p:
        draw()

def player_wins():
    print('\n***You Win!***\n')
    time.sleep(2)
    restart()

def dealer_wins():
    print('\n***Dealer Wins!***\n')
    time.sleep(2)
    restart()

def draw():
    print('***It\'s a Draw!***')
    time.sleep(2)
    restart()





def its_showtime():
    first_cards()
    hit_stay()


def restart():
    the_deck = deck_copy.copy()
    start_choice()


start_game()
